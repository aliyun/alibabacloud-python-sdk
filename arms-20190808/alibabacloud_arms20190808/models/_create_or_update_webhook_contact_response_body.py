# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateWebhookContactResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        webhook_contact: main_models.CreateOrUpdateWebhookContactResponseBodyWebhookContact = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned webhook alert contact.
        self.webhook_contact = webhook_contact

    def validate(self):
        if self.webhook_contact:
            self.webhook_contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.webhook_contact is not None:
            result['WebhookContact'] = self.webhook_contact.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WebhookContact') is not None:
            temp_model = main_models.CreateOrUpdateWebhookContactResponseBodyWebhookContact()
            self.webhook_contact = temp_model.from_map(m.get('WebhookContact'))

        return self

class CreateOrUpdateWebhookContactResponseBodyWebhookContact(DaraModel):
    def __init__(
        self,
        webhook: main_models.CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook = None,
        webhook_id: float = None,
        webhook_name: str = None,
    ):
        # The information about the webhook alert contact.
        self.webhook = webhook
        # The ID of the webhook alert contact.
        self.webhook_id = webhook_id
        # The name of the webhook alert contact.
        self.webhook_name = webhook_name

    def validate(self):
        if self.webhook:
            self.webhook.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.webhook is not None:
            result['Webhook'] = self.webhook.to_map()

        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id

        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Webhook') is not None:
            temp_model = main_models.CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook()
            self.webhook = temp_model.from_map(m.get('Webhook'))

        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')

        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')

        return self

class CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook(DaraModel):
    def __init__(
        self,
        biz_headers: str = None,
        biz_params: str = None,
        body: str = None,
        method: str = None,
        recover_body: str = None,
        url: str = None,
    ):
        # The HTTP request headers.
        self.biz_headers = biz_headers
        # The parameters in the HTTP request.
        self.biz_params = biz_params
        # The alert notification template.
        self.body = body
        # The HTTP request method.
        # 
        # *   Post
        # *   Get
        self.method = method
        # The notification template for clearing alerts.
        self.recover_body = recover_body
        # The URL of the request method.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_headers is not None:
            result['BizHeaders'] = self.biz_headers

        if self.biz_params is not None:
            result['BizParams'] = self.biz_params

        if self.body is not None:
            result['Body'] = self.body

        if self.method is not None:
            result['Method'] = self.method

        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizHeaders') is not None:
            self.biz_headers = m.get('BizHeaders')

        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

