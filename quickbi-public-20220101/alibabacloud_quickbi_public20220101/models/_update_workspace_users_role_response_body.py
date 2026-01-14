# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkspaceUsersRoleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.UpdateWorkspaceUsersRoleResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of the interface execution.
        self.result = result
        # Indicates whether the request was successful. Value range:
        # 
        # - true: The request was successful, some members may have been updated successfully while others failed, refer to FailureDetail in the response for reasons of failure
        # - false: The request failed, no data will be persisted
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.UpdateWorkspaceUsersRoleResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateWorkspaceUsersRoleResponseBodyResult(DaraModel):
    def __init__(
        self,
        failure: int = None,
        failure_detail: Dict[str, Any] = None,
        success: int = None,
        total: int = None,
    ):
        # Number of users that failed to update.
        self.failure = failure
        # Reasons for the update failures.
        self.failure_detail = failure_detail
        # Number of users that were updated successfully.
        self.success = success
        # Modify the total number of users.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure is not None:
            result['Failure'] = self.failure

        if self.failure_detail is not None:
            result['FailureDetail'] = self.failure_detail

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failure') is not None:
            self.failure = m.get('Failure')

        if m.get('FailureDetail') is not None:
            self.failure_detail = m.get('FailureDetail')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

