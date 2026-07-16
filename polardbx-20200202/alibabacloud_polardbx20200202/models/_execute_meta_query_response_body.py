# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class ExecuteMetaQueryResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ExecuteMetaQueryResponseBodyAccessDeniedDetail = None,
        data: main_models.ExecuteMetaQueryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The instance details.
        self.data = data
        # The additional information returned. If the request is successful, success is returned. If the request fails, the corresponding error code is returned.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.ExecuteMetaQueryResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.ExecuteMetaQueryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ExecuteMetaQueryResponseBodyData(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        row_count: int = None,
        rows: List[Dict[str, Any]] = None,
    ):
        # The column names.
        self.columns = columns
        # The total number of data rows.
        self.row_count = row_count
        # The number of affected or returned rows. This field is available only for compute nodes (CNs).
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['Columns'] = self.columns

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.rows is not None:
            result['Rows'] = self.rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        return self

class ExecuteMetaQueryResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The description is the same as above.
        self.auth_action = auth_action
        # The description is the same as above.
        self.auth_principal_type = auth_principal_type
        # The diagnostic information.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # NoPermissionType
        self.no_permission_type = no_permission_type
        # PolicyType
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

