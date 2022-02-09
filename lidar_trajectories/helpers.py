def data_to_tracks(datadict):
    """
    Convert frame oriented dictionary to
    track oriented dictionary
    """
    tracks = None
    return tracks


def det_region_to_utm(region, angle, origin):
    """
    Converts the detection region from sensor coordinates
    to utm
    inputs:
        region - 2d list describing the detection region
        angle - rotation angle
        origin - new position of coordinate origin (0, 0)
    output:
        region_utm - region rotated and translated to origin
    """
    region_utm = None
    return region_utm


def track_to_utm(track, angle, origin):
    """
    Converts track x,y data from sensor coordinates
    to UTM coordinates
    inputs:
        track - a data structure that contains x and y of a track
        angle - rotation angle
        origin - new position of coordinate origin (0, 0)
    output:
        track_utm - track data rotated and translated to origin
    """
    track_utm = None
    return track_utm


if __name__ == "__main__":
    pass
