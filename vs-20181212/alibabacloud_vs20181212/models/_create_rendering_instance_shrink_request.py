# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRenderingInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        attributes_shrink: str = None,
        auto_renew: bool = None,
        client_info_shrink: str = None,
        instance_billing_cycle: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth: int = None,
        period: str = None,
        rendering_spec: str = None,
        storage_size: str = None,
    ):
        # > Keep the default value unless you have special requirements. If you have special requirements, contact technical support to confirm and then specify the relevant parameters.
        # 
        # The attribute information.
        self.attributes_shrink = attributes_shrink
        # > This parameter takes effect only when `InstanceChargeType` is set to `PrePaid` (subscription).
        # 
        # Specifies whether to enable auto-renewal. Valid values:
        # * **true**: enables auto-renewal.
        # * **false**: disables auto-renewal.
        self.auto_renew = auto_renew
        # The client information.
        self.client_info_shrink = client_info_shrink
        # > This parameter takes effect only when `InstanceChargeType` is set to `PostPaid` (pay-as-you-go).
        # 
        # The billing cycle. Valid values:
        # 
        # - Hour: hour.
        self.instance_billing_cycle = instance_billing_cycle
        # The billing method of the instance. Valid values:
        # 
        # - PrePaid (default): subscription.
        # - PostPaid: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # > Only one billing method is supported. If a billing method already exists, the new value is invalid by default, and the existing billing method prevails. Note that this parameter is required when you purchase the instance for the first time.
        # 
        # The network billing type. Valid values:
        # - 95BandwidthByMonth: monthly 95th percentile bandwidth.
        self.internet_charge_type = internet_charge_type
        # The maximum bandwidth. Unit: Mbit/s. Default value: 10.
        self.internet_max_bandwidth = internet_max_bandwidth
        # > This parameter takes effect only when `InstanceChargeType` is set to `PrePaid` (subscription).
        # 
        # The subscription duration. Valid values (Note: If you select 12, the duration is calculated as one year. For other values, the unit is months):
        # 
        # - 1 (default)
        # - 2
        # - 3
        # - 4
        # - 5
        # - 6
        # - 7
        # - 8
        # - 9
        # - 12
        self.period = period
        # The specification of the cloud application service instance.
        # 
        # - If the specification belongs to the crs.cp.* series, the billing method can be subscription or pay-as-you-go.
        # - If the specification belongs to the crs.vm.* series, the billing method can be subscription or pay-as-you-go.
        # - For other series, only the subscription billing method is supported.
        # 
        # This parameter is required.
        self.rendering_spec = rendering_spec
        # The cloud storage capacity used by the cloud application service instance. Note: This is not local storage.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_info_shrink is not None:
            result['ClientInfo'] = self.client_info_shrink

        if self.instance_billing_cycle is not None:
            result['InstanceBillingCycle'] = self.instance_billing_cycle

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth is not None:
            result['InternetMaxBandwidth'] = self.internet_max_bandwidth

        if self.period is not None:
            result['Period'] = self.period

        if self.rendering_spec is not None:
            result['RenderingSpec'] = self.rendering_spec

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientInfo') is not None:
            self.client_info_shrink = m.get('ClientInfo')

        if m.get('InstanceBillingCycle') is not None:
            self.instance_billing_cycle = m.get('InstanceBillingCycle')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidth') is not None:
            self.internet_max_bandwidth = m.get('InternetMaxBandwidth')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RenderingSpec') is not None:
            self.rendering_spec = m.get('RenderingSpec')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

