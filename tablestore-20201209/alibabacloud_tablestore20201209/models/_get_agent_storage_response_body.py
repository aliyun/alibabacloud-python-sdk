# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class GetAgentStorageResponseBody(DaraModel):
    def __init__(
        self,
        agent_storage_description: str = None,
        agent_storage_name: str = None,
        agent_storage_specification: str = None,
        agent_storage_status: str = None,
        alias_name: str = None,
        create_time: str = None,
        network_source_acl: List[str] = None,
        network_type_acl: List[str] = None,
        policy: str = None,
        policy_version: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.GetAgentStorageResponseBodyTags] = None,
        user_id: str = None,
    ):
        # agent storage description
        self.agent_storage_description = agent_storage_description
        # agent storage name
        self.agent_storage_name = agent_storage_name
        # The specification of the agent storage.
        self.agent_storage_specification = agent_storage_specification
        # The status of the agent storage. Valid values:
        # - normal: Normal.
        # - forbidden: Disabled.
        # - deleting: Being released.
        self.agent_storage_status = agent_storage_status
        # The alias of the agent storage.
        self.alias_name = alias_name
        # The time when the agent storage was created.
        self.create_time = create_time
        # The list of network sources allowed for the agent storage. TRUST_PROXY: console.
        self.network_source_acl = network_source_acl
        # The list of network types allowed for the agent storage. CLASSIC: classic network. INTERNET: Internet. VPC: VPC network.
        self.network_type_acl = network_type_acl
        # The access control policy of the agent storage.
        self.policy = policy
        # The version of the agent storage policy.
        self.policy_version = policy_version
        # The region ID of the agent storage.
        self.region_id = region_id
        # Id of the request
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags of the agent storage.
        self.tags = tags
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_storage_description is not None:
            result['AgentStorageDescription'] = self.agent_storage_description

        if self.agent_storage_name is not None:
            result['AgentStorageName'] = self.agent_storage_name

        if self.agent_storage_specification is not None:
            result['AgentStorageSpecification'] = self.agent_storage_specification

        if self.agent_storage_status is not None:
            result['AgentStorageStatus'] = self.agent_storage_status

        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.network_source_acl is not None:
            result['NetworkSourceACL'] = self.network_source_acl

        if self.network_type_acl is not None:
            result['NetworkTypeACL'] = self.network_type_acl

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageDescription') is not None:
            self.agent_storage_description = m.get('AgentStorageDescription')

        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('AgentStorageSpecification') is not None:
            self.agent_storage_specification = m.get('AgentStorageSpecification')

        if m.get('AgentStorageStatus') is not None:
            self.agent_storage_status = m.get('AgentStorageStatus')

        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NetworkSourceACL') is not None:
            self.network_source_acl = m.get('NetworkSourceACL')

        if m.get('NetworkTypeACL') is not None:
            self.network_type_acl = m.get('NetworkTypeACL')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetAgentStorageResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetAgentStorageResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # (Deprecated) The tag key.
        self.tag_key = tag_key
        # (Deprecated) The tag value.
        self.tag_value = tag_value
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

