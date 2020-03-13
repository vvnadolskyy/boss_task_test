import os

from kepler import Kepler
from kepler.wrappers import ESLoggingWrapper, SentryWrapper

logging_wrapper = ESLoggingWrapper(
    service_name=os.environ['LOG_SERVICE_NAME'],
    log_level=os.environ['LOG_LEVELNAME'],
    formatter=os.environ['LOG_FORMATTER'],
    es_log_index_name=os.environ['ES_LOG_INDEX_NAME']
)

sentry_wrapper = SentryWrapper(os.environ['SENTRY_DSN'])

kepler_app = Kepler(
    root_directory=__name__,  # where to search for tasks (decorated functions)
    is_production=os.environ['IS_PRODUCTION'],  # do we execute on production now?
    logging_wrapper=logging_wrapper,  # required wrapper for you logs to appear in ES
    sentry_wrapper=sentry_wrapper  # required wrapper for you exception appear in Sentry
)
