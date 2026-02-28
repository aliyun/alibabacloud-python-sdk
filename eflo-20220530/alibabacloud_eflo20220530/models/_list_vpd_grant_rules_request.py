# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVpdGrantRulesRequest(DaraModel):
    def __init__(
        self,
        enable_page: bool = None,
        er_id: str = None,
        for_select: bool = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # Specifies whether to enable pagination query.
        self.enable_page = enable_page
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # Use the drop-down box
        self.for_select = for_select
        # Authorization Entry ID
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # The ID of the network instance that you want to query.
        self.instance_id = instance_id
        # Instance name
        self.instance_name = instance_name
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.for_select is not None:
            result['ForSelect'] = self.for_select

        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id

        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')

        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')

        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

