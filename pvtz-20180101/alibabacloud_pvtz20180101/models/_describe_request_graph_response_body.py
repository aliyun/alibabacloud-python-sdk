# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeRequestGraphResponseBody(DaraModel):
    def __init__(
        self,
        request_details: main_models.DescribeRequestGraphResponseBodyRequestDetails = None,
        request_id: str = None,
    ):
        # The details of the DNS requests.
        self.request_details = request_details
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.request_details:
            self.request_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_details is not None:
            result['RequestDetails'] = self.request_details.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestDetails') is not None:
            temp_model = main_models.DescribeRequestGraphResponseBodyRequestDetails()
            self.request_details = temp_model.from_map(m.get('RequestDetails'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRequestGraphResponseBodyRequestDetails(DaraModel):
    def __init__(
        self,
        zone_request_top: List[main_models.DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop] = None,
    ):
        self.zone_request_top = zone_request_top

    def validate(self):
        if self.zone_request_top:
            for v1 in self.zone_request_top:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ZoneRequestTop'] = []
        if self.zone_request_top is not None:
            for k1 in self.zone_request_top:
                result['ZoneRequestTop'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone_request_top = []
        if m.get('ZoneRequestTop') is not None:
            for k1 in m.get('ZoneRequestTop'):
                temp_model = main_models.DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop()
                self.zone_request_top.append(temp_model.from_map(k1))

        return self

class DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop(DaraModel):
    def __init__(
        self,
        request_count: int = None,
        time: str = None,
        timestamp: int = None,
    ):
        # The number of DNS requests.
        self.request_count = request_count
        # The time when the data was collected. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.time = time
        # The time when the data was collected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_count is not None:
            result['RequestCount'] = self.request_count

        if self.time is not None:
            result['Time'] = self.time

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

