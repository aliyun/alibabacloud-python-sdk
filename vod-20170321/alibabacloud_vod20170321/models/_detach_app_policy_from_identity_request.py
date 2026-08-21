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
        # The application ID. If the policy name is VODAppAdministratorAccess, this parameter is optional. For other policies, this parameter is required.
        # - Value (default): **app-1000000**.
        # - For more information, see [Multi-application](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The identity name.
        # 
        # - If the type is RamUser, specify the Resource Access Management (RAM) user ID.
        # - If the type is RamRole, specify the role name.
        # 
        # This parameter is required.
        self.identity_name = identity_name
        # The identity type. Valid values:
        # - **RamUser**: Resource Access Management (RAM) user.
        # - **RamRole**: RAM role.
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The policy names. Separate multiple names with commas (,). Only system policies are supported. Valid values:
        # - **VODAppFullAccess**: permissions to manage and operate all resources in the application.
        # - **VODAppReadOnlyAccess**: read-only permissions for all resources in the application.
        # - **VODAppAdministratorAccess**: application administrator permissions.
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

