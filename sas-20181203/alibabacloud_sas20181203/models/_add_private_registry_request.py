# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPrivateRegistryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        extra_param: str = None,
        net_type: int = None,
        password: str = None,
        port: int = None,
        protocol_type: int = None,
        registry_host_ip: str = None,
        registry_region_id: str = None,
        registry_type: str = None,
        registry_version: str = None,
        trans_per_hour: int = None,
        user_name: str = None,
        vpc_id: str = None,
    ):
        # The domain name of the registry.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The additional parameters for the image registry. This parameter is required when you use **quay**. The parameters include:
        # 
        # - **namespace**: The namespace.
        # - **authToken**: The authorization token.
        self.extra_param = extra_param
        # The network type. Valid values:
        # - **1**: Internet.
        # - **2**: VPC.
        # 
        # This parameter is required.
        self.net_type = net_type
        # The password.
        # 
        # This parameter is required.
        self.password = password
        # The port number.
        self.port = port
        # The protocol type. Valid values:
        # - **1**: HTTP.
        # - **2**: HTTPS.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The IP address of the registry.
        # 
        # Enter a valid IPv4 address that can be used to connect to the image registry. To specify a domain name for the image registry, use the DomainName parameter.
        # 
        # This parameter is required.
        self.registry_host_ip = registry_host_ip
        # The region ID.
        # >You can call the [ListImageRegistryRegion](~~ListImageRegistryRegion~~) operation to query the supported region IDs.
        # 
        # This parameter is required.
        self.registry_region_id = registry_region_id
        # The type of the private image registry. Valid values:
        # - **harbor**: Harbor environment.
        # - **quay**: Quay environment.
        # 
        # This parameter is required.
        self.registry_type = registry_type
        # The version of the image registry. Valid values:
        # 
        # 
        # - **V1**: Version 1.0.
        # - **V2**: Version 2.0.
        # 
        # This parameter is required.
        self.registry_version = registry_version
        # The number of images scanned per hour.
        self.trans_per_hour = trans_per_hour
        # The username of the image registry.
        # 
        # This parameter is required.
        self.user_name = user_name
        # The instance ID of the VPC.
        self.vpc_id = vpc_id

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

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.registry_host_ip is not None:
            result['RegistryHostIp'] = self.registry_host_ip

        if self.registry_region_id is not None:
            result['RegistryRegionId'] = self.registry_region_id

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.registry_version is not None:
            result['RegistryVersion'] = self.registry_version

        if self.trans_per_hour is not None:
            result['TransPerHour'] = self.trans_per_hour

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

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

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegistryHostIp') is not None:
            self.registry_host_ip = m.get('RegistryHostIp')

        if m.get('RegistryRegionId') is not None:
            self.registry_region_id = m.get('RegistryRegionId')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('RegistryVersion') is not None:
            self.registry_version = m.get('RegistryVersion')

        if m.get('TransPerHour') is not None:
            self.trans_per_hour = m.get('TransPerHour')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

