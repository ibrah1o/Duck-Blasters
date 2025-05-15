import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
ACTION = pygame.event.custom_type()  # our custom event that contains an action
clock = pygame.time.Clock()


def main():
    shield = 0

    # function to activate the shield
    # note that shield is NOT just a boolean flag,
    # but an integer. Everytime we activate the shield,
    # we increment it by 1. If we want to deactivate the
    # shield later, we can test if the deactivate event
    # is the latest one. If not, then nothing should happen.
    def activate_shield():
        nonlocal shield
        shield += 1
        return shield

    # function that creates the function that is triggered
    # after some time. It's nested so we can pass and capture
    # the id variable to check if the event is actually the
    # last deactivate event. If so, we reset shield to 0.
    def remove_shield(id):
        def action():
            nonlocal shield
            if shield == id:
                shield = 0

        return action

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return

            if e.type == pygame.KEYDOWN:
                # activate the shield
                id = activate_shield()
                # deactivate it 2000ms in the future
                # pygame will post this event into the event queue at the right time
                pygame.time.set_timer(pygame.event.Event(ACTION, action=remove_shield(id)), 2000, 1)

            if e.type == ACTION:
                # if there's an ACTION event, invoke its action!!!
                e.action()

        screen.fill('black')

        # is the shield active?
        if shield:
            pygame.draw.circle(screen, 'red', (320, 220), 35, 4)

        # our green little guy
        pygame.draw.rect(screen, 'green', (300, 200, 40, 40))
        pygame.display.flip()
        clock.tick(60)


main()