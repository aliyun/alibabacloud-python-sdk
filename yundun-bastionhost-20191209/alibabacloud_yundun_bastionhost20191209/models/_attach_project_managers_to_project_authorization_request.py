# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class AttachProjectManagersToProjectAuthorizationRequest(DaraModel):
    def __init__(
        self,
        authorization_id: int = None,
        instance_id: str = None,
        principals: List[main_models.AttachProjectManagersToProjectAuthorizationRequestPrincipals] = None,
        region_id: str = None,
    ):
        # The project authorization ID.
        # > You can call the ListProjectAuthorizations operation to query this parameter.
        # 
        # This parameter is required.
        self.authorization_id = authorization_id
        # The instance ID of the bastion host.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The information about the project administrators specified in the project authorization.
        self.principals = principals
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        if self.principals:
            for v1 in self.principals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_id is not None:
            result['AuthorizationId'] = self.authorization_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Principals'] = []
        if self.principals is not None:
            for k1 in self.principals:
                result['Principals'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationId') is not None:
            self.authorization_id = m.get('AuthorizationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.principals = []
        if m.get('Principals') is not None:
            for k1 in m.get('Principals'):
                temp_model = main_models.AttachProjectManagersToProjectAuthorizationRequestPrincipals()
                self.principals.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class AttachProjectManagersToProjectAuthorizationRequestPrincipals(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # When PrincipalType is set to RamUser, specify the ID of the RAM user to be designated as the project administrator. When PrincipalType is set to RamRole, specify the ARN of the RAM role to be designated as the project administrator.
        self.principal_id = principal_id
        # The display name of the RAM user or RAM role designated as the project administrator.
        self.principal_name = principal_name
        # The type of the project administrator. Valid values:
        # 
        # - **RamUser**: Resource Access Management (RAM) user.
        # 
        # - **RamRole**: RAM role.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

