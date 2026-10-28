# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListProductsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_info: List[main_models.ListProductsResponseBodyProductInfo] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned for this query.
        self.max_results = max_results
        # The token that marks the position of the returned query data. An empty value indicates that all data has been queried.
        self.next_token = next_token
        # The information about the Alibaba Cloud service.
        self.product_info = product_info
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned for this request.
        self.total_count = total_count

    def validate(self):
        if self.product_info:
            for v1 in self.product_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ProductInfo'] = []
        if self.product_info is not None:
            for k1 in self.product_info:
                result['ProductInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.product_info = []
        if m.get('ProductInfo') is not None:
            for k1 in m.get('ProductInfo'):
                temp_model = main_models.ListProductsResponseBodyProductInfo()
                self.product_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProductsResponseBodyProductInfo(DaraModel):
    def __init__(
        self,
        common_quota_support: str = None,
        dynamic: bool = None,
        flow_control_support: str = None,
        product_code: str = None,
        product_name: str = None,
        product_name_en: str = None,
        second_category_id: int = None,
        second_category_name: str = None,
        second_category_name_en: str = None,
        white_list_label_quota_support: str = None,
    ):
        # Specifies whether general quotas are supported. Valid values:
        # 
        # - support: Supported.
        # 
        # - unsupport: Not supported.
        self.common_quota_support = common_quota_support
        # <notice>**[Deprecated]** We recommend that you do not use this parameter.</notice>
        # 
        # Specifies whether dynamic quota adjustment is supported. Valid values:
        # 
        # - true
        # 
        # - false
        self.dynamic = dynamic
        # Specifies whether API rate limits are supported. Valid values:
        # 
        # - support: Supported.
        # 
        # - unsupport: Not supported.
        self.flow_control_support = flow_control_support
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The name of the Alibaba Cloud service.
        self.product_name = product_name
        # The English name of the Alibaba Cloud service.
        self.product_name_en = product_name_en
        # The ID of the service category.
        self.second_category_id = second_category_id
        # The name of the service category.
        self.second_category_name = second_category_name
        # The English name of the service category.
        self.second_category_name_en = second_category_name_en
        # Specifies whether privileges are supported. Valid values:
        # 
        # - support: Supported.
        # 
        # - unsupport: Not supported.
        self.white_list_label_quota_support = white_list_label_quota_support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_quota_support is not None:
            result['CommonQuotaSupport'] = self.common_quota_support

        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic

        if self.flow_control_support is not None:
            result['FlowControlSupport'] = self.flow_control_support

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_name_en is not None:
            result['ProductNameEn'] = self.product_name_en

        if self.second_category_id is not None:
            result['SecondCategoryId'] = self.second_category_id

        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name

        if self.second_category_name_en is not None:
            result['SecondCategoryNameEn'] = self.second_category_name_en

        if self.white_list_label_quota_support is not None:
            result['WhiteListLabelQuotaSupport'] = self.white_list_label_quota_support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonQuotaSupport') is not None:
            self.common_quota_support = m.get('CommonQuotaSupport')

        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')

        if m.get('FlowControlSupport') is not None:
            self.flow_control_support = m.get('FlowControlSupport')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductNameEn') is not None:
            self.product_name_en = m.get('ProductNameEn')

        if m.get('SecondCategoryId') is not None:
            self.second_category_id = m.get('SecondCategoryId')

        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')

        if m.get('SecondCategoryNameEn') is not None:
            self.second_category_name_en = m.get('SecondCategoryNameEn')

        if m.get('WhiteListLabelQuotaSupport') is not None:
            self.white_list_label_quota_support = m.get('WhiteListLabelQuotaSupport')

        return self

