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
        # The search conditions for assets. Specify the value in the JSON format. Separate multiple search conditions with commas (,). Example: `[{"name":"riskStatus","value":"YES"},{"name":"riskLevel","value":"2"}]`.
        # 
        # >  Supported search conditions include the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can call the [DescribeCriteria](~~DescribeCriteria~~) operation to query the supported search conditions.
        self.criteria = criteria
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The keyword that you want to use to query containers. This parameter depends on the value of the GroupField parameter.
        # 
        # *   If the **GroupField** parameter is set to **pod**, set this parameter to the name of the pod that you want to query.
        # *   If the **GroupField** parameter is set to **appName**, set this parameter to the name of the application that you want to query.
        # *   If the **GroupField** parameter is set to **namespace**, set this parameter to the namespace that you want to query.
        # *   If the **GroupField** parameter is set to **clusterId**, set this parameter to the ID of the cluster that you want to query.
        # *   If the **GroupField** parameter is set to **image**, set this parameter to the name of the image that you want to query.
        # 
        # >  Fuzzy match is supported.
        self.field_value = field_value
        # The group type that you want to use to query containers. Valid values:
        # 
        # *   **pod**
        # *   **appName**
        # *   **namespace**
        # *   **clusterId**
        # *   **image**
        # 
        # This parameter is required.
        self.group_field = group_field
        # The logical relationship that you want to use to evaluate multiple search conditions. Valid values:
        # 
        # *   **OR**: Search conditions are evaluated by using a logical **OR**.
        # *   **AND**: Search conditions are evaluated by using a logical **AND**.
        self.logical_exp = logical_exp
        # The number of entries to return on each page. Default value: **20**.
        # 
        # >  We recommend that you do not leave this parameter empty.
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

