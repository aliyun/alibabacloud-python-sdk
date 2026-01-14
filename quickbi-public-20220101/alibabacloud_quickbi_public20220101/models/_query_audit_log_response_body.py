# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryAuditLogResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.QueryAuditLogResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of logs.
        self.result = result
        # Indicates whether the request was successful. Possible values: 
        # - true: The request succeeded 
        # - false: The request failed
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryAuditLogResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAuditLogResponseBodyResult(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        operator_account_name: str = None,
        operator_name: str = None,
        operator_type: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
        workspace_id: str = None,
    ):
        # Log time.
        self.gmt_create = gmt_create
        # Operator account.
        self.operator_account_name = operator_account_name
        # Operator\\"s nickname.
        self.operator_name = operator_name
        # Operation type.
        self.operator_type = operator_type
        # Target ID.
        self.target_id = target_id
        # Target name.
        self.target_name = target_name
        # Target type.
        self.target_type = target_type
        # Workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.operator_account_name is not None:
            result['OperatorAccountName'] = self.operator_account_name

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('OperatorAccountName') is not None:
            self.operator_account_name = m.get('OperatorAccountName')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

