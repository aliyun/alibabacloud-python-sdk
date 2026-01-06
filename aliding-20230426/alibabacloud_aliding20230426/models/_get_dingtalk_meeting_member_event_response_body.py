# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetDingtalkMeetingMemberEventResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetDingtalkMeetingMemberEventResponseBodyData] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetDingtalkMeetingMemberEventResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetDingtalkMeetingMemberEventResponseBodyData(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        event_name: str = None,
        event_type: str = None,
        ts: int = None,
    ):
        self.event_id = event_id
        self.event_name = event_name
        self.event_type = event_type
        self.ts = ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.ts is not None:
            result['ts'] = self.ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('ts') is not None:
            self.ts = m.get('ts')

        return self

