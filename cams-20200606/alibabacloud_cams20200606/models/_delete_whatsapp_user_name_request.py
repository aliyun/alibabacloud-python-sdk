# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWhatsappUserNameRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        # The space ID of the ISV sub-customer or the instance ID of the direct customer. You can view the Space ID on the
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        return self

