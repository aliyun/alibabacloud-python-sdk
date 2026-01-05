# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        resource_group_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The ID of the serverless resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The ID of the virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The VSwitch ID.
        # 
        # This parameter is required.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

