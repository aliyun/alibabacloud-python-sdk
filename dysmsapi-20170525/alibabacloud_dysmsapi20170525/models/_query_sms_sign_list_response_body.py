# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySmsSignListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        sms_sign_list: List[main_models.QuerySmsSignListResponseBodySmsSignList] = None,
        total_count: int = None,
    ):
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The returned message.
        self.message = message
        # The number of signatures per page. Valid values: **1 to 50**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried message signatures.
        self.sms_sign_list = sms_sign_list
        # The total number of signatures.
        self.total_count = total_count

    def validate(self):
        if self.sms_sign_list:
            for v1 in self.sms_sign_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SmsSignList'] = []
        if self.sms_sign_list is not None:
            for k1 in self.sms_sign_list:
                result['SmsSignList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sms_sign_list = []
        if m.get('SmsSignList') is not None:
            for k1 in m.get('SmsSignList'):
                temp_model = main_models.QuerySmsSignListResponseBodySmsSignList()
                self.sms_sign_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QuerySmsSignListResponseBodySmsSignList(DaraModel):
    def __init__(
        self,
        app_icp_record_id: int = None,
        audit_status: str = None,
        authorization_letter_id: int = None,
        business_type: str = None,
        create_date: str = None,
        order_id: str = None,
        reason: main_models.QuerySmsSignListResponseBodySmsSignListReason = None,
        sign_name: str = None,
        trademark_id: int = None,
        authorization_letter_audit_pass: bool = None,
    ):
        self.app_icp_record_id = app_icp_record_id
        # The approval status of the signature. Valid values:
        # 
        # *   **AUDIT_STATE_INIT**: The signature is pending approval.
        # *   **AUDIT_STATE_PASS**: The signature is approved.
        # *   **AUDIT_STATE_NOT_PASS**: The signature is rejected. You can view the reason in the Reason response parameter.
        # *   **AUDIT_STATE_CANCEL**: The approval is canceled.
        self.audit_status = audit_status
        self.authorization_letter_id = authorization_letter_id
        # The type of the signature scenario. The return value ends with "type". Valid values:
        # 
        # *   Verification code type
        # *   General-purpose type
        self.business_type = business_type
        # The time when the signature was created. Format: yyyy-MM-dd HH:mm:ss.
        self.create_date = create_date
        # The ticket ID.
        self.order_id = order_id
        # The approval remarks.
        # 
        # *   If the value of AuditStatus is **AUDIT_STATE_PASS** or **AUDIT_STATE_INIT**, the value of Reason is No Approval Remarks.
        # *   If the value of AuditStatus is **AUDIT_STATE_NOT_PASS**, the reason why the signature is rejected is returned.
        self.reason = reason
        # The name of the signature.
        self.sign_name = sign_name
        self.trademark_id = trademark_id
        self.authorization_letter_audit_pass = authorization_letter_audit_pass

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_icp_record_id is not None:
            result['AppIcpRecordId'] = self.app_icp_record_id

        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.reason is not None:
            result['Reason'] = self.reason.to_map()

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.trademark_id is not None:
            result['TrademarkId'] = self.trademark_id

        if self.authorization_letter_audit_pass is not None:
            result['authorizationLetterAuditPass'] = self.authorization_letter_audit_pass

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIcpRecordId') is not None:
            self.app_icp_record_id = m.get('AppIcpRecordId')

        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Reason') is not None:
            temp_model = main_models.QuerySmsSignListResponseBodySmsSignListReason()
            self.reason = temp_model.from_map(m.get('Reason'))

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('TrademarkId') is not None:
            self.trademark_id = m.get('TrademarkId')

        if m.get('authorizationLetterAuditPass') is not None:
            self.authorization_letter_audit_pass = m.get('authorizationLetterAuditPass')

        return self

class QuerySmsSignListResponseBodySmsSignListReason(DaraModel):
    def __init__(
        self,
        reject_date: str = None,
        reject_info: str = None,
        reject_sub_info: str = None,
    ):
        # The time when the signature was rejected. Format: yyyy-MM-dd HH:mm:ss.
        self.reject_date = reject_date
        # The reason why the signature was rejected.
        self.reject_info = reject_info
        # The remarks about the rejection.
        self.reject_sub_info = reject_sub_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reject_date is not None:
            result['RejectDate'] = self.reject_date

        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info

        if self.reject_sub_info is not None:
            result['RejectSubInfo'] = self.reject_sub_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RejectDate') is not None:
            self.reject_date = m.get('RejectDate')

        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')

        if m.get('RejectSubInfo') is not None:
            self.reject_sub_info = m.get('RejectSubInfo')

        return self

