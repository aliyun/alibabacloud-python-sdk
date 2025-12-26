# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class Quota(DaraModel):
    def __init__(
        self,
        allocate_strategy: str = None,
        creator_id: str = None,
        description: str = None,
        gmt_created_time: str = None,
        gmt_modified_time: str = None,
        hyper_zones: List[str] = None,
        labels: List[main_models.Label] = None,
        latest_operation_id: str = None,
        min: main_models.ResourceSpec = None,
        parent_quota_id: str = None,
        queue_strategy: str = None,
        quota_cluster: main_models.QuotaCluster = None,
        quota_config: main_models.QuotaConfig = None,
        quota_details: main_models.QuotaDetails = None,
        quota_id: str = None,
        quota_name: str = None,
        reason_code: str = None,
        reason_message: str = None,
        resource_group_ids: List[str] = None,
        resource_type: str = None,
        status: str = None,
        sub_quotas: List[main_models.QuotaIdName] = None,
        version: str = None,
        workspaces: List[main_models.WorkspaceIdName] = None,
    ):
        self.allocate_strategy = allocate_strategy
        self.creator_id = creator_id
        self.description = description
        self.gmt_created_time = gmt_created_time
        self.gmt_modified_time = gmt_modified_time
        self.hyper_zones = hyper_zones
        self.labels = labels
        self.latest_operation_id = latest_operation_id
        self.min = min
        self.parent_quota_id = parent_quota_id
        self.queue_strategy = queue_strategy
        self.quota_cluster = quota_cluster
        self.quota_config = quota_config
        self.quota_details = quota_details
        self.quota_id = quota_id
        self.quota_name = quota_name
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.resource_group_ids = resource_group_ids
        self.resource_type = resource_type
        self.status = status
        self.sub_quotas = sub_quotas
        self.version = version
        self.workspaces = workspaces

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.min:
            self.min.validate()
        if self.quota_cluster:
            self.quota_cluster.validate()
        if self.quota_config:
            self.quota_config.validate()
        if self.quota_details:
            self.quota_details.validate()
        if self.sub_quotas:
            for v1 in self.sub_quotas:
                 if v1:
                    v1.validate()
        if self.workspaces:
            for v1 in self.workspaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_strategy is not None:
            result['AllocateStrategy'] = self.allocate_strategy

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.hyper_zones is not None:
            result['HyperZones'] = self.hyper_zones

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.latest_operation_id is not None:
            result['LatestOperationId'] = self.latest_operation_id

        if self.min is not None:
            result['Min'] = self.min.to_map()

        if self.parent_quota_id is not None:
            result['ParentQuotaId'] = self.parent_quota_id

        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy

        if self.quota_cluster is not None:
            result['QuotaCluster'] = self.quota_cluster.to_map()

        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()

        if self.quota_details is not None:
            result['QuotaDetails'] = self.quota_details.to_map()

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        result['SubQuotas'] = []
        if self.sub_quotas is not None:
            for k1 in self.sub_quotas:
                result['SubQuotas'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        result['Workspaces'] = []
        if self.workspaces is not None:
            for k1 in self.workspaces:
                result['Workspaces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateStrategy') is not None:
            self.allocate_strategy = m.get('AllocateStrategy')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('HyperZones') is not None:
            self.hyper_zones = m.get('HyperZones')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatestOperationId') is not None:
            self.latest_operation_id = m.get('LatestOperationId')

        if m.get('Min') is not None:
            temp_model = main_models.ResourceSpec()
            self.min = temp_model.from_map(m.get('Min'))

        if m.get('ParentQuotaId') is not None:
            self.parent_quota_id = m.get('ParentQuotaId')

        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')

        if m.get('QuotaCluster') is not None:
            temp_model = main_models.QuotaCluster()
            self.quota_cluster = temp_model.from_map(m.get('QuotaCluster'))

        if m.get('QuotaConfig') is not None:
            temp_model = main_models.QuotaConfig()
            self.quota_config = temp_model.from_map(m.get('QuotaConfig'))

        if m.get('QuotaDetails') is not None:
            temp_model = main_models.QuotaDetails()
            self.quota_details = temp_model.from_map(m.get('QuotaDetails'))

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.sub_quotas = []
        if m.get('SubQuotas') is not None:
            for k1 in m.get('SubQuotas'):
                temp_model = main_models.QuotaIdName()
                self.sub_quotas.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k1 in m.get('Workspaces'):
                temp_model = main_models.WorkspaceIdName()
                self.workspaces.append(temp_model.from_map(k1))

        return self

