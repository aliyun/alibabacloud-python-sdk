# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec_shrink: str = None,
        ha_vswitch_ids_shrink: str = None,
        instance_name: str = None,
        monitor_type: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_spec_shrink: str = None,
        storage_shrink: str = None,
        tag_shrink: str = None,
        use_promotion_code: bool = None,
        v_switch_ids_shrink: str = None,
        vpc_id: str = None,
    ):
        # The processor architecture.
        self.architecture_type = architecture_type
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled. This is the default value.
        # 
        # > This parameter does not take effect for pay-as-you-go instances.
        self.auto_renew = auto_renew
        # The billing method. Valid values:
        # - POST: pay-as-you-go.
        # - PRE: subscription.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The subscription duration.
        # 
        # > This parameter is required when ChargeType is set to PRE.
        self.duration = duration
        # The extended field.
        self.extra = extra
        # Specifies whether to use zone-disaster recovery resources.
        self.ha = ha
        # The zone-disaster recovery resource specifications.
        self.ha_resource_spec_shrink = ha_resource_spec_shrink
        # The list of vSwitch IDs in the secondary zone for zone-disaster recovery.
        self.ha_vswitch_ids_shrink = ha_vswitch_ids_shrink
        # The workspace name. The name must start with a lowercase letter and can contain lowercase letters, digits, and hyphens (-). The name cannot end with a hyphen.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The type of monitoring and alerting service. You can select ARMS or CloudMonitor.
        self.monitor_type = monitor_type
        # The unit of the subscription duration. Valid values:
        # 
        # - **year**: year.
        # - **month**: month.
        # 
        # > This parameter is required when ChargeType is set to PRE.
        self.pricing_cycle = pricing_cycle
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID.
        # 
        # This parameter is required.
        self.region = region
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource specifications.
        # 
        # > This parameter is required when ChargeType is set to PRE.
        self.resource_spec_shrink = resource_spec_shrink
        # The storage parameters.
        # 
        # This parameter is required.
        self.storage_shrink = storage_shrink
        # The list of tags. A maximum of 20 tags can be specified.
        self.tag_shrink = tag_shrink
        # Specifies whether to use a coupon. Valid values:
        # - true: Use a coupon.
        # - false: Do not use a coupon.
        self.use_promotion_code = use_promotion_code
        # The list of vSwitch IDs.
        # 
        # This parameter is required.
        self.v_switch_ids_shrink = v_switch_ids_shrink
        # The virtual private cloud (VPC) ID.
        # 
        # This parameter is required.
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

        if self.ha_vswitch_ids_shrink is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids_shrink

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink

        if self.storage_shrink is not None:
            result['Storage'] = self.storage_shrink

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

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

        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids_shrink = m.get('HaVSwitchIds')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')

        if m.get('Storage') is not None:
            self.storage_shrink = m.get('Storage')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids_shrink = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

