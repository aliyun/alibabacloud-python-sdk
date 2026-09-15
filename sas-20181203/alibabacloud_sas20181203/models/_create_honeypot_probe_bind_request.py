# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateHoneypotProbeBindRequest(DaraModel):
    def __init__(
        self,
        bind_port_list: List[main_models.CreateHoneypotProbeBindRequestBindPortList] = None,
        honeypot_id: str = None,
        lang: str = None,
        probe_id: str = None,
        service_ip_list: List[str] = None,
    ):
        # The list of port bindings.
        self.bind_port_list = bind_port_list
        # The honeypot ID.
        # > Call the [ListHoneypot](~~ListHoneypot~~) operation to obtain this value.
        # This parameter is required. If this parameter is not specified, the API returns InternalError (400).
        self.honeypot_id = honeypot_id
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The probe ID.
        # >Call the [ListHoneypotProbe](~~ListHoneypotProbe~~) operation to obtain this parameter.
        # This parameter is required. If this parameter is not specified, the API returns InvalidParam (400).
        self.probe_id = probe_id
        # The list of listener IP addresses.
        self.service_ip_list = service_ip_list

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
        result['BindPortList'] = []
        if self.bind_port_list is not None:
            for k1 in self.bind_port_list:
                result['BindPortList'].append(k1.to_map() if k1 else None)

        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        if self.service_ip_list is not None:
            result['ServiceIpList'] = self.service_ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_port_list = []
        if m.get('BindPortList') is not None:
            for k1 in m.get('BindPortList'):
                temp_model = main_models.CreateHoneypotProbeBindRequestBindPortList()
                self.bind_port_list.append(temp_model.from_map(k1))

        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        if m.get('ServiceIpList') is not None:
            self.service_ip_list = m.get('ServiceIpList')

        return self

class CreateHoneypotProbeBindRequestBindPortList(DaraModel):
    def __init__(
        self,
        bind_port: bool = None,
        end_port: int = None,
        fixed: bool = None,
        proto: str = None,
        start_port: int = None,
        target_port: int = None,
    ):
        # Specifies whether to bind the port. Valid values:
        # 
        # - **true**: The port is bound.
        # - **false**: The port is not bound.
        self.bind_port = bind_port
        # The end port of the probe listener.
        self.end_port = end_port
        # Specifies whether the port is fixed. Valid values:
        # 
        # - **true**: The port is fixed.
        # - **false**: The port is not fixed.
        self.fixed = fixed
        # The protocol type. Valid values:
        # 
        # - **tcp**: TCP protocol.
        # - **udp**: UDP protocol.
        self.proto = proto
        # The start port of the probe listener.
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

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        return self

