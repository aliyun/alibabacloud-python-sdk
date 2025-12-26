# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class CreateQuotaRequest(DaraModel):
    def __init__(
        self,
        allocate_strategy: str = None,
        cluster_spec: main_models.ClusterSpec = None,
        description: str = None,
        labels: List[main_models.Label] = None,
        min: main_models.ResourceSpec = None,
        parent_quota_id: str = None,
        queue_strategy: str = None,
        quota_config: main_models.QuotaConfig = None,
        quota_name: str = None,
        resource_group_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.allocate_strategy = allocate_strategy
        self.cluster_spec = cluster_spec
        self.description = description
        self.labels = labels
        self.min = min
        self.parent_quota_id = parent_quota_id
        self.queue_strategy = queue_strategy
        self.quota_config = quota_config
        self.quota_name = quota_name
        self.resource_group_ids = resource_group_ids
        self.resource_type = resource_type

    def validate(self):
        if self.cluster_spec:
            self.cluster_spec.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.min:
            self.min.validate()
        if self.quota_config:
            self.quota_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_strategy is not None:
            result['AllocateStrategy'] = self.allocate_strategy

        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec.to_map()

        if self.description is not None:
            result['Description'] = self.description

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.min is not None:
            result['Min'] = self.min.to_map()

        if self.parent_quota_id is not None:
            result['ParentQuotaId'] = self.parent_quota_id

        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy

        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateStrategy') is not None:
            self.allocate_strategy = m.get('AllocateStrategy')

        if m.get('ClusterSpec') is not None:
            temp_model = main_models.ClusterSpec()
            self.cluster_spec = temp_model.from_map(m.get('ClusterSpec'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Min') is not None:
            temp_model = main_models.ResourceSpec()
            self.min = temp_model.from_map(m.get('Min'))

        if m.get('ParentQuotaId') is not None:
            self.parent_quota_id = m.get('ParentQuotaId')

        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')

        if m.get('QuotaConfig') is not None:
            temp_model = main_models.QuotaConfig()
            self.quota_config = temp_model.from_map(m.get('QuotaConfig'))

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

