# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCardSmsDetailsRequest(DaraModel):
    def __init__(
        self,
        biz_card_id: str = None,
        biz_digit_id: str = None,
        biz_sms_id: str = None,
        current_page: int = None,
        owner_id: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_date: str = None,
    ):
        # The card SMS sending ID. When you send a card SMS by calling the [SendCardSms](https://help.aliyun.com/document_detail/434120.html) or [SendBatchCardSms](https://help.aliyun.com/document_detail/434119.html) operation, obtain the BizCardId field from the response.
        self.biz_card_id = biz_card_id
        # The digital SMS sending ID. When you send a card SMS by calling the [SendCardSms](https://help.aliyun.com/document_detail/434120.html) or [SendBatchCardSms](https://help.aliyun.com/document_detail/434119.html) operation, obtain the BizDigitalId field from the response.
        self.biz_digit_id = biz_digit_id
        # The text SMS sending ID. When you send a card SMS by calling the [SendCardSms](https://help.aliyun.com/document_detail/434120.html) or [SendBatchCardSms](https://help.aliyun.com/document_detail/434119.html) operation, obtain the BizSmsId field from the response.
        self.biz_sms_id = biz_sms_id
        # The current page number when you paginate sending records.
        self.current_page = current_page
        self.owner_id = owner_id
        # The number of card SMS records to display on each page when you paginate sending records.
        # 
        # Valid values: 1 to 50.
        self.page_size = page_size
        # The domestic mobile phone number that received the SMS. Format: an 11-digit mobile phone number. For example, 1390000****.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The card SMS sending date. Records from the last 30 days can be queried.
        # 
        # Format: yyyyMMdd. For example, 20240112.
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
        if self.biz_card_id is not None:
            result['BizCardId'] = self.biz_card_id

        if self.biz_digit_id is not None:
            result['BizDigitId'] = self.biz_digit_id

        if self.biz_sms_id is not None:
            result['BizSmsId'] = self.biz_sms_id

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
        if m.get('BizCardId') is not None:
            self.biz_card_id = m.get('BizCardId')

        if m.get('BizDigitId') is not None:
            self.biz_digit_id = m.get('BizDigitId')

        if m.get('BizSmsId') is not None:
            self.biz_sms_id = m.get('BizSmsId')

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

