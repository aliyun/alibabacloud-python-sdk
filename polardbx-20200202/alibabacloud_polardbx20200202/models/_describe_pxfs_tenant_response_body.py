# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribePxfsTenantResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribePxfsTenantResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribePxfsTenantResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The returned data.
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
            temp_model = main_models.DescribePxfsTenantResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribePxfsTenantResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePxfsTenantResponseBodyData(DaraModel):
    def __init__(
        self,
        quota_bytes: int = None,
        quota_files: int = None,
        rate_limit_rps: int = None,
        rate_limit_wbps: int = None,
        status: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        used_bytes: int = None,
        used_files: int = None,
    ):
        # The capacity quota.
        self.quota_bytes = quota_bytes
        # The file count quota.
        self.quota_files = quota_files
        # The request rate limit.
        self.rate_limit_rps = rate_limit_rps
        # The write bandwidth limit.
        self.rate_limit_wbps = rate_limit_wbps
        # The status.
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id
        # The tenant name.
        self.tenant_name = tenant_name
        # The used capacity.
        self.used_bytes = used_bytes
        # The used file count.
        self.used_files = used_files

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_bytes is not None:
            result['QuotaBytes'] = self.quota_bytes

        if self.quota_files is not None:
            result['QuotaFiles'] = self.quota_files

        if self.rate_limit_rps is not None:
            result['RateLimitRps'] = self.rate_limit_rps

        if self.rate_limit_wbps is not None:
            result['RateLimitWbps'] = self.rate_limit_wbps

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.used_bytes is not None:
            result['UsedBytes'] = self.used_bytes

        if self.used_files is not None:
            result['UsedFiles'] = self.used_files

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaBytes') is not None:
            self.quota_bytes = m.get('QuotaBytes')

        if m.get('QuotaFiles') is not None:
            self.quota_files = m.get('QuotaFiles')

        if m.get('RateLimitRps') is not None:
            self.rate_limit_rps = m.get('RateLimitRps')

        if m.get('RateLimitWbps') is not None:
            self.rate_limit_wbps = m.get('RateLimitWbps')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('UsedBytes') is not None:
            self.used_bytes = m.get('UsedBytes')

        if m.get('UsedFiles') is not None:
            self.used_files = m.get('UsedFiles')

        return self

class DescribePxfsTenantResponseBodyAccessDeniedDetail(DaraModel):
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
        # The type of the authentication principal.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
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

