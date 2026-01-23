# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetUnassociatedCustomerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        invite_info_list: main_models.GetUnassociatedCustomerResponseBodyInviteInfoList = None,
        message: str = None,
        page_info: main_models.GetUnassociatedCustomerResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error Code, Candidate Value：
        # * 200: OK
        # * 1109: System error
        self.code = code
        # List of Invitation Information
        self.invite_info_list = invite_info_list
        # Message information
        self.message = message
        # Pagination Information
        self.page_info = page_info
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
        self.success = success

    def validate(self):
        if self.invite_info_list:
            self.invite_info_list.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.invite_info_list is not None:
            result['InviteInfoList'] = self.invite_info_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InviteInfoList') is not None:
            temp_model = main_models.GetUnassociatedCustomerResponseBodyInviteInfoList()
            self.invite_info_list = temp_model.from_map(m.get('InviteInfoList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.GetUnassociatedCustomerResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetUnassociatedCustomerResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # Pagination, current page.
        self.page = page
        # Pagination, record number on each page.
        self.page_size = page_size
        # Pagination, page volume in total.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetUnassociatedCustomerResponseBodyInviteInfoList(DaraModel):
    def __init__(
        self,
        invite_info: List[main_models.GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo] = None,
    ):
        self.invite_info = invite_info

    def validate(self):
        if self.invite_info:
            for v1 in self.invite_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InviteInfo'] = []
        if self.invite_info is not None:
            for k1 in self.invite_info:
                result['InviteInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invite_info = []
        if m.get('InviteInfo') is not None:
            for k1 in m.get('InviteInfo'):
                temp_model = main_models.GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo()
                self.invite_info.append(temp_model.from_map(k1))

        return self

class GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo(DaraModel):
    def __init__(
        self,
        account_nickname: str = None,
        email: str = None,
        gmt_create: str = None,
        invite_id: int = None,
        status: int = None,
    ):
        # The name of Customer who are to be invited.
        self.account_nickname = account_nickname
        # The Email of Customer who are to be invited.
        self.email = email
        # The time of email been sent out.
        self.gmt_create = gmt_create
        # Invitation ID
        self.invite_id = invite_id
        # Invitation Status:
        # * 0 No visit on registration URL
        # * 1 Successful Registration
        # * 2 Unsuccessful Registration
        # * 3 Registration URL have been visited, but no submitted sheet/ticket.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname

        if self.email is not None:
            result['Email'] = self.email

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.invite_id is not None:
            result['InviteId'] = self.invite_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

