# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryTransferInListResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: main_models.QueryTransferInListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        if m.get('Data') is not None:
            temp_model = main_models.QueryTransferInListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryTransferInListResponseBodyData(DaraModel):
    def __init__(
        self,
        transfer_in_info: List[main_models.QueryTransferInListResponseBodyDataTransferInInfo] = None,
    ):
        self.transfer_in_info = transfer_in_info

    def validate(self):
        if self.transfer_in_info:
            for v1 in self.transfer_in_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TransferInInfo'] = []
        if self.transfer_in_info is not None:
            for k1 in self.transfer_in_info:
                result['TransferInInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.transfer_in_info = []
        if m.get('TransferInInfo') is not None:
            for k1 in m.get('TransferInInfo'):
                temp_model = main_models.QueryTransferInListResponseBodyDataTransferInInfo()
                self.transfer_in_info.append(temp_model.from_map(k1))

        return self

class QueryTransferInListResponseBodyDataTransferInInfo(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        email: str = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        instance_id: str = None,
        modification_date: str = None,
        modification_date_long: int = None,
        need_mail_check: bool = None,
        progress_bar_type: int = None,
        result_code: str = None,
        result_date: str = None,
        result_date_long: int = None,
        result_msg: str = None,
        simple_transfer_in_status: str = None,
        status: int = None,
        submission_date: str = None,
        submission_date_long: int = None,
        transfer_authorization_code_submission_date: str = None,
        transfer_authorization_code_submission_date_long: int = None,
        user_id: str = None,
        whois_mail_status: bool = None,
    ):
        self.domain_name = domain_name
        self.email = email
        self.expiration_date = expiration_date
        self.expiration_date_long = expiration_date_long
        self.instance_id = instance_id
        self.modification_date = modification_date
        self.modification_date_long = modification_date_long
        self.need_mail_check = need_mail_check
        self.progress_bar_type = progress_bar_type
        self.result_code = result_code
        self.result_date = result_date
        self.result_date_long = result_date_long
        self.result_msg = result_msg
        self.simple_transfer_in_status = simple_transfer_in_status
        self.status = status
        self.submission_date = submission_date
        self.submission_date_long = submission_date_long
        self.transfer_authorization_code_submission_date = transfer_authorization_code_submission_date
        self.transfer_authorization_code_submission_date_long = transfer_authorization_code_submission_date_long
        self.user_id = user_id
        self.whois_mail_status = whois_mail_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.email is not None:
            result['Email'] = self.email

        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date

        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date

        if self.modification_date_long is not None:
            result['ModificationDateLong'] = self.modification_date_long

        if self.need_mail_check is not None:
            result['NeedMailCheck'] = self.need_mail_check

        if self.progress_bar_type is not None:
            result['ProgressBarType'] = self.progress_bar_type

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_date is not None:
            result['ResultDate'] = self.result_date

        if self.result_date_long is not None:
            result['ResultDateLong'] = self.result_date_long

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.simple_transfer_in_status is not None:
            result['SimpleTransferInStatus'] = self.simple_transfer_in_status

        if self.status is not None:
            result['Status'] = self.status

        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date

        if self.submission_date_long is not None:
            result['SubmissionDateLong'] = self.submission_date_long

        if self.transfer_authorization_code_submission_date is not None:
            result['TransferAuthorizationCodeSubmissionDate'] = self.transfer_authorization_code_submission_date

        if self.transfer_authorization_code_submission_date_long is not None:
            result['TransferAuthorizationCodeSubmissionDateLong'] = self.transfer_authorization_code_submission_date_long

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.whois_mail_status is not None:
            result['WhoisMailStatus'] = self.whois_mail_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')

        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')

        if m.get('ModificationDateLong') is not None:
            self.modification_date_long = m.get('ModificationDateLong')

        if m.get('NeedMailCheck') is not None:
            self.need_mail_check = m.get('NeedMailCheck')

        if m.get('ProgressBarType') is not None:
            self.progress_bar_type = m.get('ProgressBarType')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultDate') is not None:
            self.result_date = m.get('ResultDate')

        if m.get('ResultDateLong') is not None:
            self.result_date_long = m.get('ResultDateLong')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('SimpleTransferInStatus') is not None:
            self.simple_transfer_in_status = m.get('SimpleTransferInStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')

        if m.get('SubmissionDateLong') is not None:
            self.submission_date_long = m.get('SubmissionDateLong')

        if m.get('TransferAuthorizationCodeSubmissionDate') is not None:
            self.transfer_authorization_code_submission_date = m.get('TransferAuthorizationCodeSubmissionDate')

        if m.get('TransferAuthorizationCodeSubmissionDateLong') is not None:
            self.transfer_authorization_code_submission_date_long = m.get('TransferAuthorizationCodeSubmissionDateLong')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WhoisMailStatus') is not None:
            self.whois_mail_status = m.get('WhoisMailStatus')

        return self

