from evomtd.config.nginx import generate_random_config
from evomtd.fitness import calculate_fitness
from evomtd.genetic import genes

import random
import mock

"""Pytest TDD Test definition file"""
__author__ = "Ernesto Serrano"
__license__ = "GPLv3"
__email__ = "erseco@correo.ugr.es"


def test_generate_random_config_len():
    """Test generation of random config"""
    config = generate_random_config()
    assert(isinstance(config, list))
    assert(len(config) == genes)

@mock.patch('evomtd.fitness.calculate_fitness',return_value=33)
def test_fitness( function ):
    config = generate_random_config()
    print(function(config))
    this_fitness = function(config)
    assert(this_fitness)
    assert(this_fitness > 0)
