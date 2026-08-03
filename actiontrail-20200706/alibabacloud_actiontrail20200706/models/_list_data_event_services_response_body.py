# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class ListDataEventServicesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataEventServicesResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDataEventServicesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataEventServicesResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        service_infos: List[main_models.ListDataEventServicesResponseBodyDataServiceInfos] = None,
    ):
        # The maximum number of entries returned for the current request.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The supported Alibaba Cloud services and the data events for each service.
        self.service_infos = service_infos

    def validate(self):
        if self.service_infos:
            for v1 in self.service_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k1 in self.service_infos:
                result['ServiceInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k1 in m.get('ServiceInfos'):
                temp_model = main_models.ListDataEventServicesResponseBodyDataServiceInfos()
                self.service_infos.append(temp_model.from_map(k1))

        return self

class ListDataEventServicesResponseBodyDataServiceInfos(DaraModel):
    def __init__(
        self,
        event_names: List[str] = None,
        service_name: str = None,
    ):
        # The data events supported by the service.
        self.event_names = event_names
        # The cloud service name.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_names is not None:
            result['EventNames'] = self.event_names

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventNames') is not None:
            self.event_names = m.get('EventNames')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

