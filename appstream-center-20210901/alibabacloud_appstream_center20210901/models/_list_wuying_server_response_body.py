# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListWuyingServerResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        wuying_server_list: List[main_models.ListWuyingServerResponseBodyWuyingServerList] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The list of workstation information.
        self.wuying_server_list = wuying_server_list

    def validate(self):
        if self.wuying_server_list:
            for v1 in self.wuying_server_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WuyingServerList'] = []
        if self.wuying_server_list is not None:
            for k1 in self.wuying_server_list:
                result['WuyingServerList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.wuying_server_list = []
        if m.get('WuyingServerList') is not None:
            for k1 in m.get('WuyingServerList'):
                temp_model = main_models.ListWuyingServerResponseBodyWuyingServerList()
                self.wuying_server_list.append(temp_model.from_map(k1))

        return self

class ListWuyingServerResponseBodyWuyingServerList(DaraModel):
    def __init__(
        self,
        add_virtual_node_pool_status: str = None,
        ali_uid: int = None,
        bandwidth: int = None,
        biz_region_id: str = None,
        charge_type: str = None,
        create_time: str = None,
        data_disk: List[main_models.ListWuyingServerResponseBodyWuyingServerListDataDisk] = None,
        expired_time: str = None,
        fota_version: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_info_list: List[main_models.ListWuyingServerResponseBodyWuyingServerListInstanceInfoList] = None,
        max_price: float = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        os_type: str = None,
        policy_group_id_list: List[str] = None,
        resource_session_status: str = None,
        security_group_ids: List[str] = None,
        server_instance_type_info: main_models.ListWuyingServerResponseBodyWuyingServerListServerInstanceTypeInfo = None,
        sessions: List[main_models.ListWuyingServerResponseBodyWuyingServerListSessions] = None,
        status: str = None,
        sub_pay_type: str = None,
        system_disk_category: str = None,
        system_disk_id: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        timer_group_id: str = None,
        users: List[str] = None,
        virtual_kubelet_ip: str = None,
        virtual_node_pool_id: str = None,
        wuying_server_id: str = None,
        wuying_server_name: str = None,
    ):
        self.add_virtual_node_pool_status = add_virtual_node_pool_status
        self.ali_uid = ali_uid
        self.bandwidth = bandwidth
        # Region.
        self.biz_region_id = biz_region_id
        # The billing method.
        self.charge_type = charge_type
        # The time when the storage resource was created.
        self.create_time = create_time
        # The data disks.
        self.data_disk = data_disk
        # The time when the subscription instance expires.
        self.expired_time = expired_time
        self.fota_version = fota_version
        # The ID of the custom image.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The list of information about the workstation instance.
        self.instance_info_list = instance_info_list
        self.max_price = max_price
        # The private IP address.
        self.network_interface_ip = network_interface_ip
        # The ID of the office network.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The type of the office network.
        self.office_site_type = office_site_type
        # The OS type.
        self.os_type = os_type
        self.policy_group_id_list = policy_group_id_list
        self.resource_session_status = resource_session_status
        self.security_group_ids = security_group_ids
        # The specifications.
        self.server_instance_type_info = server_instance_type_info
        self.sessions = sessions
        # The status of the workstation.
        self.status = status
        self.sub_pay_type = sub_pay_type
        # The type of the system disk.
        self.system_disk_category = system_disk_category
        self.system_disk_id = system_disk_id
        # The performance level (PL) of the system disk.
        self.system_disk_performance_level = system_disk_performance_level
        # The size of the system disk. Unit: GiB.
        self.system_disk_size = system_disk_size
        self.timer_group_id = timer_group_id
        self.users = users
        self.virtual_kubelet_ip = virtual_kubelet_ip
        self.virtual_node_pool_id = virtual_node_pool_id
        # The ID of the workstation.
        self.wuying_server_id = wuying_server_id
        # The name of the workstation.
        self.wuying_server_name = wuying_server_name

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.instance_info_list:
            for v1 in self.instance_info_list:
                 if v1:
                    v1.validate()
        if self.server_instance_type_info:
            self.server_instance_type_info.validate()
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_virtual_node_pool_status is not None:
            result['AddVirtualNodePoolStatus'] = self.add_virtual_node_pool_status

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        result['InstanceInfoList'] = []
        if self.instance_info_list is not None:
            for k1 in self.instance_info_list:
                result['InstanceInfoList'].append(k1.to_map() if k1 else None)

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.policy_group_id_list is not None:
            result['PolicyGroupIdList'] = self.policy_group_id_list

        if self.resource_session_status is not None:
            result['ResourceSessionStatus'] = self.resource_session_status

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.server_instance_type_info is not None:
            result['ServerInstanceTypeInfo'] = self.server_instance_type_info.to_map()

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_id is not None:
            result['SystemDiskId'] = self.system_disk_id

        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.timer_group_id is not None:
            result['TimerGroupId'] = self.timer_group_id

        if self.users is not None:
            result['Users'] = self.users

        if self.virtual_kubelet_ip is not None:
            result['VirtualKubeletIp'] = self.virtual_kubelet_ip

        if self.virtual_node_pool_id is not None:
            result['VirtualNodePoolId'] = self.virtual_node_pool_id

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        if self.wuying_server_name is not None:
            result['WuyingServerName'] = self.wuying_server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddVirtualNodePoolStatus') is not None:
            self.add_virtual_node_pool_status = m.get('AddVirtualNodePoolStatus')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.ListWuyingServerResponseBodyWuyingServerListDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        self.instance_info_list = []
        if m.get('InstanceInfoList') is not None:
            for k1 in m.get('InstanceInfoList'):
                temp_model = main_models.ListWuyingServerResponseBodyWuyingServerListInstanceInfoList()
                self.instance_info_list.append(temp_model.from_map(k1))

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PolicyGroupIdList') is not None:
            self.policy_group_id_list = m.get('PolicyGroupIdList')

        if m.get('ResourceSessionStatus') is not None:
            self.resource_session_status = m.get('ResourceSessionStatus')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('ServerInstanceTypeInfo') is not None:
            temp_model = main_models.ListWuyingServerResponseBodyWuyingServerListServerInstanceTypeInfo()
            self.server_instance_type_info = temp_model.from_map(m.get('ServerInstanceTypeInfo'))

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.ListWuyingServerResponseBodyWuyingServerListSessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskId') is not None:
            self.system_disk_id = m.get('SystemDiskId')

        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('TimerGroupId') is not None:
            self.timer_group_id = m.get('TimerGroupId')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        if m.get('VirtualKubeletIp') is not None:
            self.virtual_kubelet_ip = m.get('VirtualKubeletIp')

        if m.get('VirtualNodePoolId') is not None:
            self.virtual_node_pool_id = m.get('VirtualNodePoolId')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        if m.get('WuyingServerName') is not None:
            self.wuying_server_name = m.get('WuyingServerName')

        return self

class ListWuyingServerResponseBodyWuyingServerListSessions(DaraModel):
    def __init__(
        self,
        resource_session_start_time: str = None,
        user_id: str = None,
    ):
        self.resource_session_start_time = resource_session_start_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_session_start_time is not None:
            result['ResourceSessionStartTime'] = self.resource_session_start_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceSessionStartTime') is not None:
            self.resource_session_start_time = m.get('ResourceSessionStartTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListWuyingServerResponseBodyWuyingServerListServerInstanceTypeInfo(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gpu_memory: int = None,
        gpu_spec: str = None,
        memory: int = None,
        server_instance_type: str = None,
    ):
        # The number of vCPUs.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The memory size. Unit: MB.
        self.gpu_memory = gpu_memory
        self.gpu_spec = gpu_spec
        # The memory size. Unit: MB.
        self.memory = memory
        # Workstation specifications.
        self.server_instance_type = server_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.server_instance_type is not None:
            result['ServerInstanceType'] = self.server_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('ServerInstanceType') is not None:
            self.server_instance_type = m.get('ServerInstanceType')

        return self

class ListWuyingServerResponseBodyWuyingServerListInstanceInfoList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_interface_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the ENI.
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        return self

class ListWuyingServerResponseBodyWuyingServerListDataDisk(DaraModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_id: str = None,
        data_disk_no: str = None,
        data_disk_performance_level: str = None,
        data_disk_size: int = None,
    ):
        # The category of data disk.
        self.data_disk_category = data_disk_category
        self.data_disk_id = data_disk_id
        self.data_disk_no = data_disk_no
        # The PL of the data disk.
        self.data_disk_performance_level = data_disk_performance_level
        # The size of the data disk. Unit: GB.
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.data_disk_id is not None:
            result['DataDiskId'] = self.data_disk_id

        if self.data_disk_no is not None:
            result['DataDiskNo'] = self.data_disk_no

        if self.data_disk_performance_level is not None:
            result['DataDiskPerformanceLevel'] = self.data_disk_performance_level

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DataDiskId') is not None:
            self.data_disk_id = m.get('DataDiskId')

        if m.get('DataDiskNo') is not None:
            self.data_disk_no = m.get('DataDiskNo')

        if m.get('DataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('DataDiskPerformanceLevel')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        return self

