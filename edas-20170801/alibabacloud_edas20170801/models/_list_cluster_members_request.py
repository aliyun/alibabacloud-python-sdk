# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClusterMembersRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_page: int = None,
        ecs_list: str = None,
        page_size: int = None,
    ):
        # The ID of the cluster. You can call the ListCluster operation to query the cluster ID. For more information, see [ListCluster](https://help.aliyun.com/document_detail/154995.html).
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The number of the page to return. If you do not specify this parameter, the first page is returned.
        self.current_page = current_page
        # The number of ECS instances.
        self.ecs_list = ecs_list
        # The number of ECS instances to return on each page. If you do not specify this parameter, all ECS instances in the specified cluster are returned on one page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.ecs_list is not None:
            result['EcsList'] = self.ecs_list

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EcsList') is not None:
            self.ecs_list = m.get('EcsList')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

