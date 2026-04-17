# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAdditionalVpcLinkRequest(DaraModel):
    def __init__(
        self,
        additional_vpc_id: str = None,
        additional_vswitch_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.additional_vpc_id = additional_vpc_id
        # This parameter is required.
        self.additional_vswitch_id = additional_vswitch_id
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_vpc_id is not None:
            result['AdditionalVpcId'] = self.additional_vpc_id

        if self.additional_vswitch_id is not None:
            result['AdditionalVswitchId'] = self.additional_vswitch_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalVpcId') is not None:
            self.additional_vpc_id = m.get('AdditionalVpcId')

        if m.get('AdditionalVswitchId') is not None:
            self.additional_vswitch_id = m.get('AdditionalVswitchId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

