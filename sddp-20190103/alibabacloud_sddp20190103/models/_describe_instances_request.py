# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        feature_type: int = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
        service_region_id: str = None,
    ):
        # The page number of the paged query. Default value: **1**.
        self.current_page = current_page
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the request and response. Default value: **zh_cn**.
        # Valid values:
        # 
        # - **zh_cn**: Chinese
        # 
        # - **en_us**: English
        self.lang = lang
        # The keyword to search for. Fuzzy match is supported. For example, if you enter "data", all data that contains "data" is returned.
        self.name = name
        # The maximum number of data asset instances to return on each page of a paged query. Default value: **10**.
        self.page_size = page_size
        # The name of the product to which the data asset instance belongs, such as MaxCompute, OSS, or RDS. For more information about the supported products, see [Data assets that can be scanned for sensitive data](https://help.aliyun.com/document_detail/212906.html).
        self.product_code = product_code
        # The ID of the product to which the data asset instance belongs. You can call the [DescribeDataAssets](~~DescribeDataAssets~~) operation to query the product ID.
        self.product_id = product_id
        # The ID of the threat level for the data asset instance. The higher the threat level ID, the more sensitive the data. Valid values:
        # 
        # - **1**: No sensitive data is detected. No threat.
        # 
        # - **2**: Threat level 1.
        # 
        # - **3**: Threat level 2.
        # 
        # - **4**: Threat level 3.
        # 
        # - **5**: Threat level 4.
        # 
        # - **6**: Threat level 5.
        # 
        # - **7**: Threat level 6.
        # 
        # - **8**: Threat level 7.
        # 
        # - **9**: Threat level 8.
        # 
        # - **10**: Threat level 9.
        # 
        # - **11**: Threat level 10.
        self.risk_level_id = risk_level_id
        # The ID of the sensitive data detection rule that the data asset instance hits. You can call the [DescribeRules](~~DescribeRules~~) operation and view the value of the **Id** parameter in the response to obtain the rule ID.
        self.rule_id = rule_id
        # The region where the data asset instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/214257.html).
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        return self

