# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSAGDeviceInfoResponseBody(DaraModel):
    def __init__(
        self,
        controller_state: str = None,
        last_connected_controller_time: str = None,
        request_id: str = None,
        resettable_status: str = None,
        service_ip: str = None,
        smart_agtype: str = None,
        startup_time: str = None,
        syn_status: str = None,
        version: str = None,
        vpn_state: str = None,
    ):
        # The control status of the SAG device. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Abnormal**: abnormal
        self.controller_state = controller_state
        # The last time when the SAG device was connected to Alibaba Cloud.
        self.last_connected_controller_time = last_connected_controller_time
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the reset button of the SAG device is enabled. Valid values:
        # 
        # *   **Enabled**: enabled
        # *   **Disabled**: disabled
        self.resettable_status = resettable_status
        # The IP address of the SAG device.
        self.service_ip = service_ip
        # The model of the SAG device. Valid values:
        # 
        # *   **sag-100wm**
        # *   **sag-1000**
        self.smart_agtype = smart_agtype
        # The time when the SAG device was started.
        self.startup_time = startup_time
        # Indicates whether the settings of the SAG device are synchronized to Alibaba Cloud. Valid values:
        # 
        # *   **Synchronized**: synchronized
        # *   **Unsynchronized**: unsynchronized
        # *   **Synchronizing**: being synchronized
        self.syn_status = syn_status
        # The version of the SAG device.
        self.version = version
        # The VPN connection status of the SAG device. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Abnormal**: abnormal
        self.vpn_state = vpn_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.controller_state is not None:
            result['ControllerState'] = self.controller_state

        if self.last_connected_controller_time is not None:
            result['LastConnectedControllerTime'] = self.last_connected_controller_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resettable_status is not None:
            result['ResettableStatus'] = self.resettable_status

        if self.service_ip is not None:
            result['ServiceIP'] = self.service_ip

        if self.smart_agtype is not None:
            result['SmartAGType'] = self.smart_agtype

        if self.startup_time is not None:
            result['StartupTime'] = self.startup_time

        if self.syn_status is not None:
            result['SynStatus'] = self.syn_status

        if self.version is not None:
            result['Version'] = self.version

        if self.vpn_state is not None:
            result['VpnState'] = self.vpn_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControllerState') is not None:
            self.controller_state = m.get('ControllerState')

        if m.get('LastConnectedControllerTime') is not None:
            self.last_connected_controller_time = m.get('LastConnectedControllerTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResettableStatus') is not None:
            self.resettable_status = m.get('ResettableStatus')

        if m.get('ServiceIP') is not None:
            self.service_ip = m.get('ServiceIP')

        if m.get('SmartAGType') is not None:
            self.smart_agtype = m.get('SmartAGType')

        if m.get('StartupTime') is not None:
            self.startup_time = m.get('StartupTime')

        if m.get('SynStatus') is not None:
            self.syn_status = m.get('SynStatus')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpnState') is not None:
            self.vpn_state = m.get('VpnState')

        return self

