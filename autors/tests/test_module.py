
class Test_models_authors:
    def test_models_take_valus(self, autors_fixture):
        assert autors_fixture.name == "jan"