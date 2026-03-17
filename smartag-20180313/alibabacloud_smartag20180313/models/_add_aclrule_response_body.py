# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class AddACLRuleResponseBody(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acr_id: str = None,
        description: str = None,
        dest_cidr: str = None,
        dest_port_range: str = None,
        direction: str = None,
        dpi_group_ids: main_models.AddACLRuleResponseBodyDpiGroupIds = None,
        dpi_signature_ids: main_models.AddACLRuleResponseBodyDpiSignatureIds = None,
        gmt_create: int = None,
        ip_protocol: str = None,
        name: str = None,
        policy: str = None,
        priority: int = None,
        request_id: str = None,
        source_cidr: str = None,
        source_port_range: str = None,
        type: str = None,
    ):
        # The ID of the ACL.
        self.acl_id = acl_id
        # The ID of the ACL rule.
        self.acr_id = acr_id
        # The description of the ACL rule.
        self.description = description
        # The destination CIDR block.
        # 
        # The value of this parameter is specified in CIDR notation. Example: 192.168.10.0/24.
        self.dest_cidr = dest_cidr
        # The destination port range.
        self.dest_port_range = dest_port_range
        # The direction of traffic in which the ACL rule is applied. Valid values:
        # 
        # *   **in**: The ACL rule controls inbound network traffic of the on-premises network that is associated with the SAG instance.
        # *   **out**: The ACL rule controls outbound network traffic of the on-premises network that is associated with the SAG instance.
        self.direction = direction
        self.dpi_group_ids = dpi_group_ids
        self.dpi_signature_ids = dpi_signature_ids
        # The timestamp when the ACL rule was created.
        # 
        # The timestamp is of the Long data type. If multiple ACL rules have the same priority, the rule with the earliest timestamp takes effect.
        self.gmt_create = gmt_create
        # The protocol used by the ACL rule.
        self.ip_protocol = ip_protocol
        # The name of the ACL rule.
        self.name = name
        # The action policy of the ACL rule.
        # 
        # *   **accept**: allows the network traffic.
        # *   **drop**: blocks the network traffic.
        self.policy = policy
        # The priority of the ACL rule.
        # 
        # A smaller value indicates a higher priority. If rules have the same priority, whichever applied to the SAG devices earlier takes effect.
        self.priority = priority
        # The ID of the request.
        self.request_id = request_id
        # The source CIDR block.
        # 
        # The value of this parameter is specified in CIDR notation. Example: 192.168.1.0/24.
        self.source_cidr = source_cidr
        # The source port range.
        self.source_port_range = source_port_range
        # The type of the ACL rule:
        # 
        # *   **LAN**: The ACL rule controls network traffic transmitted through private IP addresses.
        # *   **WAN**: The ACL rule controls network traffic transmitted through public IP addresses.
        self.type = type

    def validate(self):
        if self.dpi_group_ids:
            self.dpi_group_ids.validate()
        if self.dpi_signature_ids:
            self.dpi_signature_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acr_id is not None:
            result['AcrId'] = self.acr_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr is not None:
            result['DestCidr'] = self.dest_cidr

        if self.dest_port_range is not None:
            result['DestPortRange'] = self.dest_port_range

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dpi_group_ids is not None:
            result['DpiGroupIds'] = self.dpi_group_ids.to_map()

        if self.dpi_signature_ids is not None:
            result['DpiSignatureIds'] = self.dpi_signature_ids.to_map()

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AcrId') is not None:
            self.acr_id = m.get('AcrId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidr') is not None:
            self.dest_cidr = m.get('DestCidr')

        if m.get('DestPortRange') is not None:
            self.dest_port_range = m.get('DestPortRange')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DpiGroupIds') is not None:
            temp_model = main_models.AddACLRuleResponseBodyDpiGroupIds()
            self.dpi_group_ids = temp_model.from_map(m.get('DpiGroupIds'))

        if m.get('DpiSignatureIds') is not None:
            temp_model = main_models.AddACLRuleResponseBodyDpiSignatureIds()
            self.dpi_signature_ids = temp_model.from_map(m.get('DpiSignatureIds'))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AddACLRuleResponseBodyDpiSignatureIds(DaraModel):
    def __init__(
        self,
        dpi_signature_id: List[str] = None,
    ):
        self.dpi_signature_id = dpi_signature_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_signature_id is not None:
            result['DpiSignatureId'] = self.dpi_signature_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiSignatureId') is not None:
            self.dpi_signature_id = m.get('DpiSignatureId')

        return self



class AddACLRuleResponseBodyDpiGroupIds(DaraModel):
    def __init__(
        self,
        dpi_group_id: List[str] = None,
    ):
        self.dpi_group_id = dpi_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_group_id is not None:
            result['DpiGroupId'] = self.dpi_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiGroupId') is not None:
            self.dpi_group_id = m.get('DpiGroupId')

        return self

