# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class GetDesktopGroupDetailResponseBody(DaraModel):
    def __init__(
        self,
        desktops: main_models.GetDesktopGroupDetailResponseBodyDesktops = None,
        request_id: str = None,
    ):
        # The information about shared cloud computers.
        self.desktops = desktops
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.desktops:
            self.desktops.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktops is not None:
            result['Desktops'] = self.desktops.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desktops') is not None:
            temp_model = main_models.GetDesktopGroupDetailResponseBodyDesktops()
            self.desktops = temp_model.from_map(m.get('Desktops'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDesktopGroupDetailResponseBodyDesktops(DaraModel):
    def __init__(
        self,
        allow_auto_setup: int = None,
        allow_buffer_count: int = None,
        bind_amount: int = None,
        buy_desktops_count: int = None,
        comments: str = None,
        connect_duration: int = None,
        cpu: int = None,
        creation_time: str = None,
        creator: str = None,
        data_disk_category: str = None,
        data_disk_size: str = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        directory_id: str = None,
        directory_type: str = None,
        env_id: str = None,
        env_type: str = None,
        expired_time: str = None,
        expired_times: List[str] = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        idle_disconnect_duration: int = None,
        image_id: str = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_desktops_count: int = None,
        memory: int = None,
        min_desktops_count: int = None,
        nas_file_system_id: str = None,
        nas_file_system_name: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        os_type: str = None,
        own_bundle_id: str = None,
        own_bundle_name: str = None,
        own_type: int = None,
        pay_type: str = None,
        policy_group_id: str = None,
        policy_group_ids: List[str] = None,
        policy_group_name: str = None,
        policy_group_names: List[str] = None,
        profile_follow_switch: bool = None,
        protocol_type: str = None,
        ratio_threshold: float = None,
        res_type: int = None,
        reset_type: int = None,
        scale_timer_infos: List[main_models.GetDesktopGroupDetailResponseBodyDesktopsScaleTimerInfos] = None,
        status: int = None,
        stop_duration: int = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        timer_infos: List[main_models.GetDesktopGroupDetailResponseBodyDesktopsTimerInfos] = None,
        timing_strategy_info: str = None,
        version: int = None,
    ):
        # Indicates whether automatic creation of cloud computers is allowed for subscription shared cloud computers.
        self.allow_auto_setup = allow_auto_setup
        # This parameter applies only to pay-as-you-go shared cloud computers. It specifies the number of cloud computers that are always reserved in the powered-on and idle state, ready for connections. Valid values:
        self.allow_buffer_count = allow_buffer_count
        # The number of concurrent sessions allowed per cloud computer in multi-session shared cloud computers with multiple instances.
        self.bind_amount = bind_amount
        # The initial number of cloud computers purchased. This parameter applies only to subscription shared cloud computers. Valid values: 0 to 200.
        self.buy_desktops_count = buy_desktops_count
        # The remarks.
        self.comments = comments
        # The maximum duration that a session can remain in the connected state. The session is automatically disconnected when this duration is reached. Unit: milliseconds.
        self.connect_duration = connect_duration
        # The number of vCPUs.
        self.cpu = cpu
        # The creation time. The time is in the ISO 8601 standard in UTC.
        self.creation_time = creation_time
        # The Alibaba Cloud account ID of the creator.
        self.creator = creator
        # The user disk type.
        self.data_disk_category = data_disk_category
        # The user disk capacity. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The ID of the shared cloud computer.
        self.desktop_group_id = desktop_group_id
        # The name of the shared cloud computer to query.
        self.desktop_group_name = desktop_group_name
        # The directory ID (office network ID).
        self.directory_id = directory_id
        # The directory type.
        self.directory_type = directory_type
        # The environment ID. This parameter is not publicly available.
        self.env_id = env_id
        # The environment type. This parameter is not publicly available.
        self.env_type = env_type
        # The expiration time of the subscription shared cloud computers. The time follows the ISO 8601 standard in UTC.
        self.expired_time = expired_time
        # The list of expiration times.
        self.expired_times = expired_times
        # The number of GPU cores.
        self.gpu_count = gpu_count
        # The GPU specifications.
        self.gpu_spec = gpu_spec
        # The maximum idle duration after a user session is connected. If no keyboard or mouse operation is performed within this duration, the session is disconnected. Unit: milliseconds.
        self.idle_disconnect_duration = idle_disconnect_duration
        # The image ID.
        self.image_id = image_id
        # The duration for which a session is retained after disconnection. Unit: milliseconds. Valid values: 180000 (3 minutes) to 345600000 (4 days). A value of 0 indicates that the session is retained indefinitely.
        # 
        # When a session is disconnected because the user actively disconnects or because of unexpected factors, the retention period starts from the moment of disconnection. If the user does not reconnect to the session within the retention period, the session is logged off and all unsaved data is destroyed. If the user successfully reconnects within the retention period, the user can still access the original session and the data that existed before the disconnection.
        self.keep_duration = keep_duration
        # The load balancing policy for multi-session shared cloud computers with multiple instances.
        self.load_policy = load_policy
        # - For pay-as-you-go shared cloud computers, this parameter specifies the maximum number of cloud computers that can be created.
        self.max_desktops_count = max_desktops_count
        # The memory size. Unit: MiB.
        self.memory = memory
        # - For pay-as-you-go shared cloud computers, this parameter indicates the minimum number of cloud computers to create.
        # - For subscription shared cloud computers, this parameter is equivalent to BuyDesktopsCount, indicating the number of cloud computers initially purchased.
        self.min_desktops_count = min_desktops_count
        # The ID of the NAS file system used for user data roaming.
        self.nas_file_system_id = nas_file_system_id
        # The name of the NAS file system used for user data roaming.
        self.nas_file_system_name = nas_file_system_name
        # The office network ID.
        self.office_site_id = office_site_id
        # The name of the office network to which the shared cloud computer belongs.
        self.office_site_name = office_site_name
        # The account system type of the office network.
        self.office_site_type = office_site_type
        # The operating system type of the cloud computers.
        self.os_type = os_type
        # The cloud computer template ID.
        self.own_bundle_id = own_bundle_id
        # The cloud computer template name.
        self.own_bundle_name = own_bundle_name
        # The type of the shared cloud computer.
        self.own_type = own_type
        # The billing method.
        self.pay_type = pay_type
        # The ID of the policy associated with the shared cloud computer.
        self.policy_group_id = policy_group_id
        # The list of policy IDs associated with the shared cloud computers.
        self.policy_group_ids = policy_group_ids
        # The Policy Name associated with the shared cloud computer.
        self.policy_group_name = policy_group_name
        # The list of policy names associated with the shared cloud computers.
        self.policy_group_names = policy_group_names
        # Indicates whether user data roaming is enabled.
        self.profile_follow_switch = profile_follow_switch
        # The protocol type.
        self.protocol_type = protocol_type
        # The session occupancy threshold, used as the auto scaling trigger condition for multi-session shared cloud computers. The session occupancy is calculated by using the following formula:
        # 
        # ```Session occupancy = Number of bound sessions / (Total number of cloud computer resources × Maximum number of sessions supported per cloud computer) × 100%```
        # 
        # When the session occupancy reaches this threshold, new cloud computers are created. When the session occupancy is below this threshold, excess cloud computers are deleted.
        self.ratio_threshold = ratio_threshold
        # The resource type. Currently, only ECS is supported.
        self.res_type = res_type
        # The reset type of the cloud computer.
        self.reset_type = reset_type
        # The scheduled task information.
        self.scale_timer_infos = scale_timer_infos
        # The status of the shared cloud computer.
        self.status = status
        # The idle shutdown duration. When the cloud computer has been idle for this duration, it is automatically shut down. If a user connects after shutdown, the cloud computer is automatically started. Unit: milliseconds.
        self.stop_duration = stop_duration
        # The system cloud disk type.
        self.system_disk_category = system_disk_category
        # The system cloud disk capacity. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The list of scheduled times.
        self.timer_infos = timer_infos
        # The scheduled application information.
        self.timing_strategy_info = timing_strategy_info
        # The version number of the shared cloud computer.
        self.version = version

    def validate(self):
        if self.scale_timer_infos:
            for v1 in self.scale_timer_infos:
                 if v1:
                    v1.validate()
        if self.timer_infos:
            for v1 in self.timer_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup

        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count

        if self.bind_amount is not None:
            result['BindAmount'] = self.bind_amount

        if self.buy_desktops_count is not None:
            result['BuyDesktopsCount'] = self.buy_desktops_count

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        if self.env_id is not None:
            result['EnvId'] = self.env_id

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.expired_times is not None:
            result['ExpiredTimes'] = self.expired_times

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration

        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy

        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count

        if self.nas_file_system_id is not None:
            result['NasFileSystemID'] = self.nas_file_system_id

        if self.nas_file_system_name is not None:
            result['NasFileSystemName'] = self.nas_file_system_name

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id

        if self.own_bundle_name is not None:
            result['OwnBundleName'] = self.own_bundle_name

        if self.own_type is not None:
            result['OwnType'] = self.own_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids

        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name

        if self.policy_group_names is not None:
            result['PolicyGroupNames'] = self.policy_group_names

        if self.profile_follow_switch is not None:
            result['ProfileFollowSwitch'] = self.profile_follow_switch

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold

        if self.res_type is not None:
            result['ResType'] = self.res_type

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        result['ScaleTimerInfos'] = []
        if self.scale_timer_infos is not None:
            for k1 in self.scale_timer_infos:
                result['ScaleTimerInfos'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['TimerInfos'] = []
        if self.timer_infos is not None:
            for k1 in self.timer_infos:
                result['TimerInfos'].append(k1.to_map() if k1 else None)

        if self.timing_strategy_info is not None:
            result['TimingStrategyInfo'] = self.timing_strategy_info

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')

        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')

        if m.get('BindAmount') is not None:
            self.bind_amount = m.get('BindAmount')

        if m.get('BuyDesktopsCount') is not None:
            self.buy_desktops_count = m.get('BuyDesktopsCount')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ExpiredTimes') is not None:
            self.expired_times = m.get('ExpiredTimes')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')

        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')

        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')

        if m.get('NasFileSystemID') is not None:
            self.nas_file_system_id = m.get('NasFileSystemID')

        if m.get('NasFileSystemName') is not None:
            self.nas_file_system_name = m.get('NasFileSystemName')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')

        if m.get('OwnBundleName') is not None:
            self.own_bundle_name = m.get('OwnBundleName')

        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')

        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')

        if m.get('PolicyGroupNames') is not None:
            self.policy_group_names = m.get('PolicyGroupNames')

        if m.get('ProfileFollowSwitch') is not None:
            self.profile_follow_switch = m.get('ProfileFollowSwitch')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')

        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        self.scale_timer_infos = []
        if m.get('ScaleTimerInfos') is not None:
            for k1 in m.get('ScaleTimerInfos'):
                temp_model = main_models.GetDesktopGroupDetailResponseBodyDesktopsScaleTimerInfos()
                self.scale_timer_infos.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.timer_infos = []
        if m.get('TimerInfos') is not None:
            for k1 in m.get('TimerInfos'):
                temp_model = main_models.GetDesktopGroupDetailResponseBodyDesktopsTimerInfos()
                self.timer_infos.append(temp_model.from_map(k1))

        if m.get('TimingStrategyInfo') is not None:
            self.timing_strategy_info = m.get('TimingStrategyInfo')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetDesktopGroupDetailResponseBodyDesktopsTimerInfos(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        forced: bool = None,
        status: int = None,
        timer_type: int = None,
    ):
        # The cron expression.
        self.cron_expression = cron_expression
        # Indicates whether the scheduled task is forcibly executed.
        self.forced = forced
        # The status.
        self.status = status
        # The type of the scheduled task.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.forced is not None:
            result['Forced'] = self.forced

        if self.status is not None:
            result['Status'] = self.status

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Forced') is not None:
            self.forced = m.get('Forced')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

class GetDesktopGroupDetailResponseBodyDesktopsScaleTimerInfos(DaraModel):
    def __init__(
        self,
        buy_res_amount: int = None,
        cron: str = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_res_amount: int = None,
        min_res_amount: int = None,
        ratio_threshold: float = None,
        type: str = None,
    ):
        # The number of cloud computers to purchase, which is one of the scaling policy parameters. Valid values: 0 to 200.
        self.buy_res_amount = buy_res_amount
        # The cron expression of the scheduled task.
        self.cron = cron
        # The duration for which a session is retained after disconnection. Unit: milliseconds. Valid values: 180000 (3 minutes) to 345600000 (4 days). A value of 0 indicates that the session is always retained.
        # 
        # When a session is disconnected because the user actively disconnects or because of other unexpected factors, the retention period starts from the moment of disconnection. If the user does not reconnect to the session within the retention period, the session is logged off and all unsaved data is destroyed. If the user successfully reconnects within the retention period, the user can still access the original session and the data that existed before the disconnection.
        self.keep_duration = keep_duration
        # The load balancing policy for multi-session shared cloud computers with multiple instances.
        self.load_policy = load_policy
        # The maximum number of cloud computers, which is one of the scaling policy parameters. Valid values: 0 to 200.
        self.max_res_amount = max_res_amount
        # The minimum number of cloud computers, which is one of the scaling policy parameters. Valid values: 0 to 200.
        self.min_res_amount = min_res_amount
        # The session occupancy threshold used as the trigger condition for auto scaling of multi-session shared cloud computers. The session occupancy is calculated by using the following formula:
        # 
        # ```Session occupancy = Number of bound sessions / (Total number of cloud computer resources × Maximum number of sessions supported per cloud computer) × 100%```
        # 
        # When the session occupancy reaches this threshold, new cloud computers are created. When the session occupancy is below this threshold, excess cloud computers are deleted.
        self.ratio_threshold = ratio_threshold
        # The type of the scheduled task.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_res_amount is not None:
            result['BuyResAmount'] = self.buy_res_amount

        if self.cron is not None:
            result['Cron'] = self.cron

        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration

        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy

        if self.max_res_amount is not None:
            result['MaxResAmount'] = self.max_res_amount

        if self.min_res_amount is not None:
            result['MinResAmount'] = self.min_res_amount

        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResAmount') is not None:
            self.buy_res_amount = m.get('BuyResAmount')

        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')

        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')

        if m.get('MaxResAmount') is not None:
            self.max_res_amount = m.get('MaxResAmount')

        if m.get('MinResAmount') is not None:
            self.min_res_amount = m.get('MinResAmount')

        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

