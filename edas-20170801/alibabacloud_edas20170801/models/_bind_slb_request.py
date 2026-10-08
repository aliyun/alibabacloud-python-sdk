# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindSlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        listener_port: int = None,
        slb_id: str = None,
        slb_ip: str = None,
        type: str = None,
        vserver_group_id: str = None,
    ):
        # The ID of the Enterprise Distributed Application Service (EDAS) application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The listener port.
        self.listener_port = listener_port
        # The ID of the SLB instance.
        # 
        # This parameter is required.
        self.slb_id = slb_id
        # The IP address of the SLB instance.
        # 
        # This parameter is required.
        self.slb_ip = slb_ip
        # The network type of the SLB instance. Valid values:
        # 
        # - internet: an Internet-facing instance.
        # 
        # - intranet: an internal-facing instance.
        # 
        # This parameter is required.
        self.type = type
        # The ID of the vServer group for the internal-facing SLB instance.
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.type is not None:
            result['Type'] = self.type

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

