# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeFirewallTemplateRulesApplyResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[main_models.DescribeFirewallTemplateRulesApplyResultResponseBodyData] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.data = data

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeFirewallTemplateRulesApplyResultResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        return self

class DescribeFirewallTemplateRulesApplyResultResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        port: str = None,
        remark: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
        success: bool = None,
    ):
        # The error codes when the firewall template rule fails to be applied.
        self.error_code = error_code
        # The error message that is displayed when the firewall template rule fails to be applied.
        self.error_info = error_info
        # The port range. Valid values: 1 to 65535. Specify a port range in the format of \\<start port number>/\\<end port number>. Example: `1024/1055`, which indicates that the port range of 1024 to 1055.
        # 
        # > If you set RuleProtocol to ICMP, you must set Port to -1/-1.
        self.port = port
        # The remarks of the firewall rule.
        self.remark = remark
        # The transport layer protocol that the rule supports. Valid values:
        # 
        # - TCP
        # 
        # - UDP
        # 
        # - TCP+UDP
        # 
        # - ICMP
        self.rule_protocol = rule_protocol
        # The source address to which you want to grant access permissions. CIDR blocks and IPv4 addresses are supported.
        self.source_cidr_ip = source_cidr_ip
        # The status of applying the firewall template rule to the simple application servers.
        # 
        # - Pending: The template rule does not start to be applied to the simple application servers.
        # 
        # - Applying: The template rule is being applied to the simple application servers.
        # 
        # - Success: The template rule is successfully applied to the simple application servers.
        # 
        # - PartFailed: The template rule fails to be applied to some simple application servers.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.port is not None:
            result['Port'] = self.port

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_protocol is not None:
            result['RuleProtocol'] = self.rule_protocol

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

