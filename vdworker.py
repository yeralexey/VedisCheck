from vedis import Vedis
import config
import traceback
import datetime


async def get_user_attribute(user_id, attribute):
    with Vedis(config.main_db_file) as db:
        try:
            result = db[f'{user_id}{attribute}'].decode()
        except KeyError:
            result = None
        except:
            result = False
            save_traceback(str(traceback.format_exc()))
    return result


async def write_user_attribute(user_id, attribute, data):
    with Vedis(config.main_db_file) as db:
        try:
            db[f'{user_id}{attribute}'] = data
            result = True
        except:
            result = False
            save_traceback(str(traceback.format_exc()))
    return result


def save_traceback(traceback_data: str):
    try:
        with open(config.db_fail_log, "a", encoding="utf-8") as file:
            file.write(f"\n----------------------------------\n{datetime.datetime.now()}\n{traceback_data:}")
    except:
        pass
