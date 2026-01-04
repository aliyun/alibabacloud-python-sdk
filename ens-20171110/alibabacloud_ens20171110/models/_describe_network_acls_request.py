# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkAclsRequest(DaraModel):
    def __init__(
        self,
        network_acl_id: str = None,
        network_acl_name: str = None,
        page_number: str = None,
        page_size: str = None,
        resource_id: str = None,
    ):
        # The ID of the network ACL.
        self.network_acl_id = network_acl_id
        # The name of the network ACL.
        self.network_acl_name = network_acl_name
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the associated instance.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.network_acl_name is not None:
            result['NetworkAclName'] = self.network_acl_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('NetworkAclName') is not None:
            self.network_acl_name = m.get('NetworkAclName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

