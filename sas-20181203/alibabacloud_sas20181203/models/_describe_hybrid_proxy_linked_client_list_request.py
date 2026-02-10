# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridProxyLinkedClientListRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        current_page: int = None,
        page_size: int = None,
        proxy_uuid: str = None,
        remark: str = None,
        uuid: str = None,
    ):
        # The name of the proxy cluster. You can query the name of the proxy cluster in the Security Center console.
        self.cluster_name = cluster_name
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The UUID of the proxy node. You can call the DescribeHybridProxyList operation to query the UUID of the proxy node.
        self.proxy_uuid = proxy_uuid
        # The description of the proxy cluster.
        self.remark = remark
        # The UUID of the server on which the Security Center agent is installed. You can query the UUID by querying asset information.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proxy_uuid is not None:
            result['ProxyUuid'] = self.proxy_uuid

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProxyUuid') is not None:
            self.proxy_uuid = m.get('ProxyUuid')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

