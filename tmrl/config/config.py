import yaml
import pprint
import numpy as np
import rtgym

import tmrl.config.config_constants as cfg
from tmrl import TrainingOffline
from tmrl.custom.custom_dcac_interfaces import Tm20rtgymDcacInterface
# from tmrl.custom.custom_models import Tm_hybrid_1, TMPolicy
from tmrl.custom.custom_gym_interfaces import (TM2020Interface,
                                               TM2020InterfaceLidar, TMInterface,
                                               TMInterfaceLidar)
from tmrl.custom.custom_memories import (MemoryTM2020RAM, MemoryTMNF,
                                         SeqMemoryTMNFLidar,
                                         TrajMemoryTMNFLidar,
                                         get_local_buffer_sample_lidar,
                                         get_local_buffer_sample_tm20_imgs)
from tmrl.custom.custom_preprocessors import (obs_preprocessor_tm_act_in_obs,
                                              obs_preprocessor_tm_lidar_act_in_obs)
from tmrl.drtac import Agent as DCAC_Agent
from tmrl.drtac_models import Mlp as SV_Mlp
from tmrl.drtac_models import MlpPolicy as SV_MlpPolicy
from tmrl.envs import UntouchedGymEnv
# from tmrl.sac_models import Mlp, MlpPolicy
from tmrl.sac_models import (RNNActorCritic, SquashedGaussianRNNActor)
# from tmrl.sac import SacAgent as SAC_Agent
from tmrl.spinup_sac import SpinupSacAgent as SAC_Agent
from tmrl.util import partial


def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


yaml_content = read_yaml("example.yaml")
pprint.pprint(yaml_content)