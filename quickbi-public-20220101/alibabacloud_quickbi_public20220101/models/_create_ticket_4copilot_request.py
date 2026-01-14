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
        # User\\"s account name.
        # <notice>Note: Only one of userId and accountName needs to be filled in. If neither is provided, it will default to the report owner, and the report will be accessed with that user\\"s identity.</notice>
        self.account_name = account_name
        # User\\"s account type:
        # 
        # - 1: Alibaba Cloud Primary Account
        # 
        # - 3: Quick BI Self-built Account
        # 
        # - 4: DingTalk
        # 
        # - 5: Alibaba Cloud RAM Account
        # 
        # - 6: Third-party Account (SAML, OAuth, etc.)
        # 
        # - 9: WeCom
        # 
        # - 10: Feishu
        # 
        # <notice>Note: If accountName is not empty, then accountType must also be provided.</notice>
        self.account_type = account_type
        # ID of the Smart Q module to be embedded.
        # 
        # This parameter is required.
        self.copilot_id = copilot_id
        # Expiration time.
        # 
        # - Unit: minutes, maximum 240 (4 hours).
        # 
        # - Default: 240.
        self.expire_time = expire_time
        # Range of ticket quantity:
        # 
        # - Default value is 1.
        # 
        # - Recommended value is 1.
        # 
        # - Maximum value is 99999.
        # 
        # Each time a ticket is used, the ticket count decreases by 1.
        self.ticket_num = ticket_num
        # Quick BI\\"s UserId.
        # 
        # - You can obtain this by calling [3.1.7 Get User Details Based on Third-Party Account] or other relevant APIs.
        # 
        # <notice>Note: Only one of userId and accountName needs to be filled in. If neither is provided, it will default to the report owner, and the report will be accessed with that user\\"s identity.</notice>
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

