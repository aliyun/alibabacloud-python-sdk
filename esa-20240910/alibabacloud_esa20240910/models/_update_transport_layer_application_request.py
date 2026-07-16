# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class UpdateTransportLayerApplicationRequest(DaraModel):
    def __init__(
        self,
        application_id: int = None,
        cross_border_optimization: str = None,
        ip_access_rule: str = None,
        ipv_6: str = None,
        keep_alive_protection: str = None,
        rules: List[main_models.UpdateTransportLayerApplicationRequestRules] = None,
        site_id: int = None,
        static_ip: str = None,
    ):
        # The Layer 4 application ID. You can call the [ListTransportLayerApplications](~~ListTransportLayerApplications~~) operation to obtain the application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to enable network access optimization for the Chinese mainland. This feature is disabled by default. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.cross_border_optimization = cross_border_optimization
        # The IP access rule switch. When enabled, WAF IP access rules take effect for the Layer 4 application. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.ip_access_rule = ip_access_rule
        # The IPv6 switch. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.ipv_6 = ipv_6
        # Specifies whether to enable keep-alive protection. This feature is disabled by default. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.keep_alive_protection = keep_alive_protection
        # The list of forwarding rules. For each rule, all parameters except the comment are required.
        self.rules = rules
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Specifies whether to enable static IP. This feature is disabled by default. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.cross_border_optimization is not None:
            result['CrossBorderOptimization'] = self.cross_border_optimization

        if self.ip_access_rule is not None:
            result['IpAccessRule'] = self.ip_access_rule

        if self.ipv_6 is not None:
            result['Ipv6'] = self.ipv_6

        if self.keep_alive_protection is not None:
            result['KeepAliveProtection'] = self.keep_alive_protection

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
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CrossBorderOptimization') is not None:
            self.cross_border_optimization = m.get('CrossBorderOptimization')

        if m.get('IpAccessRule') is not None:
            self.ip_access_rule = m.get('IpAccessRule')

        if m.get('Ipv6') is not None:
            self.ipv_6 = m.get('Ipv6')

        if m.get('KeepAliveProtection') is not None:
            self.keep_alive_protection = m.get('KeepAliveProtection')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateTransportLayerApplicationRequestRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StaticIp') is not None:
            self.static_ip = m.get('StaticIp')

        return self

class UpdateTransportLayerApplicationRequestRules(DaraModel):
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
        # The client IP pass-through protocol. Valid values:
        # - **off**: disabled.
        # - **PPv1**: PROXY Protocol v1, which supports client IP pass-through for TCP.
        # - **PPv2**: PROXY Protocol v2, which supports client IP pass-through for TCP and UDP.
        # - **SPP**: Simple Proxy Protocol, which supports client IP pass-through for UDP.
        self.client_ippass_through_mode = client_ippass_through_mode
        # The comment for the rule.
        self.comment = comment
        # The edge port. Valid values:
        # 
        # - A single port, such as 80.
        # - A port range, such as 81-85, which represents ports 81, 82, 83, 84, and 85.
        # - A combination of ports and port ranges separated by commas, such as 80,81-85,90, which represents ports 80, 81, 82, 83, 84, 85, and 90.
        # - Edge ports within a single rule and across multiple rules cannot overlap.
        self.edge_port = edge_port
        # The forwarding rule protocol. Valid values:
        # 
        # - TCP: TCP protocol.
        # - UDP: UDP protocol.
        self.protocol = protocol
        # The specific value of the origin.
        self.source = source
        # Origin Server Port. Valid values:
        # 
        # - A single port. When Origin Server Port is a single port, any valid edge port combination is supported.
        # - A port range. Origin Server Port can be set to a port range only when the edge port is a port range, and the range size must match the edge port range. For example, if the edge port is 90-93, you cannot set Origin Server Port to 81-85 because Origin Server Port range is 5 while the edge port range is 4, which are inconsistent.
        self.source_port = source_port
        # The origin type. Valid values:
        # - **ip**: IP address.
        # - **domain**: domain name.
        # - **OP**: origin IPAM pool.
        # - **LB**: load balancing.
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

