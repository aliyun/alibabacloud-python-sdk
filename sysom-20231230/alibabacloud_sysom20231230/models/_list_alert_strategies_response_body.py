# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListAlertStrategiesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAlertStrategiesResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total = total

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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAlertStrategiesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAlertStrategiesResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        enabled: bool = None,
        id: int = None,
        k_8s_label: bool = None,
        name: str = None,
        strategy: main_models.ListAlertStrategiesResponseBodyDataStrategy = None,
        uid: str = None,
        updated_at: int = None,
    ):
        self.created_at = created_at
        self.enabled = enabled
        self.id = id
        self.k_8s_label = k_8s_label
        self.name = name
        self.strategy = strategy
        self.uid = uid
        self.updated_at = updated_at

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.id is not None:
            result['id'] = self.id

        if self.k_8s_label is not None:
            result['k8sLabel'] = self.k_8s_label

        if self.name is not None:
            result['name'] = self.name

        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()

        if self.uid is not None:
            result['uid'] = self.uid

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('k8sLabel') is not None:
            self.k_8s_label = m.get('k8sLabel')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('strategy') is not None:
            temp_model = main_models.ListAlertStrategiesResponseBodyDataStrategy()
            self.strategy = temp_model.from_map(m.get('strategy'))

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class ListAlertStrategiesResponseBodyDataStrategy(DaraModel):
    def __init__(
        self,
        clusters: List[str] = None,
        destinations: List[int] = None,
        items: List[str] = None,
    ):
        self.clusters = clusters
        self.destinations = destinations
        self.items = items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clusters is not None:
            result['clusters'] = self.clusters

        if self.destinations is not None:
            result['destinations'] = self.destinations

        if self.items is not None:
            result['items'] = self.items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')

        if m.get('destinations') is not None:
            self.destinations = m.get('destinations')

        if m.get('items') is not None:
            self.items = m.get('items')

        return self

