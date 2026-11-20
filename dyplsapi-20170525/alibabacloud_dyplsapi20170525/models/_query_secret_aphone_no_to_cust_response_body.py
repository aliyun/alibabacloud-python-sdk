# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySecretAPhoneNoToCustResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QuerySecretAPhoneNoToCustResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of the denied access.
        self.access_denied_detail = access_denied_detail
        # Request status code.
        self.code = code
        # The struct for querying the A number reporting status.
        self.data = data
        # Error message for a failed operation.
        self.message = message
        # The returned ID.
        self.request_id = request_id
        # Indicates whether the request succeeded. Valid values:
        # 
        # - true: Succeeded.
        # 
        # - false: Failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QuerySecretAPhoneNoToCustResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySecretAPhoneNoToCustResponseBodyData(DaraModel):
    def __init__(
        self,
        ano_white_group_id: str = None,
        cust_phone_no: str = None,
        no_type: str = None,
        phone_no_a: str = None,
        remark: str = None,
        report_result: str = None,
        report_status: str = None,
    ):
        # The ID of the A number group to which the number belongs.
        self.ano_white_group_id = ano_white_group_id
        # The contact phone number of the handler or legal representative for landline reporting.
        self.cust_phone_no = cust_phone_no
        # The number type. Valid values:
        # 
        # - Mobile: Mobile phone number.
        # 
        # - Fixed: Landline number.
        self.no_type = no_type
        # A number.
        self.phone_no_a = phone_no_a
        # Remarks (user\\"s own business notes).
        self.remark = remark
        # The reason for review failure.
        self.report_result = report_result
        # The reporting result. Valid values:
        # 
        # - REVIEWING: Under review.
        # 
        # - PASS: Review passed.
        # 
        # - FAIL: Review failed.
        self.report_status = report_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ano_white_group_id is not None:
            result['ANoWhiteGroupId'] = self.ano_white_group_id

        if self.cust_phone_no is not None:
            result['CustPhoneNo'] = self.cust_phone_no

        if self.no_type is not None:
            result['NoType'] = self.no_type

        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.report_result is not None:
            result['ReportResult'] = self.report_result

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ANoWhiteGroupId') is not None:
            self.ano_white_group_id = m.get('ANoWhiteGroupId')

        if m.get('CustPhoneNo') is not None:
            self.cust_phone_no = m.get('CustPhoneNo')

        if m.get('NoType') is not None:
            self.no_type = m.get('NoType')

        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ReportResult') is not None:
            self.report_result = m.get('ReportResult')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        return self

