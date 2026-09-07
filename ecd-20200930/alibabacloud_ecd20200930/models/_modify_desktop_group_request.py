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
        # Specifies whether to allow automatic creation of cloud computers in the subscription shared cloud computer. This parameter takes effect only when the `ChargeType` parameter is set to `PrePaid`, and is required in this case.
        self.allow_auto_setup = allow_auto_setup
        # The number of cloud computers that can be reserved in a pay-as-you-go shared cloud computer. This parameter takes effect only when the `ChargeType` parameter is set to `PostPaid`, and is required in this case. Valid values: 
        # - 0: no reservation
        # - N: reserve N cloud computers (1 ≤ N ≤ 100)
        # 
        # > If no available cloud computers are reserved, the system must create and start a cloud computer before assigning it to the user when an end user initiates a connection request. This process takes a relatively long time. Reserve a certain number of cloud computers as needed to ensure a good experience for end users.
        self.allow_buffer_count = allow_buffer_count
        # The number of concurrent sessions allowed on each cloud computer in a multi-session shared cloud computer with multiple cloud computers.
        # 
        # > This parameter is not yet available.
        self.bind_amount = bind_amount
        # - For subscription shared cloud computers: the number of cloud computers to purchase. Valid values: 0 to 200.
        # - For pay-as-you-go shared cloud computers: the minimum number of cloud computers to create in the pool. Default value: 1. Valid values: 0 to the value of `MaxDesktopsCount`.
        self.buy_desktops_count = buy_desktops_count
        # The type of the shared cloud computer.
        # 
        # > This parameter is not yet available.
        self.classify = classify
        # The remarks.
        self.comments = comments
        # The maximum duration that a session can remain in the connected state. The session is automatically disconnected when this duration is reached. Unit: milliseconds. Valid values: 900000 (15 minutes) to 345600000 (4 days).
        self.connect_duration = connect_duration
        # The retention period before cloud computers in the cloud computer pool are automatically deleted.
        self.delete_duration = delete_duration
        # The shared cloud computer ID.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # The shared cloud computer name.
        self.desktop_group_name = desktop_group_name
        # Specifies whether to disable session management.
        self.disable_session_config = disable_session_config
        # The NAS file system ID used by the user data roaming feature.
        # 
        # > This parameter is not yet available.
        self.file_system_id = file_system_id
        # The maximum idle duration after a user session is connected. If no keyboard or mouse activity occurs within this duration, the session is disconnected. Unit: milliseconds. Valid values: 360000 (6 minutes) to 3600000 (60 minutes).
        # 
        # 30 seconds before this duration is reached, the end user in the session receives a prompt to save document data. The end user must save document data promptly to avoid data loss.
        # 
        # > This parameter applies only to cloud computers with an image version of 1.0.2 or later.
        self.idle_disconnect_duration = idle_disconnect_duration
        # The image ID.
        self.image_id = image_id
        # The retention period after a session is disconnected. Unit: milliseconds. Valid values: 180000 (3 minutes) to 345600000 (4 days). A value of 0 indicates that the session is always retained.
        # 
        # When a session is disconnected because the user actively disconnects or because of other unexpected factors, the retention period starts from the time of disconnection. If the user does not reconnect to the session within the retention period, the session is logged off and all unsaved data is destroyed. If the user successfully reconnects within the retention period, the user can access the original session and the data that existed before the disconnection.
        self.keep_duration = keep_duration
        # The load balancing policy for multi-session shared cloud computers with multiple cloud computers.
        # 
        # > This parameter is not yet available.
        self.load_policy = load_policy
        # The maximum number of cloud computers that a pay-as-you-go shared cloud computer can contain. Valid values: 0 to 500.
        self.max_desktops_count = max_desktops_count
        # The maximum number of cloud computers that can be subject to automatic creation in a subscription shared cloud computer. This parameter takes effect only when the `ChargeType` parameter is set to `PrePaid`, and is required in this case. Default value: 1. Valid values: 0 to the value of `MaxDesktopsCount`.
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
        # The session occupancy threshold, which is used as the auto scaling trigger condition for multi-session shared cloud computers with multiple cloud computers. The session occupancy is calculated by using the following formula:
        # 
        # ```Session occupancy = Number of attached sessions / (Total number of cloud computer resources × Maximum number of sessions supported per cloud computer) × 100%```
        # 
        # When the session occupancy reaches this threshold, new cloud computers are created. When the session occupancy is below this threshold, excess cloud computers are deleted.
        # 
        # > This parameter is not yet available.
        self.ratio_threshold = ratio_threshold
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The cloud computer reset type.
        self.reset_type = reset_type
        # The scaling policy group ID.
        # 
        # > This parameter is not yet available.
        self.scale_strategy_id = scale_strategy_id
        # The idle shutdown duration. When the idle duration of a cloud computer reaches this value, the cloud computer is automatically shut down. If a user connects after the shutdown, the cloud computer is automatically started. Unit: milliseconds.
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

