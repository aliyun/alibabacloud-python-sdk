# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWhatsappUserNameRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
        transfer_action: str = None,
        username: str = None,
    ):
        # The space ID of the ISV sub-customer or the instance ID of the direct customer. You can view the space ID on the
        # <props="china">[Channel Management](https://chatapp.console.aliyun.com/ChannelsManagement)
        # <props="intl">[Channel Management](https://chatapp.console.alibabacloud.com/CustomerList)
        # page.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The business phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The transfer action that controls what happens when the requested username is currently used by another business phone number in the same business asset portfolio. For example, use this parameter when you want to move an existing username to another phone number. Valid values:
        # 
        #  - none (default): does not transfer the account. If another business phone number in the same business asset portfolio already uses this username, the request fails with error code 147005.
        # 
        #  - force_transfer: transfers the account from the other business phone number to this business phone number. The account is removed from the other phone number and assigned to this phone number.
        self.transfer_action = transfer_action
        # Whatsapp user name
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.transfer_action is not None:
            result['TransferAction'] = self.transfer_action

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('TransferAction') is not None:
            self.transfer_action = m.get('TransferAction')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

