import asyncio
from aiohttp import ClientSession, ClientConnectorError
from argparse import ArgumentParser, RawDescriptionHelpFormatter


DEFAULT_URL = "http://localhost"
DEFAULT_SIZE = 10


async def visit_url(url: str, session: ClientSession, **kwargs) -> tuple:
    try:
        response = await session.request(method="GET", url=url, **kwargs)
    except ClientConnectorError:
        return (url, 404)
    return (url, response.status)


async def make_requests(url: str, size: int, **kwargs) -> None:
    async with ClientSession() as session:
        tasks = []
        for x in range(size):
            tasks.append(visit_url(url=url, session=session, **kwargs))
        results = await asyncio.gather(*tasks)

    statuses = []
    for result in results:
        statuses.append(result[1])
    print("Sent " + str(size) + " requests of which " + str(100 * statuses.count(200) / size) + "% successful")


def define_arguments():
    description = ("Overwhelm a URL with requests.\nFabio Noris <github.com/fabionoris>")
    example = ("Example:\n  %(prog)s -u https://example.com -s 10")
    parser = ArgumentParser(description=description, epilog=example, formatter_class=RawDescriptionHelpFormatter)
    parser._action_groups.pop()
    optional = parser.add_argument_group('Optional arguments')
    optional.add_argument("-u", "--url", dest="url", type=str, help="The URL to overwhelmed with requests.", default=DEFAULT_URL)
    optional.add_argument("-s", "--size", dest="size", type=int, help="The number of requests to perform.", default=DEFAULT_SIZE)
    return parser.parse_args()


if __name__ == "__main__":
    from sys import version_info

    version_info >= (8, 7), "%(prog)s requires Python 3.7+"

    args = define_arguments()
    asyncio.get_event_loop().run_until_complete(make_requests(url=args.url, size=args.size))
