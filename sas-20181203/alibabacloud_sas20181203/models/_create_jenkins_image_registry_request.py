# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJenkinsImageRegistryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        extra_param: str = None,
        net_type: int = None,
        password: str = None,
        persistence_day: int = None,
        protocol_type: int = None,
        region_id: str = None,
        registry_host_ip: str = None,
        registry_name: str = None,
        registry_type: str = None,
        registry_version: str = None,
        source_ip: str = None,
        trans_per_hour: int = None,
        user_name: str = None,
        vpc_id: str = None,
        white_list: str = None,
    ):
        # The domain name of the image repository.
        self.domain_name = domain_name
        # The additional parameters of the image repository. The value of this parameter contains the following fields:
        # 
        # *   **namespace**: the namespace
        # *   **authToken**: the authorization token
        self.extra_param = extra_param
        # The network type. Valid values:
        # 
        # *   **1**: Internet
        # *   **2**: Virtual Private Cloud (VPC)
        self.net_type = net_type
        # The password.
        self.password = password
        # The number of days during which assets can be retained.
        self.persistence_day = persistence_day
        # The type of the protocol. Valid values:
        # 
        # *   **1**: HTTP
        # *   **2**: HTTPS
        self.protocol_type = protocol_type
        # The region ID of the image repository.
        self.region_id = region_id
        # The IP address of the image repository.
        self.registry_host_ip = registry_host_ip
        # The alias of the image repository.
        self.registry_name = registry_name
        # The type of the image repository. Valid values:
        # 
        # *   **CI/CD**: Jenkins
        self.registry_type = registry_type
        # The version of the image repository. Default value: -. Valid values:
        # 
        # *   **-**: the default version
        # *   **V1**: V1.0
        # *   **V2**: V2.0
        self.registry_version = registry_version
        # The source IP address of the request.
        self.source_ip = source_ip
        # The number of images that can be scanned per hour.
        self.trans_per_hour = trans_per_hour
        # The username.
        self.user_name = user_name
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The whitelist of IP addresses.
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.extra_param is not None:
            result['ExtraParam'] = self.extra_param

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.password is not None:
            result['Password'] = self.password

        if self.persistence_day is not None:
            result['PersistenceDay'] = self.persistence_day

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.registry_host_ip is not None:
            result['RegistryHostIp'] = self.registry_host_ip

        if self.registry_name is not None:
            result['RegistryName'] = self.registry_name

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.registry_version is not None:
            result['RegistryVersion'] = self.registry_version

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.trans_per_hour is not None:
            result['TransPerHour'] = self.trans_per_hour

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ExtraParam') is not None:
            self.extra_param = m.get('ExtraParam')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PersistenceDay') is not None:
            self.persistence_day = m.get('PersistenceDay')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegistryHostIp') is not None:
            self.registry_host_ip = m.get('RegistryHostIp')

        if m.get('RegistryName') is not None:
            self.registry_name = m.get('RegistryName')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('RegistryVersion') is not None:
            self.registry_version = m.get('RegistryVersion')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TransPerHour') is not None:
            self.trans_per_hour = m.get('TransPerHour')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

