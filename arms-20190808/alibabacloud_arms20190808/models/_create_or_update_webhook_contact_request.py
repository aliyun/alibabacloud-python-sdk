# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateWebhookContactRequest(DaraModel):
    def __init__(
        self,
        biz_headers: str = None,
        biz_params: str = None,
        body: str = None,
        method: str = None,
        recover_body: str = None,
        url: str = None,
        webhook_id: int = None,
        webhook_name: str = None,
    ):
        # The HTTP request headers.
        self.biz_headers = biz_headers
        # The parameters in the HTTP request.
        self.biz_params = biz_params
        # The notification template that is sent when an alert is triggered. This parameter is required if the **Method** parameter is set to **Post**. You can use the `$content` placeholder to specify the notification content. The content cannot exceed 500 characters in length. For more information, see [Variable description of a notification template](https://help.aliyun.com/document_detail/251834.html).\\\\
        self.body = body
        # The HTTP request method.
        # 
        # *   Post
        # *   Get
        # 
        # This parameter is required.
        self.method = method
        # The notification template that is sent when an alert is resolved. This parameter is required if the **Method** parameter is set to **Post**. You can use the `$content` placeholder to specify the notification content. The content cannot exceed 500 characters in length. For more information, see [Variable description of a notification template](https://help.aliyun.com/document_detail/251834.html).
        self.recover_body = recover_body
        # The URL of the HTTP request **method**.
        # 
        # This parameter is required.
        self.url = url
        # The ID of the webhook alert contact.
        # 
        # *   If you do not specify this parameter, a new webhook alert contact is created.
        # * If you specify this parameter, the specified webhook alert contact is modified.
        self.webhook_id = webhook_id
        # The name of the webhook alert contact.
        # 
        # This parameter is required.
        self.webhook_name = webhook_name

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

        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id

        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name

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

        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')

        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')

        return self

