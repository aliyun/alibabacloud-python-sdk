# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateExecutionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execution_id: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the execution.
        self.description = description
        # The ID of the execution.
        # 
        # This parameter is required.
        self.execution_id = execution_id
        # The information about the parameters.
        self.parameters = parameters
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the execution.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

