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
        # Indicates whether the request was successful.
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
        roles: List[str] = None,
        seat_id: str = None,
        spec_type: str = None,
        status: str = None,
    ):
        # The member business ID.
        self.account_biz_id = account_biz_id
        # The ID of the member account.
        self.account_id = account_id
        # The name of the member account.
        self.account_name = account_name
        # API Key ID
        self.api_key_id = api_key_id
        # The email address of the member.
        self.email = email
        # The time when the member joined.
        self.gmt_create = gmt_create
        # The masked API key.
        self.masked_api_key = masked_api_key
        # The organization ID.
        self.org_id = org_id
        # The list of member roles.
        self.roles = roles
        # The ID used to allocate the seat resource.
        self.seat_id = seat_id
        # The seat specification type. Valid values:
        # - standard: Standard seat.
        # - pro: Pro seat.
        # - max: Premium seat.
        self.spec_type = spec_type
        # The member status.
        self.status = status

    def validate(self):
        pass

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

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.seat_id is not None:
            result['SeatId'] = self.seat_id

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('SeatId') is not None:
            self.seat_id = m.get('SeatId')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

