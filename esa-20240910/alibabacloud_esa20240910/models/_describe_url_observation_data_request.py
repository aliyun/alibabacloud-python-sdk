# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUrlObservationDataRequest(DaraModel):
    def __init__(
        self,
        client_platform: str = None,
        end_time: str = None,
        metric: str = None,
        site_id: str = None,
        start_time: str = None,
        url: str = None,
    ):
        # The platform of the device. If the parameter is left empty, all devices are queried.
        # 
        # *   PC
        # *   Mobile
        self.client_platform = client_platform
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The time must be in UTC.
        self.end_time = end_time
        # The metric data that is detected.
        # 
        # *   TTFB: Measures the time between when a resource initiates a request and when the first byte of the response starts to arrive.
        # *   FCP: Measures the time between when the page is loaded and when any part of the page\\"s content is rendered on the screen.
        # *   LCP: Reports the rendering time of the largest image or text block visible in the viewport.
        # *   CLS: A metric that measures the maximum layout mutation score for every unexpected layout change that occurs throughout the life of the page.
        # *   INP: Measures the responsiveness of the page, or how long it takes for the page to respond to user input in a visible way.
        # *   FID: Measures the time between when the user first interacts with the page and when the browser is actually able to start processing the event handler in response to that interaction.
        self.metric = metric
        # The website ID, which can be obtained by calling the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The beginning of the time range to query.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The URL of the web page to monitor.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_platform is not None:
            result['ClientPlatform'] = self.client_platform

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientPlatform') is not None:
            self.client_platform = m.get('ClientPlatform')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

