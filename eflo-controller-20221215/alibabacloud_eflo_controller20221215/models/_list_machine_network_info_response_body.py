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
        # machine network infomation
        self.machine_network_info = machine_network_info
        # Id of the request
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
        # Network of cluster
        self.cluster_net = cluster_net
        # Specifies whether to enable the Jumbo Frames feature for the instance. Valid values:
        # 
        # *   true: The Jumbo Frame feature is enabled for the instance.
        # *   false: The Jumbo Frame feature is disabled for the instance.
        # 
        # Take note of the following items:
        # 
        # *   The instance must be in the Running (`Running`) or Stopped (`Stopped`) state.
        # *   The instance must reside in a VPC.
        # *   After the Jumbo Frames feature is enabled, the MTU value of the instance is set to 8500. After the Jumbo Frames feature is disabled, the MTU value of the instance is set to 1500. You can enable the Jumbo Frames feature only for specific instance types. For more information, see [Jumbo Frames](https://help.aliyun.com/document_detail/200512.html).
        self.enable_jumbo_frame = enable_jumbo_frame
        # HPN zone
        self.hpn_zone = hpn_zone
        # Specifies whether dpu machine.
        self.is_dpu_mode = is_dpu_mode
        # The type of machine.
        self.machine_type = machine_type
        # Network architecture
        self.net_arch = net_arch
        # The ID of the region in which the application is located.
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

