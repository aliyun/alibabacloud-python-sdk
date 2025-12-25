# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecUserOperationsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecUserOperationsResponseBodyData] = None,
        request_id: str = None,
    ):
        # The operation records.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApisecUserOperationsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApisecUserOperationsResponseBodyData(DaraModel):
    def __init__(
        self,
        from_status: str = None,
        note: str = None,
        object_id: str = None,
        operation_source: str = None,
        time: int = None,
        to_status: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # The state before the operation.
        # 
        # Valid values of the risk state:
        # 
        # *   **toBeConfirmed**
        # *   **confirmed**
        # *   **toBeFixed**
        # *   **fixed**
        # *   **ignored**
        # 
        # Valid values of the event state:
        # 
        # *   **toBeConfirmed**
        # *   **confirmed**
        # *   **ignored**
        self.from_status = from_status
        # The remarks.
        self.note = note
        # The object ID of the operation record.
        self.object_id = object_id
        self.operation_source = operation_source
        # The time at which the operation was performed. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.time = time
        # The state after the operation.
        # 
        # Valid values of the risk state:
        # 
        # *   **toBeConfirmed**
        # *   **confirmed**
        # *   **toBeFixed**
        # *   **fixed**
        # *   **ignored**
        # 
        # Valid values of the event state:
        # 
        # *   **toBeConfirmed**
        # *   **confirmed**
        # *   **ignored**
        self.to_status = to_status
        # The type of the operation record. Valid values:
        # 
        # *   **abnormal**: risk detection
        # *   **event**: security event
        self.type = type
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_status is not None:
            result['FromStatus'] = self.from_status

        if self.note is not None:
            result['Note'] = self.note

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.operation_source is not None:
            result['OperationSource'] = self.operation_source

        if self.time is not None:
            result['Time'] = self.time

        if self.to_status is not None:
            result['ToStatus'] = self.to_status

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromStatus') is not None:
            self.from_status = m.get('FromStatus')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('OperationSource') is not None:
            self.operation_source = m.get('OperationSource')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('ToStatus') is not None:
            self.to_status = m.get('ToStatus')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

