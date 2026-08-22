# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenSearchResourceUsageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeOpenSearchResourceUsageResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeOpenSearchResourceUsageResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The returned data.
        self.data = data
        # Id of the request
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
            temp_model = main_models.DescribeOpenSearchResourceUsageResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeOpenSearchResourceUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOpenSearchResourceUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        doc_count: int = None,
        index_count: int = None,
        storage_size_in_bytes: int = None,
        storage_total_in_bytes: int = None,
        storage_usage_percent: float = None,
    ):
        # The total number of documents in the cluster.
        self.doc_count = doc_count
        # The number of indexes. This is a filter condition for the number of indexes that the missing index table currently has. The input format is `operator + separator "" + index count`, for example, `>=100`.
        self.index_count = index_count
        # The used storage space, in bytes.
        self.storage_size_in_bytes = storage_size_in_bytes
        # The total storage capacity, in bytes.
        self.storage_total_in_bytes = storage_total_in_bytes
        # The storage space usage.
        self.storage_usage_percent = storage_usage_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_count is not None:
            result['DocCount'] = self.doc_count

        if self.index_count is not None:
            result['IndexCount'] = self.index_count

        if self.storage_size_in_bytes is not None:
            result['StorageSizeInBytes'] = self.storage_size_in_bytes

        if self.storage_total_in_bytes is not None:
            result['StorageTotalInBytes'] = self.storage_total_in_bytes

        if self.storage_usage_percent is not None:
            result['StorageUsagePercent'] = self.storage_usage_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocCount') is not None:
            self.doc_count = m.get('DocCount')

        if m.get('IndexCount') is not None:
            self.index_count = m.get('IndexCount')

        if m.get('StorageSizeInBytes') is not None:
            self.storage_size_in_bytes = m.get('StorageSizeInBytes')

        if m.get('StorageTotalInBytes') is not None:
            self.storage_total_in_bytes = m.get('StorageTotalInBytes')

        if m.get('StorageUsagePercent') is not None:
            self.storage_usage_percent = m.get('StorageUsagePercent')

        return self

class DescribeOpenSearchResourceUsageResponseBodyAccessDeniedDetail(DaraModel):
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

