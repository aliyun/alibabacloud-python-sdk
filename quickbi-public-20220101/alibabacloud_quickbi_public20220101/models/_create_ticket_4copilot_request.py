# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTicket4CopilotRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: int = None,
        copilot_id: str = None,
        expire_time: int = None,
        ticket_num: int = None,
        user_id: str = None,
    ):
        # The name of the user account.
        # >Notice: Note: Specify either UserId or AccountName. If you leave both parameters empty, the ticket is bound to the API caller by default. Access is then granted based on the caller\\"s identity.
        self.account_name = account_name
        # The type of the user account:
        # 
        # - 1: Alibaba Cloud account
        # 
        # - 3: Quick BI user
        # 
        # - 4: DingTalk
        # 
        # - 5: RAM user
        # 
        # - 6: Third-party account (an account integrated using protocols such as SAML or OAuth)
        # 
        # - 9: WeCom
        # 
        # - 10: Lark
        # 
        # >Notice: 
        # 
        # Note: This parameter is required if you specify AccountName.
        self.account_type = account_type
        # The ID of the embedded Copilot module.
        # 
        # This parameter is required.
        self.copilot_id = copilot_id
        # The expiration time of the ticket.
        # 
        # - Unit: minutes. The maximum validity period is 240 minutes (4 hours).
        # 
        # - Default: 240 minutes.
        self.expire_time = expire_time
        # The number of times the ticket can be used. The value can range from 1 to 99,999.
        # 
        # - Default: 1.
        # 
        # - Recommended: 1.
        # 
        # - Maximum: 99,999.
        # 
        # Each access decrements the ticket\\"s usage count by one.
        self.ticket_num = ticket_num
        # The ID of the Quick BI user. This is not your Alibaba Cloud account ID. Call the QueryUserInfoByAccount operation to obtain the user ID. Example: `fe67f61a35a94b7da1a34ba174a7****`.
        # 
        # >Notice: 
        # 
        # Note: Specify either UserId or AccountName. If you leave both parameters empty, the ticket is bound to the API caller by default. Access is then granted based on the caller\\"s identity.
        self.user_id = user_id

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

        if self.copilot_id is not None:
            result['CopilotId'] = self.copilot_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('CopilotId') is not None:
            self.copilot_id = m.get('CopilotId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

