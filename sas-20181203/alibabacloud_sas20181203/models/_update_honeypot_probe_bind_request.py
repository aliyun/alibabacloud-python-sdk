# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class UpdateHoneypotProbeBindRequest(DaraModel):
    def __init__(
        self,
        bind_id: str = None,
        bind_port_list: List[main_models.UpdateHoneypotProbeBindRequestBindPortList] = None,
        bind_type: str = None,
        current_page: int = None,
        honeypot_id: str = None,
        id: int = None,
        lang: str = None,
        page_size: int = None,
        ports: str = None,
        probe_id: str = None,
        service_ip_list: List[str] = None,
        set_status: int = None,
    ):
        # The unique ID of the honeypot to which the probe is bound.
        self.bind_id = bind_id
        # The ports that are bound to the probe.
        self.bind_port_list = bind_port_list
        # The operation that the probe performs. Valid values:
        # 
        # *   **forward_honey**: forward traffic to a honeypot
        # *   **scan_port**: monitor and scan
        self.bind_type = bind_type
        # The page number. Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # The honeypot ID.
        # 
        # >  You can call the [ListHoneypot](~~ListHoneypot~~) operation to obtain the IDs of honeypots.
        self.honeypot_id = honeypot_id
        # The port ID of the probe service.
        self.id = id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned per page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The ports that are monitored.
        self.ports = ports
        # The probe ID.
        # 
        # >  You can call the [ListHoneypotProbe](~~ListHoneypotProbe~~) operation to query the IDs of probes.
        self.probe_id = probe_id
        # The IP addresses that are monitored.
        self.service_ip_list = service_ip_list
        # The status of the port.
        self.set_status = set_status

    def validate(self):
        if self.bind_port_list:
            for v1 in self.bind_port_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_id is not None:
            result['BindId'] = self.bind_id

        result['BindPortList'] = []
        if self.bind_port_list is not None:
            for k1 in self.bind_port_list:
                result['BindPortList'].append(k1.to_map() if k1 else None)

        if self.bind_type is not None:
            result['BindType'] = self.bind_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.ports is not None:
            result['Ports'] = self.ports

        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        if self.service_ip_list is not None:
            result['ServiceIpList'] = self.service_ip_list

        if self.set_status is not None:
            result['SetStatus'] = self.set_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')

        self.bind_port_list = []
        if m.get('BindPortList') is not None:
            for k1 in m.get('BindPortList'):
                temp_model = main_models.UpdateHoneypotProbeBindRequestBindPortList()
                self.bind_port_list.append(temp_model.from_map(k1))

        if m.get('BindType') is not None:
            self.bind_type = m.get('BindType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Ports') is not None:
            self.ports = m.get('Ports')

        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        if m.get('ServiceIpList') is not None:
            self.service_ip_list = m.get('ServiceIpList')

        if m.get('SetStatus') is not None:
            self.set_status = m.get('SetStatus')

        return self

class UpdateHoneypotProbeBindRequestBindPortList(DaraModel):
    def __init__(
        self,
        bind_port: bool = None,
        end_port: int = None,
        fixed: bool = None,
        id: int = None,
        proto: str = None,
        start_port: int = None,
        target_port: int = None,
    ):
        # Specifies whether to bind a port. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.bind_port = bind_port
        # The end port on which the probe monitors.
        self.end_port = end_port
        # Specifies whether the port is fixed. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.fixed = fixed
        # The UUID of the port.
        self.id = id
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.proto = proto
        # The start port on which the probe monitors.
        self.start_port = start_port
        # The destination port.
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_port is not None:
            result['BindPort'] = self.bind_port

        if self.end_port is not None:
            result['EndPort'] = self.end_port

        if self.fixed is not None:
            result['Fixed'] = self.fixed

        if self.id is not None:
            result['Id'] = self.id

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.start_port is not None:
            result['StartPort'] = self.start_port

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindPort') is not None:
            self.bind_port = m.get('BindPort')

        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')

        if m.get('Fixed') is not None:
            self.fixed = m.get('Fixed')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        return self

