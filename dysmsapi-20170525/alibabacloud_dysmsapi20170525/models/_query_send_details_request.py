# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySendDetailsRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        current_page: int = None,
        owner_id: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_date: str = None,
    ):
        # The delivery receipt ID. This is the `BizId` returned in the response when you call the [SendSms](https://help.aliyun.com/document_detail/419273.html) or [SendBatchSms](https://help.aliyun.com/document_detail/419274.html) operation.
        # 
        # > You can specify only one `BizId`.
        self.biz_id = biz_id
        # The current page number for paginated results.
        # 
        # This parameter is required.
        self.current_page = current_page
        self.owner_id = owner_id
        # The number of delivery records to return on each page.
        # 
        # Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The phone number to query. The format is as follows:
        # 
        # - For messages to the Chinese mainland, use an 11-digit phone number, such as 1390000\\*\\*\\*\\*.
        # 
        # - For international SMS, use the format: country/region code + phone number, such as 8520000\\*\\*\\*\\*.
        # 
        # > You can specify only one phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The date when the SMS message was sent. You can query records from the past 30 days.
        # 
        # Format: **yyyyMMdd**, for example, 20250601.
        # 
        # This parameter is required.
        self.send_date = send_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.send_date is not None:
            result['SendDate'] = self.send_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')

        return self

