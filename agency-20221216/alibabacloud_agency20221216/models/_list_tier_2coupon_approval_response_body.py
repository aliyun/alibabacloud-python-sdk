# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class ListTier2CouponApprovalResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListTier2CouponApprovalResponseBodyData] = None,
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
                temp_model = main_models.ListTier2CouponApprovalResponseBodyData()
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

class ListTier2CouponApprovalResponseBodyData(DaraModel):
    def __init__(
        self,
        application_sheet_id: str = None,
        application_time: str = None,
        approval_status: str = None,
        t_2partner_name: str = None,
        t_2partner_uid: int = None,
        total_amount: str = None,
    ):
        self.application_sheet_id = application_sheet_id
        self.application_time = application_time
        self.approval_status = approval_status
        self.t_2partner_name = t_2partner_name
        self.t_2partner_uid = t_2partner_uid
        self.total_amount = total_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_sheet_id is not None:
            result['ApplicationSheetId'] = self.application_sheet_id

        if self.application_time is not None:
            result['ApplicationTime'] = self.application_time

        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.t_2partner_name is not None:
            result['T2PartnerName'] = self.t_2partner_name

        if self.t_2partner_uid is not None:
            result['T2PartnerUid'] = self.t_2partner_uid

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationSheetId') is not None:
            self.application_sheet_id = m.get('ApplicationSheetId')

        if m.get('ApplicationTime') is not None:
            self.application_time = m.get('ApplicationTime')

        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('T2PartnerName') is not None:
            self.t_2partner_name = m.get('T2PartnerName')

        if m.get('T2PartnerUid') is not None:
            self.t_2partner_uid = m.get('T2PartnerUid')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        return self

