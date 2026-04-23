# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterQueryBillingRuleListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ModelRouterQueryBillingRuleListResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # maxResults
        self.max_results = max_results
        # nextToken
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ModelRouterQueryBillingRuleListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ModelRouterQueryBillingRuleListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ModelRouterQueryBillingRuleListResponseBodyDataList] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ModelRouterQueryBillingRuleListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ModelRouterQueryBillingRuleListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        billing_type: str = None,
        delete_tag: int = None,
        effective_time: str = None,
        expire_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        model_code: str = None,
        model_id: int = None,
        model_name: str = None,
        model_type: str = None,
        pricing_config: Any = None,
        symbol: str = None,
        version: int = None,
    ):
        self.billing_type = billing_type
        self.delete_tag = delete_tag
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.model_code = model_code
        self.model_id = model_id
        self.model_name = model_name
        self.model_type = model_type
        self.pricing_config = pricing_config
        self.symbol = symbol
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_type is not None:
            result['billingType'] = self.billing_type

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.pricing_config is not None:
            result['pricingConfig'] = self.pricing_config

        if self.symbol is not None:
            result['symbol'] = self.symbol

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingType') is not None:
            self.billing_type = m.get('billingType')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('pricingConfig') is not None:
            self.pricing_config = m.get('pricingConfig')

        if m.get('symbol') is not None:
            self.symbol = m.get('symbol')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

