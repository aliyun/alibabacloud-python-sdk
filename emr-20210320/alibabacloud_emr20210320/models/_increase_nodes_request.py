# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class IncreaseNodesRequest(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.ApplicationConfig] = None,
        auto_pay_order: bool = None,
        auto_renew: bool = None,
        cluster_id: str = None,
        increase_node_count: int = None,
        min_increase_node_count: int = None,
        node_group_id: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        promotions: List[main_models.Promotion] = None,
        region_id: str = None,
    ):
        # The application configurations. The number of array elements can range from 1 to 1,000.
        self.application_configs = application_configs
        # Specifies whether to automatically pay for the order. This parameter is effective only when the PaymentType of the node group is Subscription. Valid values:
        # 
        # - true: Automatically pays for the order.
        # 
        # - false: Does not automatically pay for the order.
        # 
        # Default value: false.
        self.auto_pay_order = auto_pay_order
        # Specifies whether to enable auto-renewal for the added nodes. The default value is false. Valid values:
        # 
        # - true: Enables auto-renewal.
        # 
        # - false: Disables auto-renewal.
        self.auto_renew = auto_renew
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The number of nodes to add. Valid values: 1 to 500.
        # 
        # This parameter is required.
        self.increase_node_count = increase_node_count
        # The minimum number of nodes to add in this scale-out operation. The value must be between 1 and 500.
        # 
        # - If you set this parameter and the available ECS inventory is less than IncreaseNodeCount, the system attempts to create at least the number of nodes specified by MinIncreaseNodeCount. The scale-out flow is then marked as `PARTIAL_COMPLETED`.
        # 
        # - If you do not set this parameter and the available ECS inventory is less than IncreaseNodeCount, the scale-out flow fails and is marked as `FAILED`.
        self.min_increase_node_count = min_increase_node_count
        # The ID of the node group to scale out.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The subscription duration. If PaymentDurationUnit is set to Month, valid values are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.payment_duration = payment_duration
        # The unit of the subscription duration. Valid values:
        # 
        # - Month: The unit is month.
        self.payment_duration_unit = payment_duration_unit
        self.promotions = promotions
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()
        if self.promotions:
            for v1 in self.promotions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['ApplicationConfigs'].append(k1.to_map() if k1 else None)

        if self.auto_pay_order is not None:
            result['AutoPayOrder'] = self.auto_pay_order

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.increase_node_count is not None:
            result['IncreaseNodeCount'] = self.increase_node_count

        if self.min_increase_node_count is not None:
            result['MinIncreaseNodeCount'] = self.min_increase_node_count

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k1 in m.get('ApplicationConfigs'):
                temp_model = main_models.ApplicationConfig()
                self.application_configs.append(temp_model.from_map(k1))

        if m.get('AutoPayOrder') is not None:
            self.auto_pay_order = m.get('AutoPayOrder')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('IncreaseNodeCount') is not None:
            self.increase_node_count = m.get('IncreaseNodeCount')

        if m.get('MinIncreaseNodeCount') is not None:
            self.min_increase_node_count = m.get('MinIncreaseNodeCount')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.Promotion()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

