from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import make_pipeline
import numpy as np


class Oversampler:

    def __init__(self):
        self.sampler = RandomOverSampler(random_state=0)

    def oversample(self, features, labels):
        features = np.array(features)
        features = features.reshape(-1, 1)
        featuresOversampled, labelsOversampled = self.sampler.fit_resample(features, labels)

        return featuresOversampled, labelsOversampled

