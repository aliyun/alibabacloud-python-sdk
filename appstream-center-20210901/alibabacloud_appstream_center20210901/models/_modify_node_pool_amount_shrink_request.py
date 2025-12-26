# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNodePoolAmountShrinkRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        node_pool_shrink: str = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The parameters related to the configuration change of the node pool.
        # 
        # This parameter is required.
        self.node_pool_shrink = node_pool_shrink
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

