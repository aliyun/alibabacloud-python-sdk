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
        rules: List[main_models.UpdateTransportLayerApplicationRequestRules] = None,
        site_id: int = None,
        static_ip: str = None,
    ):
        # Transport layer application ID, which can be obtained by calling the [ListTransportLayerApplications](~~ListTransportLayerApplications~~) interface.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Whether to enable China mainland network access optimization, default is disabled. Value range:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.cross_border_optimization = cross_border_optimization
        # IP access rule switch. When enabled, the IP access rules in WAF will take effect on the transport layer application.
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.ip_access_rule = ip_access_rule
        # IPv6 switch.
        self.ipv_6 = ipv_6
        # Forwarding rule list. Details of each rule. Except for the comment, all other parameters are required.
        self.rules = rules
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) interface.
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.cross_border_optimization is not None:
            result['CrossBorderOptimization'] = self.cross_border_optimization

        if self.ip_access_rule is not None:
            result['IpAccessRule'] = self.ip_access_rule

        if self.ipv_6 is not None:
            result['Ipv6'] = self.ipv_6

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
        # Client IP pass-through protocol, supports:
        # - **off**: No pass-through.
        # - **PPv1**: PROXY Protocol v1, supports client IP pass-through for TCP protocol.
        # - **PPv2**: PROXY Protocol v2, supports client IP pass-through for TCP and UDP protocols.
        # - **SPP**: Simple Proxy Protocol, supports client IP pass-through for UDP protocol.
        self.client_ippass_through_mode = client_ippass_through_mode
        # Comment information for the rule.
        self.comment = comment
        # Edge port. Supports:
        # 
        # - A single port, e.g., 80.
        # - Port range, e.g., 81-85, representing ports 81, 82, 83, 84, 85.
        # - Combination of ports and port ranges, separated by commas, e.g., 80,81-85,90, representing ports 80, 81, 82, 83, 84, 85, 90.
        # - Edge ports within a single rule and between multiple rules must not overlap.
        self.edge_port = edge_port
        # Forwarding rule protocol, supports:
        # 
        # - TCP: TCP protocol.
        # - UDP: UDP protocol.
        self.protocol = protocol
        # Specific value of the source.
        self.source = source
        # Source port. Supports:
        # 
        # - A single port, when the source port is a single port, any valid edge port combination is supported.
        # - Port range, only when the edge port is a port range, the source port can be set as a port range, and the size of the range must match that of the edge port. For example, if the edge port is 90-93, the source port cannot be set to 81-85 because the source port range is 5 and the edge port range is 3, which do not match.
        self.source_port = source_port
        # Source type, supports:
        # - **ip**: IP address.
        # - **domain**: Domain name.
        # - **OP**: Origin pool.
        # - **LB**: Load balancer.
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

