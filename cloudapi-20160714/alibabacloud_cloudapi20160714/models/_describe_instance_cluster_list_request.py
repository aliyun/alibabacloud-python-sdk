# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceClusterListRequest(DaraModel):
    def __init__(
        self,
        instance_cluster_id: str = None,
        instance_cluster_name: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        # The cluster ID.
        self.instance_cluster_id = instance_cluster_id
        # The cluster name.
        self.instance_cluster_name = instance_cluster_name
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_cluster_id is not None:
            result['InstanceClusterId'] = self.instance_cluster_id

        if self.instance_cluster_name is not None:
            result['InstanceClusterName'] = self.instance_cluster_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceClusterId') is not None:
            self.instance_cluster_id = m.get('InstanceClusterId')

        if m.get('InstanceClusterName') is not None:
            self.instance_cluster_name = m.get('InstanceClusterName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

