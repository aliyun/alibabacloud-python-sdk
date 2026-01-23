# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class CustomerQuotaRecordListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.CustomerQuotaRecordListResponseBodyData] = None,
        msg: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # Status code of returning result, 200 means success.
        self.code = code
        # Listed data of returning result
        self.data = data
        # Description of returning data
        self.msg = msg
        # Current page number
        self.page_no = page_no
        # Record number on each page
        self.page_size = page_size
        # ID of request
        self.request_id = request_id
        # Total volume
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

        if self.msg is not None:
            result['Msg'] = self.msg

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
                temp_model = main_models.CustomerQuotaRecordListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class CustomerQuotaRecordListResponseBodyData(DaraModel):
    def __init__(
        self,
        operation_submit_type: str = None,
        operation_time: str = None,
        operation_type_code: str = None,
        operation_type_desc: str = None,
        operation_uid: str = None,
        update_after_amount: str = None,
        update_amount: str = None,
        update_before_amount: str = None,
    ):
        # The way to submit the quota adjustment operation. API/ACPN
        self.operation_submit_type = operation_submit_type
        # The time of submit the quota adjustment operation.
        self.operation_time = operation_time
        # Operation Type Enum</br>
        # all All types</br>
        # quota_create Create quota</br>
        # quota_amount_adjust Adjust the amount of quota</br>
        self.operation_type_code = operation_type_code
        # The description of submitted quota adjustment operation.
        self.operation_type_desc = operation_type_desc
        # The UID of operator(Partner\\"s UID).
        self.operation_uid = operation_uid
        # Updated quota amount
        self.update_after_amount = update_after_amount
        # The difference amount between updated quota and original quota.
        self.update_amount = update_amount
        # Original quota amount
        self.update_before_amount = update_before_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_submit_type is not None:
            result['OperationSubmitType'] = self.operation_submit_type

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.operation_type_code is not None:
            result['OperationTypeCode'] = self.operation_type_code

        if self.operation_type_desc is not None:
            result['OperationTypeDesc'] = self.operation_type_desc

        if self.operation_uid is not None:
            result['OperationUid'] = self.operation_uid

        if self.update_after_amount is not None:
            result['UpdateAfterAmount'] = self.update_after_amount

        if self.update_amount is not None:
            result['UpdateAmount'] = self.update_amount

        if self.update_before_amount is not None:
            result['UpdateBeforeAmount'] = self.update_before_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationSubmitType') is not None:
            self.operation_submit_type = m.get('OperationSubmitType')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('OperationTypeCode') is not None:
            self.operation_type_code = m.get('OperationTypeCode')

        if m.get('OperationTypeDesc') is not None:
            self.operation_type_desc = m.get('OperationTypeDesc')

        if m.get('OperationUid') is not None:
            self.operation_uid = m.get('OperationUid')

        if m.get('UpdateAfterAmount') is not None:
            self.update_after_amount = m.get('UpdateAfterAmount')

        if m.get('UpdateAmount') is not None:
            self.update_amount = m.get('UpdateAmount')

        if m.get('UpdateBeforeAmount') is not None:
            self.update_before_amount = m.get('UpdateBeforeAmount')

        return self

