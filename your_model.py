# This is where the interfaces to your model should be. Please edit the functions below and add whatever is needed
# for your model to work


def get_model():
    return {'time': 0}


def get_features(model, patient_id):
    return model['time']


def get_estimate(features):
    return features + 500


def update_state(model, event):
    model['time'] = event.time
