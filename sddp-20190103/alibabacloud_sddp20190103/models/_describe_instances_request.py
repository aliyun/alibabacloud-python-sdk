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
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang
        # The keyword that is used to search for data assets. DSC searches for data assets based on the keyword that you specify in fuzzy match mode. For example, if you specify data, all data assets whose names contain data are queried.
        self.name = name
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The name of the service to which the data asset belongs, such as MaxCompute, OSS, and ApsaraDB RDS. For more information about the types of data assets from which DSC can scan for sensitive data, see [Supported data assets](https://help.aliyun.com/document_detail/212906.html).
        self.product_code = product_code
        # The ID of the service to which the data asset belongs. You can call the [DescribeDataAssets](~~DescribeDataAssets~~) operation to query the ID of the service.
        self.product_id = product_id
        # The sensitivity level ID of the data asset. A higher sensitivity level indicates that the identified data is more sensitive. Valid values:
        # 
        # *   **1**: No sensitive data is identified.
        # *   **2**: sensitive data at level 1.
        # *   **3**: sensitive data at level 2.
        # *   **4**: sensitive data at level 3
        # *   **5**: sensitive data at level 4.
        # *   **6**: sensitive data at level 5.
        # *   **7**: sensitive data at level 6.
        # *   **8**: sensitive data at level 7.
        # *   **9**: sensitive data at level 8.
        # *   **10**: sensitive data at level 9.
        # *   **11**: sensitive data at level 10.
        self.risk_level_id = risk_level_id
        # The ID of the sensitive data detection rule that the data asset hits. You can call the [DescribeRules](~~DescribeRules~~) operation and obtain the ID of the sensitive data detection rule from the **Id** response parameter.
        self.rule_id = rule_id
        # The region where the data asset resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/214257.html).
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

