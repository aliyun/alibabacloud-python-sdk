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
        keep_alive_protection: str = None,
        record_name: str = None,
        request_id: str = None,
        rules: List[main_models.GetTransportLayerApplicationResponseBodyRules] = None,
        rules_count: int = None,
        site_id: int = None,
        static_ip: str = None,
        static_ip_v4list: List[main_models.GetTransportLayerApplicationResponseBodyStaticIpV4List] = None,
        status: str = None,
    ):
        self.application_id = application_id
        self.cname = cname
        self.cross_border_optimization = cross_border_optimization
        self.ip_access_rule = ip_access_rule
        self.ipv_6 = ipv_6
        self.keep_alive_protection = keep_alive_protection
        self.record_name = record_name
        self.request_id = request_id
        self.rules = rules
        self.rules_count = rules_count
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

        if self.keep_alive_protection is not None:
            result['KeepAliveProtection'] = self.keep_alive_protection

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

        if m.get('KeepAliveProtection') is not None:
            self.keep_alive_protection = m.get('KeepAliveProtection')

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
        self.client_ippass_through_mode = client_ippass_through_mode
        self.comment = comment
        self.edge_port = edge_port
        self.protocol = protocol
        self.rule_id = rule_id
        self.source = source
        self.source_port = source_port
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

