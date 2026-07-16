# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupedContainerInstancesRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        current_page: int = None,
        field_value: str = None,
        group_field: str = None,
        logical_exp: str = None,
        page_size: int = None,
    ):
        # The conditions for searching assets. This parameter is in JSON format. Separate multiple conditions with commas (,). Example: `[{"name":"riskStatus","value":"YES"},{"name":"riskLevel","value":"2"}]`.
        # > You can search for assets by instance ID, instance name, VPC ID, region, public IP address, and other conditions. Call [DescribeCriteria](~~DescribeCriteria~~) to query the supported search conditions.
        self.criteria = criteria
        # The page number of the page to return. Default value: **1**, which indicates that the first page is returned.
        self.current_page = current_page
        # The search condition for the specified group type. Set the search condition based on the type specified by GroupField:
        # - If **GroupField** is set to **pod**: specify the pod name to query.
        # - If **GroupField** is set to **appName**: specify the application name to query.
        # - If **GroupField** is set to **namespace**: specify the namespace to query.
        # - If **GroupField** is set to **clusterId**: specify the cluster ID to query.
        # - If **GroupField** is set to **image**: specify the image name to query.
        # > All the preceding search conditions support fuzzy match.
        self.field_value = field_value
        # The group type to query. Valid values:
        # - **pod**: pod
        # - **appName**: application name
        # - **namespace**: namespace
        # - **clusterId**: cluster ID
        # - **image**: image.
        # 
        # This parameter is required.
        self.group_field = group_field
        # The logical relationship among multiple search conditions. Valid values:
        # - **OR**: The search conditions are evaluated with a logical OR.
        # - **AND**: The search conditions are evaluated with a logical AND.
        self.logical_exp = logical_exp
        # The number of container assets to display on each page when paging is used. Default value: **20**, which indicates that 20 container assets are displayed on each page.
        # > Do not leave PageSize empty.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.group_field is not None:
            result['GroupField'] = self.group_field

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('GroupField') is not None:
            self.group_field = m.get('GroupField')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

