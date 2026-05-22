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
        self.client_platform = client_platform
        self.end_time = end_time
        self.metric = metric
        # This parameter is required.
        self.site_id = site_id
        self.start_time = start_time
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

