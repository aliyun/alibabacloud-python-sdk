# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentStoragesShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_storage_name: str = None,
        agent_storage_name_list_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag_shrink: str = None,
    ):
        # agent storage name
        self.agent_storage_name = agent_storage_name
        # The list of agent storage names, used to query multiple specified agent storages in a batch.
        self.agent_storage_name_list_shrink = agent_storage_name_list_shrink
        # The maximum number of tag resources to return in this request.
        self.max_results = max_results
        # The token used to retrieve the next page of results when the total number of tag resources exceeds the value of MaxResults. This parameter has a value only when not all tag resources are returned.
        self.next_token = next_token
        # The resource group ID. You can query this ID in the resource group console.
        self.resource_group_id = resource_group_id
        # The status of the agent storage.
        self.status = status
        # The list of tags.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_storage_name is not None:
            result['AgentStorageName'] = self.agent_storage_name

        if self.agent_storage_name_list_shrink is not None:
            result['AgentStorageNameList'] = self.agent_storage_name_list_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('AgentStorageNameList') is not None:
            self.agent_storage_name_list_shrink = m.get('AgentStorageNameList')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

