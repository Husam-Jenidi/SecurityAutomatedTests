#!/usr/bin/env python3
import asyncio
import requests

WHOAMI_ORACLE = "andreavalenza"

test_values = {
    'semicolon': ';whoami',
    'ampersand': '&whoami',
    'logical AND': '&&whoami',
    'pipe': '|whoami',
    'logical OR': '||whoami',
    'subshell': '$(whoami)',
}

async def test_step(test_name, test_value, file_name):
    cookies = { 'a': '1' }
    headers = { }
    params = {
        'host': test_value,
        'file': file_name,
    }
    response = await loop.run_in_executor(None, requests.get, 'http://localhost:4000/application/' + params["file"] + '?host=' + test_value)
    print(response.text)
    test_result = not WHOAMI_ORACLE in response.text
    print (test_result)

    print("{} {}: {}".format("\u2705" if test_result else "\u274c", test_name, file_name))

async def main():
    file_names = ["ping.php", "ping-no-scape.php","ping-no-semicol.php","ping-no-pipe.php","ping-no-output.php","ping-no-amp.php","ping-escapeshellcmd.php","echo.php","echo-name.php"]
    tasks = []
    for file_name in file_names:
        for test_name, test_value in test_values.items():
            tasks.append(asyncio.ensure_future(test_step(test_name, test_value, file_name)))
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
