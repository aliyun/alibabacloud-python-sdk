# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeGatewayAttributeResponseBody(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        create_time: str = None,
        current_version: str = None,
        db_type: str = None,
        endpoints: List[main_models.DescribeGatewayAttributeResponseBodyEndpoints] = None,
        expire_time: str = None,
        expired: bool = None,
        gw_cluster_id: str = None,
        gw_description: str = None,
        latest_version: str = None,
        modify_time: str = None,
        pay_type: str = None,
        region_id: str = None,
        request_id: str = None,
        running_version: str = None,
        security_iparrays: List[main_models.DescribeGatewayAttributeResponseBodySecurityIPArrays] = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The specification code for the gateway instance.
        self.class_code = class_code
        # The time when the gateway instance was created.
        self.create_time = create_time
        self.current_version = current_version
        # The database type.
        self.db_type = db_type
        # A list of endpoints for the gateway instance.
        self.endpoints = endpoints
        # The time when the subscription for the gateway instance expires.
        # 
        # This parameter is empty for pay-as-you-go instances.
        self.expire_time = expire_time
        # Indicates whether the subscription for the gateway instance has expired. Valid values:
        # 
        # - true
        # 
        # - false
        self.expired = expired
        # The ID of the gateway instance.
        self.gw_cluster_id = gw_cluster_id
        # The description of the gateway instance.
        self.gw_description = gw_description
        self.latest_version = latest_version
        # The time when the gateway instance was last modified.
        self.modify_time = modify_time
        # The billing method of the gateway instance. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # 
        # - **Prepaid**: subscription.
        self.pay_type = pay_type
        # The ID of the region.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        self.running_version = running_version
        # A list of IP whitelists for the gateway instance.
        self.security_iparrays = security_iparrays
        # The status of the gateway instance. Valid values:
        # 
        # - **CREATE**: The gateway instance is being created.
        # 
        # - **ACTIVATION**: The gateway instance is running.
        self.status = status
        # The ID of the VSwitch where the gateway instance is deployed.
        self.v_switch_id = v_switch_id
        # The ID of the VPC where the gateway instance is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.security_iparrays:
            for v1 in self.security_iparrays:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.db_type is not None:
            result['DbType'] = self.db_type

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.gw_description is not None:
            result['GwDescription'] = self.gw_description

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.running_version is not None:
            result['RunningVersion'] = self.running_version

        result['SecurityIPArrays'] = []
        if self.security_iparrays is not None:
            for k1 in self.security_iparrays:
                result['SecurityIPArrays'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.DescribeGatewayAttributeResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('GwDescription') is not None:
            self.gw_description = m.get('GwDescription')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningVersion') is not None:
            self.running_version = m.get('RunningVersion')

        self.security_iparrays = []
        if m.get('SecurityIPArrays') is not None:
            for k1 in m.get('SecurityIPArrays'):
                temp_model = main_models.DescribeGatewayAttributeResponseBodySecurityIPArrays()
                self.security_iparrays.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeGatewayAttributeResponseBodySecurityIPArrays(DaraModel):
    def __init__(
        self,
        security_iparray_name: str = None,
        security_iparray_tag: str = None,
        security_iplist: str = None,
    ):
        # The name of the IP whitelist. The default value is `default`.
        self.security_iparray_name = security_iparray_name
        # The tag of the IP whitelist.
        self.security_iparray_tag = security_iparray_tag
        # A comma-separated list of IP addresses in the IP whitelist.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_iparray_name is not None:
            result['SecurityIPArrayName'] = self.security_iparray_name

        if self.security_iparray_tag is not None:
            result['SecurityIPArrayTag'] = self.security_iparray_tag

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIPArrayName') is not None:
            self.security_iparray_name = m.get('SecurityIPArrayName')

        if m.get('SecurityIPArrayTag') is not None:
            self.security_iparray_tag = m.get('SecurityIPArrayTag')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

class DescribeGatewayAttributeResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        address: str = None,
        endpoint_id: str = None,
        gw_cluster_id: str = None,
        net_type: str = None,
        port: str = None,
        tunnel_id: str = None,
        vpc_id: str = None,
    ):
        # The endpoint address.
        self.address = address
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The ID of the gateway instance.
        self.gw_cluster_id = gw_cluster_id
        # The network type of the endpoint. Valid values:
        # 
        # - **Private**: VPC endpoint.
        # 
        # - **Public**: public endpoint.
        self.net_type = net_type
        # The port number.
        self.port = port
        # The tunnel ID.
        self.tunnel_id = tunnel_id
        # The ID of the VPC to which the endpoint belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

