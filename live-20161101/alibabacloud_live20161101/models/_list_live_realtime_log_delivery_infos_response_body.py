# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListLiveRealtimeLogDeliveryInfosResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.ListLiveRealtimeLogDeliveryInfosResponseBodyContent = None,
        request_id: str = None,
    ):
        # Details about the configuration of real-time log delivery.
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
            temp_model = main_models.ListLiveRealtimeLogDeliveryInfosResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLiveRealtimeLogDeliveryInfosResponseBodyContent(DaraModel):
    def __init__(
        self,
        realtime_log_delivery_infos: List[main_models.ListLiveRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos] = None,
    ):
        self.realtime_log_delivery_infos = realtime_log_delivery_infos

    def validate(self):
        if self.realtime_log_delivery_infos:
            for v1 in self.realtime_log_delivery_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RealtimeLogDeliveryInfos'] = []
        if self.realtime_log_delivery_infos is not None:
            for k1 in self.realtime_log_delivery_infos:
                result['RealtimeLogDeliveryInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.realtime_log_delivery_infos = []
        if m.get('RealtimeLogDeliveryInfos') is not None:
            for k1 in m.get('RealtimeLogDeliveryInfos'):
                temp_model = main_models.ListLiveRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos()
                self.realtime_log_delivery_infos.append(temp_model.from_map(k1))

        return self

class ListLiveRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The name of the Logstore to which log entries are delivered.
        self.logstore = logstore
        # The name of the Log Service project that is used for real-time log delivery.
        self.project = project
        # The ID of the region where the Log Service project is deployed.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

