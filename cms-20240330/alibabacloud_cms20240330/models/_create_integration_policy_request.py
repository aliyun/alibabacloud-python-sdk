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
        # The entity group used to create the policy. You can quickly create a policy using an entity group. The clusterId and vpcId parameters are independent of each other.
        self.entity_group = entity_group
        # The policy name.
        self.policy_name = policy_name
        # The policy type. Valid values: CS, ECS, and Cloud.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource tags.
        self.tags = tags
        # The workspace.
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
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        cluster_namespace: str = None,
        disable_policy_share: bool = None,
        entity_group_id: str = None,
        entity_user_id: str = None,
        vpc_id: str = None,
    ):
        # The cluster entity type. Examples: acs.ack.cluster, acs.one.cluster, and acs.asi.cluster.
        self.cluster_entity_type = cluster_entity_type
        # The cluster ID.
        self.cluster_id = cluster_id
        self.cluster_namespace = cluster_namespace
        # Specifies whether to disable unique policy binding. If this parameter is set to true, you can create multiple policies for a container cluster.
        self.disable_policy_share = disable_policy_share
        # The entity group ID.
        self.entity_group_id = entity_group_id
        # The ID of the user who owns the cluster.
        self.entity_user_id = entity_user_id
        # The virtual private cloud (VPC) ID.
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

        if self.cluster_namespace is not None:
            result['clusterNamespace'] = self.cluster_namespace

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

        if m.get('clusterNamespace') is not None:
            self.cluster_namespace = m.get('clusterNamespace')

        if m.get('disablePolicyShare') is not None:
            self.disable_policy_share = m.get('disablePolicyShare')

        if m.get('entityGroupId') is not None:
            self.entity_group_id = m.get('entityGroupId')

        if m.get('entityUserId') is not None:
            self.entity_user_id = m.get('entityUserId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

