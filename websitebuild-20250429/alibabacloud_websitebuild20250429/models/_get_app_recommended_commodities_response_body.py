# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetAppRecommendedCommoditiesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.GetAppRecommendedCommoditiesResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.GetAppRecommendedCommoditiesResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class GetAppRecommendedCommoditiesResponseBodyModule(DaraModel):
    def __init__(
        self,
        commodities: List[main_models.GetAppRecommendedCommoditiesResponseBodyModuleCommodities] = None,
    ):
        self.commodities = commodities

    def validate(self):
        if self.commodities:
            for v1 in self.commodities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Commodities'] = []
        if self.commodities is not None:
            for k1 in self.commodities:
                result['Commodities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodities = []
        if m.get('Commodities') is not None:
            for k1 in m.get('Commodities'):
                temp_model = main_models.GetAppRecommendedCommoditiesResponseBodyModuleCommodities()
                self.commodities.append(temp_model.from_map(k1))

        return self

class GetAppRecommendedCommoditiesResponseBodyModuleCommodities(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        extend: Dict[str, str] = None,
        order_type: str = None,
        priority: int = None,
        promotion_commodity_id: str = None,
        redirect_url: str = None,
        status: str = None,
    ):
        self.commodity_code = commodity_code
        self.extend = extend
        self.order_type = order_type
        self.priority = priority
        self.promotion_commodity_id = promotion_commodity_id
        self.redirect_url = redirect_url
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.promotion_commodity_id is not None:
            result['PromotionCommodityId'] = self.promotion_commodity_id

        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PromotionCommodityId') is not None:
            self.promotion_commodity_id = m.get('PromotionCommodityId')

        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

