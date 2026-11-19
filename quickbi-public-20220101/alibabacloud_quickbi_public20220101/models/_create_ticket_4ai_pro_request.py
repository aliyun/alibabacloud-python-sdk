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
        # The account of the access user to bind. Use this parameter together with AccountType when QuickBIUserId is not specified.
        self.account_name = account_name
        # The account type of the user. Valid values:
        # - 1: Alibaba Cloud account.
        # - 3: Quick BI custom account.
        # - 4: DingTalk.
        # - 5: RAM user.
        # - 9: WeCom.
        self.account_type = account_type
        # The ID of the AIPro embedding configuration. The configuration must exist, belong to the current organization, and have a status of 1.
        # 
        # This parameter is required.
        self.ai_pro_id = ai_pro_id
        # The custom pass-through parameter. If specified, it must be a valid JSON string.
        self.custom_param = custom_param
        # The validity period of the ticket, in minutes. Default value: 240. The value must be greater than 0.
        self.expire_time = expire_time
        # The QuickBI user ID of the access user to bind. Specify either this parameter or the combination of AccountName and AccountType.
        self.quick_biuser_id = quick_biuser_id
        # The custom system identifier. The length must be less than 150 characters.
        self.system_uid = system_uid
        # The number of times the ticket can be used. Default value: 1. Valid values: 1 to 99999.
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

