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
        # Card SMS sending ID, which is the BizCardId field in the response when calling SendCardSms or SendBatchCardSms.
        self.biz_card_id = biz_card_id
        # Digital SMS sending ID, which is the BizDigitalId field in the response when calling SendCardSms or SendBatchCardSms.
        self.biz_digit_id = biz_digit_id
        # Text SMS sending ID, which is the BizSmsId field in the response when calling SendCardSms or SendBatchCardSms.
        self.biz_sms_id = biz_sms_id
        # For paginated viewing of sending records, specify the current page number of the sending records.
        self.current_page = current_page
        self.owner_id = owner_id
        # For paginated viewing of sending records, specify the number of card SMS records to display per page.
        # 
        # The value range is 1~50.
        self.page_size = page_size
        # Domestic phone number that received the SMS. Format: 11-digit phone number, for example, 1390000****.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Card SMS sending date, supports querying records from the last 30 days.
        # 
        # Format: yyyyMMdd, for example, 20240112.
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

