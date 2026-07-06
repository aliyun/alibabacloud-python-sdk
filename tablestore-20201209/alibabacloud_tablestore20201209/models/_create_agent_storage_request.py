# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class CreateAgentStorageRequest(DaraModel):
    def __init__(
        self,
        agent_storage_description: str = None,
        agent_storage_name: str = None,
        network: str = None,
        network_source_acl: List[str] = None,
        network_type_acl: List[str] = None,
        policy: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateAgentStorageRequestTags] = None,
    ):
        # The description of the agent storage. The description must be 3 to 256 characters in length.
        self.agent_storage_description = agent_storage_description
        # The name of the agent storage. The naming conventions are as follows:
        # - The name can contain only letters, digits, and hyphens (-).
        # - The name must start with a letter.
        # - The name cannot end with a hyphen (-).
        # - The name is case-insensitive.
        # - The name must be 3 to 16 characters in length.
        # - The name cannot contain the following words: ali, ay, ots, taobao, or admin.
        # 
        # This parameter is required.
        self.agent_storage_name = agent_storage_name
        # (Deprecated) The network type of the agent storage. Valid values: NORMAL and VPC_CONSOLE. Default value: NORMAL.
        self.network = network
        # The list of allowed network sources for the agent storage. All sources are allowed by default. Valid values:
        # - TRUST_PROXY: console.
        self.network_source_acl = network_source_acl
        # The list of allowed network types for the agent storage. All types are allowed by default. Valid values:
        # - CLASSIC: classic network.
        # - INTERNET: public network.
        # - VPC: VPC network.
        self.network_type_acl = network_type_acl
        # The access control policy for the agent storage in JSON format. For the syntax, see https://www.alibabacloud.com/help/en/ram/user-guide/policy-structure-and-syntax.
        self.policy = policy
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tags = tags

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

        if self.network is not None:
            result['Network'] = self.network

        if self.network_source_acl is not None:
            result['NetworkSourceACL'] = self.network_source_acl

        if self.network_type_acl is not None:
            result['NetworkTypeACL'] = self.network_type_acl

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageDescription') is not None:
            self.agent_storage_description = m.get('AgentStorageDescription')

        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('NetworkSourceACL') is not None:
            self.network_source_acl = m.get('NetworkSourceACL')

        if m.get('NetworkTypeACL') is not None:
            self.network_type_acl = m.get('NetworkTypeACL')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateAgentStorageRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self



class CreateAgentStorageRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The key can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag. The value can be up to 64 characters in length.
        # 
        # This parameter is required.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

