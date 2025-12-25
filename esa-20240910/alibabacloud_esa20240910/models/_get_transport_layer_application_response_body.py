# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetTransportLayerApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application_id: int = None,
        cname: str = None,
        cross_border_optimization: str = None,
        ip_access_rule: str = None,
        ipv_6: str = None,
        record_name: str = None,
        request_id: str = None,
        rules: List[main_models.GetTransportLayerApplicationResponseBodyRules] = None,
        rules_count: int = None,
        site_id: int = None,
        static_ip: str = None,
        static_ip_v4list: List[main_models.GetTransportLayerApplicationResponseBodyStaticIpV4List] = None,
        status: str = None,
    ):
        # Specific value of the origin, which needs to match the type of the origin.
        self.application_id = application_id
        # Whether to enable China mainland network access optimization, default is off. Value range:
        # - on: Enabled.
        # - off: Disabled.
        self.cname = cname
        self.cross_border_optimization = cross_border_optimization
        # #/components/schemas/WafRuleMatch2
        self.ip_access_rule = ip_access_rule
        # Ipv6 switch
        self.ipv_6 = ipv_6
        # Query Transport Layer Acceleration Application
        self.record_name = record_name
        # Id of the request
        self.request_id = request_id
        # Edge port. Supports:
        # 
        # - A single port, such as 80.
        # - Port range, such as 81-85, representing ports 81, 82, 83, 84, 85.
        # - Combination of ports and port ranges, separated by commas, for example 80,81-85,90, representing ports 80, 81, 82, 83, 84, 85, 90.
        self.rules = rules
        # Forwarding rule protocol, with values:
        # 
        # - TCP: TCP protocol.
        # - UDP: UDP protocol.
        self.rules_count = rules_count
        # Details of the forwarding rule.
        self.site_id = site_id
        self.static_ip = static_ip
        self.static_ip_v4list = static_ip_v4list
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

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.GetTransportLayerApplicationResponseBodyRules()
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
                temp_model = main_models.GetTransportLayerApplicationResponseBodyStaticIpV4List()
                self.static_ip_v4list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetTransportLayerApplicationResponseBodyStaticIpV4List(DaraModel):
    def __init__(
        self,
        address: str = None,
        status: str = None,
    ):
        self.address = address
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

class GetTransportLayerApplicationResponseBodyRules(DaraModel):
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
        # The domain name of the transport layer application.
        self.client_ippass_through_mode = client_ippass_through_mode
        # Switch for IP access rules. When turned on, the IP access rules in WAF take effect on the transport layer application.
        # 
        # - on: Turned on.
        # - off: Turned off.
        self.comment = comment
        # Comment information of the rule.
        self.edge_port = edge_port
        # Client IP pass-through protocol, supporting:
        # - **off**: No pass-through.
        # - **PPv1**: PROXY Protocol v1, supports client IP pass-through for TCP protocol.
        # - **PPv2**: PROXY Protocol v2, supports client IP pass-through for TCP and UDP protocols.
        # - **SPP**: Simple Proxy Protocol, supports client IP pass-through for UDP protocol.
        self.protocol = protocol
        # Status of the transport layer application
        # 
        # - **deploying**: Deploying. In this state, modification and deletion are not allowed.
        # - **active**: Active.
        self.rule_id = rule_id
        # Origin port. Supports:
        # 
        # - A single port, when the origin port is a single port, any valid edge port combination is supported.
        # - Port range, only when the edge port is a port range, the origin port can be set as a port range and the size of the range must be consistent with the edge port. For example, if the edge port is 90-93, the origin port cannot be set to 81-85 because the origin port range is 5 and the edge port range is 3, which are inconsistent.
        self.source = source
        # The CNAME domain corresponding to the transport layer acceleration application. This field is not empty only when the site is accessed via CNAME.
        self.source_port = source_port
        # Rule ID.
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

