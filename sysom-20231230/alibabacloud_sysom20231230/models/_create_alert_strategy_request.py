# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class CreateAlertStrategyRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        k_8s_label: bool = None,
        name: str = None,
        strategy: main_models.CreateAlertStrategyRequestStrategy = None,
    ):
        # This parameter is required.
        self.enabled = enabled
        self.k_8s_label = k_8s_label
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.strategy = strategy

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.k_8s_label is not None:
            result['k8sLabel'] = self.k_8s_label

        if self.name is not None:
            result['name'] = self.name

        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('k8sLabel') is not None:
            self.k_8s_label = m.get('k8sLabel')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('strategy') is not None:
            temp_model = main_models.CreateAlertStrategyRequestStrategy()
            self.strategy = temp_model.from_map(m.get('strategy'))

        return self

class CreateAlertStrategyRequestStrategy(DaraModel):
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

