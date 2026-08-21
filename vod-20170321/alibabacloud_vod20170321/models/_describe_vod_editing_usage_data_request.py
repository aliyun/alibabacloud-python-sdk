# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodEditingUsageDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        owner_id: int = None,
        region: str = None,
        specification: str = None,
        start_time: str = None,
    ):
        # The application ID. For more information, see [Multi-application](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time must be in UTC.
        self.end_time = end_time
        self.owner_id = owner_id
        # The region. By default, data from all regions is returned. You can specify multiple regions separated by commas (,).
        self.region = region
        # The output specification.
        self.specification = specification
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time must be in UTC.
        # 
        # If you leave this parameter empty, data from the last 24 hours is queried by default.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

