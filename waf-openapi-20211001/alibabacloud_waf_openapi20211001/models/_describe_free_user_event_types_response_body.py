# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeFreeUserEventTypesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeFreeUserEventTypesResponseBodyData] = None,
        request_id: str = None,
    ):
        # The types of security events on which basic detection is performed.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeFreeUserEventTypesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFreeUserEventTypesResponseBodyData(DaraModel):
    def __init__(
        self,
        event_num: str = None,
        event_type: str = None,
    ):
        # The number of security events.
        self.event_num = event_num
        # The type of the security event.
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_num is not None:
            result['EventNum'] = self.event_num

        if self.event_type is not None:
            result['EventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventNum') is not None:
            self.event_num = m.get('EventNum')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        return self

