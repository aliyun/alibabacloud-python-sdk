# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDefenseRulesRequest(DaraModel):
    def __init__(
        self,
        defense_type: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        rule_type: str = None,
    ):
        # The type of the protection rule. Valid values:
        # 
        # - **template** (default): template protection rules.
        # 
        # - **resource**: rules for protected objects.
        # 
        # - **global**: global rules.
        self.defense_type = defense_type
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The query conditions. Specify this parameter as a JSON string.
        # 
        # > The query results for protection rules vary based on the query conditions. For more information, see **Query parameter details**.
        self.query = query
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the protection rule. Valid values:
        # 
        # - **whitelist**: a whitelist rule
        # 
        # - **defense** (default): a protection rule
        # 
        # > This parameter is required only when **DefenseType** is set to **template**.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

