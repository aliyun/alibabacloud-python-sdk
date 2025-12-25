# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateIntegrationPolicyRequest(DaraModel):
    def __init__(
        self,
        entity_group: main_models.CreateIntegrationPolicyRequestEntityGroup = None,
        policy_name: str = None,
        policy_type: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateIntegrationPolicyRequestTags] = None,
        workspace: str = None,
    ):
        # Entity group for creating the policy. Policies can be quickly created using the entity group, and `clusterId` and `vpcId` are independent of each other.
        self.entity_group = entity_group
        # Policy name
        self.policy_name = policy_name
        # Policy type: CS/ECS/Cloud
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Resource tags.
        self.tags = tags
        # Workspace.
        self.workspace = workspace

    def validate(self):
        if self.entity_group:
            self.entity_group.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_group is not None:
            result['entityGroup'] = self.entity_group.to_map()

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.policy_type is not None:
            result['policyType'] = self.policy_type

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityGroup') is not None:
            temp_model = main_models.CreateIntegrationPolicyRequestEntityGroup()
            self.entity_group = temp_model.from_map(m.get('entityGroup'))

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateIntegrationPolicyRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class CreateIntegrationPolicyRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag `key` value.
        self.key = key
        # Tag `value` value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreateIntegrationPolicyRequestEntityGroup(DaraModel):
    def __init__(
        self,
        cluster_entity_type: str = None,
        cluster_id: str = None,
        disable_policy_share: bool = None,
        entity_group_id: str = None,
        entity_user_id: str = None,
        vpc_id: str = None,
    ):
        # Cluster entity type, such as acs.ack.cluster/acs.one.cluster/acs.asi.cluster or others.
        self.cluster_entity_type = cluster_entity_type
        # Cluster ID.
        self.cluster_id = cluster_id
        # Whether to disable the unique binding of the Policy. If enabled, multiple Policies can be created for a single container cluster.
        self.disable_policy_share = disable_policy_share
        # Entity group ID.
        self.entity_group_id = entity_group_id
        # User ID to which the cluster belongs.
        self.entity_user_id = entity_user_id
        # VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_entity_type is not None:
            result['clusterEntityType'] = self.cluster_entity_type

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.disable_policy_share is not None:
            result['disablePolicyShare'] = self.disable_policy_share

        if self.entity_group_id is not None:
            result['entityGroupId'] = self.entity_group_id

        if self.entity_user_id is not None:
            result['entityUserId'] = self.entity_user_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterEntityType') is not None:
            self.cluster_entity_type = m.get('clusterEntityType')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('disablePolicyShare') is not None:
            self.disable_policy_share = m.get('disablePolicyShare')

        if m.get('entityGroupId') is not None:
            self.entity_group_id = m.get('entityGroupId')

        if m.get('entityUserId') is not None:
            self.entity_user_id = m.get('entityUserId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

