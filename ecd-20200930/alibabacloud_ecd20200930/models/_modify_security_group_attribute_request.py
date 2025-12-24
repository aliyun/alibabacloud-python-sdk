# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifySecurityGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        authorize_egress: List[main_models.ModifySecurityGroupAttributeRequestAuthorizeEgress] = None,
        authorize_ingress: List[main_models.ModifySecurityGroupAttributeRequestAuthorizeIngress] = None,
        office_site_id: str = None,
        region_id: str = None,
        revoke_egress: List[main_models.ModifySecurityGroupAttributeRequestRevokeEgress] = None,
        revoke_ingress: List[main_models.ModifySecurityGroupAttributeRequestRevokeIngress] = None,
    ):
        self.authorize_egress = authorize_egress
        self.authorize_ingress = authorize_ingress
        # This parameter is required.
        self.office_site_id = office_site_id
        # This parameter is required.
        self.region_id = region_id
        self.revoke_egress = revoke_egress
        self.revoke_ingress = revoke_ingress

    def validate(self):
        if self.authorize_egress:
            for v1 in self.authorize_egress:
                 if v1:
                    v1.validate()
        if self.authorize_ingress:
            for v1 in self.authorize_ingress:
                 if v1:
                    v1.validate()
        if self.revoke_egress:
            for v1 in self.revoke_egress:
                 if v1:
                    v1.validate()
        if self.revoke_ingress:
            for v1 in self.revoke_ingress:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizeEgress'] = []
        if self.authorize_egress is not None:
            for k1 in self.authorize_egress:
                result['AuthorizeEgress'].append(k1.to_map() if k1 else None)

        result['AuthorizeIngress'] = []
        if self.authorize_ingress is not None:
            for k1 in self.authorize_ingress:
                result['AuthorizeIngress'].append(k1.to_map() if k1 else None)

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RevokeEgress'] = []
        if self.revoke_egress is not None:
            for k1 in self.revoke_egress:
                result['RevokeEgress'].append(k1.to_map() if k1 else None)

        result['RevokeIngress'] = []
        if self.revoke_ingress is not None:
            for k1 in self.revoke_ingress:
                result['RevokeIngress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorize_egress = []
        if m.get('AuthorizeEgress') is not None:
            for k1 in m.get('AuthorizeEgress'):
                temp_model = main_models.ModifySecurityGroupAttributeRequestAuthorizeEgress()
                self.authorize_egress.append(temp_model.from_map(k1))

        self.authorize_ingress = []
        if m.get('AuthorizeIngress') is not None:
            for k1 in m.get('AuthorizeIngress'):
                temp_model = main_models.ModifySecurityGroupAttributeRequestAuthorizeIngress()
                self.authorize_ingress.append(temp_model.from_map(k1))

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.revoke_egress = []
        if m.get('RevokeEgress') is not None:
            for k1 in m.get('RevokeEgress'):
                temp_model = main_models.ModifySecurityGroupAttributeRequestRevokeEgress()
                self.revoke_egress.append(temp_model.from_map(k1))

        self.revoke_ingress = []
        if m.get('RevokeIngress') is not None:
            for k1 in m.get('RevokeIngress'):
                temp_model = main_models.ModifySecurityGroupAttributeRequestRevokeIngress()
                self.revoke_ingress.append(temp_model.from_map(k1))

        return self

class ModifySecurityGroupAttributeRequestRevokeIngress(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        nic_type: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.description = description
        self.dest_cidr_ip = dest_cidr_ip
        self.ip_protocol = ip_protocol
        self.nic_type = nic_type
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nic_type is not None:
            result['NicType'] = self.nic_type

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

class ModifySecurityGroupAttributeRequestRevokeEgress(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        nic_type: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.description = description
        self.dest_cidr_ip = dest_cidr_ip
        self.ip_protocol = ip_protocol
        self.nic_type = nic_type
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nic_type is not None:
            result['NicType'] = self.nic_type

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

class ModifySecurityGroupAttributeRequestAuthorizeIngress(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        nic_type: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.description = description
        self.dest_cidr_ip = dest_cidr_ip
        self.ip_protocol = ip_protocol
        self.nic_type = nic_type
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nic_type is not None:
            result['NicType'] = self.nic_type

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

class ModifySecurityGroupAttributeRequestAuthorizeEgress(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        nic_type: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.description = description
        self.dest_cidr_ip = dest_cidr_ip
        self.ip_protocol = ip_protocol
        self.nic_type = nic_type
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nic_type is not None:
            result['NicType'] = self.nic_type

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

