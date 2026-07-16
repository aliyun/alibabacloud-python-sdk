# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTablesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: int = None,
        lang: str = None,
        name: str = None,
        package_id: int = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
        service_region_id: str = None,
        template_id: int = None,
    ):
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The ID of the instance to which the data asset table belongs. Call the [DescribeInstances](~~DescribeInstances~~) operation to obtain this ID.
        self.instance_id = instance_id
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The search keyword. Fuzzy search is supported. For example, if you enter test, all results that contain test are returned.
        self.name = name
        # The ID of the package to which the data asset table belongs. Call the [DescribePackages](~~DescribePackages~~) operation to obtain this ID.
        self.package_id = package_id
        # The maximum number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The name of the product to which the data asset table belongs. Valid values include MaxCompute, OSS, ADS, OTS, and RDS. For more information about the supported products, see [Data asset types that support sensitive data detection](https://help.aliyun.com/document_detail/212906.html).
        self.product_code = product_code
        # The ID of the product to which the data asset table belongs. Call the [DescribeDataAssets](~~DescribeDataAssets~~) operation to obtain this ID.
        self.product_id = product_id
        # The ID of the risk level for the data asset table. Each risk level ID corresponds to a risk level name. Valid values:
        # 
        # - **1**: N/A. No sensitive data is detected.
        # 
        # - **2**: S1. Level 1 sensitive data.
        # 
        # - **3**: S2. Level 2 sensitive data.
        # 
        # - **4**: S3. Level 3 sensitive data.
        # 
        # - **5**: S4. Level 4 sensitive data.
        self.risk_level_id = risk_level_id
        # The ID of the sensitive data detection rule that the data asset table hits. Call the [DescribeRules](~~DescribeRules~~) operation to obtain this ID.
        self.rule_id = rule_id
        # The region where Data Security Center is available. For more information, see [Supported regions](https://help.aliyun.com/document_detail/214257.html).
        self.service_region_id = service_region_id
        # The ID of the industry-specific template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.package_id is not None:
            result['PackageId'] = self.package_id

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

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

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

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

