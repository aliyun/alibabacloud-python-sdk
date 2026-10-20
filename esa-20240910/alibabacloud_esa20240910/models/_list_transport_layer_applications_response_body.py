# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListTransportLayerApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListTransportLayerApplicationsResponseBodyApplications] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of Layer 4 applications.
        self.applications = applications
        # The current page number, which is the same as the PageNumber request parameter.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of Layer 4 applications.
        self.total_count = total_count

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListTransportLayerApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTransportLayerApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_id: int = None,
        cname: str = None,
        cross_border_optimization: str = None,
        ip_access_rule: str = None,
        ipv_6: str = None,
        keep_alive_protection: str = None,
        record_name: str = None,
        rules: List[main_models.ListTransportLayerApplicationsResponseBodyApplicationsRules] = None,
        rules_count: int = None,
        site_id: int = None,
        static_ip: str = None,
        static_ip_v4list: List[main_models.ListTransportLayerApplicationsResponseBodyApplicationsStaticIpV4List] = None,
        status: str = None,
    ):
        # The ID of the Layer 4 application.
        self.application_id = application_id
        # The CNAME domain name corresponding to the Layer 4 acceleration application. This field is not empty only when the site is onboarded by using a CNAME record.
        self.cname = cname
        # Specifies whether to enable network access optimization for the Chinese mainland. Default value: off. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.cross_border_optimization = cross_border_optimization
        # Specifies whether to enable the IP access rule. After this feature is enabled, the IP access rules in WAF take effect for the Layer 4 application. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.ip_access_rule = ip_access_rule
        # Specifies whether to enable IPv6. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.ipv_6 = ipv_6
        # Specifies whether to enable connection keep-alive protection. Default value: off. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.keep_alive_protection = keep_alive_protection
        # The domain name of the Layer 4 application.
        self.record_name = record_name
        # The list of forwarding rules.
        self.rules = rules
        # The number of forwarding rules included in the Layer 4 acceleration application.
        self.rules_count = rules_count
        # The site ID.
        self.site_id = site_id
        # Specifies whether to enable the static IP address feature. Default value: off. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.static_ip = static_ip
        # The list of static IPv4 addresses assigned to the Layer 4 application after the static IP address feature is enabled.
        # 
        # This parameter is required.
        self.static_ip_v4list = static_ip_v4list
        # The status of the Layer 4 application. Valid values:
        # 
        # - **deploying**: Deploying. In this state, modification and deletion are not allowed.
        # - **active**: Active.
        self.status = status

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.static_ip_v4list:
            for v1 in self.static_ip_v4list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.cname is not None:
            result['Cname'] = self.cname

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

        if self.rules_count is not None:
            result['RulesCount'] = self.rules_count

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.static_ip is not None:
            result['StaticIp'] = self.static_ip

        result['StaticIpV4List'] = []
        if self.static_ip_v4list is not None:
            for k1 in self.static_ip_v4list:
                result['StaticIpV4List'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

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
                temp_model = main_models.ListTransportLayerApplicationsResponseBodyApplicationsRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('RulesCount') is not None:
            self.rules_count = m.get('RulesCount')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StaticIp') is not None:
            self.static_ip = m.get('StaticIp')

        self.static_ip_v4list = []
        if m.get('StaticIpV4List') is not None:
            for k1 in m.get('StaticIpV4List'):
                temp_model = main_models.ListTransportLayerApplicationsResponseBodyApplicationsStaticIpV4List()
                self.static_ip_v4list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListTransportLayerApplicationsResponseBodyApplicationsStaticIpV4List(DaraModel):
    def __init__(
        self,
        address: str = None,
        status: str = None,
    ):
        # The IP address.
        self.address = address
        # The status of the IP address. Valid values:
        # 
        # - healthy: Healthy.
        # - unhealthy: Unhealthy.
        # - unknown: The IP address is being prepared.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListTransportLayerApplicationsResponseBodyApplicationsRules(DaraModel):
    def __init__(
        self,
        client_ippass_through_mode: str = None,
        comment: str = None,
        edge_port: str = None,
        protocol: str = None,
        rule_id: int = None,
        source: str = None,
        source_port: str = None,
        source_type: str = None,
    ):
        # The protocol used to pass through the client IP address. Valid values:
        # - **off**: Does not pass through the client IP address.
        # - **PPv1**: PROXY protocol version 1, which supports passing through the client IP address over TCP.
        # - **PPv2**: PROXY protocol version 2, which supports passing through the client IP address over TCP and UDP.
        # - **SPP**: Simple Proxy Protocol, which supports passing through the client IP address over UDP.
        self.client_ippass_through_mode = client_ippass_through_mode
        # The description of the rule.
        self.comment = comment
        # The edge port. Valid values:
        # 
        # - A single port, such as 80.
        # - A port range, such as 81-85, which represents ports 81, 82, 83, 84, and 85.
        # - A combination of ports and port ranges, separated by commas, such as 80,81-85,90, which represents ports 80, 81, 82, 83, 84, 85, and 90.
        self.edge_port = edge_port
        # The protocol of the forwarding rule. Valid values:
        # 
        # - TCP: TCP
        # - UDP: UDP
        self.protocol = protocol
        # The ID of the Layer 4 acceleration rule.
        self.rule_id = rule_id
        # The specific value of the origin server, which must match the origin server type.
        self.source = source
        # The origin server port. Valid values:
        # 
        # - A single port. If the origin server port is a single port, any valid combination of edge ports is supported.
        # - A port range. The origin server port can be set to a port range only when the edge port is a port range, and the range size must be the same as that of the edge port. For example, if the edge port is 90-93, you cannot set the origin server port to 81-85 because the origin server port range includes 5 ports and the edge port range includes 4 ports, which do not match.
        self.source_port = source_port
        # The origin server type. Valid values:
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

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

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

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

