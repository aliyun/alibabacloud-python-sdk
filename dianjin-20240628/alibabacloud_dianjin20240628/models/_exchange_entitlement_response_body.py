# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class ExchangeEntitlementResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ExchangeEntitlementResponseBodyData = None,
        message: str = None,
        retry_able: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.retry_able = retry_able
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.retry_able is not None:
            result['retryAble'] = self.retry_able

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ExchangeEntitlementResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ExchangeEntitlementResponseBodyData(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        effective_at: str = None,
        endpoint: str = None,
        expire_at: str = None,
        key_hash: str = None,
        redemption_order_no: str = None,
        reused: bool = None,
        template: main_models.ExchangeEntitlementResponseBodyDataTemplate = None,
    ):
        self.api_key = api_key
        self.effective_at = effective_at
        self.endpoint = endpoint
        self.expire_at = expire_at
        self.key_hash = key_hash
        self.redemption_order_no = redemption_order_no
        self.reused = reused
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.effective_at is not None:
            result['effectiveAt'] = self.effective_at

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        if self.key_hash is not None:
            result['keyHash'] = self.key_hash

        if self.redemption_order_no is not None:
            result['redemptionOrderNo'] = self.redemption_order_no

        if self.reused is not None:
            result['reused'] = self.reused

        if self.template is not None:
            result['template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('effectiveAt') is not None:
            self.effective_at = m.get('effectiveAt')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('keyHash') is not None:
            self.key_hash = m.get('keyHash')

        if m.get('redemptionOrderNo') is not None:
            self.redemption_order_no = m.get('redemptionOrderNo')

        if m.get('reused') is not None:
            self.reused = m.get('reused')

        if m.get('template') is not None:
            temp_model = main_models.ExchangeEntitlementResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('template'))

        return self

class ExchangeEntitlementResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        allowed_models: List[str] = None,
        quota_limit: int = None,
        template_id: int = None,
        template_name: str = None,
        type: str = None,
    ):
        self.allowed_models = allowed_models
        self.quota_limit = quota_limit
        self.template_id = template_id
        self.template_name = template_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        if self.quota_limit is not None:
            result['quotaLimit'] = self.quota_limit

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        if m.get('quotaLimit') is not None:
            self.quota_limit = m.get('quotaLimit')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

