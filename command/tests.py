from automation.factories import commander
import asyncio
# Create your tests here.''


class CommandTest():
    def run(self, function_id, args):

        from .models import Command, Function

        f = Function.objects.get(id=function_id)
        cmd = Command()
        cmd.function = f
        cmd.args = args
        commander.run(cmd)


class FunctionTest():
    def __init__(self):
        # self.loop = asyncio.get_event_loop()
        pass

    def callback(self, message):
        print(message)

    async def run_async_test(self):
        from command.functions import test_function_async
        args = ['hello', 5, self.callback]
        asyncio.create_task(test_function_async(*args))
        # await asyncio.sleep(4)
        print("We have run the code")

    def run(self):
        loop = asyncio.get_event_loop()
        print("We are about to run, yeess")
        loop.run_until_complete(self.run_async_test())
