import aiohttp

from core.settings import app_settings


class LineProvider:
    async def get_events(self):
        list_events_path_url = "/events"

        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get(app_settings.line_provider_url + list_events_path_url) as events_list_response:
                return await events_list_response.json()
