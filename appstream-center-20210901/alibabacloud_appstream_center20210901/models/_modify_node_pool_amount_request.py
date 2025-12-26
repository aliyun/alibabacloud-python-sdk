# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ModifyNodePoolAmountRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        node_pool: main_models.ModifyNodePoolAmountRequestNodePool = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The parameters related to the configuration change of the node pool.
        # 
        # This parameter is required.
        self.node_pool = node_pool
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        if self.node_pool:
            self.node_pool.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('NodePool') is not None:
            temp_model = main_models.ModifyNodePoolAmountRequestNodePool()
            self.node_pool = temp_model.from_map(m.get('NodePool'))

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

class ModifyNodePoolAmountRequestNodePool(DaraModel):
    def __init__(
        self,
        node_amount: int = None,
        pre_paid_node_amount_modify_mode: str = None,
        pre_paid_node_amount_modify_node_ids: List[str] = None,
    ):
        # The total number of subscription nodes after the change.
        # 
        # This parameter is required.
        self.node_amount = node_amount
        # The change mode of subscription nodes.
        # 
        # Valid value:
        # 
        # *   EXPAND_FROM_POST_PAID_EXPLICIT: changes from specified pay-as-you-go nodes
        self.pre_paid_node_amount_modify_mode = pre_paid_node_amount_modify_mode
        # The nodes for which you want to change the billing method.
        self.pre_paid_node_amount_modify_node_ids = pre_paid_node_amount_modify_node_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount

        if self.pre_paid_node_amount_modify_mode is not None:
            result['PrePaidNodeAmountModifyMode'] = self.pre_paid_node_amount_modify_mode

        if self.pre_paid_node_amount_modify_node_ids is not None:
            result['PrePaidNodeAmountModifyNodeIds'] = self.pre_paid_node_amount_modify_node_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')

        if m.get('PrePaidNodeAmountModifyMode') is not None:
            self.pre_paid_node_amount_modify_mode = m.get('PrePaidNodeAmountModifyMode')

        if m.get('PrePaidNodeAmountModifyNodeIds') is not None:
            self.pre_paid_node_amount_modify_node_ids = m.get('PrePaidNodeAmountModifyNodeIds')

        return self

