import arcade

from player import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = 'PIF GAME'

CARD_SCALING = 0.25

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CADET_BLUE)

        self.cards_player_list = None

    def setup(self):
        self.cards_player_list = arcade.SpriteList()

        self.build_player_cards()


    def build_player_cards(self):

        position_x = 300
        angle = 40
        y = 1
        initial_position_y = 200

        positions_y = {
            1:initial_position_y, 2:initial_position_y + 20,
            3:initial_position_y + 40, 4:initial_position_y + 40,
            5:initial_position_y + 40, 6:initial_position_y + 30,
            7:initial_position_y + 10, 8:initial_position_y - 20,
            9:initial_position_y - 50
        }

        for card in player_cards:

            position_y = positions_y[y]

            card_name = 'CARDS/' + card[0] + '_' + card[1] + '.png'
            self.cards_player = arcade.Sprite(card_name, CARD_SCALING)
            self.cards_player.center_x = position_x
            self.cards_player.center_y = position_y
            self.cards_player.angle = angle
            self.cards_player_list.append(self.cards_player)

            position_x += 50
            y += 1
            angle -= 10

    def on_draw(self):
        arcade.start_render()

        self.cards_player_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()