# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetAllowedIpListResponseBody(DaraModel):
    def __init__(
        self,
        allowed_list: main_models.GetAllowedIpListResponseBodyAllowedList = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The IP address whitelist.
        self.allowed_list = allowed_list
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.allowed_list:
            self.allowed_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_list is not None:
            result['AllowedList'] = self.allowed_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedList') is not None:
            temp_model = main_models.GetAllowedIpListResponseBodyAllowedList()
            self.allowed_list = temp_model.from_map(m.get('AllowedList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAllowedIpListResponseBodyAllowedList(DaraModel):
    def __init__(
        self,
        deploy_type: int = None,
        internet_list: List[main_models.GetAllowedIpListResponseBodyAllowedListInternetList] = None,
        vpc_list: List[main_models.GetAllowedIpListResponseBodyAllowedListVpcList] = None,
    ):
        # The deployment mode of the instance. Valid values:
        # 
        # *   **4**: allows access from the Internet and a virtual private cloud (VPC).
        # *   **5**: allows access from a VPC.
        # 
        # >  Only integrators need to concern themselves with the value of this parameter.
        self.deploy_type = deploy_type
        # The whitelist for access from the Internet.
        self.internet_list = internet_list
        # The whitelist for access from a virtual private cloud (VPC).
        self.vpc_list = vpc_list

    def validate(self):
        if self.internet_list:
            for v1 in self.internet_list:
                 if v1:
                    v1.validate()
        if self.vpc_list:
            for v1 in self.vpc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        result['InternetList'] = []
        if self.internet_list is not None:
            for k1 in self.internet_list:
                result['InternetList'].append(k1.to_map() if k1 else None)

        result['VpcList'] = []
        if self.vpc_list is not None:
            for k1 in self.vpc_list:
                result['VpcList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        self.internet_list = []
        if m.get('InternetList') is not None:
            for k1 in m.get('InternetList'):
                temp_model = main_models.GetAllowedIpListResponseBodyAllowedListInternetList()
                self.internet_list.append(temp_model.from_map(k1))

        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k1 in m.get('VpcList'):
                temp_model = main_models.GetAllowedIpListResponseBodyAllowedListVpcList()
                self.vpc_list.append(temp_model.from_map(k1))

        return self

class GetAllowedIpListResponseBodyAllowedListVpcList(DaraModel):
    def __init__(
        self,
        allowed_ip_group: Dict[str, str] = None,
        allowed_ip_list: List[str] = None,
        black_iplist: List[str] = None,
        black_ipmap: Dict[str, str] = None,
        port_range: str = None,
        security_group_id: str = None,
        user_defined_shared_security_group: bool = None,
    ):
        # The group to which the IP address whitelist belongs.
        self.allowed_ip_group = allowed_ip_group
        # The information about the IP address whitelist.
        self.allowed_ip_list = allowed_ip_list
        self.black_iplist = black_iplist
        self.black_ipmap = black_ipmap
        # The port range. Valid value:
        # 
        # **9092/9092**.
        self.port_range = port_range
        self.security_group_id = security_group_id
        self.user_defined_shared_security_group = user_defined_shared_security_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_ip_group is not None:
            result['AllowedIpGroup'] = self.allowed_ip_group

        if self.allowed_ip_list is not None:
            result['AllowedIpList'] = self.allowed_ip_list

        if self.black_iplist is not None:
            result['BlackIPList'] = self.black_iplist

        if self.black_ipmap is not None:
            result['BlackIPMap'] = self.black_ipmap

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.user_defined_shared_security_group is not None:
            result['UserDefinedSharedSecurityGroup'] = self.user_defined_shared_security_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedIpGroup') is not None:
            self.allowed_ip_group = m.get('AllowedIpGroup')

        if m.get('AllowedIpList') is not None:
            self.allowed_ip_list = m.get('AllowedIpList')

        if m.get('BlackIPList') is not None:
            self.black_iplist = m.get('BlackIPList')

        if m.get('BlackIPMap') is not None:
            self.black_ipmap = m.get('BlackIPMap')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('UserDefinedSharedSecurityGroup') is not None:
            self.user_defined_shared_security_group = m.get('UserDefinedSharedSecurityGroup')

        return self

class GetAllowedIpListResponseBodyAllowedListInternetList(DaraModel):
    def __init__(
        self,
        allowed_ip_group: Dict[str, str] = None,
        allowed_ip_list: List[str] = None,
        black_iplist: List[str] = None,
        black_ipmap: Dict[str, str] = None,
        port_range: str = None,
        security_group_id: str = None,
        user_defined_shared_security_group: bool = None,
    ):
        # The group to which the IP address whitelist belongs.
        self.allowed_ip_group = allowed_ip_group
        # The information about the IP address whitelist.
        self.allowed_ip_list = allowed_ip_list
        self.black_iplist = black_iplist
        self.black_ipmap = black_ipmap
        # The port range. Valid value:
        # 
        # **9093/9093**.
        self.port_range = port_range
        self.security_group_id = security_group_id
        self.user_defined_shared_security_group = user_defined_shared_security_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_ip_group is not None:
            result['AllowedIpGroup'] = self.allowed_ip_group

        if self.allowed_ip_list is not None:
            result['AllowedIpList'] = self.allowed_ip_list

        if self.black_iplist is not None:
            result['BlackIPList'] = self.black_iplist

        if self.black_ipmap is not None:
            result['BlackIPMap'] = self.black_ipmap

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.user_defined_shared_security_group is not None:
            result['UserDefinedSharedSecurityGroup'] = self.user_defined_shared_security_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedIpGroup') is not None:
            self.allowed_ip_group = m.get('AllowedIpGroup')

        if m.get('AllowedIpList') is not None:
            self.allowed_ip_list = m.get('AllowedIpList')

        if m.get('BlackIPList') is not None:
            self.black_iplist = m.get('BlackIPList')

        if m.get('BlackIPMap') is not None:
            self.black_ipmap = m.get('BlackIPMap')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('UserDefinedSharedSecurityGroup') is not None:
            self.user_defined_shared_security_group = m.get('UserDefinedSharedSecurityGroup')

        return self

