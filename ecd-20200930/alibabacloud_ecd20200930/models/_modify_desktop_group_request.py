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
        # Specifies whether to enable automatic creation of cloud computers in a subscription shared cloud computer group. This parameter is required and takes effect only when `ChargeType` is set to `PrePaid`.
        self.allow_auto_setup = allow_auto_setup
        # The number of cloud computers to reserve in a pay-as-you-go shared cloud computer group. This parameter is required and takes effect only when `ChargeType` is set to `PostPaid`. Valid values:
        # 
        # - 0: No cloud computers are reserved.
        # 
        # - N: N cloud computers are reserved (1 ≤ N ≤ 100).
        # 
        # > If you do not reserve any cloud computers, the system must create and start one when an end user requests a connection. This process takes longer. Reserve a specific number of cloud computers to ensure a good user experience.
        self.allow_buffer_count = allow_buffer_count
        # The number of concurrent sessions that each cloud computer in a multi-session shared cloud computer group can support.
        # 
        # > This parameter is not yet available.
        self.bind_amount = bind_amount
        # - For a subscription shared cloud computer group: the number of cloud computers to purchase. Valid values: 0 to 200.
        # 
        # - For a pay-as-you-go shared cloud computer group: the minimum number of cloud computers to create in the pool. Default value: 1. Valid values: 0 to the value of `MaxDesktopsCount`.
        self.buy_desktops_count = buy_desktops_count
        # The type of the shared cloud computer group.
        # 
        # > This parameter is not yet available.
        self.classify = classify
        # The remarks.
        self.comments = comments
        # The maximum duration of a session. When the session duration reaches this value, the session is automatically disconnected. Unit: milliseconds. Valid values: 900000 (15 minutes) to 345600000 (4 days).
        self.connect_duration = connect_duration
        self.delete_duration = delete_duration
        # The ID of the shared cloud computer group.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # Shared cloud desktop name.
        self.desktop_group_name = desktop_group_name
        # Specifies whether to disable session management.
        self.disable_session_config = disable_session_config
        # The ID of the NAS file system used for user data roaming.
        # 
        # > This parameter is not yet available.
        self.file_system_id = file_system_id
        # The maximum idle time for a session. If there is no keyboard or mouse input within this time, the session disconnects. Unit: milliseconds. Valid values: 360000 (6 minutes) to 3600000 (60 minutes).
        # 
        # Thirty seconds before the session disconnects, the end user receives a message to save their data. The end user must save their data to prevent data loss.
        # 
        # > This parameter is applicable only to cloud computers with an image version of 1.0.2 or later.
        self.idle_disconnect_duration = idle_disconnect_duration
        # The image ID.
        self.image_id = image_id
        # The duration to keep a session active after it disconnects. Unit: milliseconds. Valid values range from 180000 (3 minutes) to 345600000 (4 days). A value of 0 means the session is always kept active.
        # 
        # When a session disconnects, either intentionally or unexpectedly, a timer begins. If the user fails to reconnect within this duration, the session is logged off, and any unsaved data is destroyed. If the user reconnects within this duration, they can resume the original session and access the data from before the disconnection.
        self.keep_duration = keep_duration
        # The load balancing policy for a multi-session shared cloud computer group that contains multiple cloud computers.
        # 
        # > This parameter is not yet available.
        self.load_policy = load_policy
        # The maximum number of cloud computers that a pay-as-you-go shared cloud computer group can contain. Valid values: 0 to 500.
        self.max_desktops_count = max_desktops_count
        # The maximum number of cloud computers that are automatically created in a subscription shared cloud computer group. This parameter is required and takes effect only when `ChargeType` is set to `PrePaid`. Default value: 1. Valid values: 0 to the value of `MaxDesktopsCount`.
        self.min_desktops_count = min_desktops_count
        # The cloud computer template ID.
        self.own_bundle_id = own_bundle_id
        # The policy ID.
        self.policy_group_id = policy_group_id
        # The list of policy group IDs.
        self.policy_group_ids = policy_group_ids
        # Specifies whether to enable user data roaming.
        # 
        # > This parameter is not yet available.
        self.profile_follow_switch = profile_follow_switch
        # The session usage threshold. This threshold is a condition for triggering auto scaling in a multi-session shared cloud computer group. The session usage is calculated using the following formula:
        # 
        # `Session usage = Number of active sessions / (Total number of cloud computers × Maximum number of sessions per cloud computer) × 100%`
        # 
        # When the session usage reaches this threshold, new cloud computers are created. If the session usage is below this threshold, idle cloud computers are deleted.
        # 
        # > This parameter is not yet available.
        self.ratio_threshold = ratio_threshold
        # The region ID. Call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to get a list of regions that WUYING Workspace supports.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The reset type for the cloud computers.
        self.reset_type = reset_type
        # The ID of the auto scaling policy group.
        # 
        # > This parameter is not yet available.
        self.scale_strategy_id = scale_strategy_id
        # The idle shutdown time. The cloud computer automatically shuts down when it is idle for this amount of time. If a user connects to a shutdown cloud computer, it automatically starts. Unit: milliseconds.
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

