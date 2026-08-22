# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeContextDBSecurityIpsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeContextDBSecurityIpsResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeContextDBSecurityIpsResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The paginated result of the instance list.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeContextDBSecurityIpsResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeContextDBSecurityIpsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContextDBSecurityIpsResponseBodyData(DaraModel):
    def __init__(
        self,
        context_dbinstance_name: str = None,
        dbinstance_name: str = None,
        group_items: List[main_models.DescribeContextDBSecurityIpsResponseBodyDataGroupItems] = None,
    ):
        # The context service instance name.
        self.context_dbinstance_name = context_dbinstance_name
        # The instance name.
        self.dbinstance_name = dbinstance_name
        # The whitelist group list.
        self.group_items = group_items

    def validate(self):
        if self.group_items:
            for v1 in self.group_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_dbinstance_name is not None:
            result['ContextDBInstanceName'] = self.context_dbinstance_name

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        result['GroupItems'] = []
        if self.group_items is not None:
            for k1 in self.group_items:
                result['GroupItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextDBInstanceName') is not None:
            self.context_dbinstance_name = m.get('ContextDBInstanceName')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        self.group_items = []
        if m.get('GroupItems') is not None:
            for k1 in m.get('GroupItems'):
                temp_model = main_models.DescribeContextDBSecurityIpsResponseBodyDataGroupItems()
                self.group_items.append(temp_model.from_map(k1))

        return self

class DescribeContextDBSecurityIpsResponseBodyDataGroupItems(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        group_tag: str = None,
        security_iplist: str = None,
    ):
        # The whitelist group name.
        self.group_name = group_name
        # The group tag.
        self.group_tag = group_tag
        # The details of the whitelist group.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

class DescribeContextDBSecurityIpsResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The authentication action.
        self.auth_action = auth_action
        # The display name of the authentication principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The authentication principal type.
        self.auth_principal_type = auth_principal_type
        # The diagnostic information.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # NoPermissionType
        self.no_permission_type = no_permission_type
        # The policy type.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

