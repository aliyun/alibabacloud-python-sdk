# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class ListRealtimeLogDeliveryResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.ListRealtimeLogDeliveryResponseBodyContent = None,
        request_id: str = None,
    ):
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.ListRealtimeLogDeliveryResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRealtimeLogDeliveryResponseBodyContent(DaraModel):
    def __init__(
        self,
        realtime_log_delivery_info: List[main_models.ListRealtimeLogDeliveryResponseBodyContentRealtimeLogDeliveryInfo] = None,
    ):
        self.realtime_log_delivery_info = realtime_log_delivery_info

    def validate(self):
        if self.realtime_log_delivery_info:
            for v1 in self.realtime_log_delivery_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RealtimeLogDeliveryInfo'] = []
        if self.realtime_log_delivery_info is not None:
            for k1 in self.realtime_log_delivery_info:
                result['RealtimeLogDeliveryInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.realtime_log_delivery_info = []
        if m.get('RealtimeLogDeliveryInfo') is not None:
            for k1 in m.get('RealtimeLogDeliveryInfo'):
                temp_model = main_models.ListRealtimeLogDeliveryResponseBodyContentRealtimeLogDeliveryInfo()
                self.realtime_log_delivery_info.append(temp_model.from_map(k1))

        return self

class ListRealtimeLogDeliveryResponseBodyContentRealtimeLogDeliveryInfo(DaraModel):
    def __init__(
        self,
        dm_id: int = None,
        domain: str = None,
        logstore: str = None,
        project: str = None,
        region: str = None,
        status: str = None,
    ):
        self.dm_id = dm_id
        self.domain = domain
        self.logstore = logstore
        self.project = project
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dm_id is not None:
            result['DmId'] = self.dm_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.region is not None:
            result['Region'] = self.region

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DmId') is not None:
            self.dm_id = m.get('DmId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

