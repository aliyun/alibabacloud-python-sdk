# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePackagesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: int = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
    ):
        # The page number to return.
        self.current_page = current_page
        # The ID of the asset instance to which the data asset package belongs.
        # 
        # > To query the list of MaxCompute data asset packages that are authorized for an SDPP connection by instance ID, call the **DescribeInstances** operation to obtain the instance ID.
        self.instance_id = instance_id
        # The language of the request and response. The default value is **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The keyword for the search. Fuzzy matching is supported.
        self.name = name
        # The maximum number of entries to return on each page.
        self.page_size = page_size
        # The ID of the product to which the data asset package belongs.
        # 
        # > To query the list of MaxCompute data asset packages that are authorized for an SDPP connection by product ID, call the **DescribeDataAssets** operation to obtain the product ID.
        self.product_id = product_id
        # The ID of the risk level for the data asset package.
        # 
        # - **1**: N/A: No sensitive data is detected.
        # 
        # - **2**: S1: Level 1 sensitive data.
        # 
        # - **3**: S2: Level 2 sensitive data.
        # 
        # - **4**: S3: Level 3 sensitive data.
        # 
        # - **5**: S4: Level 4 sensitive data.
        self.risk_level_id = risk_level_id
        # The ID of the sensitive data detection rule that the data asset package matches.
        # 
        # > To query the list of MaxCompute data asset packages that are authorized for an SDPP connection by the ID of a matching sensitive data detection rule, call the **DescribeRules** operation to obtain the rule ID.
        self.rule_id = rule_id

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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

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

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

