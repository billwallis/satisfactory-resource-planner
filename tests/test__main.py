from satisfactory_resource_planner import main


def test__main__happy_path():
    assert main.main() == 0
