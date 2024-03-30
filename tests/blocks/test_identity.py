import pytest

from scoutos.blocks import Block, Identity


def initialize_identity_block():
    default_config = {
        "key": "this_block_key",
    }

    return Identity(**default_config)


def test_loading():
    block = initialize_identity_block()

    assert isinstance(block, Identity)
    assert isinstance(block, Block)
    assert block.key == "this_block_key"


@pytest.mark.parametrize(
    "run_input",
    [
        {"one": 1},
        {"one": 1, "too": "also"},
    ],
)
def test_run(run_input):
    block = initialize_identity_block()
    result = block.run(run_input)

    assert result == run_input