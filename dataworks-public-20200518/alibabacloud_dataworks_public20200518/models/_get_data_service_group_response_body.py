# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetDataServiceGroupResponseBody(DaraModel):
    def __init__(
        self,
        group: main_models.GetDataServiceGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The details of the business process.
        self.group = group
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = main_models.GetDataServiceGroupResponseBodyGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataServiceGroupResponseBodyGroup(DaraModel):
    def __init__(
        self,
        api_gateway_group_id: str = None,
        created_time: str = None,
        creator_id: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The ID of the API group that is associated with the business process in the API Gateway console.
        self.api_gateway_group_id = api_gateway_group_id
        # The time when the business process was created.
        self.created_time = created_time
        # The user identifier (UID) of the creator of the business process. The value of this parameter may be empty for creators of some existing business processes.
        self.creator_id = creator_id
        # The description of the business process.
        self.description = description
        # The business process ID.
        self.group_id = group_id
        # The name of the business process.
        self.group_name = group_name
        # The time when the business process was last modified.
        self.modified_time = modified_time
        # The workspace ID.
        self.project_id = project_id
        # The tenant ID.
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

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiGatewayGroupId') is not None:
            self.api_gateway_group_id = m.get('ApiGatewayGroupId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

