"""Module to pre process image data > tabular data set"""
import urllib.request
import h5py
import numpy as np

BANDS = [
    "Coastal_Aerosol",
    "Blue",
    "Green",
    "Red",
    "Vegetation_Red_Edge",
    "Vegetation_Red_Edge_2",
    "Vegetation_Red_Edge_3",
    "NIR",
    "Narrow_NIR",
    "Water_Vapor",
    "SWIR_1",
    "SWIR_2",
]

##################
## data loader ###
##################
def load_data(url, data):
    """input url > nparray dataset"""
    file_name = f"{data}set.h5"
    urllib.request.urlretrieve(url, file_name)
    data_set = h5py.File(file_name, "r")
    # check cols in the dataset
    data_cols = data_set.keys()
    print()
    print(data_cols)
    for col in data_cols:
        tmp = np.array(data_set[col])
        # Check for Nans
        mask = np.isnan(tmp) | np.equal(tmp, None)
        num_na = np.count_nonzero(mask)
        print(f"{col} : {len(tmp)} values, {num_na} Nans")
    return data_set


##################
## image process #
##################
def data_scaler(col_data):
    """takes in col and scales it"""
    mean_col = np.mean(col_data)
    std_col = np.std(col_data)
    col_data_normalized = (col_data - mean_col)/std_col
    col_data_normalized = col_data_normalized.reshape((len(col_data), 15, 15, 1))
    return col_data_normalized


def make_histogram(channel):
    """takes in a band and creates histograms for each image"""
    channel_histogram = []
    channel_min = np.min(channel)
    channel_max = np.max(channel)
    for i in range(len(channel)):
        tmp_img = channel[i, :, :, :]
        hist_tmp, _ = np.histogram(
            tmp_img, bins=16, range=(channel_min, channel_max)
        )
        channel_histogram.append(hist_tmp)
    feature_matrix = np.vstack(channel_histogram)
    return feature_matrix


def create_features(data):
    """input data -> scaled image data"""
    images = np.array(data["images"])
    # Scale bands
    band_data = {}
    for i, band in enumerate(BANDS):
        band_info = images[:, :, :, i]
        band_scaled = data_scaler(band_info)
        band_name = f"{band}_scaled"
        band_data[band_name] = band_scaled

    # 💡 TODO: reduce local assignment 25 -> 15
    # cloud information
    cloud_data = np.array(data["cloud"])
    cloud_scaled = data_scaler(cloud_data)
    band_data["cloud_scaled"] = cloud_scaled

    # scl information
    scl_data = np.array(data["scl"])
    scl_scaled = data_scaler(scl_data)
    band_data["scl_scaled"] = scl_scaled

    # latitide information
    lat_data = np.array(data["lat"])
    lat_scaled = data_scaler(lat_data)
    band_data["lat_scaled"] = lat_scaled

    # Longitude
    lon_data = np.array(data["lon"])
    lon_scaled = data_scaler(lon_data)
    band_data["lon_scaled"] = lon_scaled

    # evi calculation
    nir_band = band_data["NIR_scaled"]  # 8th band
    red_band = band_data["Red_scaled"]  # 4th band
    blue_band = band_data["Blue_scaled"]  # 2nd band
    evi_data = 2.5 * (
        (nir_band - red_band) / (nir_band + 6 * red_band - 7.5 * blue_band + 1)
    )
    band_data["evi_scaled"] = evi_data

    # make histograms
    values_list = list(band_data.values())
    features = []
    for val in values_list:
        tmp_feature = make_histogram(val)
        features.append(tmp_feature)
    features_complete = np.hstack(features)
    return features_complete


def create_targets(data):
    """takes in agbd col and returns an array of targets"""
    targets = np.array(data["agbd"])
    return targets


def main():
    """run through the urls and create datasets"""
    # 🛑 change links to point to data urls
    file_urls = [
        "url to train file",
        "url to validation file",
        "url to test file",
    ]
    data_set = ["train", "val", "test"]

    for i, url in enumerate(file_urls):
        dataset = data_set[i]
        print(f"loading {dataset} set ....")
        file = load_data(url, dataset)
        x_features = create_features(file)
        y_features = create_targets(file)
        np.savetxt(
            f"y_{dataset}.txt",
            y_features,
            delimiter="\t",
            header="agbd",
        )
        np.savetxt(
            f"X_{dataset}.txt",
            x_features,
            delimiter="\t"
        )
        print(f"{dataset} set successfully created!")


if __name__ == "__main__":
    main()
