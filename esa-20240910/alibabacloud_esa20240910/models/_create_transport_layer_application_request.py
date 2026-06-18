# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateTransportLayerApplicationRequest(DaraModel):
    def __init__(
        self,
        cross_border_optimization: str = None,
        ip_access_rule: str = None,
        ipv_6: str = None,
        keep_alive_protection: str = None,
        record_name: str = None,
        rules: List[main_models.CreateTransportLayerApplicationRequestRules] = None,
        site_id: int = None,
        static_ip: str = None,
    ):
        # Enables or disables network optimization for access from the Chinese mainland. This feature is disabled by default. Valid values:
        # 
        # - `on`: Enables the optimization.
        # 
        # - `off`: Disables the optimization.
        self.cross_border_optimization = cross_border_optimization
        # Applies IP access rules from Web Application Firewall (WAF) to this Transport Layer Application. Valid values:
        # 
        # - `on`: Enables the feature.
        # 
        # - `off`: Disables the feature.
        self.ip_access_rule = ip_access_rule
        # Enables or disables IPv6 support.
        self.ipv_6 = ipv_6
        # Enables or disables keep-alive protection.
        self.keep_alive_protection = keep_alive_protection
        # The domain name of the Transport Layer Application.
        # 
        # This parameter is required.
        self.record_name = record_name
        # The list of forwarding rules.
        # 
        # This parameter is required.
        self.rules = rules
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        self.static_ip = static_ip

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_border_optimization is not None:
            result['CrossBorderOptimization'] = self.cross_border_optimization

        if self.ip_access_rule is not None:
            result['IpAccessRule'] = self.ip_access_rule

        if self.ipv_6 is not None:
            result['Ipv6'] = self.ipv_6

        if self.keep_alive_protection is not None:
            result['KeepAliveProtection'] = self.keep_alive_protection

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.static_ip is not None:
            result['StaticIp'] = self.static_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossBorderOptimization') is not None:
            self.cross_border_optimization = m.get('CrossBorderOptimization')

        if m.get('IpAccessRule') is not None:
            self.ip_access_rule = m.get('IpAccessRule')

        if m.get('Ipv6') is not None:
            self.ipv_6 = m.get('Ipv6')

        if m.get('KeepAliveProtection') is not None:
            self.keep_alive_protection = m.get('KeepAliveProtection')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreateTransportLayerApplicationRequestRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StaticIp') is not None:
            self.static_ip = m.get('StaticIp')

        return self

class CreateTransportLayerApplicationRequestRules(DaraModel):
    def __init__(
        self,
        client_ippass_through_mode: str = None,
        comment: str = None,
        edge_port: str = None,
        protocol: str = None,
        source: str = None,
        source_port: str = None,
        source_type: str = None,
    ):
        # The client IP passthrough protocol. Valid values:
        # 
        # - **off**: Disables client IP passthrough.
        # 
        # - **PPv1**: PROXY Protocol v1. Preserves the client IP address for TCP connections.
        # 
        # - **PPv2**: PROXY Protocol v2. Preserves the client IP address for TCP and UDP connections.
        # 
        # - **SPP**: Simple Proxy Protocol. Preserves the client IP address for UDP connections.
        # 
        # This parameter is required.
        self.client_ippass_through_mode = client_ippass_through_mode
        # An optional comment for the rule.
        self.comment = comment
        # The edge port. Supported formats:
        # 
        # - A single port, for example, `80`.
        # 
        # - A port range, for example, `81-85`, which includes ports 81, 82, 83, 84, and 85.
        # 
        # - A combination of ports and port ranges separated by commas, for example, `80,81-85,90`, which includes ports 80, 81, 82, 83, 84, 85, and 90.
        # 
        # Edge ports cannot overlap within a single rule or across multiple rules.
        # 
        # This parameter is required.
        self.edge_port = edge_port
        # The forwarding protocol. Valid values:
        # 
        # - `TCP`: The TCP protocol.
        # 
        # - `UDP`: The UDP protocol.
        # 
        # This parameter is required.
        self.protocol = protocol
        # The origin address. The value must match the specified `SourceType`.
        # 
        # This parameter is required.
        self.source = source
        # The origin port. Supported formats:
        # 
        # - A single port, which supports any valid combination of edge ports.
        # 
        # - A port range. You can specify a port range only if the edge port is also a port range. The origin and edge port ranges must be the same size. For example, if the edge port range is `90-93` (4 ports), the origin port range cannot be `81-85` (5 ports).
        # 
        # This parameter is required.
        self.source_port = source_port
        # The origin type. Valid values:
        # 
        # - **ip**: An IP address.
        # 
        # - **domain**: A domain name.
        # 
        # - **OP**: An origin pool.
        # 
        # - **LB**: A load balancer.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ippass_through_mode is not None:
            result['ClientIPPassThroughMode'] = self.client_ippass_through_mode

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.edge_port is not None:
            result['EdgePort'] = self.edge_port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.source is not None:
            result['Source'] = self.source

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIPPassThroughMode') is not None:
            self.client_ippass_through_mode = m.get('ClientIPPassThroughMode')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('EdgePort') is not None:
            self.edge_port = m.get('EdgePort')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

