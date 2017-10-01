import math
import subprocess

def event_hour_transform(h_value):
    value = math.cos(2*math.pi*(h_value-6)/24)
    return value


def label_attendance(attend):
    if attend == 'yes' or attend == 'waitlist':
        return 1
    else:
        return 0


def lat_lon_similarity(lat1, lon1, lat2, lon2):
    lat_diff = lat1-lat2
    lon_diff = lon1-lon2
    sim = (lat_diff**2+lon_diff**2)**(0.5)
    return sim


def visualize_tree(clf, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("dt.dot", 'w') as f:
        tree.export_graphviz(clf, out_file=f,
                        feature_names=feature_names)

    command = ["dot", "-Tpng", "dt.dot", "-o", "./dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")