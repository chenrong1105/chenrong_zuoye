import yaml

class Testgetdatas:
    def test_get_adddatas(self):
        with open("datas/calc_add.yml", encoding="utf-8") as f:
            self.mydatas = yaml.safe_load(f)
            self.adddatas = self.mydatas['add']['datas']
            self.addmyids = self.mydatas['add']['myids']
            return [self.adddatas,self.addmyids]

    def test_get_subdatas(self):
        with open("datas/calc_sub.yml", encoding="utf-8") as f:
            self.mydatas = yaml.safe_load(f)
            self.subdatas = self.mydatas['sub']['datas']
            self.submyids = self.mydatas['sub']['myids']
            return [self.subdatas,self.submyids]

    def test_get_muldatas(self):
        with open("datas/calc_mul.yml", encoding="utf-8") as f:
            self.mydatas = yaml.safe_load(f)
            self.muldatas = self.mydatas['mul']['datas']
            self.mulmyids = self.mydatas['mul']['myids']
            return [self.muldatas,self.mulmyids]

    def test_get_divdatas(self):
        with open("datas/calc_div.yml", encoding="utf-8") as f:
            self.mydatas = yaml.safe_load(f)
            self.divdatas = self.mydatas['div']['datas']
            self.divmyids = self.mydatas['div']['myids']
            return [self.divdatas,self.divmyids]