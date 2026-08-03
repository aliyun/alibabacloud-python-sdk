# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class GetAccessKeyLastUsedProductsResponseBody(DaraModel):
    def __init__(
        self,
        products: List[main_models.GetAccessKeyLastUsedProductsResponseBodyProducts] = None,
        request_id: str = None,
    ):
        # The list of returned Alibaba Cloud services.
        # 
        # This parameter is required.
        self.products = products
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.GetAccessKeyLastUsedProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccessKeyLastUsedProductsResponseBodyProducts(DaraModel):
    def __init__(
        self,
        detail: str = None,
        service_name: str = None,
        service_name_cn: str = None,
        service_name_en: str = None,
        source: str = None,
        used_timestamp: int = None,
    ):
        # The event details.
        self.detail = detail
        # The Alibaba Cloud service.
        self.service_name = service_name
        # The Chinese name of the Alibaba Cloud service.
        self.service_name_cn = service_name_cn
        # The English name of the Alibaba Cloud service.
        self.service_name_en = service_name_en
        # The source of the last usage record.
        # 
        # Valid values:
        # 
        # - Internal
        # 
        #   <!-- -->
        # 
        #   :
        # 
        #   <!-- -->
        # 
        #   Other event
        # 
        #   <!-- -->
        # 
        # - ManagementEvent
        # 
        #   <!-- -->
        # 
        #   :
        # 
        #   <!-- -->
        # 
        #   Management event
        # 
        #   <!-- -->
        # 
        # - DataEvent
        # 
        #   <!-- -->
        # 
        #   :
        # 
        #   <!-- -->
        # 
        #   Data event
        # 
        #   <!-- -->
        self.source = source
        # The timestamp when the Alibaba Cloud service was used. Unit: milliseconds.
        self.used_timestamp = used_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_name_cn is not None:
            result['ServiceNameCn'] = self.service_name_cn

        if self.service_name_en is not None:
            result['ServiceNameEn'] = self.service_name_en

        if self.source is not None:
            result['Source'] = self.source

        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceNameCn') is not None:
            self.service_name_cn = m.get('ServiceNameCn')

        if m.get('ServiceNameEn') is not None:
            self.service_name_en = m.get('ServiceNameEn')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')

        return self

