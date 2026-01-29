# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryFinancialAccountInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryFinancialAccountInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryFinancialAccountInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryFinancialAccountInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        is_financial_account: bool = None,
        member_group_id: int = None,
        member_group_name: str = None,
        member_nick_name: str = None,
        user_name: str = None,
    ):
        # The type of the financial account. A value of MASTER indicates that the account is a management account. A value of MEMBER indicates that the account is a member.
        self.account_type = account_type
        # Indicates whether the account is a financial account. A value of true indicates that the account is a financial account. A value of false indicates that the account is not a financial account.
        self.is_financial_account = is_financial_account
        # The ID of the group to which the member belongs.
        self.member_group_id = member_group_id
        # The name of the group to which the member belongs.
        self.member_group_name = member_group_name
        # The display name of the member.
        self.member_nick_name = member_nick_name
        # The username of the account.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.is_financial_account is not None:
            result['IsFinancialAccount'] = self.is_financial_account

        if self.member_group_id is not None:
            result['MemberGroupId'] = self.member_group_id

        if self.member_group_name is not None:
            result['MemberGroupName'] = self.member_group_name

        if self.member_nick_name is not None:
            result['MemberNickName'] = self.member_nick_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('IsFinancialAccount') is not None:
            self.is_financial_account = m.get('IsFinancialAccount')

        if m.get('MemberGroupId') is not None:
            self.member_group_id = m.get('MemberGroupId')

        if m.get('MemberGroupName') is not None:
            self.member_group_name = m.get('MemberGroupName')

        if m.get('MemberNickName') is not None:
            self.member_nick_name = m.get('MemberNickName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

