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
        # The user operation records for API security.
        self.data = data
        # The ID of the request.
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
        # The status of the threat detection or security event before the operation was performed.
        # 
        # Valid values for threat detection:
        # 
        # - **toBeConfirmed**: to be confirmed.
        # 
        # - **confirmed**: confirmed.
        # 
        # - **toBeFixed**: to be fixed.
        # 
        # - **fixed**: fixed.
        # 
        # - **ignored**: ignored.
        # 
        # Valid values for a security event:
        # 
        # - **toBeConfirmed**: to be confirmed.
        # 
        # - **confirmed**: confirmed.
        # 
        # - **ignored**: ignored.
        self.from_status = from_status
        # The remarks that the user added to the operation record.
        self.note = note
        # The ID of the threat detection or security event associated with the operation record.
        self.object_id = object_id
        # The source of the operation. Valid values:
        # 
        # - **system**: the operation was automatically performed by the system.
        # 
        # - **custom**: the operation was manually performed by a user.
        self.operation_source = operation_source
        # The time when the operation was performed. This value is a UNIX timestamp. Unit: seconds.
        self.time = time
        # The status of the threat detection or security event after the operation was performed.
        # 
        # Valid values for threat detection:
        # 
        # - **toBeConfirmed**: to be confirmed.
        # 
        # - **confirmed**: confirmed.
        # 
        # - **toBeFixed**: to be fixed.
        # 
        # - **fixed**: fixed.
        # 
        # - **ignored**: ignored.
        # 
        # Valid values for a security event:
        # 
        # - **toBeConfirmed**: to be confirmed.
        # 
        # - **confirmed**: confirmed.
        # 
        # - **ignored**: ignored.
        self.to_status = to_status
        # The type of the operation record. Valid values:
        # 
        # - **abnormal**: threat detection.
        # 
        # - **event**: security event.
        self.type = type
        # The ID of the user who performed the operation.
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

