import warnings
from decorators.deprecated import deprecated


@deprecated(reason="Use new_func instead")
def old_func():
    return "legacy"


def test_deprecated_warns():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = old_func()
        assert result == "legacy"
        assert any("deprecated" in str(warning.message).lower()
                   for warning in w)
