import datetime
import logging
import time
from json.decoder import JSONDecodeError

import aiohttp_cors as aiohttp_cors
from aiohttp.web_response import json_response

from config.config import RestApiServer
from config.rest_api_constant import RouteApiConstant
from errors import ApiBadRequest
from rest_api_server.database.database import Database

LOGGER = logging.getLogger(__name__)


class RouteHandler(object):
    def __init__(self, database=Database()):
        self._database = database

    async def circulating_supply(self, request):
        return json_response(51206064)

    def add_route(self, app):
        app.router.add_get(RestApiServer.API_VERSION + RouteApiConstant.circulating_supply, self.circulating_supply)

        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
        })

        # Configure CORS on all routes.
        for route in list(app.router.routes()):
            cors.add(route)


async def decode_request(request):
    try:
        return await request.json()
    except JSONDecodeError:
        raise ApiBadRequest('Improper JSON format')


def validate_fields(required_fields, body):
    for field in required_fields:
        if body.get(field) is None:
            raise ApiBadRequest(
                "'{}' parameter is required".format(field))


def get_time():
    dts = datetime.datetime.utcnow()
    return round(time.mktime(dts.timetuple()) + dts.microsecond / 1e6)
