# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeUserEventTypeResponseBody(DaraModel):
    def __init__(
        self,
        event: List[main_models.DescribeUserEventTypeResponseBodyEvent] = None,
        request_id: str = None,
    ):
        # The types and statistics of security events.
        self.event = event
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.event:
            for v1 in self.event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Event'] = []
        if self.event is not None:
            for k1 in self.event:
                result['Event'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event = []
        if m.get('Event') is not None:
            for k1 in m.get('Event'):
                temp_model = main_models.DescribeUserEventTypeResponseBodyEvent()
                self.event.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserEventTypeResponseBodyEvent(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_count: int = None,
        event_parent_type: str = None,
        event_type: str = None,
    ):
        # The code of the security event.
        self.event_code = event_code
        # The number of events.
        self.event_count = event_count
        # The parent type of the security event.
        self.event_parent_type = event_parent_type
        # The type of the security event.
        # 
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported types of security events.
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.event_parent_type is not None:
            result['EventParentType'] = self.event_parent_type

        if self.event_type is not None:
            result['EventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('EventParentType') is not None:
            self.event_parent_type = m.get('EventParentType')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        return self

