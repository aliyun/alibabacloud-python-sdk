# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListMachineNetworkInfoRequest(DaraModel):
    def __init__(
        self,
        machine_hpn_info: List[main_models.ListMachineNetworkInfoRequestMachineHpnInfo] = None,
    ):
        # hpn information of machine
        self.machine_hpn_info = machine_hpn_info

    def validate(self):
        if self.machine_hpn_info:
            for v1 in self.machine_hpn_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MachineHpnInfo'] = []
        if self.machine_hpn_info is not None:
            for k1 in self.machine_hpn_info:
                result['MachineHpnInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_hpn_info = []
        if m.get('MachineHpnInfo') is not None:
            for k1 in m.get('MachineHpnInfo'):
                temp_model = main_models.ListMachineNetworkInfoRequestMachineHpnInfo()
                self.machine_hpn_info.append(temp_model.from_map(k1))

        return self

class ListMachineNetworkInfoRequestMachineHpnInfo(DaraModel):
    def __init__(
        self,
        hpn_zone: str = None,
        machine_type: str = None,
        region_id: str = None,
    ):
        # hpn zone infomation
        self.hpn_zone = hpn_zone
        # The type of machine.
        self.machine_type = machine_type
        # The ID of the region in which the application is located.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

