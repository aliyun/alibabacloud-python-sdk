# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class CreateAppInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_name: str = None,
        app_package_type: str = None,
        app_policy_id: str = None,
        auth_mode: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        cluster_id: str = None,
        network: main_models.CreateAppInstanceGroupRequestNetwork = None,
        node_pool: main_models.CreateAppInstanceGroupRequestNodePool = None,
        period: int = None,
        period_unit: str = None,
        pre_open_app_id: str = None,
        product_type: str = None,
        promotion_id: str = None,
        runtime_policy: main_models.CreateAppInstanceGroupRequestRuntimePolicy = None,
        security_policy: main_models.CreateAppInstanceGroupRequestSecurityPolicy = None,
        session_timeout: int = None,
        storage_policy: main_models.CreateAppInstanceGroupRequestStoragePolicy = None,
        sub_pay_type: str = None,
        user_define_policy: main_models.CreateAppInstanceGroupRequestUserDefinePolicy = None,
        user_group_ids: List[str] = None,
        user_info: main_models.CreateAppInstanceGroupRequestUserInfo = None,
        users: List[str] = None,
        video_policy: main_models.CreateAppInstanceGroupRequestVideoPolicy = None,
    ):
        # The application image ID. You can obtain the ID from the **O&M** > **Custom Images** or **System Images** page in the [WUYING Cloud Application console](https://appstreaming.console.aliyun.com/).
        # 
        # This parameter is required.
        self.app_center_image_id = app_center_image_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # The package type.
        self.app_package_type = app_package_type
        # The policy ID.
        self.app_policy_id = app_policy_id
        # The authorization mode of the delivery group.
        self.auth_mode = auth_mode
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # The region ID of the delivery group. For information about supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The sales mode.
        # 
        # This parameter is required.
        self.charge_resource_mode = charge_resource_mode
        # The billing method.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The cluster ID.
        self.cluster_id = cluster_id
        # The network configuration.
        # 
        # > To use this parameter, submit a ticket.
        self.network = network
        # The node pool object.
        self.node_pool = node_pool
        # The subscription duration of the resource when `ChargeType` is set to `PrePaid`. This parameter is required. The unit is specified by `PeriodUnit`.
        # 
        # - If `PeriodUnit` is set to `Week`, valid values:
        # 
        #    - 1
        # 
        # - If `PeriodUnit` is set to `Month`, valid values:
        # 
        #    - 1
        #    - 2
        #    - 3
        #    - 6
        # 
        # - If `PeriodUnit` is set to `Year`, valid values:
        # 
        #    - 1
        #    - 2
        #    - 3
        # 
        # > If `ChargeType` is set to `PostPaid`, set this parameter to 1.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration when `ChargeType` is set to `PrePaid`.
        # 
        # > This parameter is case-sensitive. For example, `Week` is valid, but `week` is invalid.
        # If the request parameters do not match the valid combinations, such as `2 Week`, the API call succeeds but an error occurs during the order placement.
        # 
        # > If `ChargeType` is set to `PostPaid`, set this parameter to `Month`.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The pre-opened application ID.
        self.pre_open_app_id = pre_open_app_id
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The promotion ID. You can call the [GetResourcePrice](https://help.aliyun.com/document_detail/428503.html) operation to obtain the ID.
        self.promotion_id = promotion_id
        # The runtime policy.
        self.runtime_policy = runtime_policy
        # The security policy.
        self.security_policy = security_policy
        # The application recycling timeout period, in minutes. After an end user disconnects from a cloud application for a period of time, the cloud application process exits. This period is the application recycling timeout. Set this parameter to `-1` if you do not want the application to be recycled. Valid values: -1 and 3 to 300 (integer). Default value: `15`.
        # 
        # This parameter is required.
        self.session_timeout = session_timeout
        # The storage policy.
        self.storage_policy = storage_policy
        # The billing method subtype.
        self.sub_pay_type = sub_pay_type
        # The user-defined policy.
        self.user_define_policy = user_define_policy
        # The list of authorized user group IDs.
        self.user_group_ids = user_group_ids
        # The user information of the users to be added to the delivery group. This field is required if the `Users` parameter is specified.
        self.user_info = user_info
        # The list of usernames to be added to the delivery group as assigned users.
        self.users = users
        # The display policy.
        self.video_policy = video_policy

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.runtime_policy:
            self.runtime_policy.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()
        if self.user_define_policy:
            self.user_define_policy.validate()
        if self.user_info:
            self.user_info.validate()
        if self.video_policy:
            self.video_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.app_package_type is not None:
            result['AppPackageType'] = self.app_package_type

        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id

        if self.auth_mode is not None:
            result['AuthMode'] = self.auth_mode

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.runtime_policy is not None:
            result['RuntimePolicy'] = self.runtime_policy.to_map()

        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.user_define_policy is not None:
            result['UserDefinePolicy'] = self.user_define_policy.to_map()

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        if self.users is not None:
            result['Users'] = self.users

        if self.video_policy is not None:
            result['VideoPolicy'] = self.video_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppPackageType') is not None:
            self.app_package_type = m.get('AppPackageType')

        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')

        if m.get('AuthMode') is not None:
            self.auth_mode = m.get('AuthMode')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Network') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('NodePool') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestNodePool()
            self.node_pool = temp_model.from_map(m.get('NodePool'))

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RuntimePolicy') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestRuntimePolicy()
            self.runtime_policy = temp_model.from_map(m.get('RuntimePolicy'))

        if m.get('SecurityPolicy') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m.get('SecurityPolicy'))

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('StoragePolicy') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m.get('StoragePolicy'))

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('UserDefinePolicy') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestUserDefinePolicy()
            self.user_define_policy = temp_model.from_map(m.get('UserDefinePolicy'))

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserInfo') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        if m.get('Users') is not None:
            self.users = m.get('Users')

        if m.get('VideoPolicy') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestVideoPolicy()
            self.video_policy = temp_model.from_map(m.get('VideoPolicy'))

        return self

class CreateAppInstanceGroupRequestVideoPolicy(DaraModel):
    def __init__(
        self,
        frame_rate: int = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        streaming_mode: str = None,
        terminal_resolution_adaptive: bool = None,
        webrtc: bool = None,
    ):
        # The frame rate (FPS).
        self.frame_rate = frame_rate
        # The height of the resolution, in pixels.
        self.session_resolution_height = session_resolution_height
        # The width of the resolution, in pixels.
        self.session_resolution_width = session_resolution_width
        # The streaming mode. Used together with the `Webrtc` parameter to specify the protocol type.
        # 
        # - `Webrtc`=`true` and `StreamingMode`=`video`: WebRTC streaming.
        # - `Webrtc`=`false` and `StreamingMode`=`video`: video streaming.
        # - `Webrtc`=`false` and `StreamingMode`=`mix`: mixed streaming.
        self.streaming_mode = streaming_mode
        # Specifies whether to use adaptive resolution.
        # 
        # - `true`: The session resolution follows the terminal display area. In this case, `SessionResolutionWidth` and `SessionResolutionHeight` specify the maximum resolution values.
        # 
        # - `false`: The session resolution does not follow the terminal display area. In this case, the resolution is fixed to the values of `SessionResolutionWidth` and `SessionResolutionHeight`.
        self.terminal_resolution_adaptive = terminal_resolution_adaptive
        # Specifies whether to enable WebRTC. Used together with the `StreamingMode` parameter to specify the protocol type.
        # 
        # - `Webrtc`=`true` and `StreamingMode`=`video`: WebRTC streaming.
        # - `Webrtc`=`false` and `StreamingMode`=`video`: video streaming.
        # - `Webrtc`=`false` and `StreamingMode`=`mix`: mixed streaming.
        self.webrtc = webrtc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height

        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width

        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode

        if self.terminal_resolution_adaptive is not None:
            result['TerminalResolutionAdaptive'] = self.terminal_resolution_adaptive

        if self.webrtc is not None:
            result['Webrtc'] = self.webrtc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')

        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')

        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')

        if m.get('TerminalResolutionAdaptive') is not None:
            self.terminal_resolution_adaptive = m.get('TerminalResolutionAdaptive')

        if m.get('Webrtc') is not None:
            self.webrtc = m.get('Webrtc')

        return self

class CreateAppInstanceGroupRequestUserInfo(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The user account type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateAppInstanceGroupRequestUserDefinePolicy(DaraModel):
    def __init__(
        self,
        custom_config: str = None,
    ):
        # The custom policy content. The content must comply with the image version specifications. To use this parameter, submit a ticket to enable the whitelist.
        self.custom_config = custom_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_config is not None:
            result['CustomConfig'] = self.custom_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomConfig') is not None:
            self.custom_config = m.get('CustomConfig')

        return self

class CreateAppInstanceGroupRequestStoragePolicy(DaraModel):
    def __init__(
        self,
        storage_type_list: List[str] = None,
        user_profile: main_models.CreateAppInstanceGroupRequestStoragePolicyUserProfile = None,
    ):
        # The list of storage types.
        self.storage_type_list = storage_type_list
        # The user data roaming configuration.
        self.user_profile = user_profile

    def validate(self):
        if self.user_profile:
            self.user_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_type_list is not None:
            result['StorageTypeList'] = self.storage_type_list

        if self.user_profile is not None:
            result['UserProfile'] = self.user_profile.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageTypeList') is not None:
            self.storage_type_list = m.get('StorageTypeList')

        if m.get('UserProfile') is not None:
            temp_model = main_models.CreateAppInstanceGroupRequestStoragePolicyUserProfile()
            self.user_profile = temp_model.from_map(m.get('UserProfile'))

        return self

class CreateAppInstanceGroupRequestStoragePolicyUserProfile(DaraModel):
    def __init__(
        self,
        remote_storage_path: str = None,
        remote_storage_type: str = None,
        user_profile_switch: bool = None,
    ):
        # The remote storage path for user data roaming.
        # - If not specified, the default value is the delivery group ID.
        # - For cross-delivery-group (same VPC) user data roaming, set the same value for all delivery groups involved.
        self.remote_storage_path = remote_storage_path
        # The remote storage type used for user data roaming.
        self.remote_storage_type = remote_storage_type
        # Specifies whether to enable user data roaming.
        self.user_profile_switch = user_profile_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remote_storage_path is not None:
            result['RemoteStoragePath'] = self.remote_storage_path

        if self.remote_storage_type is not None:
            result['RemoteStorageType'] = self.remote_storage_type

        if self.user_profile_switch is not None:
            result['UserProfileSwitch'] = self.user_profile_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemoteStoragePath') is not None:
            self.remote_storage_path = m.get('RemoteStoragePath')

        if m.get('RemoteStorageType') is not None:
            self.remote_storage_type = m.get('RemoteStorageType')

        if m.get('UserProfileSwitch') is not None:
            self.user_profile_switch = m.get('UserProfileSwitch')

        return self

class CreateAppInstanceGroupRequestSecurityPolicy(DaraModel):
    def __init__(
        self,
        reset_after_unbind: bool = None,
        skip_user_auth_check: bool = None,
    ):
        # Specifies whether to reset after unbinding.
        self.reset_after_unbind = reset_after_unbind
        # Specifies whether to skip user authorization verification.
        self.skip_user_auth_check = skip_user_auth_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reset_after_unbind is not None:
            result['ResetAfterUnbind'] = self.reset_after_unbind

        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResetAfterUnbind') is not None:
            self.reset_after_unbind = m.get('ResetAfterUnbind')

        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')

        return self

class CreateAppInstanceGroupRequestRuntimePolicy(DaraModel):
    def __init__(
        self,
        debug_mode: str = None,
        per_session_per_app: bool = None,
        persistent_app_instance_schedule_mode: str = None,
        session_pre_open: str = None,
        session_type: str = None,
        session_user_generation_mode: str = None,
    ):
        # Specifies whether to enable debug mode. To call `GetDebugAppInstance` and `CreateImageFromAppInstanceGroup`, set this field to `ON`.
        self.debug_mode = debug_mode
        # Specifies whether to allow only one application per session.
        # - When enabled, opening multiple applications in the delivery group allocates a separate session for each application, consuming more sessions.
        self.per_session_per_app = per_session_per_app
        # The scheduling mode for persistent sessions.
        self.persistent_app_instance_schedule_mode = persistent_app_instance_schedule_mode
        # Specifies whether to enable session pre-opening.
        # - If not specified, the default value is true.
        self.session_pre_open = session_pre_open
        # The session type.
        self.session_type = session_type
        # The generation mode for session users.
        # - wyid: The session pre-open (SessionPreOpen) must be set to false.
        self.session_user_generation_mode = session_user_generation_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug_mode is not None:
            result['DebugMode'] = self.debug_mode

        if self.per_session_per_app is not None:
            result['PerSessionPerApp'] = self.per_session_per_app

        if self.persistent_app_instance_schedule_mode is not None:
            result['PersistentAppInstanceScheduleMode'] = self.persistent_app_instance_schedule_mode

        if self.session_pre_open is not None:
            result['SessionPreOpen'] = self.session_pre_open

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        if self.session_user_generation_mode is not None:
            result['SessionUserGenerationMode'] = self.session_user_generation_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugMode') is not None:
            self.debug_mode = m.get('DebugMode')

        if m.get('PerSessionPerApp') is not None:
            self.per_session_per_app = m.get('PerSessionPerApp')

        if m.get('PersistentAppInstanceScheduleMode') is not None:
            self.persistent_app_instance_schedule_mode = m.get('PersistentAppInstanceScheduleMode')

        if m.get('SessionPreOpen') is not None:
            self.session_pre_open = m.get('SessionPreOpen')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        if m.get('SessionUserGenerationMode') is not None:
            self.session_user_generation_mode = m.get('SessionUserGenerationMode')

        return self

class CreateAppInstanceGroupRequestNodePool(DaraModel):
    def __init__(
        self,
        max_idle_app_instance_amount: int = None,
        max_scaling_amount: int = None,
        node_amount: int = None,
        node_capacity: int = None,
        node_instance_type: str = None,
        recurrence_schedules: List[main_models.CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        # The maximum number of idle sessions. When this value is specified, auto scale-out is triggered only when the session usage exceeds `ScalingUsageThreshold` and the number of idle sessions in the current delivery group is less than `MaxIdleAppInstanceAmount`. Otherwise, the idle sessions are considered sufficient and no auto scale-out is performed. This parameter allows you to flexibly control elastic scaling behavior and reduce costs.
        self.max_idle_app_instance_amount = max_idle_app_instance_amount
        # The maximum number of resources that can be created during scale-out. This field is required when `StrategyType` is set to `NODE_SCALING_BY_USAGE` (elastic resources).
        self.max_scaling_amount = max_scaling_amount
        # The number of resources to purchase. Valid values: 1 to 100.
        # 
        # >- This parameter is required for subscription resources.
        # >- This parameter is required for pay-as-you-go resources when the scaling mode (`StrategyType`) is set to fixed quantity (`NODE_FIXED`) or auto scaling (`NODE_SCALING_BY_USAGE`).
        self.node_amount = node_amount
        # The number of concurrent sessions, which is the number of sessions that a single resource can handle simultaneously. Too many concurrent sessions may degrade the application experience. The valid value range varies by resource specification. You can call the ListNodeInstanceType operation to obtain the valid value range for each resource specification.
        self.node_capacity = node_capacity
        # The instance type ID of the resource to purchase. You can call the [ListNodeInstanceType](https://help.aliyun.com/document_detail/428502.html) operation to obtain the ID.
        self.node_instance_type = node_instance_type
        # The list of recurrence schedules. This field is required when `StrategyType` (scaling mode) is set to `NODE_SCALING_BY_SCHEDULE` (scheduled scaling).
        self.recurrence_schedules = recurrence_schedules
        # The maximum duration (in minutes) that a resource without active sessions is retained. When no sessions are connected to a resource, a countdown starts based on this value. The resource is released when the countdown ends. Valid values: 5 to 120. Default value: 5. The following exceptions apply:
        # 
        # - If releasing the resource would trigger auto scale-out again, the scale-down is not performed to avoid repeated scaling operations.
        # - If auto scale-out is triggered due to increased sessions during this period, the resource is not released as originally planned, and the countdown restarts.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The number of resources to create per scale-out operation. Valid values: 1 to 10. This field is required when `StrategyType` is set to `NODE_SCALING_BY_USAGE` (elastic resources).
        self.scaling_step = scaling_step
        # The upper threshold of session usage (%). Auto scale-out is triggered when the session usage exceeds this threshold. The session usage is calculated as follows: `Session usage = Current sessions ÷ (Total resources × Concurrent sessions per resource) × 100%`. This field is required when `StrategyType` is set to `NODE_SCALING_BY_USAGE` (elastic resources). Valid values: 0 to 100. Default value: 85.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The date when the policy expires. Format: yyyy-MM-dd. The interval between the expiration date and the effective date must be between 7 days and 1 year, inclusive. This field is required when `StrategyType` (scaling mode) is set to `NODE_SCALING_BY_SCHEDULE` (scheduled scaling).
        self.strategy_disable_date = strategy_disable_date
        # The date when the policy takes effect. Format: yyyy-MM-dd. The date must be equal to or later than the current date. This field is required when `StrategyType` (scaling mode) is set to `NODE_SCALING_BY_SCHEDULE` (scheduled scaling).
        self.strategy_enable_date = strategy_enable_date
        # The scaling mode.
        # 
        # > 
        # >- `NODE_FIXED` (fixed quantity): applicable to subscription and pay-as-you-go resources.
        # >- `NODE_SCALING_BY_USAGE` (auto scaling): applicable to subscription and pay-as-you-go resources.
        # >- `NODE_SCALING_BY_SCHEDULE` (scheduled scaling): applicable only to pay-as-you-go resources.
        self.strategy_type = strategy_type
        # Specifies whether to enable the resource prefetch policy. This field is required when `StrategyType` (scaling mode) is set to `NODE_SCALING_BY_SCHEDULE` (scheduled scaling).
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for v1 in self.recurrence_schedules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_idle_app_instance_amount is not None:
            result['MaxIdleAppInstanceAmount'] = self.max_idle_app_instance_amount

        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount

        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount

        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity

        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type

        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k1 in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k1.to_map() if k1 else None)

        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes

        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step

        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold

        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date

        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxIdleAppInstanceAmount') is not None:
            self.max_idle_app_instance_amount = m.get('MaxIdleAppInstanceAmount')

        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')

        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')

        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')

        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')

        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k1 in m.get('RecurrenceSchedules'):
                temp_model = main_models.CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k1))

        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')

        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')

        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')

        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')

        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')

        return self

class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules(DaraModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[main_models.CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        # The type of the recurrence schedule. You must specify both `RecurrenceType` and `RecurrenceValues`.
        self.recurrence_type = recurrence_type
        # The list of recurrence values.
        self.recurrence_values = recurrence_values
        # The list of time periods for the recurrence schedule. Requirements for time period settings:
        # 
        # - You can add up to 3 time periods.
        # - Time periods must not overlap.
        # - The interval between time periods must be at least 5 minutes.
        # - Each time period must be at least 15 minutes long.
        # - All time periods combined must not span across days.
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for v1 in self.timer_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values

        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k1 in self.timer_periods:
                result['TimerPeriods'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')

        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k1 in m.get('TimerPeriods'):
                temp_model = main_models.CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k1))

        return self

class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods(DaraModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The resource count.
        self.amount = amount
        # The end time. Format: HH:mm.
        self.end_time = end_time
        # The start time. Format: HH:mm.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class CreateAppInstanceGroupRequestNetwork(DaraModel):
    def __init__(
        self,
        domain_rules: List[main_models.CreateAppInstanceGroupRequestNetworkDomainRules] = None,
        ip_expire_minutes: int = None,
        office_site_id: str = None,
        routes: List[main_models.CreateAppInstanceGroupRequestNetworkRoutes] = None,
        strategy_type: str = None,
        v_switch_ids: List[str] = None,
    ):
        # The domain name rule configurations.
        self.domain_rules = domain_rules
        # The duration (in minutes) after which the public IP address is refreshed upon the next logon. Minimum value: 60.
        self.ip_expire_minutes = ip_expire_minutes
        # The office network ID.
        self.office_site_id = office_site_id
        # The route configurations. This parameter can be configured only when the network policy type (`StrategyType`) is set to mixed mode (`Mixed`).
        self.routes = routes
        # The network policy type.
        self.strategy_type = strategy_type
        # The list of vSwitch IDs.
        # 
        # - Valid only for custom office networks.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.domain_rules:
            for v1 in self.domain_rules:
                 if v1:
                    v1.validate()
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainRules'] = []
        if self.domain_rules is not None:
            for k1 in self.domain_rules:
                result['DomainRules'].append(k1.to_map() if k1 else None)

        if self.ip_expire_minutes is not None:
            result['IpExpireMinutes'] = self.ip_expire_minutes

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        result['Routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['Routes'].append(k1.to_map() if k1 else None)

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_rules = []
        if m.get('DomainRules') is not None:
            for k1 in m.get('DomainRules'):
                temp_model = main_models.CreateAppInstanceGroupRequestNetworkDomainRules()
                self.domain_rules.append(temp_model.from_map(k1))

        if m.get('IpExpireMinutes') is not None:
            self.ip_expire_minutes = m.get('IpExpireMinutes')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        self.routes = []
        if m.get('Routes') is not None:
            for k1 in m.get('Routes'):
                temp_model = main_models.CreateAppInstanceGroupRequestNetworkRoutes()
                self.routes.append(temp_model.from_map(k1))

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class CreateAppInstanceGroupRequestNetworkRoutes(DaraModel):
    def __init__(
        self,
        destination: str = None,
        mode: str = None,
    ):
        # The access destination. CIDR format.
        self.destination = destination
        # The network egress mode.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination is not None:
            result['Destination'] = self.destination

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class CreateAppInstanceGroupRequestNetworkDomainRules(DaraModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The policy value.
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

