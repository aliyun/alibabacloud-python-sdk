# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class UpdateConversationalAutomationRequest(DaraModel):
    def __init__(
        self,
        commands: List[main_models.UpdateConversationalAutomationRequestCommands] = None,
        cust_space_id: str = None,
        enable_welcome_message: bool = None,
        owner_id: int = None,
        phone_number: str = None,
        prompts: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The commands.
        self.commands = commands
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
        self.prompts = prompts
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.commands:
            for v1 in self.commands:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Commands'] = []
        if self.commands is not None:
            for k1 in self.commands:
                result['Commands'].append(k1.to_map() if k1 else None)

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.prompts is not None:
            result['Prompts'] = self.prompts

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k1 in m.get('Commands'):
                temp_model = main_models.UpdateConversationalAutomationRequestCommands()
                self.commands.append(temp_model.from_map(k1))

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Prompts') is not None:
            self.prompts = m.get('Prompts')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class UpdateConversationalAutomationRequestCommands(DaraModel):
    def __init__(
        self,
        command_description: str = None,
        command_name: str = None,
    ):
        # The description of the command.
        self.command_description = command_description
        # The command name.
        self.command_name = command_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_description is not None:
            result['CommandDescription'] = self.command_description

        if self.command_name is not None:
            result['CommandName'] = self.command_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')

        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        return self

