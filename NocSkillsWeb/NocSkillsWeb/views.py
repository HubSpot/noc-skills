import requests
import logging

from django.shortcuts import render
from django.template import loader, RequestContext
from django.conf import settings
from django.http import HttpResponseServerError


logger = logging.getLogger(__name__)


def index(request):
    url = "http://%s:%i/list" % (settings.NOC_SKILLS_API_HOST, settings.NOC_SKILLS_API_PORT)
    try:
        r = requests.get(url)
    except requests.ConnectionError, e:
        logger.error("Unable to load list of data from %s: %s" % (url, e))
        return HttpResponseServerError("<h1>Backend Data Error</h1><p>Unable to connect to the back-end service at %s" % (url))
    except requests.Timeout, e:
        logger.error("Requesting data from %s timed out: %s" % (url, e))
        return HttpResponseServerError("<h1>Data Retrieval Timed Out</h1><p>Accessing back-end service timed out")
    reasons = r.json()
    logger.info("Reasons: %s" % (reasons))
    return render(request, 'index.html', {'reasons': reasons})