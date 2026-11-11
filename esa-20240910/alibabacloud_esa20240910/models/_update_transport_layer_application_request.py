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
        # The Layer 4 application ID. You can obtain the ID by calling the [ListTransportLayerApplications](~~ListTransportLayerApplications~~) API operation.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to enable network access optimization for the Chinese mainland. Default value: off. Valid values:
        # 
        # - on: Enable.
        # - off: Disable.
        self.cross_border_optimization = cross_border_optimization
        # Specifies whether to enable the IP access rule. After this feature is enabled, the IP access rules in WAF take effect for the Layer 4 application. Valid values:
        # 
        # - on: Enable.
        # - off: Disable.
        self.ip_access_rule = ip_access_rule
        # Specifies whether to enable IPv6. Valid values:
        # 
        # - on: Enable.
        # - off: Disable.
        self.ipv_6 = ipv_6
        # Specifies whether to enable connection keep-alive protection. Default value: off. Valid values:
        # 
        # - on: Enable.
        # - off: Disable.
        self.keep_alive_protection = keep_alive_protection
        # The list of forwarding rules. For rule details, all parameters except the comment are required for each rule.
        self.rules = rules
        # The site ID. You can obtain the ID by calling the [ListSites](~~ListSites~~) API operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Specifies whether to enable the static IP address feature. Default value: off. Valid values:
        # 
        # - on: Enable.
        # - off: Disable.
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
        # The client IP address pass-through protocol. Valid values:
        # - **off**: Do not pass through.
        # - **PPv1**: PROXY protocol v1, which supports client IP address pass-through for the TCP protocol.
        # - **PPv2**: PROXY protocol v2, which supports client IP address pass-through for the TCP and UDP protocols.
        # - **SPP**: Simple Proxy Protocol, which supports client IP address pass-through for the UDP protocol.
        self.client_ippass_through_mode = client_ippass_through_mode
        # The comment for the rule.
        self.comment = comment
        # The edge port. Valid values:
        # 
        # - A single port, such as 80.
        # - A port range, such as 81-85, which represents ports 81, 82, 83, 84, and 85.
        # - A combination of ports and port ranges, separated by commas, such as 80,81-85,90, which represents ports 80, 81, 82, 83, 84, 85, and 90.
        # - The edge ports within a single rule and the edge ports across multiple rules must not overlap.
        self.edge_port = edge_port
        # The protocol of the forwarding rule. Valid values:
        # 
        # - TCP: TCP.
        # - UDP: UDP.
        self.protocol = protocol
        # The specific value of the origin server.
        self.source = source
        # The origin server port. Valid values:
        # 
        # - A single port. If the origin server port is a single port, any valid combination of edge ports is supported.
        # - A port range. The origin server port can be set to a port range only when the edge port is a port range, and the range size must be the same as that of the edge port. For example, if the edge port is 90-93, you cannot set the origin server port to 81-85 because the origin server port range is 5 and the edge port range is 3, which are inconsistent.
        self.source_port = source_port
        # The origin server type. Valid values:
        # - **ip**: IP address.
        # - **domain**: Domain name.
        # - **OP**: Origin IPAM pool.
        # - **LB**: Load balancing.
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

