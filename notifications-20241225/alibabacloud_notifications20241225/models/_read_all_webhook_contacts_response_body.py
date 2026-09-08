# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadAllWebhookContactsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ReadAllWebhookContactsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The query result.
        self.data = data
        # The business message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ReadAllWebhookContactsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadAllWebhookContactsResponseBodyData(DaraModel):
    def __init__(
        self,
        bot_security_token: str = None,
        contact_id: int = None,
        contact_name: str = None,
        security_token: str = None,
        server_url: str = None,
        template_code: str = None,
        webhook_type: str = None,
    ):
        # The security token.
        self.bot_security_token = bot_security_token
        # webhook id
        self.contact_id = contact_id
        # The name of the webhook contact.
        self.contact_name = contact_name
        # The security token (deprecated).
        self.security_token = security_token
        # The bot URL.
        self.server_url = server_url
        # The template code.
        self.template_code = template_code
        # The webhook type.
        self.webhook_type = webhook_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_security_token is not None:
            result['BotSecurityToken'] = self.bot_security_token

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.server_url is not None:
            result['ServerUrl'] = self.server_url

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.webhook_type is not None:
            result['WebhookType'] = self.webhook_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotSecurityToken') is not None:
            self.bot_security_token = m.get('BotSecurityToken')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('WebhookType') is not None:
            self.webhook_type = m.get('WebhookType')

        return self

