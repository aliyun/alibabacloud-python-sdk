# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopsInGroupResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        online_pre_paid_desktops_count: int = None,
        paid_desktops: List[main_models.DescribeDesktopsInGroupResponseBodyPaidDesktops] = None,
        paid_desktops_count: int = None,
        post_paid_desktops: List[main_models.DescribeDesktopsInGroupResponseBodyPostPaidDesktops] = None,
        post_paid_desktops_count: int = None,
        post_paid_desktops_total_amount: int = None,
        request_id: str = None,
        running_pre_paid_desktops_count: int = None,
        stoped_pre_paid_desktops_count: int = None,
        stopped_pre_paid_desktops_count: int = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The number of subscription cloud computers that are in the Connected state.
        self.online_pre_paid_desktops_count = online_pre_paid_desktops_count
        # The subscription cloud computers.
        self.paid_desktops = paid_desktops
        # The total number of subscription cloud computers.
        self.paid_desktops_count = paid_desktops_count
        # The pay-as-you-go cloud computers.
        self.post_paid_desktops = post_paid_desktops
        # The total number of pay-as-you-go cloud computers.
        self.post_paid_desktops_count = post_paid_desktops_count
        # The total amount of bills for pay-as-you-go cloud computers.
        self.post_paid_desktops_total_amount = post_paid_desktops_total_amount
        # The request ID.
        self.request_id = request_id
        # The number of subscription cloud computers that are in the Running state.
        self.running_pre_paid_desktops_count = running_pre_paid_desktops_count
        # The number of subscription cloud computers that are in the Stopped state.
        self.stoped_pre_paid_desktops_count = stoped_pre_paid_desktops_count
        # The number of subscription cloud computers that are in the Stopped state.
        self.stopped_pre_paid_desktops_count = stopped_pre_paid_desktops_count

    def validate(self):
        if self.paid_desktops:
            for v1 in self.paid_desktops:
                 if v1:
                    v1.validate()
        if self.post_paid_desktops:
            for v1 in self.post_paid_desktops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.online_pre_paid_desktops_count is not None:
            result['OnlinePrePaidDesktopsCount'] = self.online_pre_paid_desktops_count

        result['PaidDesktops'] = []
        if self.paid_desktops is not None:
            for k1 in self.paid_desktops:
                result['PaidDesktops'].append(k1.to_map() if k1 else None)

        if self.paid_desktops_count is not None:
            result['PaidDesktopsCount'] = self.paid_desktops_count

        result['PostPaidDesktops'] = []
        if self.post_paid_desktops is not None:
            for k1 in self.post_paid_desktops:
                result['PostPaidDesktops'].append(k1.to_map() if k1 else None)

        if self.post_paid_desktops_count is not None:
            result['PostPaidDesktopsCount'] = self.post_paid_desktops_count

        if self.post_paid_desktops_total_amount is not None:
            result['PostPaidDesktopsTotalAmount'] = self.post_paid_desktops_total_amount

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.running_pre_paid_desktops_count is not None:
            result['RunningPrePaidDesktopsCount'] = self.running_pre_paid_desktops_count

        if self.stoped_pre_paid_desktops_count is not None:
            result['StopedPrePaidDesktopsCount'] = self.stoped_pre_paid_desktops_count

        if self.stopped_pre_paid_desktops_count is not None:
            result['StoppedPrePaidDesktopsCount'] = self.stopped_pre_paid_desktops_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OnlinePrePaidDesktopsCount') is not None:
            self.online_pre_paid_desktops_count = m.get('OnlinePrePaidDesktopsCount')

        self.paid_desktops = []
        if m.get('PaidDesktops') is not None:
            for k1 in m.get('PaidDesktops'):
                temp_model = main_models.DescribeDesktopsInGroupResponseBodyPaidDesktops()
                self.paid_desktops.append(temp_model.from_map(k1))

        if m.get('PaidDesktopsCount') is not None:
            self.paid_desktops_count = m.get('PaidDesktopsCount')

        self.post_paid_desktops = []
        if m.get('PostPaidDesktops') is not None:
            for k1 in m.get('PostPaidDesktops'):
                temp_model = main_models.DescribeDesktopsInGroupResponseBodyPostPaidDesktops()
                self.post_paid_desktops.append(temp_model.from_map(k1))

        if m.get('PostPaidDesktopsCount') is not None:
            self.post_paid_desktops_count = m.get('PostPaidDesktopsCount')

        if m.get('PostPaidDesktopsTotalAmount') is not None:
            self.post_paid_desktops_total_amount = m.get('PostPaidDesktopsTotalAmount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningPrePaidDesktopsCount') is not None:
            self.running_pre_paid_desktops_count = m.get('RunningPrePaidDesktopsCount')

        if m.get('StopedPrePaidDesktopsCount') is not None:
            self.stoped_pre_paid_desktops_count = m.get('StopedPrePaidDesktopsCount')

        if m.get('StoppedPrePaidDesktopsCount') is not None:
            self.stopped_pre_paid_desktops_count = m.get('StoppedPrePaidDesktopsCount')

        return self

class DescribeDesktopsInGroupResponseBodyPostPaidDesktops(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        create_duration: str = None,
        create_time: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        disk_type: str = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        end_user_name: str = None,
        end_user_names: List[str] = None,
        fota_version: str = None,
        gpu_driver_version: str = None,
        image_id: str = None,
        image_name: str = None,
        management_flag: str = None,
        management_flags: List[str] = None,
        member_eni_ip: str = None,
        os_type: str = None,
        primary_eni_ip: str = None,
        protocol_type: str = None,
        release_time: str = None,
        reset_time: str = None,
        system_disk_size: int = None,
    ):
        # The connection status of the cloud computer.
        # 
        # Valid values:
        # 
        # *   Unknown
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Connected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Disconnected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.connection_status = connection_status
        # The retention period. Unit: milliseconds.
        self.create_duration = create_duration
        # The time when the cloud computer was created.
        self.create_time = create_time
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # The status of the cloud computer.
        # 
        # Valid values:
        # 
        # *   Stopped
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Starting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Rebuilding
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopping
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Expired
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleted
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Pending
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.desktop_status = desktop_status
        # The type of the disk.
        # 
        # Valid values:
        # 
        # *   SYSTEM: system disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DATA: data disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.disk_type = disk_type
        # The ID of the authorized user.
        self.end_user_id = end_user_id
        # The IDs of the end users who are connected to the cloud computers in the cloud computer pool. If no end users are connected, no values are returned for this parameter.
        self.end_user_ids = end_user_ids
        # The username of the authorized user.
        self.end_user_name = end_user_name
        # The usernames of the end users who are connected to the cloud computers in the cloud computer pool. If no end users are connected, no values are returned for this parameter.
        self.end_user_names = end_user_names
        # The image version.
        self.fota_version = fota_version
        # The version of the GPU driver.
        self.gpu_driver_version = gpu_driver_version
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The flag that is used to manage the cloud computer.
        # 
        # Valid values:
        # 
        # *   Updating: The configurations of the cloud computer are being updated.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NoFlag: No flags are attached to the cloud computer.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.management_flag = management_flag
        # The flags that are used to manage the cloud computers.
        self.management_flags = management_flags
        # The IP address of the member NIC of the instance.
        self.member_eni_ip = member_eni_ip
        # The OS.
        # 
        # Valid values:
        # 
        # *   Linux
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.os_type = os_type
        # The IP address of the primary NIC of the instance.
        self.primary_eni_ip = primary_eni_ip
        # The protocol.
        # 
        # Valid values:
        # 
        # *   HDX: HDX protocol
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ASP: ASP protocol provided by Alibaba Cloud
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.protocol_type = protocol_type
        # The time when the cloud computer was released.
        self.release_time = release_time
        # The time when the cloud computer was reset.
        self.reset_time = reset_time
        # The system disk size. Unit: GiB.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.create_duration is not None:
            result['CreateDuration'] = self.create_duration

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name

        if self.end_user_names is not None:
            result['EndUserNames'] = self.end_user_names

        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag

        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags

        if self.member_eni_ip is not None:
            result['MemberEniIp'] = self.member_eni_ip

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.primary_eni_ip is not None:
            result['PrimaryEniIp'] = self.primary_eni_ip

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.reset_time is not None:
            result['ResetTime'] = self.reset_time

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('CreateDuration') is not None:
            self.create_duration = m.get('CreateDuration')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')

        if m.get('EndUserNames') is not None:
            self.end_user_names = m.get('EndUserNames')

        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')

        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')

        if m.get('MemberEniIp') is not None:
            self.member_eni_ip = m.get('MemberEniIp')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PrimaryEniIp') is not None:
            self.primary_eni_ip = m.get('PrimaryEniIp')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('ResetTime') is not None:
            self.reset_time = m.get('ResetTime')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

class DescribeDesktopsInGroupResponseBodyPaidDesktops(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        disk_type: str = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        end_user_name: str = None,
        end_user_names: List[str] = None,
        expired_time: str = None,
        fota_version: str = None,
        gpu_driver_version: str = None,
        image_id: str = None,
        image_name: str = None,
        management_flag: str = None,
        management_flags: List[str] = None,
        member_eni_ip: str = None,
        os_type: str = None,
        primary_eni_ip: str = None,
        protocol_type: str = None,
        reset_time: str = None,
        system_disk_size: int = None,
    ):
        # The connection status of the cloud computer.
        # 
        # Valid values:
        # 
        # *   Unknown
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Connected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Disconnected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.connection_status = connection_status
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # The status of the cloud computer.
        # 
        # Valid values:
        # 
        # *   Stopped
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Starting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Rebuilding
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopping
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Expired
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleted
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Pending
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.desktop_status = desktop_status
        # The type of the disk.
        # 
        # Valid values:
        # 
        # *   SYSTEM: system disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DATA: data disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.disk_type = disk_type
        # The ID of the authorized user.
        self.end_user_id = end_user_id
        # The IDs of the end users who are connected to the cloud computers in the cloud computer share. If no end users are connected, no values are returned for this parameter.
        self.end_user_ids = end_user_ids
        # The username of the authorized user.
        self.end_user_name = end_user_name
        # The usernames of the end users who are connected to the cloud computers in the cloud computer share. If no end users are connected, no values are returned for this parameter.
        self.end_user_names = end_user_names
        self.expired_time = expired_time
        # The image version.
        self.fota_version = fota_version
        # The version of the GPU driver.
        self.gpu_driver_version = gpu_driver_version
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The flag that is used to manage the cloud computer.
        # 
        # Valid values:
        # 
        # *   Updating: The configurations of the cloud computer are being updated.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NoFlag: No flags are attached to the cloud computer.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.management_flag = management_flag
        # The flags that are used to manage the cloud computers.
        self.management_flags = management_flags
        # The IP address of the member network interface controller (NIC) of the instance.
        self.member_eni_ip = member_eni_ip
        # The OS.
        # 
        # Valid values:
        # 
        # *   Linux
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.os_type = os_type
        # The IP address of the primary NIC of the instance.
        self.primary_eni_ip = primary_eni_ip
        # The protocol.
        # 
        # Valid values:
        # 
        # *   HDX: High-definition Experience (HDX) protocol
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ASP: Adaptive Streaming Protocol (ASP) protocol provided by Alibaba Cloud
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.protocol_type = protocol_type
        # The time when the cloud computer was reset.
        self.reset_time = reset_time
        # The system disk size. Unit: GiB.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name

        if self.end_user_names is not None:
            result['EndUserNames'] = self.end_user_names

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag

        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags

        if self.member_eni_ip is not None:
            result['MemberEniIp'] = self.member_eni_ip

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.primary_eni_ip is not None:
            result['PrimaryEniIp'] = self.primary_eni_ip

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.reset_time is not None:
            result['ResetTime'] = self.reset_time

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')

        if m.get('EndUserNames') is not None:
            self.end_user_names = m.get('EndUserNames')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')

        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')

        if m.get('MemberEniIp') is not None:
            self.member_eni_ip = m.get('MemberEniIp')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PrimaryEniIp') is not None:
            self.primary_eni_ip = m.get('PrimaryEniIp')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ResetTime') is not None:
            self.reset_time = m.get('ResetTime')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

