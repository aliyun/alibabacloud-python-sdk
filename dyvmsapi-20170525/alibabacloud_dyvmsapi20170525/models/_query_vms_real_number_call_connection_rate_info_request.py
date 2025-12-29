# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryVmsRealNumberCallConnectionRateInfoRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        real_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        time_period: str = None,
        virtual_number: str = None,
    ):
        self.owner_id = owner_id
        # 真实号码
        self.real_number = real_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 时间段
        self.time_period = time_period
        # 虚拟号码
        self.virtual_number = virtual_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.real_number is not None:
            result['RealNumber'] = self.real_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.time_period is not None:
            result['TimePeriod'] = self.time_period

        if self.virtual_number is not None:
            result['VirtualNumber'] = self.virtual_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RealNumber') is not None:
            self.real_number = m.get('RealNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TimePeriod') is not None:
            self.time_period = m.get('TimePeriod')

        if m.get('VirtualNumber') is not None:
            self.virtual_number = m.get('VirtualNumber')

        return self

