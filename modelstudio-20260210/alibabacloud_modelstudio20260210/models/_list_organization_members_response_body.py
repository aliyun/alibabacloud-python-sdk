# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class ListOrganizationMembersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListOrganizationMembersResponseBodyData] = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        success: bool = None,
        total: int = None,
    ):
        # The response status code.
        self.code = code
        # The business data.
        self.data = data
        # The response message.
        self.message = message
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # Indicates whether the request is successful.
        self.success = success
        # The total number of records.
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

        if self.success is not None:
            result['Success'] = self.success

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
                temp_model = main_models.ListOrganizationMembersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListOrganizationMembersResponseBodyData(DaraModel):
    def __init__(
        self,
        account_biz_id: str = None,
        account_id: str = None,
        account_name: str = None,
        api_key_id: str = None,
        email: str = None,
        gmt_create: str = None,
        masked_api_key: str = None,
        org_id: str = None,
        pack_limit_info: main_models.ListOrganizationMembersResponseBodyDataPackLimitInfo = None,
        roles: List[str] = None,
        seat_id: str = None,
        spec_type: str = None,
        status: str = None,
        subscription_info: main_models.ListOrganizationMembersResponseBodyDataSubscriptionInfo = None,
    ):
        # The member business ID.
        self.account_biz_id = account_biz_id
        # The ID of the member accounts.
        self.account_id = account_id
        # The name of the member accounts.
        self.account_name = account_name
        # API Key ID
        self.api_key_id = api_key_id
        # The member email address.
        self.email = email
        # The time when the member joined.
        self.gmt_create = gmt_create
        # The masked API key.
        self.masked_api_key = masked_api_key
        # The organization ID.
        self.org_id = org_id
        self.pack_limit_info = pack_limit_info
        # The list of member roles.
        self.roles = roles
        # The seat resource allocate ID.
        self.seat_id = seat_id
        # The seat specification type. Valid values:
        # - standard: Standard seat.
        # - pro: Pro seat.
        # - max: Max seat.
        self.spec_type = spec_type
        # The member status.
        self.status = status
        self.subscription_info = subscription_info

    def validate(self):
        if self.pack_limit_info:
            self.pack_limit_info.validate()
        if self.subscription_info:
            self.subscription_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_biz_id is not None:
            result['AccountBizId'] = self.account_biz_id

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.api_key_id is not None:
            result['ApiKeyId'] = self.api_key_id

        if self.email is not None:
            result['Email'] = self.email

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.masked_api_key is not None:
            result['MaskedApiKey'] = self.masked_api_key

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.pack_limit_info is not None:
            result['PackLimitInfo'] = self.pack_limit_info.to_map()

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.seat_id is not None:
            result['SeatId'] = self.seat_id

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.status is not None:
            result['Status'] = self.status

        if self.subscription_info is not None:
            result['SubscriptionInfo'] = self.subscription_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountBizId') is not None:
            self.account_biz_id = m.get('AccountBizId')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ApiKeyId') is not None:
            self.api_key_id = m.get('ApiKeyId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('MaskedApiKey') is not None:
            self.masked_api_key = m.get('MaskedApiKey')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('PackLimitInfo') is not None:
            temp_model = main_models.ListOrganizationMembersResponseBodyDataPackLimitInfo()
            self.pack_limit_info = temp_model.from_map(m.get('PackLimitInfo'))

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('SeatId') is not None:
            self.seat_id = m.get('SeatId')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubscriptionInfo') is not None:
            temp_model = main_models.ListOrganizationMembersResponseBodyDataSubscriptionInfo()
            self.subscription_info = temp_model.from_map(m.get('SubscriptionInfo'))

        return self

class ListOrganizationMembersResponseBodyDataSubscriptionInfo(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        equity_list: List[main_models.ListOrganizationMembersResponseBodyDataSubscriptionInfoEquityList] = None,
        instance_code: str = None,
        pay_mode: str = None,
        product_code: str = None,
        spec_type: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.equity_list = equity_list
        self.instance_code = instance_code
        self.pay_mode = pay_mode
        self.product_code = product_code
        self.spec_type = spec_type
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.equity_list:
            for v1 in self.equity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['EquityList'] = []
        if self.equity_list is not None:
            for k1 in self.equity_list:
                result['EquityList'].append(k1.to_map() if k1 else None)

        if self.instance_code is not None:
            result['InstanceCode'] = self.instance_code

        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.equity_list = []
        if m.get('EquityList') is not None:
            for k1 in m.get('EquityList'):
                temp_model = main_models.ListOrganizationMembersResponseBodyDataSubscriptionInfoEquityList()
                self.equity_list.append(temp_model.from_map(k1))

        if m.get('InstanceCode') is not None:
            self.instance_code = m.get('InstanceCode')

        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListOrganizationMembersResponseBodyDataSubscriptionInfoEquityList(DaraModel):
    def __init__(
        self,
        cycle_end_time: int = None,
        cycle_start_time: int = None,
        cycle_surplus_value: float = None,
        cycle_total_value: float = None,
        equity_type: str = None,
        equity_unit: str = None,
    ):
        self.cycle_end_time = cycle_end_time
        self.cycle_start_time = cycle_start_time
        self.cycle_surplus_value = cycle_surplus_value
        self.cycle_total_value = cycle_total_value
        self.equity_type = equity_type
        self.equity_unit = equity_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_end_time is not None:
            result['CycleEndTime'] = self.cycle_end_time

        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time

        if self.cycle_surplus_value is not None:
            result['CycleSurplusValue'] = self.cycle_surplus_value

        if self.cycle_total_value is not None:
            result['CycleTotalValue'] = self.cycle_total_value

        if self.equity_type is not None:
            result['EquityType'] = self.equity_type

        if self.equity_unit is not None:
            result['EquityUnit'] = self.equity_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleEndTime') is not None:
            self.cycle_end_time = m.get('CycleEndTime')

        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')

        if m.get('CycleSurplusValue') is not None:
            self.cycle_surplus_value = m.get('CycleSurplusValue')

        if m.get('CycleTotalValue') is not None:
            self.cycle_total_value = m.get('CycleTotalValue')

        if m.get('EquityType') is not None:
            self.equity_type = m.get('EquityType')

        if m.get('EquityUnit') is not None:
            self.equity_unit = m.get('EquityUnit')

        return self

class ListOrganizationMembersResponseBodyDataPackLimitInfo(DaraModel):
    def __init__(
        self,
        available_limit: float = None,
        cycle_end_time: int = None,
        cycle_start_time: int = None,
        frozen_credits: float = None,
        has_share_limit: bool = None,
        is_available: bool = None,
        last_confirmed_time: int = None,
        upper_limit: float = None,
        used_credits: float = None,
    ):
        self.available_limit = available_limit
        self.cycle_end_time = cycle_end_time
        self.cycle_start_time = cycle_start_time
        self.frozen_credits = frozen_credits
        self.has_share_limit = has_share_limit
        self.is_available = is_available
        self.last_confirmed_time = last_confirmed_time
        self.upper_limit = upper_limit
        self.used_credits = used_credits

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_limit is not None:
            result['AvailableLimit'] = self.available_limit

        if self.cycle_end_time is not None:
            result['CycleEndTime'] = self.cycle_end_time

        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time

        if self.frozen_credits is not None:
            result['FrozenCredits'] = self.frozen_credits

        if self.has_share_limit is not None:
            result['HasShareLimit'] = self.has_share_limit

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.last_confirmed_time is not None:
            result['LastConfirmedTime'] = self.last_confirmed_time

        if self.upper_limit is not None:
            result['UpperLimit'] = self.upper_limit

        if self.used_credits is not None:
            result['UsedCredits'] = self.used_credits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableLimit') is not None:
            self.available_limit = m.get('AvailableLimit')

        if m.get('CycleEndTime') is not None:
            self.cycle_end_time = m.get('CycleEndTime')

        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')

        if m.get('FrozenCredits') is not None:
            self.frozen_credits = m.get('FrozenCredits')

        if m.get('HasShareLimit') is not None:
            self.has_share_limit = m.get('HasShareLimit')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('LastConfirmedTime') is not None:
            self.last_confirmed_time = m.get('LastConfirmedTime')

        if m.get('UpperLimit') is not None:
            self.upper_limit = m.get('UpperLimit')

        if m.get('UsedCredits') is not None:
            self.used_credits = m.get('UsedCredits')

        return self

