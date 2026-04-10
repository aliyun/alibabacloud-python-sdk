# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class QueryRedemptionRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryRedemptionRecordsResponseBodyData = None,
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
            temp_model = main_models.QueryRedemptionRecordsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class QueryRedemptionRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.QueryRedemptionRecordsResponseBodyDataItems] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.page = page
        self.page_size = page_size
        self.total = total
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        if self.total_pages is not None:
            result['totalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.QueryRedemptionRecordsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')

        return self

class QueryRedemptionRecordsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        allowed_models: List[str] = None,
        effective_at: str = None,
        expire_at: str = None,
        gmt_create: str = None,
        id: int = None,
        key_hash: str = None,
        out_biz_no: str = None,
        quota_balance: int = None,
        quota_status: str = None,
        redemption_order_no: str = None,
        status: str = None,
        template_id: int = None,
        tenant_id: int = None,
    ):
        self.allowed_models = allowed_models
        self.effective_at = effective_at
        self.expire_at = expire_at
        self.gmt_create = gmt_create
        self.id = id
        self.key_hash = key_hash
        self.out_biz_no = out_biz_no
        self.quota_balance = quota_balance
        self.quota_status = quota_status
        self.redemption_order_no = redemption_order_no
        self.status = status
        self.template_id = template_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        if self.effective_at is not None:
            result['effectiveAt'] = self.effective_at

        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.key_hash is not None:
            result['keyHash'] = self.key_hash

        if self.out_biz_no is not None:
            result['outBizNo'] = self.out_biz_no

        if self.quota_balance is not None:
            result['quotaBalance'] = self.quota_balance

        if self.quota_status is not None:
            result['quotaStatus'] = self.quota_status

        if self.redemption_order_no is not None:
            result['redemptionOrderNo'] = self.redemption_order_no

        if self.status is not None:
            result['status'] = self.status

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        if m.get('effectiveAt') is not None:
            self.effective_at = m.get('effectiveAt')

        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('keyHash') is not None:
            self.key_hash = m.get('keyHash')

        if m.get('outBizNo') is not None:
            self.out_biz_no = m.get('outBizNo')

        if m.get('quotaBalance') is not None:
            self.quota_balance = m.get('quotaBalance')

        if m.get('quotaStatus') is not None:
            self.quota_status = m.get('quotaStatus')

        if m.get('redemptionOrderNo') is not None:
            self.redemption_order_no = m.get('redemptionOrderNo')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

