import pytest
from helpers.context import Context


@pytest.fixture(scope='class')
def context(request):
    context = Context()

    def context_teardown():
        context.driver.quit()
    request.addfinalizer(context_teardown)
    return context
