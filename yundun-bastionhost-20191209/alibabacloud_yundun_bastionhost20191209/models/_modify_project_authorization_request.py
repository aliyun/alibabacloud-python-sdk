# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyProjectAuthorizationRequest(DaraModel):
    def __init__(
        self,
        authorization_id: int = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        region_id: str = None,
        scope_type: int = None,
    ):
        # The ID of the project authorization to be modified.
        # > You can call the ListProjectAuthorizations operation to obtain this parameter.
        # 
        # This parameter is required.
        self.authorization_id = authorization_id
        # The new description of the project authorization.
        self.description = description
        # The ID of the Bastionhost instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new name of the project authorization.
        self.name = name
        # The region ID of the Bastionhost instance.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The scope of assets that can be managed by the authorization after modification. Valid values:
        # 
        # - **1**: all projects
        # 
        # - **2**: specified projects
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_id is not None:
            result['AuthorizationId'] = self.authorization_id

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationId') is not None:
            self.authorization_id = m.get('AuthorizationId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

