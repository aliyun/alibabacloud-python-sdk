# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateJenkinsImageRegistryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateJenkinsImageRegistryResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        time_cost: int = None,
    ):
        # The result of creating the image repository.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # The time consumed. Unit: seconds.
        self.time_cost = time_cost

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateJenkinsImageRegistryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        return self

class CreateJenkinsImageRegistryResponseBodyData(DaraModel):
    def __init__(
        self,
        black_list: str = None,
        domain_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        net_type: int = None,
        password: str = None,
        persistence_day: int = None,
        protocol_type: int = None,
        region_id: str = None,
        registry_host_ip: str = None,
        registry_name: str = None,
        registry_type: str = None,
        token: str = None,
        trans_per_hour: int = None,
        user_name: str = None,
        vpc_id: str = None,
        white_list: str = None,
    ):
        # The blacklist.
        self.black_list = black_list
        # The domain name of the image repository.
        self.domain_name = domain_name
        # The creation time. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_create = gmt_create
        # The update time. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_modified = gmt_modified
        # The ID of the image repository.
        self.id = id
        # The network type. Valid values:
        # 
        # *   **1**: Internet
        # *   **2**: VPC
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
        # The authentication token of the user.
        self.token = token
        # The number of images that can be scanned per hour.
        self.trans_per_hour = trans_per_hour
        # The username.
        self.user_name = user_name
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The whitelist.
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_list is not None:
            result['BlackList'] = self.black_list

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

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

        if self.token is not None:
            result['Token'] = self.token

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
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('TransPerHour') is not None:
            self.trans_per_hour = m.get('TransPerHour')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

