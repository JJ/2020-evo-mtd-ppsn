import evomtd.fitness
import evomtd.genetic
import evomtd.config.nginx

"""Pytest TDD Test definition file"""
__author__ = "Ernesto Serrano"
__license__ = "GPLv3"
__email__ = "erseco@correo.ugr.es"


def test_generate_random_config_len():
    """Test generation of random config"""
    config = generate_random_config()
    assert(isinstance(config, list))
    assert(len(config) == genetic.genes)

def test_fitness():
    config = generate_random_config()
    this_fitness = calculate_fitness(config)
    assert(this_fitness)
    assert(this_fitness == 999)
