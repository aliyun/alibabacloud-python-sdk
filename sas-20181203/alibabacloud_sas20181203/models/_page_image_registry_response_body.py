# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class PageImageRegistryResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.PageImageRegistryResponseBodyList] = None,
        page_info: main_models.PageImageRegistryResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of image repositories.
        self.list = list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.PageImageRegistryResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.PageImageRegistryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PageImageRegistryResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class PageImageRegistryResponseBodyList(DaraModel):
    def __init__(
        self,
        black_list: str = None,
        domain_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        image_count: int = None,
        jenkins_env: str = None,
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
        # The IP address blacklist.
        self.black_list = black_list
        # The domain name of the image repository.
        self.domain_name = domain_name
        # The time when the image repository was created. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_create = gmt_create
        # The time when the image repository was updated. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_modified = gmt_modified
        # The ID of the image repository.
        self.id = id
        # The number of images that are stored in the image repository.
        self.image_count = image_count
        # The information about the Jenkins environment.
        self.jenkins_env = jenkins_env
        # The network type. Valid values:
        # 
        # *   **1**: Internet.
        # *   **2**: virtual private cloud (VPC).
        self.net_type = net_type
        # The password.
        self.password = password
        # The number of days for which assets are retained.
        self.persistence_day = persistence_day
        # The type of the protocol. Valid values:
        # 
        # *   **1**: HTTP.
        # *   **2**: HTTPS.
        self.protocol_type = protocol_type
        # The region ID of the image repository.
        self.region_id = region_id
        # The IP address of the image repository.
        self.registry_host_ip = registry_host_ip
        # The alias of the image repository.
        self.registry_name = registry_name
        # The type of the image repository. Valid values:
        # 
        # *   **acr**: Container Registry.
        # *   **harbor**: Harbor.
        # *   **quay**: Quay.
        # *   **CI/CD**: Jenkins.
        self.registry_type = registry_type
        # The authentication token of the user.
        self.token = token
        # The number of scan tasks that are performed per hour.
        self.trans_per_hour = trans_per_hour
        # The username.
        self.user_name = user_name
        # The VPC ID.
        self.vpc_id = vpc_id
        # The IP address whitelist.
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

        if self.image_count is not None:
            result['ImageCount'] = self.image_count

        if self.jenkins_env is not None:
            result['JenkinsEnv'] = self.jenkins_env

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

        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')

        if m.get('JenkinsEnv') is not None:
            self.jenkins_env = m.get('JenkinsEnv')

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

