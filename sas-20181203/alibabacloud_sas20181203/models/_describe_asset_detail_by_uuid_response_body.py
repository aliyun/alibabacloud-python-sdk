# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetDetailByUuidResponseBody(DaraModel):
    def __init__(
        self,
        asset_detail: main_models.DescribeAssetDetailByUuidResponseBodyAssetDetail = None,
        request_id: str = None,
    ):
        # The details of the server.
        self.asset_detail = asset_detail
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.asset_detail:
            self.asset_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_detail is not None:
            result['AssetDetail'] = self.asset_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetDetail') is not None:
            temp_model = main_models.DescribeAssetDetailByUuidResponseBodyAssetDetail()
            self.asset_detail = temp_model.from_map(m.get('AssetDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAssetDetailByUuidResponseBodyAssetDetail(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        auth_modify_time: int = None,
        auth_version: int = None,
        bind: bool = None,
        client_status: str = None,
        client_version: str = None,
        cpu: int = None,
        cpu_info: str = None,
        create_time: int = None,
        disk_info_list: List[str] = None,
        flag: int = None,
        group_trace: str = None,
        host_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        ip_list: List[str] = None,
        kernel: str = None,
        mac_list: List[str] = None,
        mem: int = None,
        memory: int = None,
        os: str = None,
        os_detail: str = None,
        os_name: str = None,
        region: str = None,
        region_id: str = None,
        region_name: str = None,
        sys_info: str = None,
        tag: str = None,
        uuid: str = None,
        vpc_instance_id: str = None,
    ):
        # The type of the asset. Valid values:
        # 
        # *   **0**: ECS instance
        # *   **1**: Server Load Balancer (SLB) instance
        # *   **2**: NAT gateway
        # *   **3**: ApsaraDB RDS database
        # *   **4**: ApsaraDB for MongoDB database
        # *   **5**: ApsaraDB for Redis database
        # *   **6**: image
        # *   **7**: container
        self.asset_type = asset_type
        # The timestamp when Security Center is authorized to protect the asset. Unit: milliseconds.
        self.auth_modify_time = auth_modify_time
        # The edition of Security Center that is authorized to protect the asset. Valid values:
        # 
        # *   **1**: Basic edition (Unauthorized)
        # *   **6**: Anti-virus edition
        # *   **5**: Advanced edition
        # *   **3**: Enterprise edition
        # *   **7**: Ultimate edition
        self.auth_version = auth_version
        # Indicates whether Security Center is authorized to protect the asset. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.bind = bind
        # The status of the Security Center agent. Valid values:
        # 
        # *   **pause**: The Security Center agent suspends protection for your server.
        # *   **online**: The Security Center agent is protecting your server.
        # *   **offline**: The Security Center agent does not protect your server.
        self.client_status = client_status
        # The version of the Security Center agent.
        self.client_version = client_version
        # The number of CPU cores.
        self.cpu = cpu
        # The details of the CPU.
        self.cpu_info = cpu_info
        # The timestamp when Security Center records the details of the server. Unit: milliseconds.
        self.create_time = create_time
        # An array that consists of the information about the disk.
        self.disk_info_list = disk_info_list
        # Indicates whether the asset is provided by Alibaba Cloud. Valid values:
        # 
        # *   **0**: yes
        # *   **1**: no
        self.flag = flag
        # The group to which the server belongs. By default, the servers that are not grouped belong to the **Default** group.
        self.group_trace = group_trace
        # The name of the host.
        self.host_name = host_name
        # The ID of the server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The IP address that is assigned to the Elastic Compute Service (ECS) instance.
        self.ip = ip
        # The IP addresses of the server.
        self.ip_list = ip_list
        # The kernel version of the operating system.
        self.kernel = kernel
        # The media access control (MAC) addresses of the server.
        self.mac_list = mac_list
        # The memory size of the server. Unit: GB.
        self.mem = mem
        # The memory size of the server. Unit: MB.
        self.memory = memory
        # The operating system type of the server.
        self.os = os
        # The operating system version of the server.
        self.os_detail = os_detail
        # The name of the operating system.
        self.os_name = os_name
        # The region in which the server resides.
        self.region = region
        # The ID of the region in which the asset resides.
        self.region_id = region_id
        # The name of the region in which the server resides.
        self.region_name = region_name
        # The operating system information about the server.
        self.sys_info = sys_info
        # The tag that is added to the server.
        self.tag = tag
        # The UUID of the server.
        self.uuid = uuid
        # The ID of the virtual private cloud (VPC) in which the server resides.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.auth_modify_time is not None:
            result['AuthModifyTime'] = self.auth_modify_time

        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.bind is not None:
            result['Bind'] = self.bind

        if self.client_status is not None:
            result['ClientStatus'] = self.client_status

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.disk_info_list is not None:
            result['DiskInfoList'] = self.disk_info_list

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.group_trace is not None:
            result['GroupTrace'] = self.group_trace

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.kernel is not None:
            result['Kernel'] = self.kernel

        if self.mac_list is not None:
            result['MacList'] = self.mac_list

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.os is not None:
            result['Os'] = self.os

        if self.os_detail is not None:
            result['OsDetail'] = self.os_detail

        if self.os_name is not None:
            result['OsName'] = self.os_name

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.sys_info is not None:
            result['SysInfo'] = self.sys_info

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AuthModifyTime') is not None:
            self.auth_modify_time = m.get('AuthModifyTime')

        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CpuInfo') is not None:
            self.cpu_info = m.get('CpuInfo')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DiskInfoList') is not None:
            self.disk_info_list = m.get('DiskInfoList')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('GroupTrace') is not None:
            self.group_trace = m.get('GroupTrace')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('Kernel') is not None:
            self.kernel = m.get('Kernel')

        if m.get('MacList') is not None:
            self.mac_list = m.get('MacList')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsDetail') is not None:
            self.os_detail = m.get('OsDetail')

        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('SysInfo') is not None:
            self.sys_info = m.get('SysInfo')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

