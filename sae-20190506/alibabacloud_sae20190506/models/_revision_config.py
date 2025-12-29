# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class RevisionConfig(DaraModel):
    def __init__(
        self,
        containers: List[main_models.Container] = None,
        enable_arms_metrics: bool = None,
        web_network_config: main_models.WebNetworkConfig = None,
    ):
        # This parameter is required.
        self.containers = containers
        self.enable_arms_metrics = enable_arms_metrics
        self.web_network_config = web_network_config

    def validate(self):
        if self.containers:
            for v1 in self.containers:
                 if v1:
                    v1.validate()
        if self.web_network_config:
            self.web_network_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Containers'] = []
        if self.containers is not None:
            for k1 in self.containers:
                result['Containers'].append(k1.to_map() if k1 else None)

        if self.enable_arms_metrics is not None:
            result['EnableArmsMetrics'] = self.enable_arms_metrics

        if self.web_network_config is not None:
            result['WebNetworkConfig'] = self.web_network_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.containers = []
        if m.get('Containers') is not None:
            for k1 in m.get('Containers'):
                temp_model = main_models.Container()
                self.containers.append(temp_model.from_map(k1))

        if m.get('EnableArmsMetrics') is not None:
            self.enable_arms_metrics = m.get('EnableArmsMetrics')

        if m.get('WebNetworkConfig') is not None:
            temp_model = main_models.WebNetworkConfig()
            self.web_network_config = temp_model.from_map(m.get('WebNetworkConfig'))

        return self

