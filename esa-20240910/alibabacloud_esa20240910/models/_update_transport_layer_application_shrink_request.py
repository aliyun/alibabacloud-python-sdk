# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTransportLayerApplicationShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: int = None,
        cross_border_optimization: str = None,
        ip_access_rule: str = None,
        ipv_6: str = None,
        rules_shrink: str = None,
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
        self.rules_shrink = rules_shrink
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) interface.
        # 
        # This parameter is required.
        self.site_id = site_id
        self.static_ip = static_ip

    def validate(self):
        pass

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

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

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

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StaticIp') is not None:
            self.static_ip = m.get('StaticIp')

        return self

