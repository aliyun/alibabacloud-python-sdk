# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListApsWebhookResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        webhook: List[main_models.ListApsWebhookResponseBodyWebhook] = None,
    ):
        # API status or POP error code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The unique ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The array of webhooks.
        self.webhook = webhook

    def validate(self):
        if self.webhook:
            for v1 in self.webhook:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['Webhook'] = []
        if self.webhook is not None:
            for k1 in self.webhook:
                result['Webhook'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.webhook = []
        if m.get('Webhook') is not None:
            for k1 in m.get('Webhook'):
                temp_model = main_models.ListApsWebhookResponseBodyWebhook()
                self.webhook.append(temp_model.from_map(k1))

        return self

class ListApsWebhookResponseBodyWebhook(DaraModel):
    def __init__(
        self,
        key: str = None,
        name: str = None,
        url: str = None,
        webhook_id: str = None,
        webhook_type: str = None,
    ):
        # Signing key
        self.key = key
        # The name of the webhook.
        self.name = name
        # The request URL.
        self.url = url
        # The ID of the webhook that you want to delete.
        self.webhook_id = webhook_id
        # Webhook type.
        self.webhook_type = webhook_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        if self.url is not None:
            result['Url'] = self.url

        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id

        if self.webhook_type is not None:
            result['WebhookType'] = self.webhook_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')

        if m.get('WebhookType') is not None:
            self.webhook_type = m.get('WebhookType')

        return self

