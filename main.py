import game_engine
import configuration
import menu_screen


def main():
    '''
    Main function of a program in which everything is being called.
    '''
    config = configuration.Configuration()
    engine = game_engine.GameEngine(config)
    screen = menu_screen.MenuScreen(engine, config)

    engine.set_screen(screen)
    engine.run()


if __name__ == '__main__':
    main()
