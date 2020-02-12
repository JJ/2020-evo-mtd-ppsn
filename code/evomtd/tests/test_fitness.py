from evomtd.fitness import *
from evomtd.genetic import *
from evomtd.config.nginx import *

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

@mock.patch('evomtd.fitness.calculate_fitness', return_value=random.randint(0,999))
def test_fitness( function ):
    config = generate_random_config()
    this_fitness = calculate_fitness(config)
    assert(this_fitness)
    assert(this_fitness > 0)
