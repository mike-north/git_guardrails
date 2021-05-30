import pytest
from click.testing import CliRunner
from git_guardrails.command_line import main, validate
import git_guardrails.__main__ # noqa


# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


def test_root_entry():
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
    assert result.output == """Usage: main [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  validate  Examine the current Git workspace and perform some sanity-checking
"""


def test_validate_help():
    runner = CliRunner()
    result = runner.invoke(validate, ['--help'])
    assert result.exit_code == 0
    assert result.output == """Usage: validate [OPTIONS]

  Examine the current Git workspace and perform some sanity-checking

Options:
  -v, --verbose / --no-verbose
  --cwd TEXT
  --current-branch TEXT
  --color / --no-color
  --tty / --no-tty
  --help                        Show this message and exit.
"""