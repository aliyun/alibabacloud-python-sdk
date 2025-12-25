# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        region_id: str = None,
        vpc_id: str = None,
        workspace_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the workspace.
        # 
        # This parameter is required.
        self.description = description
        # The region to which the workspace belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The name of the workspace.
        # 
        # This parameter is required.
        self.workspace_name = workspace_name

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

