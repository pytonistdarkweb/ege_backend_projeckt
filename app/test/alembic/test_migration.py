from alembic.command import downgrade, upgrade
import pytest
from alembic.config import Config
from alembic.script import Script, ScriptDirectory


def get_revisions() -> list[Script]:
    # Получаем директорию с миграциями alembic
    config = Config()
    config.set_main_option("script_location", "app/db/alembic")
    revisions_dir = ScriptDirectory.from_config(config)
    # Получаем миграции и сортируем в порядке от первой до последней
    revisions = list(revisions_dir.walk_revisions("base", "heads"))
    revisions.reverse()
    return revisions


def _do_upgrade_downgrade_upgrade(config: Config, rev_up: str, rev_down: str) -> None:
    upgrade(config, rev_up)
    downgrade(config, rev_down)
    upgrade(config, rev_up)


@pytest.mark.parametrize("revision", get_revisions())
def test_migrations_stairway(alembic_config: Config, revision: Script) -> None:
    rev_up = revision.revision
    if isinstance(revision.down_revision, tuple):
        # у merge-миграций в родителях указаны нескольк миграции поэтому пробуем провести миграцию для каждой ветви
        for rev_down in revision.down_revision:
            _do_upgrade_downgrade_upgrade(alembic_config, rev_up, rev_down)
    else:
        # -1 используется для downgrade первой миграции (т.к. ее down_revision равен None)
        rev_down = revision.down_revision if revision.down_revision is not None else "-1"
        _do_upgrade_downgrade_upgrade(alembic_config, rev_up, rev_down)