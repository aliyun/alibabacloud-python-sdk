# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDDoSStatusResponseBody(DaraModel):
    def __init__(
        self,
        ddo_sstatus: List[main_models.DescribeDDoSStatusResponseBodyDDoSStatus] = None,
        request_id: str = None,
    ):
        # Indicates whether DDoS attacks occur on specific domain names.
        self.ddo_sstatus = ddo_sstatus
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ddo_sstatus:
            for v1 in self.ddo_sstatus:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DDoSStatus'] = []
        if self.ddo_sstatus is not None:
            for k1 in self.ddo_sstatus:
                result['DDoSStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddo_sstatus = []
        if m.get('DDoSStatus') is not None:
            for k1 in m.get('DDoSStatus'):
                temp_model = main_models.DescribeDDoSStatusResponseBodyDDoSStatus()
                self.ddo_sstatus.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDDoSStatusResponseBodyDDoSStatus(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        status: str = None,
    ):
        # The type of events that are triggered by DDoS attacks. Valid values:
        # 
        # *   defense: traffic scrubbing events.
        # *   blackhole: blackhole filtering events.
        self.event_type = event_type
        # Indicates whether DDoS attacks occur on specific domain names. Valid value:
        # 
        # *   **doing**: DDoS attacks occur on specific domain names.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

