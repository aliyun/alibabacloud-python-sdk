# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListMachineNetworkInfoResponseBody(DaraModel):
    def __init__(
        self,
        machine_network_info: List[main_models.ListMachineNetworkInfoResponseBodyMachineNetworkInfo] = None,
        request_id: str = None,
    ):
        # The network information of the machine types.
        self.machine_network_info = machine_network_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.machine_network_info:
            for v1 in self.machine_network_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MachineNetworkInfo'] = []
        if self.machine_network_info is not None:
            for k1 in self.machine_network_info:
                result['MachineNetworkInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_network_info = []
        if m.get('MachineNetworkInfo') is not None:
            for k1 in m.get('MachineNetworkInfo'):
                temp_model = main_models.ListMachineNetworkInfoResponseBodyMachineNetworkInfo()
                self.machine_network_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMachineNetworkInfoResponseBodyMachineNetworkInfo(DaraModel):
    def __init__(
        self,
        cluster_net: str = None,
        enable_jumbo_frame: bool = None,
        hpn_zone: str = None,
        is_dpu_mode: bool = None,
        machine_type: str = None,
        net_arch: str = None,
        region_id: str = None,
    ):
        # The cluster network.
        self.cluster_net = cluster_net
        # Indicates whether jumbo frames are enabled.
        self.enable_jumbo_frame = enable_jumbo_frame
        # The cluster ID.
        self.hpn_zone = hpn_zone
        # Indicates whether the machine is in DPU mode.
        self.is_dpu_mode = is_dpu_mode
        # The machine type.
        self.machine_type = machine_type
        # The network architecture.
        self.net_arch = net_arch
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_net is not None:
            result['ClusterNet'] = self.cluster_net

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.is_dpu_mode is not None:
            result['IsDpuMode'] = self.is_dpu_mode

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.net_arch is not None:
            result['NetArch'] = self.net_arch

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNet') is not None:
            self.cluster_net = m.get('ClusterNet')

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('IsDpuMode') is not None:
            self.is_dpu_mode = m.get('IsDpuMode')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('NetArch') is not None:
            self.net_arch = m.get('NetArch')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

