# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTaskFlowConstantsResponseBody(DaraModel):
    def __init__(
        self,
        dag_constants: main_models.ListTaskFlowConstantsResponseBodyDagConstants = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # A list of constant key-value pairs for the task flow.
        self.dag_constants = dag_constants
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.dag_constants:
            self.dag_constants.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_constants is not None:
            result['DagConstants'] = self.dag_constants.to_map()

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
        if m.get('DagConstants') is not None:
            temp_model = main_models.ListTaskFlowConstantsResponseBodyDagConstants()
            self.dag_constants = temp_model.from_map(m.get('DagConstants'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTaskFlowConstantsResponseBodyDagConstants(DaraModel):
    def __init__(
        self,
        dag_constant: List[main_models.ListTaskFlowConstantsResponseBodyDagConstantsDagConstant] = None,
    ):
        self.dag_constant = dag_constant

    def validate(self):
        if self.dag_constant:
            for v1 in self.dag_constant:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DagConstant'] = []
        if self.dag_constant is not None:
            for k1 in self.dag_constant:
                result['DagConstant'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dag_constant = []
        if m.get('DagConstant') is not None:
            for k1 in m.get('DagConstant'):
                temp_model = main_models.ListTaskFlowConstantsResponseBodyDagConstantsDagConstant()
                self.dag_constant.append(temp_model.from_map(k1))

        return self

class ListTaskFlowConstantsResponseBodyDagConstantsDagConstant(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The constant key.
        self.key = key
        # The constant value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

