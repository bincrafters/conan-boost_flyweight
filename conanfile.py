from conans import ConanFile, tools


class BoostFlyweightConan(ConanFile):
    name = "Boost.Flyweight"
    version = "1.65.1"

    requires = \
        "Boost.Generator/1.65.1@bincrafters/testing", \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Detail/1.65.1@bincrafters/testing", \
        "Boost.Functional/1.65.1@bincrafters/testing", \
        "Boost.Interprocess/1.65.1@bincrafters/testing", \
        "Boost.Mpl/1.65.1@bincrafters/testing", \
        "Boost.Multi_Index/1.65.1@bincrafters/testing", \
        "Boost.Parameter/1.65.1@bincrafters/testing", \
        "Boost.Preprocessor/1.65.1@bincrafters/testing", \
        "Boost.Serialization/1.65.1@bincrafters/testing", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing"

    lib_short_names = ["flyweight"]
    is_header_only = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-flyweight"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    def package_id(self):
        self.info.header_only()

    # END
