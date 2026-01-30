# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetTier2CouponApprovalDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTier2CouponApprovalDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTier2CouponApprovalDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTier2CouponApprovalDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        applicant_info: main_models.GetTier2CouponApprovalDetailResponseBodyDataApplicantInfo = None,
        application_reason: str = None,
        application_sheet_id: str = None,
        approval_status: str = None,
        coupon_receipt_uid_list: List[main_models.GetTier2CouponApprovalDetailResponseBodyDataCouponReceiptUidList] = None,
        remaining_quota: str = None,
        total_amount: str = None,
    ):
        self.applicant_info = applicant_info
        self.application_reason = application_reason
        self.application_sheet_id = application_sheet_id
        self.approval_status = approval_status
        self.coupon_receipt_uid_list = coupon_receipt_uid_list
        self.remaining_quota = remaining_quota
        self.total_amount = total_amount

    def validate(self):
        if self.applicant_info:
            self.applicant_info.validate()
        if self.coupon_receipt_uid_list:
            for v1 in self.coupon_receipt_uid_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant_info is not None:
            result['ApplicantInfo'] = self.applicant_info.to_map()

        if self.application_reason is not None:
            result['ApplicationReason'] = self.application_reason

        if self.application_sheet_id is not None:
            result['ApplicationSheetId'] = self.application_sheet_id

        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        result['CouponReceiptUidList'] = []
        if self.coupon_receipt_uid_list is not None:
            for k1 in self.coupon_receipt_uid_list:
                result['CouponReceiptUidList'].append(k1.to_map() if k1 else None)

        if self.remaining_quota is not None:
            result['RemainingQuota'] = self.remaining_quota

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantInfo') is not None:
            temp_model = main_models.GetTier2CouponApprovalDetailResponseBodyDataApplicantInfo()
            self.applicant_info = temp_model.from_map(m.get('ApplicantInfo'))

        if m.get('ApplicationReason') is not None:
            self.application_reason = m.get('ApplicationReason')

        if m.get('ApplicationSheetId') is not None:
            self.application_sheet_id = m.get('ApplicationSheetId')

        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        self.coupon_receipt_uid_list = []
        if m.get('CouponReceiptUidList') is not None:
            for k1 in m.get('CouponReceiptUidList'):
                temp_model = main_models.GetTier2CouponApprovalDetailResponseBodyDataCouponReceiptUidList()
                self.coupon_receipt_uid_list.append(temp_model.from_map(k1))

        if m.get('RemainingQuota') is not None:
            self.remaining_quota = m.get('RemainingQuota')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        return self

class GetTier2CouponApprovalDetailResponseBodyDataCouponReceiptUidList(DaraModel):
    def __init__(
        self,
        nominal_value: str = None,
        uid: int = None,
    ):
        self.nominal_value = nominal_value
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class GetTier2CouponApprovalDetailResponseBodyDataApplicantInfo(DaraModel):
    def __init__(
        self,
        applicable_products: str = None,
        application_time: str = None,
        order_type: str = None,
        t_2partner_name: str = None,
        t_2partner_uid: int = None,
        valid_until: str = None,
    ):
        self.applicable_products = applicable_products
        self.application_time = application_time
        self.order_type = order_type
        self.t_2partner_name = t_2partner_name
        self.t_2partner_uid = t_2partner_uid
        self.valid_until = valid_until

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products

        if self.application_time is not None:
            result['ApplicationTime'] = self.application_time

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.t_2partner_name is not None:
            result['T2PartnerName'] = self.t_2partner_name

        if self.t_2partner_uid is not None:
            result['T2PartnerUid'] = self.t_2partner_uid

        if self.valid_until is not None:
            result['ValidUntil'] = self.valid_until

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')

        if m.get('ApplicationTime') is not None:
            self.application_time = m.get('ApplicationTime')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('T2PartnerName') is not None:
            self.t_2partner_name = m.get('T2PartnerName')

        if m.get('T2PartnerUid') is not None:
            self.t_2partner_uid = m.get('T2PartnerUid')

        if m.get('ValidUntil') is not None:
            self.valid_until = m.get('ValidUntil')

        return self

