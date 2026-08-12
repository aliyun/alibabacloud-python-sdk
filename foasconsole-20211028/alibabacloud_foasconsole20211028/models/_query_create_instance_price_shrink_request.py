# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCreateInstancePriceShrinkRequest(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec_shrink: str = None,
        instance_name: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
        storage_shrink: str = None,
        use_promotion_code: bool = None,
        v_switch_ids_shrink: str = None,
        vpc_id: str = None,
    ):
        # The processor architecture.
        self.architecture_type = architecture_type
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: enables auto-renewal.
        # - **false**: does not enable auto-renewal. (Default)
        # 
        # >This parameter is invalid for pay-as-you-go instances.
        self.auto_renew = auto_renew
        # The billing type. Valid values:
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The number of billing cycles.
        self.duration = duration
        # The extended reserved field.
        self.extra = extra
        # Specifies whether to select zone-disaster recovery resources.
        self.ha = ha
        # The zone-disaster recovery resource specifications.
        self.ha_resource_spec_shrink = ha_resource_spec_shrink
        # The workspace name.
        self.instance_name = instance_name
        # The billing cycle. Subscription instances support only Year and Month. Pay-as-you-go instances support Hour.
        self.pricing_cycle = pricing_cycle
        # The coupon code.
        self.promotion_code = promotion_code
        # The region.
        # 
        # This parameter is required.
        self.region = region
        # The resource specifications.
        self.resource_spec_shrink = resource_spec_shrink
        # The storage information.
        self.storage_shrink = storage_shrink
        # Specifies whether to use a coupon. Valid values:
        self.use_promotion_code = use_promotion_code
        # The vSwitch IDs.
        self.v_switch_ids_shrink = v_switch_ids_shrink
        # The VPC ID of the user.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.ha is not None:
            result['Ha'] = self.ha

        if self.ha_resource_spec_shrink is not None:
            result['HaResourceSpec'] = self.ha_resource_spec_shrink

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink

        if self.storage_shrink is not None:
            result['Storage'] = self.storage_shrink

        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code

        if self.v_switch_ids_shrink is not None:
            result['VSwitchIds'] = self.v_switch_ids_shrink

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('HaResourceSpec') is not None:
            self.ha_resource_spec_shrink = m.get('HaResourceSpec')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')

        if m.get('Storage') is not None:
            self.storage_shrink = m.get('Storage')

        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids_shrink = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

