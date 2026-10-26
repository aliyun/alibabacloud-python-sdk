# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTicket4AiProRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: int = None,
        ai_pro_id: str = None,
        custom_param: str = None,
        expire_time: int = None,
        quick_biuser_id: str = None,
        system_uid: str = None,
        ticket_num: int = None,
    ):
        self.account_name = account_name
        self.account_type = account_type
        # This parameter is required.
        self.ai_pro_id = ai_pro_id
        self.custom_param = custom_param
        self.expire_time = expire_time
        self.quick_biuser_id = quick_biuser_id
        self.system_uid = system_uid
        self.ticket_num = ticket_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.ai_pro_id is not None:
            result['AiProId'] = self.ai_pro_id

        if self.custom_param is not None:
            result['CustomParam'] = self.custom_param

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.quick_biuser_id is not None:
            result['QuickBIUserId'] = self.quick_biuser_id

        if self.system_uid is not None:
            result['SystemUid'] = self.system_uid

        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AiProId') is not None:
            self.ai_pro_id = m.get('AiProId')

        if m.get('CustomParam') is not None:
            self.custom_param = m.get('CustomParam')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('QuickBIUserId') is not None:
            self.quick_biuser_id = m.get('QuickBIUserId')

        if m.get('SystemUid') is not None:
            self.system_uid = m.get('SystemUid')

        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')

        return self

