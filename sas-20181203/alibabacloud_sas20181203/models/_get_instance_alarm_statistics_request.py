# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceAlarmStatisticsRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        uuid: str = None,
    ):
        # The data source for statistics on instance alarms, with a default value of aqs:
        # - *sas*: Situation Awareness data source
        # - *aqs*: Alarm event data
        # - *honeypot*: Honeypot
        self.from_ = from_
        # The UUID of the server to be queried.
        # > Call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) API to obtain this parameter.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

