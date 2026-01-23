# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class QueryReversedDeductionHistoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryReversedDeductionHistoryResponseBodyData] = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
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

        if self.message is not None:
            result['Message'] = self.message

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.QueryReversedDeductionHistoryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryReversedDeductionHistoryResponseBodyData(DaraModel):
    def __init__(
        self,
        offset_amount: str = None,
        operation_submit_type: str = None,
        operation_time: str = None,
        operation_uid: str = None,
    ):
        self.offset_amount = offset_amount
        self.operation_submit_type = operation_submit_type
        self.operation_time = operation_time
        self.operation_uid = operation_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offset_amount is not None:
            result['OffsetAmount'] = self.offset_amount

        if self.operation_submit_type is not None:
            result['OperationSubmitType'] = self.operation_submit_type

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.operation_uid is not None:
            result['OperationUid'] = self.operation_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OffsetAmount') is not None:
            self.offset_amount = m.get('OffsetAmount')

        if m.get('OperationSubmitType') is not None:
            self.operation_submit_type = m.get('OperationSubmitType')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('OperationUid') is not None:
            self.operation_uid = m.get('OperationUid')

        return self

