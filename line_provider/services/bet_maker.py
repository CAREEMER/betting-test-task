import aiohttp

from core.settings import app_settings


class BetMaker:
    @staticmethod
    async def send_event_update(event_id: str, state: str):
        update_bets_url_path = f"/update-bets/{event_id}/?state={state}"

        async with aiohttp.ClientSession() as session:
            async with session.post(app_settings.bet_maker_url + update_bets_url_path) as response:
                print(await response.text())
