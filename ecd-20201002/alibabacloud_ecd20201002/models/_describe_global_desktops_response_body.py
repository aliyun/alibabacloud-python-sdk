# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalDesktopsResponseBody(DaraModel):
    def __init__(
        self,
        desktops: List[main_models.DescribeGlobalDesktopsResponseBodyDesktops] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details about the cloud computer.
        self.desktops = desktops
        # The token used to start the next query. If NextToken is empty, it indicates that there is no next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.desktops:
            for v1 in self.desktops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Desktops'] = []
        if self.desktops is not None:
            for k1 in self.desktops:
                result['Desktops'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktops = []
        if m.get('Desktops') is not None:
            for k1 in m.get('Desktops'):
                temp_model = main_models.DescribeGlobalDesktopsResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGlobalDesktopsResponseBodyDesktops(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        clients: List[main_models.DescribeGlobalDesktopsResponseBodyDesktopsClients] = None,
        connection_status: str = None,
        cpu: int = None,
        creation_time: str = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        desktop_timers: List[main_models.DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers] = None,
        desktop_type: str = None,
        directory_id: str = None,
        disks: List[main_models.DescribeGlobalDesktopsResponseBodyDesktopsDisks] = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        expired_time: str = None,
        fota_update: main_models.DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate = None,
        gpu_memory: int = None,
        hibernation_beta: bool = None,
        host_name: str = None,
        image_id: str = None,
        last_start_time: str = None,
        local_name: str = None,
        management_flags: List[str] = None,
        memory: int = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        os: str = None,
        os_description: str = None,
        os_type: str = None,
        platform: str = None,
        policy_group_id: str = None,
        protocol_type: str = None,
        real_desktop_id: str = None,
        region_id: str = None,
        region_location: str = None,
        session_type: str = None,
        sessions: List[main_models.DescribeGlobalDesktopsResponseBodyDesktopsSessions] = None,
        support_hibernation: bool = None,
        user_custom_name: str = None,
    ):
        # The billing method of the cloud computer pool.
        # 
        # Valid value:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        self.charge_type = charge_type
        # The information about the supported clients.
        self.clients = clients
        # The state of the endpoint connection.
        # 
        # Valid values:
        # 
        # *   Connected
        # *   Disconnecting
        # *   Pending.
        # *   Connecting.
        # *   Disconnected.
        # *   Deleting
        self.connection_status = connection_status
        # The number of vCPUs.
        self.cpu = cpu
        # The time when the cloud computer was created.
        self.creation_time = creation_time
        # The ID of the cloud computer share.
        self.desktop_group_id = desktop_group_id
        # The cloud compute ID.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # The cloud computer status.
        self.desktop_status = desktop_status
        # The cloud computer timer object.
        self.desktop_timers = desktop_timers
        # The cloud computer type.
        self.desktop_type = desktop_type
        # The network ID of the office. Same as `OfficeSiteId`.
        self.directory_id = directory_id
        # The disks.
        self.disks = disks
        # The names of end users.
        self.end_user_id = end_user_id
        # The list of end user.
        self.end_user_ids = end_user_ids
        # The expiration time of the cloud computer.
        # 
        # *   For a cloud computer that is a package year or month, the return value is meaningful.
        # *   For pay-as-you-go cloud computers, the `2099-12-31T15:59Z` is returned.
        self.expired_time = expired_time
        # The information about image update.
        self.fota_update = fota_update
        # The GPU memory size. For GPU-accelerated cloud computers, this return value is significant. Unit: MB.
        self.gpu_memory = gpu_memory
        # Indicates whether this is a beta version of the hibernation feature.
        self.hibernation_beta = hibernation_beta
        # The hostname of the cloud desktop.
        self.host_name = host_name
        # The image ID.
        self.image_id = image_id
        # The time when the cloud desktop was last started.
        self.last_start_time = last_start_time
        # The region name.
        self.local_name = local_name
        # The list of cloud computer status.
        self.management_flags = management_flags
        # The memory of the cloud computer. Unit: MiB.
        self.memory = memory
        # The IP address of the ENI.
        self.network_interface_ip = network_interface_ip
        # The IDs of the office networks.
        self.office_site_id = office_site_id
        # OS Type
        self.os = os
        self.os_description = os_description
        # The operating system.
        # 
        # Valid value:
        # 
        # *   Linux
        # *   Windows
        self.os_type = os_type
        # The OS platform.
        # 
        # Valid value:
        # 
        # *   Ubuntu
        # *   UOS
        # *   CentOS
        # *   Windows Server 2019
        # *   Windows Server 2016
        self.platform = platform
        # The cloud computer policy ID.
        self.policy_group_id = policy_group_id
        # The type of the protocol.
        # 
        # Valid value:
        # 
        # *   High-definition Experience (HDX)
        # *   ASP
        self.protocol_type = protocol_type
        # If a shared cloud computer is assigned a real cloud computer, the ID of the cloud computer is displayed.
        self.real_desktop_id = real_desktop_id
        # The region ID.
        self.region_id = region_id
        self.region_location = region_location
        # The type of the session.
        # 
        # Valid value:
        # 
        # *   SINGLE_SESSION
        # *   MULTIPLE_SESSION
        self.session_type = session_type
        # The list of session information.
        self.sessions = sessions
        # Indicates whether hibernation is supported.
        # 
        # Valid values:
        # 
        # *   true: supported
        # *   false: not supported
        self.support_hibernation = support_hibernation
        # The custom cloud computer name.
        self.user_custom_name = user_custom_name

    def validate(self):
        if self.clients:
            for v1 in self.clients:
                 if v1:
                    v1.validate()
        if self.desktop_timers:
            for v1 in self.desktop_timers:
                 if v1:
                    v1.validate()
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()
        if self.fota_update:
            self.fota_update.validate()
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        result['Clients'] = []
        if self.clients is not None:
            for k1 in self.clients:
                result['Clients'].append(k1.to_map() if k1 else None)

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        result['DesktopTimers'] = []
        if self.desktop_timers is not None:
            for k1 in self.desktop_timers:
                result['DesktopTimers'].append(k1.to_map() if k1 else None)

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.fota_update is not None:
            result['FotaUpdate'] = self.fota_update.to_map()

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.hibernation_beta is not None:
            result['HibernationBeta'] = self.hibernation_beta

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.os is not None:
            result['Os'] = self.os

        if self.os_description is not None:
            result['OsDescription'] = self.os_description

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.real_desktop_id is not None:
            result['RealDesktopId'] = self.real_desktop_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_location is not None:
            result['RegionLocation'] = self.region_location

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.support_hibernation is not None:
            result['SupportHibernation'] = self.support_hibernation

        if self.user_custom_name is not None:
            result['UserCustomName'] = self.user_custom_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        self.clients = []
        if m.get('Clients') is not None:
            for k1 in m.get('Clients'):
                temp_model = main_models.DescribeGlobalDesktopsResponseBodyDesktopsClients()
                self.clients.append(temp_model.from_map(k1))

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        self.desktop_timers = []
        if m.get('DesktopTimers') is not None:
            for k1 in m.get('DesktopTimers'):
                temp_model = main_models.DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers()
                self.desktop_timers.append(temp_model.from_map(k1))

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeGlobalDesktopsResponseBodyDesktopsDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FotaUpdate') is not None:
            temp_model = main_models.DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate()
            self.fota_update = temp_model.from_map(m.get('FotaUpdate'))

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('HibernationBeta') is not None:
            self.hibernation_beta = m.get('HibernationBeta')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsDescription') is not None:
            self.os_description = m.get('OsDescription')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RealDesktopId') is not None:
            self.real_desktop_id = m.get('RealDesktopId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionLocation') is not None:
            self.region_location = m.get('RegionLocation')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DescribeGlobalDesktopsResponseBodyDesktopsSessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('SupportHibernation') is not None:
            self.support_hibernation = m.get('SupportHibernation')

        if m.get('UserCustomName') is not None:
            self.user_custom_name = m.get('UserCustomName')

        return self

class DescribeGlobalDesktopsResponseBodyDesktopsSessions(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        establishment_time: str = None,
    ):
        # End user information.
        self.end_user_id = end_user_id
        # The time when the session was created.
        self.establishment_time = establishment_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')

        return self

class DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate(DaraModel):
    def __init__(
        self,
        channel: str = None,
        current_app_version: str = None,
        force: bool = None,
        new_app_version: str = None,
        new_dcd_version: str = None,
        project: str = None,
        release_note: str = None,
        release_note_en: str = None,
        release_note_jp: str = None,
        size: str = None,
    ):
        # Subscription Channel
        self.channel = channel
        # The current version number of the cloud computer.
        self.current_app_version = current_app_version
        # Whether to force upgrade.
        self.force = force
        # The version number of the application after the update.
        self.new_app_version = new_app_version
        self.new_dcd_version = new_dcd_version
        # The name of the project.
        self.project = project
        # The description of the version that can be upgraded.
        self.release_note = release_note
        # The English release note for the new image version.
        self.release_note_en = release_note_en
        # The Japanese release note for the new image version.
        self.release_note_jp = release_note_jp
        # The size of the update package for the cloud computer image. Unit: MiB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version

        if self.force is not None:
            result['Force'] = self.force

        if self.new_app_version is not None:
            result['NewAppVersion'] = self.new_app_version

        if self.new_dcd_version is not None:
            result['NewDcdVersion'] = self.new_dcd_version

        if self.project is not None:
            result['Project'] = self.project

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en

        if self.release_note_jp is not None:
            result['ReleaseNoteJp'] = self.release_note_jp

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('NewAppVersion') is not None:
            self.new_app_version = m.get('NewAppVersion')

        if m.get('NewDcdVersion') is not None:
            self.new_dcd_version = m.get('NewDcdVersion')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')

        if m.get('ReleaseNoteJp') is not None:
            self.release_note_jp = m.get('ReleaseNoteJp')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribeGlobalDesktopsResponseBodyDesktopsDisks(DaraModel):
    def __init__(
        self,
        disk_id: str = None,
        disk_size: int = None,
        disk_type: str = None,
    ):
        # The disk ID.
        self.disk_id = disk_id
        # The disk size. Unit: GiB.
        self.disk_size = disk_size
        # The disk type.
        # 
        # Valid value:
        # 
        # *   SYSTEM: a system disk.
        # *   DATA: a data disk.
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        return self

class DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers(DaraModel):
    def __init__(
        self,
        allow_client_setting: bool = None,
        cron_expression: str = None,
        enforce: bool = None,
        execution_time: str = None,
        interval: int = None,
        operation_type: str = None,
        reset_type: str = None,
        timer_type: str = None,
    ):
        # Whether to allow clients to set policies.
        self.allow_client_setting = allow_client_setting
        # The CRON expression for the scheduled task.
        # 
        # For example, a `0 0 4 1/1 * ?` indicates that the operation is executed every day from 4:00 a.m. on the first day of each month.
        self.cron_expression = cron_expression
        # Indicates whether to forcibly execute the scheduled task. To `true` indicates that cloud computer and connection status detection are ignored, and scheduled tasks are forcibly executed.
        self.enforce = enforce
        # The task duration.
        self.execution_time = execution_time
        # The interval at which the monitoring data was queried. Unit: seconds.
        self.interval = interval
        # The type of the scheduled task.
        # 
        # Valid values:
        # 
        # *   HIBERNATE
        # *   SHUTDOWN
        self.operation_type = operation_type
        # For a reset task, you must set the reset type.
        # 
        # Valid values:
        # 
        # *   RESET_TYPE_SYSTEM: resets the system disk.
        # *   RESET_TYPE_USER_DISK: resets the data disk.
        # *   RESET_TYPE_BOTH: resets the system disk and data disk.
        self.reset_type = reset_type
        # The type of the scheduled task.
        # 
        # Valid values:
        # 
        # *   NoOperationDisconnect: scheduled disconnection upon inactivity.
        # *   NoConnectShutdown: connectionless shutdown.
        # *   TimerBoot: scheduled start.
        # *   TimerReset: scheduled reset.
        # *   NoOperationShutdown: scheduled shutdown upon inactivity.
        # *   TimerShutdown: Stops the cloud computers on schedule.
        # *   NoOperationReboot: scheduled restart upon inactivity.
        # *   TimerReboot: scheduled restart.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_client_setting is not None:
            result['AllowClientSetting'] = self.allow_client_setting

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.enforce is not None:
            result['Enforce'] = self.enforce

        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowClientSetting') is not None:
            self.allow_client_setting = m.get('AllowClientSetting')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')

        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

class DescribeGlobalDesktopsResponseBodyDesktopsClients(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # The client type.
        # 
        # Valid values:
        # 
        # *   html5: the web client.
        # *   android: the Android client.
        # *   linux: Linux client.
        # *   ios: the iOS client.
        # *   windows: the Windows client.
        # *   macos: the macOS client.
        self.client_type = client_type
        # The status of the client.
        # 
        # Valid values:
        # 
        # *   OFF: does not allow logon.
        # *   ON: allows logon.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

