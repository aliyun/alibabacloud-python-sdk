# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetShutdownPolicyRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetShutdownPolicyRecordResponseBodyData] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetShutdownPolicyRecordResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetShutdownPolicyRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        current_policy: str = None,
        operation_path: str = None,
        operation_time: str = None,
        operator: str = None,
        previous_policy: str = None,
    ):
        self.current_policy = current_policy
        self.operation_path = operation_path
        self.operation_time = operation_time
        self.operator = operator
        self.previous_policy = previous_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_policy is not None:
            result['CurrentPolicy'] = self.current_policy

        if self.operation_path is not None:
            result['OperationPath'] = self.operation_path

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.previous_policy is not None:
            result['PreviousPolicy'] = self.previous_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPolicy') is not None:
            self.current_policy = m.get('CurrentPolicy')

        if m.get('OperationPath') is not None:
            self.operation_path = m.get('OperationPath')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('PreviousPolicy') is not None:
            self.previous_policy = m.get('PreviousPolicy')

        return self

