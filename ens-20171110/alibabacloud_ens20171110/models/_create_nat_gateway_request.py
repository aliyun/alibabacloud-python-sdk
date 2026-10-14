# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateNatGatewayRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_billing_cycle: str = None,
        instance_type: str = None,
        name: str = None,
        network_id: str = None,
        tag: List[main_models.CreateNatGatewayRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The ID of the ENS edge zone.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The billing cycle of the instance. Valid values: Hour and Month.
        self.instance_billing_cycle = instance_billing_cycle
        # The NAT gateway specification. Valid value: **enat.default**.
        self.instance_type = instance_type
        # The name of the NAT gateway. The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        # The network ID.
        # 
        # This parameter is required.
        self.network_id = network_id
        # The resource tags.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_billing_cycle is not None:
            result['InstanceBillingCycle'] = self.instance_billing_cycle

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.name is not None:
            result['Name'] = self.name

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceBillingCycle') is not None:
            self.instance_billing_cycle = m.get('InstanceBillingCycle')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateNatGatewayRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class CreateNatGatewayRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. Valid values of N: **1** to **20**.
        # 
        # - Cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # - Can be up to 64 characters in length.
        # - Cannot be an empty string.
        self.key = key
        # The tag value of the resource. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length, cannot start with acs:, and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

