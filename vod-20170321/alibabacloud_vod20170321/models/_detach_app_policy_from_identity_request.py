# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachAppPolicyFromIdentityRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        identity_name: str = None,
        identity_type: str = None,
        policy_names: str = None,
    ):
        # The ID of the application. This parameter is optional if you set PolicyNames to VODAppAdministratorAccess. This parameter is required if you set PolicyNames to a value other than VODAppAdministratorAccess.
        # 
        # *   Default value: **app-1000000**.
        # *   For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The ID of the RAM user or the name of the RAM role.
        # 
        # *   Specifies the ID of the RAM user for this parameter if you set IdentityType to RamUser.
        # *   Specifies the name of the RAM role for this parameter if you set IdentityType to RamRole.
        # 
        # This parameter is required.
        self.identity_name = identity_name
        # The type of the identity. Valid values:
        # 
        # *   **RamUser**: RAM user
        # *   **RamRole**: RAM role
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The name of the policy. Separate multiple names with commas (,). Only system policies are supported.
        # 
        # *   **VODAppFullAccess**: permissions to manage all resources in an application
        # *   **VODAppReadOnlyAccess**: permissions to read all resources in an application
        # *   **VODAppAdministratorAccess**: permissions of the application administrator
        # 
        # This parameter is required.
        self.policy_names = policy_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')

        return self

