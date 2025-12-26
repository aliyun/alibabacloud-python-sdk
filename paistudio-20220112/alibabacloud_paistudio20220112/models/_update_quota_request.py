# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class UpdateQuotaRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        labels: List[main_models.Label] = None,
        queue_strategy: str = None,
        quota_config: main_models.QuotaConfig = None,
        quota_name: str = None,
    ):
        self.description = description
        self.labels = labels
        self.queue_strategy = queue_strategy
        self.quota_config = quota_config
        self.quota_name = quota_name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.quota_config:
            self.quota_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy

        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')

        if m.get('QuotaConfig') is not None:
            temp_model = main_models.QuotaConfig()
            self.quota_config = temp_model.from_map(m.get('QuotaConfig'))

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        return self

