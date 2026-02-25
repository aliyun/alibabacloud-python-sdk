# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeNodeGroupsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        component_type: str = None,
        instance_id: str = None,
        node_group_ids: List[str] = None,
        node_group_name: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.component_type = component_type
        self.instance_id = instance_id
        self.node_group_ids = node_group_ids
        self.node_group_name = node_group_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.node_group_ids is not None:
            result['nodeGroupIds'] = self.node_group_ids

        if self.node_group_name is not None:
            result['nodeGroupName'] = self.node_group_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('nodeGroupIds') is not None:
            self.node_group_ids = m.get('nodeGroupIds')

        if m.get('nodeGroupName') is not None:
            self.node_group_name = m.get('nodeGroupName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

