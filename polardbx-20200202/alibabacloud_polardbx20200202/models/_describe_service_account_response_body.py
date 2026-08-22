# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceAccountResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeServiceAccountResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeServiceAccountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The instance details.
        self.data = data
        # The response message. "success" is returned if the request was successful. Otherwise, an error code is returned.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeServiceAccountResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeServiceAccountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeServiceAccountResponseBodyData(DaraModel):
    def __init__(
        self,
        service_accounts: List[main_models.DescribeServiceAccountResponseBodyDataServiceAccounts] = None,
    ):
        # A service account in the list.
        self.service_accounts = service_accounts

    def validate(self):
        if self.service_accounts:
            for v1 in self.service_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServiceAccounts'] = []
        if self.service_accounts is not None:
            for k1 in self.service_accounts:
                result['ServiceAccounts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_accounts = []
        if m.get('ServiceAccounts') is not None:
            for k1 in m.get('ServiceAccounts'):
                temp_model = main_models.DescribeServiceAccountResponseBodyDataServiceAccounts()
                self.service_accounts.append(temp_model.from_map(k1))

        return self

class DescribeServiceAccountResponseBodyDataServiceAccounts(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        created_time: str = None,
        service_account_type: str = None,
        status: str = None,
    ):
        # The account name.
        self.account_name = account_name
        # The creation time.
        self.created_time = created_time
        # The service account type.
        self.service_account_type = service_account_type
        # The status of the backup set. Valid values:
        # 
        # - **0**: Backing up.
        # - **1**: Backup succeeded.
        # - **2**: Backup failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.service_account_type is not None:
            result['ServiceAccountType'] = self.service_account_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ServiceAccountType') is not None:
            self.service_account_type = m.get('ServiceAccountType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeServiceAccountResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The authentication action.
        self.auth_action = auth_action
        # The authentication principal type.
        self.auth_principal_type = auth_principal_type
        # The diagnostic information.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of the permission denial.
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

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

