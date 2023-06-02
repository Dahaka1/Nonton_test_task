from typing import Sized


def test_input(*args: Sized) -> None:
	assert all(len(arg) in [0, 2] for arg in args), \
		"It needs to create empty instances or by choosing all of args/kwargs in amount 2"
