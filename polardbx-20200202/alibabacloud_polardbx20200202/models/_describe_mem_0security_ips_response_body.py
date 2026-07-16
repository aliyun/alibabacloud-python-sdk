# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeMem0SecurityIpsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeMem0SecurityIpsResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeMem0SecurityIpsResponseBodyData = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The data list.
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
            temp_model = main_models.DescribeMem0SecurityIpsResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeMem0SecurityIpsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMem0SecurityIpsResponseBodyData(DaraModel):
    def __init__(
        self,
        custins_name: str = None,
        groups: List[main_models.DescribeMem0SecurityIpsResponseBodyDataGroups] = None,
    ):
        # The name of the memory engine instance.
        self.custins_name = custins_name
        # The groups corresponding to the consumed service.
        self.groups = groups

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custins_name is not None:
            result['CustinsName'] = self.custins_name

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustinsName') is not None:
            self.custins_name = m.get('CustinsName')

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeMem0SecurityIpsResponseBodyDataGroups()
                self.groups.append(temp_model.from_map(k1))

        return self

class DescribeMem0SecurityIpsResponseBodyDataGroups(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        group_tag: str = None,
        ip_lists: str = None,
    ):
        # The name of the whitelist group.
        self.group_name = group_name
        # The tag of the group.
        self.group_tag = group_tag
        # Indicates whether the IP addresses that are already used for DNAT entries can also be used for SNAT entries. Valid values:
        # 
        # - **true**: The IP addresses can also be used for SNAT entries.
        # 
        # - **false**: The IP addresses cannot be used for SNAT entries.
        self.ip_lists = ip_lists

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

        if self.ip_lists is not None:
            result['IpLists'] = self.ip_lists

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')

        if m.get('IpLists') is not None:
            self.ip_lists = m.get('IpLists')

        return self

class DescribeMem0SecurityIpsResponseBodyAccessDeniedDetail(DaraModel):
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
        # Same as above.
        self.auth_action = auth_action
        # The identity used for authentication in the request.
        self.auth_principal_display_name = auth_principal_display_name
        # Same as above.
        self.auth_principal_owner_id = auth_principal_owner_id
        # Same as above.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of no-permission error.
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

