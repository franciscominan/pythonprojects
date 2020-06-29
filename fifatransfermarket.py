class Club:
    def __init__(self, name, funds, squad, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.name = name
        self.funds = funds
        self.squad = squad

    def info(self):
        return f'Club Info:\nName: {self.name}\nFunds: ${self.funds} M'

    def show_squad(self):
        return self.squad

    def sell_player(self, player):
        self.funds += self.squad[player.title()]
        del self.squad[player.title()]
        return f'Transfer Complete. {player.title()} was removed from your squad.'

    def buy_player(self, player, value):
        self.funds -= value
        self.squad.update({player.title(): value})
        return f'Transfer complete. {player.title()} was added to your squad.'


class RealMadrid(Club):
    def __init__(self):
        info = {
            'name': 'Real Madrid C.F.',
            'funds': 1000,
            'squad': {
                'Courtois': 100, 'Marcelo': 80, 'Ramos': 80,
                'Varane': 70, 'Carvajal': 60, 'Casemiro': 90,
                'Valverde': 70, 'Isco': 100, 'Bale': 90,
                'Hazard': 120, 'Benzema': 100
            }
        }
        super().__init__(**info)


real_madrid = RealMadrid()
print(real_madrid.buy_player('messi', 200))
print(real_madrid.info())
print(real_madrid.show_squad())
print(real_madrid.sell_player('hazard'))
print(real_madrid.show_squad())


class Barcelona(Club):
    def __init__(self):
        info = {
            'name': 'FC Barcelona',
            'funds': 1000,
            'squad': {
                'Ter Stegen': 90, 'Jordi Alba': 80, 'Umiti': 80,
                'Pique': 90, 'Sergi Roberto': 80, 'de Jong': 150,
                'Rakitic': 60, 'Busquets': 90, 'Griezmann': 120,
                'Suarez': 80, 'Messi': 200
            }
        }
        super().__init__(**info)
