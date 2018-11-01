import logging
from mlagents.trainers.trainer import UnityTrainerException

logger = logging.getLogger("mlagents.trainers")


class RewardSignal(object):
    def evaluate(self, current_info, next_info):
        """
        Returns the number of training steps the trainer has performed
        :return: the intrinsic reward provided by the generator
        """
        raise UnityTrainerException("The evaluate function was not implemented.")