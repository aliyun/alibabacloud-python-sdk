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
        # The transport layer application ID. You can obtain this ID by calling the [ListTransportLayerApplications](~~ListTransportLayerApplications~~) operation.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to enable cross-border optimization for network access from the Chinese mainland. This feature is disabled by default. Valid values:
        # 
        # - on: Enables the feature.
        # 
        # - off: Disables the feature.
        self.cross_border_optimization = cross_border_optimization
        # Specifies whether to enable IP access rules. If enabled, the IP access rules in WAF apply to the transport layer application. Valid values:
        # 
        # - on: Enables the feature.
        # 
        # - off: Disables the feature.
        self.ip_access_rule = ip_access_rule
        # Specifies whether to enable IPv6. Valid values: `on` and `off`.
        self.ipv_6 = ipv_6
        self.keep_alive_protection = keep_alive_protection
        # A list of forwarding rules. For each rule, all parameters are required except for `Comment`.
        self.rules = rules
        # The site ID. You can obtain this ID by calling the [ListSites](~~ListSites~~) operation.
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
        # Specifies the protocol for client IP pass-through. Valid values:
        # 
        # - **off**: Disables client IP pass-through.
        # 
        # - **PPv1**: PROXY Protocol v1. Supports client IP pass-through for the TCP protocol.
        # 
        # - **PPv2**: PROXY Protocol v2. Supports client IP pass-through for both TCP and UDP protocols.
        # 
        # - **SPP**: Simple Proxy Protocol. Supports client IP pass-through for the UDP protocol.
        self.client_ippass_through_mode = client_ippass_through_mode
        # An optional comment for the forwarding rule.
        self.comment = comment
        # The edge port. The following formats are supported:
        # 
        # - A single port, for example, `80`.
        # 
        # - A port range, for example, `81-85`. This range includes ports 81, 82, 83, 84, and 85.
        # 
        # - A combination of ports and port ranges separated by commas, for example, `80,81-85,90`. This includes ports 80, 81, 82, 83, 84, 85, and 90.
        # 
        # - Edge ports cannot overlap within a single rule or across multiple rules.
        self.edge_port = edge_port
        # The forwarding protocol. Valid values:
        # 
        # - TCP: Transmission Control Protocol.
        # 
        # - UDP: User Datagram Protocol.
        self.protocol = protocol
        # The source, which must correspond to the specified `SourceType`. For example, if `SourceType` is `ip`, this parameter must be an IP address.
        self.source = source
        # The source port. The following formats are supported:
        # 
        # - A single port. When a single source port is used, any valid format can be used for the edge port.
        # 
        # - A port range. You can specify a port range for the source port only if the edge port is also a port range, and their sizes must match. For example, if `EdgePort` is `90-93`, you cannot set `SourcePort` to `81-85` because their sizes (4 and 5 ports, respectively) do not match.
        self.source_port = source_port
        # The type of the source. Valid values:
        # 
        # - **ip**: An IP address.
        # 
        # - **domain**: A domain name.
        # 
        # - **OP**: An origin pool.
        # 
        # - **LB**: A load balancer.
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

