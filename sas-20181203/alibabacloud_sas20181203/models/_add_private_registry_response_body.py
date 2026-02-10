# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddPrivateRegistryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.AddPrivateRegistryResponseBodyData = None,
        request_id: str = None,
    ):
        # The handling result.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.AddPrivateRegistryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddPrivateRegistryResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        domain_name: str = None,
        id: int = None,
        net_type: int = None,
        password: str = None,
        protocol_type: int = None,
        region_id: str = None,
        registry_host_ip: str = None,
        registry_type: str = None,
        registry_version: str = None,
        token: str = None,
        trans_per_hour: int = None,
        user_name: str = None,
        vpc_id: str = None,
    ):
        # The ID of the user.
        self.ali_uid = ali_uid
        # The domain name of the image repository.
        self.domain_name = domain_name
        # The ID of the image repository.
        self.id = id
        # The network type. Valid values:
        # 
        # *   **1**: Internet
        # *   **2**: VPC
        self.net_type = net_type
        # The password.
        self.password = password
        # The type of the protocol. Valid values:
        # 
        # *   **1**: HTTP
        # *   **2**: HTTPS
        self.protocol_type = protocol_type
        # The region ID of the image repository.
        self.region_id = region_id
        # The IP address of the image repository.
        self.registry_host_ip = registry_host_ip
        # The type of the image repository. Valid values:
        # 
        # *   **harbor**
        # *   **quay**
        self.registry_type = registry_type
        # The version of the image repository. Default value: -. Valid values:
        # 
        # *   **-**: the default version
        # *   **V1**
        # *   **V2**
        self.registry_version = registry_version
        # The value of the token.
        self.token = token
        # The number of scan tasks that are performed per hour.
        self.trans_per_hour = trans_per_hour
        # The username.
        self.user_name = user_name
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.id is not None:
            result['Id'] = self.id

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.password is not None:
            result['Password'] = self.password

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.registry_host_ip is not None:
            result['RegistryHostIp'] = self.registry_host_ip

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.registry_version is not None:
            result['RegistryVersion'] = self.registry_version

        if self.token is not None:
            result['Token'] = self.token

        if self.trans_per_hour is not None:
            result['TransPerHour'] = self.trans_per_hour

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegistryHostIp') is not None:
            self.registry_host_ip = m.get('RegistryHostIp')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('RegistryVersion') is not None:
            self.registry_version = m.get('RegistryVersion')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('TransPerHour') is not None:
            self.trans_per_hour = m.get('TransPerHour')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

