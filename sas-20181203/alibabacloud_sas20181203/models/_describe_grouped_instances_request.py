# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupedInstancesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        field_value: str = None,
        group_field: str = None,
        lang: str = None,
        machine_types: str = None,
        no_page: bool = None,
        page_size: int = None,
        sale_version_check_code: str = None,
        vendor: int = None,
        vendors: str = None,
    ):
        # The page number from which query results start to be displayed. Default value: **1**, indicating that query results are displayed starting from page 1.
        self.current_page = current_page
        # The name of the asset group to query. Fuzzy search is supported.
        self.field_value = field_value
        # The filter condition for querying assets. Valid values:
        # 
        # - **groupId**: queries assets by group.
        # - **regionId**: queries assets by region.
        # - **vpcInstanceId**: queries assets by Virtual Private Cloud (VPC).
        # 
        # This parameter is required.
        self.group_field = group_field
        # The language type for requests and responses. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The type of assets to query. Fixed value: **ecs**, indicating Elastic Compute Service (ECS) instances.
        self.machine_types = machine_types
        # Specifies whether to enable paginated queries. Default value: **true**. Valid values:
        # - **true**: enables paginated queries.
        # - **false**: disables paginated queries.
        self.no_page = no_page
        # The number of entries per page in a paginated query. Default value: **20**, indicating that 20 entries of asset information are displayed per page.
        self.page_size = page_size
        # The edition filter for querying assets. Valid values:
        # 
        # - **sas_gte_advanced**: Advanced edition or higher
        # - **sas_gte_enterprise**: Enterprise edition or higher
        # - **sas_gt_basic**: paid editions
        # - **sas_eq_advanced**: Advanced edition only
        # - **sas_gt_anti_virus**: editions higher than Anti-virus edition
        self.sale_version_check_code = sale_version_check_code
        # The server vendor. Valid values:
        # 
        # - **0**: Alibaba Cloud assets
        # - **1**: non-cloud assets
        # - **2**: IDC assets
        # - **3**, **4**, **5**, **7**: assets from other cloud providers
        # - **8**: lightweight assets
        self.vendor = vendor
        # The server vendors. Separate multiple vendors with commas (,). Valid values:
        # 
        # - **0**: Alibaba Cloud assets
        # - **1**: non-cloud assets
        # - **2**: IDC assets
        # - **3**, **4**, **5**, **7**: assets from other cloud providers
        # - **8**: lightweight assets
        self.vendors = vendors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.group_field is not None:
            result['GroupField'] = self.group_field

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types

        if self.no_page is not None:
            result['NoPage'] = self.no_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sale_version_check_code is not None:
            result['SaleVersionCheckCode'] = self.sale_version_check_code

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vendors is not None:
            result['Vendors'] = self.vendors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('GroupField') is not None:
            self.group_field = m.get('GroupField')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')

        if m.get('NoPage') is not None:
            self.no_page = m.get('NoPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SaleVersionCheckCode') is not None:
            self.sale_version_check_code = m.get('SaleVersionCheckCode')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('Vendors') is not None:
            self.vendors = m.get('Vendors')

        return self

