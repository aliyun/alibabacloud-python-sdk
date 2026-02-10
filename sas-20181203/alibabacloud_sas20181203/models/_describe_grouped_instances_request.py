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
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The name of the group to which the assets belong. Fuzzy search is supported.
        self.field_value = field_value
        # The filter condition that you want to use to query the assets. Valid values:
        # 
        # *   **groupId**: the group to which the assets belong
        # *   **regionId**: the region in which the assets reside
        # *   **vpcInstanceId**: the virtual private cloud (VPC) in which the assets reside
        # 
        # This parameter is required.
        self.group_field = group_field
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The type of the assets that you want to query. Set the value to **ecs**, which indicates Elastic Compute Service (ECS) instances.
        self.machine_types = machine_types
        # Specifies whether to enable paged query. Default value: **true**. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.no_page = no_page
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The edition of Security Center that protects the asset. Valid values:
        # 
        # * **sas_gte_advanced**: the Advanced edition or higher
        # * **sas_gte_enterprise**: the Enterprise edition or higher
        # * **sas_gt_basic:** a paid edition
        # * **sas_eq_advanced:** the Advanced edition
        # * **sas_gt_anti_virus:** an edition higher than the Anti-virus edition
        self.sale_version_check_code = sale_version_check_code
        # The source of the server. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud.
        # *   **1**: a third-party cloud server
        # *   **2**: a server in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a lightweight asset
        self.vendor = vendor
        # The source of the server. Separate multiple sources with commas (,).Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud.
        # *   **1**: a third-party cloud server
        # *   **2**: a server in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a lightweight asset
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

