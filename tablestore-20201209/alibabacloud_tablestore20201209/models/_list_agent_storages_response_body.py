# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class ListAgentStoragesResponseBody(DaraModel):
    def __init__(
        self,
        agent_storages: List[main_models.ListAgentStoragesResponseBodyAgentStorages] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of agent storage information.
        self.agent_storages = agent_storages
        # The token used to retrieve the next page of results when the total number of tag resources exceeds the value of MaxResults. This parameter has a value only when not all tag resources are returned.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The total number of agent storages returned.
        self.total_count = total_count

    def validate(self):
        if self.agent_storages:
            for v1 in self.agent_storages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AgentStorages'] = []
        if self.agent_storages is not None:
            for k1 in self.agent_storages:
                result['AgentStorages'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_storages = []
        if m.get('AgentStorages') is not None:
            for k1 in m.get('AgentStorages'):
                temp_model = main_models.ListAgentStoragesResponseBodyAgentStorages()
                self.agent_storages.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAgentStoragesResponseBodyAgentStorages(DaraModel):
    def __init__(
        self,
        agent_storage_description: str = None,
        agent_storage_name: str = None,
        agent_storage_specification: str = None,
        agent_storage_status: str = None,
        alias_name: str = None,
        create_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        user_id: str = None,
    ):
        # agent storage description
        self.agent_storage_description = agent_storage_description
        # The agent storage name, which is a unique key.
        self.agent_storage_name = agent_storage_name
        # The specifications of the agent storage.
        self.agent_storage_specification = agent_storage_specification
        # The status of the agent storage. Valid values:
        # - normal: Normal.
        # - forbidden: Disabled.
        # - deleting: Being released.
        self.agent_storage_status = agent_storage_status
        # The alias of the agent storage.
        self.alias_name = alias_name
        # The creation time of the agent storage.
        self.create_time = create_time
        # The region ID of the agent storage.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

