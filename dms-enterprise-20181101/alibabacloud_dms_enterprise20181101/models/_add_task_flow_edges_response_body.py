# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class AddTaskFlowEdgesResponseBody(DaraModel):
    def __init__(
        self,
        edge_ids: main_models.AddTaskFlowEdgesResponseBodyEdgeIds = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of task flow edge IDs.
        self.edge_ids = edge_ids
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.edge_ids:
            self.edge_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edge_ids is not None:
            result['EdgeIds'] = self.edge_ids.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdgeIds') is not None:
            temp_model = main_models.AddTaskFlowEdgesResponseBodyEdgeIds()
            self.edge_ids = temp_model.from_map(m.get('EdgeIds'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddTaskFlowEdgesResponseBodyEdgeIds(DaraModel):
    def __init__(
        self,
        edge_id: List[int] = None,
    ):
        self.edge_id = edge_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edge_id is not None:
            result['EdgeId'] = self.edge_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdgeId') is not None:
            self.edge_id = m.get('EdgeId')

        return self

