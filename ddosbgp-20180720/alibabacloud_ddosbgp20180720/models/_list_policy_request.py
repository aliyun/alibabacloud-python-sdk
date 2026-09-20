# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPolicyRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        product_type: str = None,
        type: str = None,
    ):
        # The policy name.
        self.name = name
        # The page number of the current page in a paging query.
        self.page_no = page_no
        # The number of entries per page in a paging query. Default value: **10**.
        self.page_size = page_size
        # The applicable product type. Valid values:
        #  - **ecs**: queries the default policy applicable to ECS.
        # 
        # -  **slb**: queries the default policy applicable to SLB.
        # 
        # -  **eip**: queries the default policy applicable to EIP.
        # 
        #  - **gf-eip**: queries the default policy applicable to elastic IP addresses (EIPs) with Anti-DDoS Proxy Enabled.
        # 
        # > This parameter takes effect only when the policy type is `default`.
        self.product_type = product_type
        # The policy type. Valid values:
        # 
        # - **default**: the default mitigation policy.
        # 
        # - **l3**: the IP-specific mitigation policy.
        # 
        # - **l4**: the port-specific mitigation policy.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

