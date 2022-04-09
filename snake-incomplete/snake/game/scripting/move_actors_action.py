from game.scripting.action import Action


class MoveActorsAction(Action):
  def execute(self, cast, script):
  # Override the execute(cast, script) method as follows:
    # 1) get all the actors from the cast
    actors = cast.get_all_actors()
    # 2) loop through the actors
    for actor in actors:
    # 3) call the move_next() method on each actor
      actor.move_next()