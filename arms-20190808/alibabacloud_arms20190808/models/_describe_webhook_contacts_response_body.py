# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeWebhookContactsResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.DescribeWebhookContactsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned objects.
        self.page_bean = page_bean
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.DescribeWebhookContactsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWebhookContactsResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        total: int = None,
        webhook_contacts: List[main_models.DescribeWebhookContactsResponseBodyPageBeanWebhookContacts] = None,
    ):
        # The page number of the returned page.
        self.page = page
        # The number of alert contacts displayed on each page.
        self.size = size
        # The total number of alert contacts.
        self.total = total
        # The list of webhook alert contacts.
        self.webhook_contacts = webhook_contacts

    def validate(self):
        if self.webhook_contacts:
            for v1 in self.webhook_contacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        result['WebhookContacts'] = []
        if self.webhook_contacts is not None:
            for k1 in self.webhook_contacts:
                result['WebhookContacts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        self.webhook_contacts = []
        if m.get('WebhookContacts') is not None:
            for k1 in m.get('WebhookContacts'):
                temp_model = main_models.DescribeWebhookContactsResponseBodyPageBeanWebhookContacts()
                self.webhook_contacts.append(temp_model.from_map(k1))

        return self

class DescribeWebhookContactsResponseBodyPageBeanWebhookContacts(DaraModel):
    def __init__(
        self,
        webhook: main_models.DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook = None,
        webhook_id: float = None,
        webhook_name: str = None,
    ):
        # The details of the webhook alert contact.
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
            temp_model = main_models.DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook()
            self.webhook = temp_model.from_map(m.get('Webhook'))

        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')

        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')

        return self

class DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook(DaraModel):
    def __init__(
        self,
        biz_headers: Dict[str, Any] = None,
        biz_params: Dict[str, Any] = None,
        body: str = None,
        method: str = None,
        recover_body: str = None,
        url: str = None,
    ):
        # The header of the HTTP request.
        self.biz_headers = biz_headers
        # The parameters in the HTTP request.
        self.biz_params = biz_params
        # The alert notification template.
        self.body = body
        # The HTTP request method.
        # 
        # *   Get
        # *   Post
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

