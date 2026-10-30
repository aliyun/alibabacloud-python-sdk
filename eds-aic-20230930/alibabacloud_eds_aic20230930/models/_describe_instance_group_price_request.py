# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceGroupPriceRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        bandwidth: int = None,
        biz_region_id: str = None,
        image_id: str = None,
        instance_group_spec: str = None,
        instance_version: str = None,
        number_of_instances: int = None,
        order_type: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        sale_mode: str = None,
    ):
        # The number of instance groups.
        self.amount = amount
        # The ID of the bandwidth plan.
        self.bandwidth = bandwidth
        # The region ID.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The image ID.
        self.image_id = image_id
        # The instance group specifications.
        # 
        # This parameter is required.
        self.instance_group_spec = instance_group_spec
        # The instance version. You do not need to specify this parameter. The system automatically matches the value.
        self.instance_version = instance_version
        # The number of instances in the instance group.
        self.number_of_instances = number_of_instances
        # The order type.
        self.order_type = order_type
        # The subscription period. The unit is specified by PeriodUnit. Default value: 1.
        self.period = period
        # The unit of the subscription period. Default value: Month.
        self.period_unit = period_unit
        # The ID of the promotion.
        self.promotion_id = promotion_id
        # The sales mode. You do not need to specify this parameter. The system automatically matches the value.
        self.sale_mode = sale_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec

        if self.instance_version is not None:
            result['InstanceVersion'] = self.instance_version

        if self.number_of_instances is not None:
            result['NumberOfInstances'] = self.number_of_instances

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')

        if m.get('InstanceVersion') is not None:
            self.instance_version = m.get('InstanceVersion')

        if m.get('NumberOfInstances') is not None:
            self.number_of_instances = m.get('NumberOfInstances')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        return self

