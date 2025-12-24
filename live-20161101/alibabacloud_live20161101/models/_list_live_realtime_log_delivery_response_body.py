# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListLiveRealtimeLogDeliveryResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.ListLiveRealtimeLogDeliveryResponseBodyContent = None,
        request_id: str = None,
    ):
        # The configurations of real-time log delivery.
        self.content = content
        # The request ID.
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
            temp_model = main_models.ListLiveRealtimeLogDeliveryResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLiveRealtimeLogDeliveryResponseBodyContent(DaraModel):
    def __init__(
        self,
        realtime_log_delivery_info: List[main_models.ListLiveRealtimeLogDeliveryResponseBodyContentRealtimeLogDeliveryInfo] = None,
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
                temp_model = main_models.ListLiveRealtimeLogDeliveryResponseBodyContentRealtimeLogDeliveryInfo()
                self.realtime_log_delivery_info.append(temp_model.from_map(k1))

        return self

class ListLiveRealtimeLogDeliveryResponseBodyContentRealtimeLogDeliveryInfo(DaraModel):
    def __init__(
        self,
        dm_id: int = None,
        domain_name: str = None,
        logstore: str = None,
        project: str = None,
        region: str = None,
        status: str = None,
    ):
        # The ID of the domain name.
        self.dm_id = dm_id
        # The streaming domain.
        self.domain_name = domain_name
        # The name of the Logstore to which log entries are delivered.
        self.logstore = logstore
        # The name of the Log Service project that is used for real-time log delivery.
        self.project = project
        # The ID of the region where the Log Service project is deployed.
        self.region = region
        # The status of real-time log delivery. Valid values:
        # 
        # *   **online**: enabled
        # *   **offline**: disabled
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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

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

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

