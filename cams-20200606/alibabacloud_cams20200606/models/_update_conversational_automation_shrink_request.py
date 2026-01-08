# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConversationalAutomationShrinkRequest(DaraModel):
    def __init__(
        self,
        commands_shrink: str = None,
        cust_space_id: str = None,
        enable_welcome_message: bool = None,
        owner_id: int = None,
        phone_number: str = None,
        prompts_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The commands.
        self.commands_shrink = commands_shrink
        # The space ID of the RAM user within the independent software vendor (ISV) account or the instance ID of the customer of Alibaba Cloud.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # Specifies whether to enable the welcoming message.
        self.enable_welcome_message = enable_welcome_message
        self.owner_id = owner_id
        # The phone number of the enterprise.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The opening remarks.
        self.prompts_shrink = prompts_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commands_shrink is not None:
            result['Commands'] = self.commands_shrink

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.prompts_shrink is not None:
            result['Prompts'] = self.prompts_shrink

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands_shrink = m.get('Commands')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Prompts') is not None:
            self.prompts_shrink = m.get('Prompts')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

