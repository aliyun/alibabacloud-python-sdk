# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDesktopGroupRequest(DaraModel):
    def __init__(
        self,
        allow_auto_setup: int = None,
        allow_buffer_count: int = None,
        bind_amount: int = None,
        buy_desktops_count: int = None,
        classify: str = None,
        comments: str = None,
        connect_duration: int = None,
        delete_duration: int = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        disable_session_config: bool = None,
        file_system_id: str = None,
        idle_disconnect_duration: int = None,
        image_id: str = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_desktops_count: int = None,
        min_desktops_count: int = None,
        own_bundle_id: str = None,
        policy_group_id: str = None,
        policy_group_ids: List[str] = None,
        profile_follow_switch: bool = None,
        ratio_threshold: float = None,
        region_id: str = None,
        reset_type: int = None,
        scale_strategy_id: str = None,
        stop_duration: int = None,
    ):
        # Specifies whether to enable auto-creation of cloud computers for the subscription cloud computer share. You must specify this parameter when `ChargeType` is set to `PrePaid`.
        # 
        # Valid values:
        # 
        # *   0: disable auto-creation of cloud computers.
        # *   1: enables auto-creation of cloud computers.
        self.allow_auto_setup = allow_auto_setup
        # The maximum number of standby cloud computers that can be reserved within the pay-as-you-go cloud computer share. You must specify this property only when `ChargeType` is set to `PostPaid`. Valid values:
        # 
        # *   0: does not reserve any cloud computer.
        # *   N: reserves N cloud computers (1≤ N ≤ 100).
        # 
        # >  Setting this parameter to 0 means no cloud computers will be reserved within the cloud computer share. In this case, the system must create, start, and assign cloud computers to end users upon request, which can be time-consuming. To improve user experience, we recommend that you reserve a specific number of cloud computers.
        self.allow_buffer_count = allow_buffer_count
        # The number of concurrent sessions allowed for each cloud computer within the multi-session many-to-many share.
        # 
        # >  This parameter is not publicly available.
        self.bind_amount = bind_amount
        # *   For subscription cloud computer shares, this parameter specifies the number of purchased cloud computers. Valid values: 0 to 200.
        # *   For pay-as-you-go cloud computer shares, this parameter specifies the minimum number of cloud computers created in the initial batch. Default value: 1. Valid values: 0 to `MaxDesktopsCount`.
        self.buy_desktops_count = buy_desktops_count
        # The type of the cloud computer share.
        # 
        # >  This parameter is not publicly available.
        # 
        # Valid values:
        # 
        # *   teacher: teacher-oriented.
        # *   student: student-oriented.
        self.classify = classify
        # The remarks.
        self.comments = comments
        # The maximum period of time during which the session is connected. When the specified maximum period of time is reached, the session is automatically disconnected. Unit: milliseconds. Valid values: 900000 to 345600000. That is, the session can be connected for 15 to 5,760 minutes (4 days).
        self.connect_duration = connect_duration
        self.delete_duration = delete_duration
        # The ID of the cloud computer share.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # The name of the cloud computer share.
        self.desktop_group_name = desktop_group_name
        # Specifies whether to disable session management.
        self.disable_session_config = disable_session_config
        # The ID of the File Storage NAS (NAS) file system for the user data roaming feature.
        # 
        # >  This parameter is unavailable.
        self.file_system_id = file_system_id
        # After an end user connects to a cloud computer, the session is established. If the system does not detect inputs from the keyboard or mouse within the specified period of time, the session is closed. Unit: milliseconds. Valid values: 360000 to 3600000 (6 minutes to 60 minutes)
        # 
        # End users can receive a prompt to save data before sessions are disconnected. The system sends the prompt 30 seconds before the specified period of time is reached. To prevent data loss, end users must save the data of the sessions.
        # 
        # >  This parameter is suitable only for cloud computers whose image version is v1.0.2 or later.
        self.idle_disconnect_duration = idle_disconnect_duration
        # The IDs of the images.
        self.image_id = image_id
        # The retention period of a session after it is disconnected. Unit: milliseconds. Valid values: 180000 to 345600000. That is, the session can be retained for 3 to 5,760 minutes (4 days) after it is disconnected. If you set this parameter to 0, the session is permanently retained after it is disconnected.
        # 
        # When a session is disconnected, take note of the following situations: If an end user does not resume the session within the specified duration, the session is closed and all unsaved data is cleared. If the end user resumes the session within the specified duration, the end user can continue to access data of the session.
        self.keep_duration = keep_duration
        # The load balancing policy for the multi-session many-to-many share.
        # 
        # >  This parameter is not publicly available.
        # 
        # Valid values:
        # 
        # *   0: depth first.
        # *   1: breadth first.
        self.load_policy = load_policy
        # The maximum number of cloud computers allowed in the pay-as-you-go cloud computer share. Valid values: 0 to 500.
        self.max_desktops_count = max_desktops_count
        # The maximum number of auto-created cloud computers allowed in the subscription cloud computer share. You must specify this parameter when `ChargeType` is set to `PrePaid`. Default value: 1. Valid values: 0 to `MaxDesktopsCount`.
        self.min_desktops_count = min_desktops_count
        # The ID of the cloud computer template.
        self.own_bundle_id = own_bundle_id
        # The ID of the security policy.
        self.policy_group_id = policy_group_id
        # The IDs of policy groups.
        self.policy_group_ids = policy_group_ids
        # Specifies whether to enable user data roaming.
        # 
        # >  This parameter is unavailable.
        self.profile_follow_switch = profile_follow_switch
        # The threshold for the ratio of connected sessions, which triggers automatic scaling of cloud computers within the multi-session many-to-many share. To calculate the ratio of connected sessions, use the following formula:
        # 
        # `Ratio of connected sessions = Number of connected sessions/(Total number of cloud computers × Maximum number of sessions allowed for each cloud computer) × 100%`
        # 
        # If the session ratio exceeds the threshold, new cloud computers are provisioned. If it falls below the threshold, additional cloud computers are removed.
        # 
        # >  This parameter is not publicly available.
        self.ratio_threshold = ratio_threshold
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The disk reset type of cloud computers.
        # 
        # Valid values:
        # 
        # *   0: does not reset disks.
        # 
        # *   1: resets only the system disks.
        # 
        # *   2: resets only the user disks.
        # 
        # *   3: resets the system disks and user disks.
        self.reset_type = reset_type
        # The ID of the scaling policy group.
        # 
        # >  This parameter is unavailable.
        self.scale_strategy_id = scale_strategy_id
        # The period of time before the idle cloud computer enters the Stopped state. When the specified period of time is reached, the cloud computer is automatically stopped. If an end user connects to the stopped cloud computer, the cloud computer automatically starts. Unit: milliseconds.
        self.stop_duration = stop_duration

    def validate(self):
        pass

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

        if self.classify is not None:
            result['Classify'] = self.classify

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration

        if self.delete_duration is not None:
            result['DeleteDuration'] = self.delete_duration

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.disable_session_config is not None:
            result['DisableSessionConfig'] = self.disable_session_config

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

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

        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count

        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids

        if self.profile_follow_switch is not None:
            result['ProfileFollowSwitch'] = self.profile_follow_switch

        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id

        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration

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

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')

        if m.get('DeleteDuration') is not None:
            self.delete_duration = m.get('DeleteDuration')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('DisableSessionConfig') is not None:
            self.disable_session_config = m.get('DisableSessionConfig')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

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

        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')

        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')

        if m.get('ProfileFollowSwitch') is not None:
            self.profile_follow_switch = m.get('ProfileFollowSwitch')

        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')

        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')

        return self

