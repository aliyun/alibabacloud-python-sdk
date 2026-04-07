# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataServiceGroupRequest(DaraModel):
    def __init__(
        self,
        api_gateway_group_id: str = None,
        description: str = None,
        group_name: str = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The ID of the API group that is associated with the business process in the API Gateway console. You can log on to the API Gateway console and go to the Group Details page to view the ID.
        # 
        # This parameter is required.
        self.api_gateway_group_id = api_gateway_group_id
        # The description of the business process.
        self.description = description
        # The name of the business process.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The tenant ID. This parameter is deprecated.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_gateway_group_id is not None:
            result['ApiGatewayGroupId'] = self.api_gateway_group_id

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiGatewayGroupId') is not None:
            self.api_gateway_group_id = m.get('ApiGatewayGroupId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

