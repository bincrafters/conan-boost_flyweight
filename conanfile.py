#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostFlyweightConan(base.BoostBaseConan):
    name = "boost_flyweight"
    url = "https://github.com/bincrafters/conan-boost_flyweight"
    lib_short_names = ["flyweight"]
    header_only_libs = ["flyweight"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_interprocess",
        "boost_mpl",
        "boost_multi_index",
        "boost_parameter",
        "boost_preprocessor",
        "boost_serialization",
        "boost_smart_ptr",
        "boost_throw_exception",
        "boost_type_traits"
    ]


