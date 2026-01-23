# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListAlertWebhooksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        webhooks: List[main_models.ListAlertWebhooksResponseBodyWebhooks] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total = total
        # webhooks
        self.webhooks = webhooks

    def validate(self):
        if self.webhooks:
            for v1 in self.webhooks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        result['webhooks'] = []
        if self.webhooks is not None:
            for k1 in self.webhooks:
                result['webhooks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        self.webhooks = []
        if m.get('webhooks') is not None:
            for k1 in m.get('webhooks'):
                temp_model = main_models.ListAlertWebhooksResponseBodyWebhooks()
                self.webhooks.append(temp_model.from_map(k1))

        return self

class ListAlertWebhooksResponseBodyWebhooks(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        headers: Dict[str, Any] = None,
        lang: str = None,
        method: str = None,
        name: str = None,
        url: str = None,
        webhook_id: str = None,
    ):
        self.content_type = content_type
        # headers
        self.headers = headers
        self.lang = lang
        self.method = method
        self.name = name
        self.url = url
        self.webhook_id = webhook_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.headers is not None:
            result['headers'] = self.headers

        if self.lang is not None:
            result['lang'] = self.lang

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        if self.url is not None:
            result['url'] = self.url

        if self.webhook_id is not None:
            result['webhookId'] = self.webhook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('webhookId') is not None:
            self.webhook_id = m.get('webhookId')

        return self

