# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetConversationalAutomationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetConversationalAutomationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetConversationalAutomationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetConversationalAutomationResponseBodyData(DaraModel):
    def __init__(
        self,
        commands: List[main_models.GetConversationalAutomationResponseBodyDataCommands] = None,
        enable_welcome_message: bool = None,
        phone_number: str = None,
        prompts: List[str] = None,
    ):
        # The commands.
        self.commands = commands
        # Indicates whether the welcoming message is enabled.
        self.enable_welcome_message = enable_welcome_message
        # The phone number of the enterprise.
        self.phone_number = phone_number
        # The opening remarks.
        self.prompts = prompts

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

        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.prompts is not None:
            result['Prompts'] = self.prompts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k1 in m.get('Commands'):
                temp_model = main_models.GetConversationalAutomationResponseBodyDataCommands()
                self.commands.append(temp_model.from_map(k1))

        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Prompts') is not None:
            self.prompts = m.get('Prompts')

        return self

class GetConversationalAutomationResponseBodyDataCommands(DaraModel):
    def __init__(
        self,
        command_description: str = None,
        command_name: str = None,
    ):
        # The description of the command.
        self.command_description = command_description
        # The name of the command.
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

