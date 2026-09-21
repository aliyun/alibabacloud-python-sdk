# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetBrowserInstanceGroupResponseBody(DaraModel):
    def __init__(
        self,
        browser_instance_group_model: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModel = None,
        request_id: str = None,
    ):
        # The details of the browser group.
        self.browser_instance_group_model = browser_instance_group_model
        # The request ID, which is used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.browser_instance_group_model:
            self.browser_instance_group_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_instance_group_model is not None:
            result['BrowserInstanceGroupModel'] = self.browser_instance_group_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserInstanceGroupModel') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModel()
            self.browser_instance_group_model = temp_model.from_map(m.get('BrowserInstanceGroupModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModel(DaraModel):
    def __init__(
        self,
        auth_notification_enabled: bool = None,
        authorized_user_info: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelAuthorizedUserInfo = None,
        biz_region_id: str = None,
        browser_config: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelBrowserConfig = None,
        browser_instance_group_id: str = None,
        browser_instance_group_name: str = None,
        browser_instance_group_set_id: str = None,
        charge_type: str = None,
        default_access_url: str = None,
        duration: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelDuration = None,
        expired_time: str = None,
        gmt_create: str = None,
        homepage: str = None,
        image_id: str = None,
        instance_type: str = None,
        max_amount: int = None,
        network: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNetwork = None,
        node_instance_type: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNodeInstanceType = None,
        node_pool: List[main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNodePool] = None,
        os_type: str = None,
        policy: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicy = None,
        status: str = None,
        sub_pay_type: str = None,
        support_user_group_mixed_auth: bool = None,
        tier: str = None,
        timers: List[main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelTimers] = None,
        user_group_auth_mode: str = None,
        user_limit: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelUserLimit = None,
    ):
        # Indicates whether authorization and deauthorization notification emails are enabled. `true` indicates that the feature is enabled. `false` indicates that the feature is disabled.
        self.auth_notification_enabled = auth_notification_enabled
        # The statistics of authorized users for the browser group.
        self.authorized_user_info = authorized_user_info
        # The business region where the browser group resides.
        self.biz_region_id = biz_region_id
        # The current browser configuration.
        self.browser_config = browser_config
        # The cloud browser group ID.
        self.browser_instance_group_id = browser_instance_group_id
        # The cloud browser group name.
        self.browser_instance_group_name = browser_instance_group_name
        # The ID of the browser group set to which the browser group belongs.
        self.browser_instance_group_set_id = browser_instance_group_set_id
        # The billing type. In MAU scenarios, `PostPaid` is returned, which indicates the pay-as-you-go billing method.
        self.charge_type = charge_type
        # The default access URL of the browser group. Use the URL returned by the API to access the browser group. Replace the resource ID in the example with your actual value.
        self.default_access_url = default_access_url
        # The plan duration information. In MAU scenarios, plan duration does not apply, and an empty object may be returned.
        self.duration = duration
        # The expiration time of the browser group. This field does not apply to MAU scenarios and is not returned.
        self.expired_time = expired_time
        # The creation time of the browser group. The value is an RFC 3339 time string in the `yyyy-MM-ddTHH:mm:ss.SSSXXX` format, which includes milliseconds and a time zone offset. The `+00:00` in the example indicates the UTC time zone.
        self.gmt_create = gmt_create
        # The homepage URL of the browser group.
        self.homepage = homepage
        # The image ID used by the browser group.
        self.image_id = image_id
        # The instance type used by the browser group.
        self.instance_type = instance_type
        # The maximum number of instances configured for the MAU scenario.
        self.max_amount = max_amount
        # The office network and website access restriction configuration.
        self.network = network
        # The node specifications information. This field does not apply to MAU scenarios.
        self.node_instance_type = node_instance_type
        # The list of node pool information. In MAU scenarios, this field does not apply and an empty list may be returned.
        self.node_pool = node_pool
        # The operating system type of the browser group. The current MAU product scenario uses Windows.
        self.os_type = os_type
        # The policy configuration returned for the browser group. The policy fields are used to view existing settings and do not indicate that all corresponding creation parameters are configurable.
        self.policy = policy
        # The status of the browser instance group.
        # 
        # - `DEPLOYING`: Being deployed.
        # - `PUBLISHED`: Deployed.
        # - `FAILED`: Deployment failed.
        # - `EXPIRED`: Expired.
        # - `CEASED`: Suspended due to overdue payment.
        # - `MAINTAINING`: Being updated.
        # - `MAINTAIN_FAILED`: Update failed.
        # - `DELETING`: Being deleted.
        # - `UNAVAILABLE`: Unavailable.
        self.status = status
        # The sub-billing type. In MAU scenarios, the actual returned value is `mau`, which indicates billing by monthly active users.
        self.sub_pay_type = sub_pay_type
        # Indicates whether mixed authorization of users and user groups is supported. `true` indicates supported, and `false` indicates not supported. Evaluate this value based on the current authorization mode.
        self.support_user_group_mixed_auth = support_user_group_mixed_auth
        # The version of the browser.
        # 
        # - `Basic`: Basic Edition.
        # - `Pro`: Premium Edition.
        # 
        # In MAU scenarios, the value is `Pro`.
        self.tier = tier
        # The session timer configurations currently returned. These are for viewing the effective settings and do not indicate that the creation API supports setting this parameter.
        self.timers = timers
        # The current authorization mode.
        # 
        # - `Mixed`: Mixed authorization of users and user groups.
        # - `User`: User authorization.
        # - `UserGroup`: User group authorization.
        self.user_group_auth_mode = user_group_auth_mode
        # The user quota information.
        self.user_limit = user_limit

    def validate(self):
        if self.authorized_user_info:
            self.authorized_user_info.validate()
        if self.browser_config:
            self.browser_config.validate()
        if self.duration:
            self.duration.validate()
        if self.network:
            self.network.validate()
        if self.node_instance_type:
            self.node_instance_type.validate()
        if self.node_pool:
            for v1 in self.node_pool:
                 if v1:
                    v1.validate()
        if self.policy:
            self.policy.validate()
        if self.timers:
            for v1 in self.timers:
                 if v1:
                    v1.validate()
        if self.user_limit:
            self.user_limit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_notification_enabled is not None:
            result['AuthNotificationEnabled'] = self.auth_notification_enabled

        if self.authorized_user_info is not None:
            result['AuthorizedUserInfo'] = self.authorized_user_info.to_map()

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.browser_config is not None:
            result['BrowserConfig'] = self.browser_config.to_map()

        if self.browser_instance_group_id is not None:
            result['BrowserInstanceGroupId'] = self.browser_instance_group_id

        if self.browser_instance_group_name is not None:
            result['BrowserInstanceGroupName'] = self.browser_instance_group_name

        if self.browser_instance_group_set_id is not None:
            result['BrowserInstanceGroupSetId'] = self.browser_instance_group_set_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.default_access_url is not None:
            result['DefaultAccessUrl'] = self.default_access_url

        if self.duration is not None:
            result['Duration'] = self.duration.to_map()

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.homepage is not None:
            result['Homepage'] = self.homepage

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_amount is not None:
            result['MaxAmount'] = self.max_amount

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type.to_map()

        result['NodePool'] = []
        if self.node_pool is not None:
            for k1 in self.node_pool:
                result['NodePool'].append(k1.to_map() if k1 else None)

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.support_user_group_mixed_auth is not None:
            result['SupportUserGroupMixedAuth'] = self.support_user_group_mixed_auth

        if self.tier is not None:
            result['Tier'] = self.tier

        result['Timers'] = []
        if self.timers is not None:
            for k1 in self.timers:
                result['Timers'].append(k1.to_map() if k1 else None)

        if self.user_group_auth_mode is not None:
            result['UserGroupAuthMode'] = self.user_group_auth_mode

        if self.user_limit is not None:
            result['UserLimit'] = self.user_limit.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthNotificationEnabled') is not None:
            self.auth_notification_enabled = m.get('AuthNotificationEnabled')

        if m.get('AuthorizedUserInfo') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelAuthorizedUserInfo()
            self.authorized_user_info = temp_model.from_map(m.get('AuthorizedUserInfo'))

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('BrowserConfig') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelBrowserConfig()
            self.browser_config = temp_model.from_map(m.get('BrowserConfig'))

        if m.get('BrowserInstanceGroupId') is not None:
            self.browser_instance_group_id = m.get('BrowserInstanceGroupId')

        if m.get('BrowserInstanceGroupName') is not None:
            self.browser_instance_group_name = m.get('BrowserInstanceGroupName')

        if m.get('BrowserInstanceGroupSetId') is not None:
            self.browser_instance_group_set_id = m.get('BrowserInstanceGroupSetId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DefaultAccessUrl') is not None:
            self.default_access_url = m.get('DefaultAccessUrl')

        if m.get('Duration') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelDuration()
            self.duration = temp_model.from_map(m.get('Duration'))

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Homepage') is not None:
            self.homepage = m.get('Homepage')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxAmount') is not None:
            self.max_amount = m.get('MaxAmount')

        if m.get('Network') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('NodeInstanceType') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNodeInstanceType()
            self.node_instance_type = temp_model.from_map(m.get('NodeInstanceType'))

        self.node_pool = []
        if m.get('NodePool') is not None:
            for k1 in m.get('NodePool'):
                temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNodePool()
                self.node_pool.append(temp_model.from_map(k1))

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Policy') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('SupportUserGroupMixedAuth') is not None:
            self.support_user_group_mixed_auth = m.get('SupportUserGroupMixedAuth')

        if m.get('Tier') is not None:
            self.tier = m.get('Tier')

        self.timers = []
        if m.get('Timers') is not None:
            for k1 in m.get('Timers'):
                temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelTimers()
                self.timers.append(temp_model.from_map(k1))

        if m.get('UserGroupAuthMode') is not None:
            self.user_group_auth_mode = m.get('UserGroupAuthMode')

        if m.get('UserLimit') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelUserLimit()
            self.user_limit = temp_model.from_map(m.get('UserLimit'))

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelUserLimit(DaraModel):
    def __init__(
        self,
        user_quota: int = None,
    ):
        # The user quota.
        self.user_quota = user_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_quota is not None:
            result['UserQuota'] = self.user_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserQuota') is not None:
            self.user_quota = m.get('UserQuota')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelTimers(DaraModel):
    def __init__(
        self,
        interval: int = None,
        timer_type: str = None,
    ):
        # The session retention duration after disconnection, in minutes. A value of `-1` indicates that the session is not unbound due to this timeout, but is still subject to authorization and other session release policies.
        self.interval = interval
        # The timer configuration type. `SESSION_TIMEOUT` indicates the session retention duration after disconnection.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['Interval'] = self.interval

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicy(DaraModel):
    def __init__(
        self,
        app_content_protection: str = None,
        authorize_access_policy_rules: List[main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyAuthorizeAccessPolicyRules] = None,
        client_types: List[main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyClientTypes] = None,
        clipboard_policy: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyClipboardPolicy = None,
        disconnect_keep_session: str = None,
        disconnect_keep_session_time: int = None,
        file_manager: str = None,
        html_5file_transfer: str = None,
        no_operation_disconnect: str = None,
        no_operation_disconnect_time: int = None,
        policy_id: str = None,
        policy_version: str = None,
        video_policy: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyVideoPolicy = None,
        watermark_policy: main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyWatermarkPolicy = None,
    ):
        # The screenshot protection switch.
        # 
        # - `on`: Screenshot protection is enabled.
        # - `off`: Screenshot protection is disabled.
        self.app_content_protection = app_content_protection
        # The client access IP address whitelist rules.
        self.authorize_access_policy_rules = authorize_access_policy_rules
        # The list of client access control configurations.
        self.client_types = client_types
        # The clipboard transfer direction, content type, and size limit settings. read indicates transfer from the local PC to the cloud browser. write indicates transfer from the cloud browser to the local PC.
        self.clipboard_policy = clipboard_policy
        # The data retention policy for sessions after disconnection.
        # 
        # - `customTime`: The session is retained for the duration specified by `DisconnectKeepSessionTime`.
        # - `persistent`: The session is not subject to automatic release based on disconnection duration.
        # 
        # **Note:** The `persistent` option is still subject to authorization and other release policies.
        self.disconnect_keep_session = disconnect_keep_session
        # The session retention duration after disconnection. Unit: seconds. This value is for viewing the configuration only and does not indicate that this parameter can be set through the create operation.
        self.disconnect_keep_session_time = disconnect_keep_session_time
        # The floating ball file manager switch.
        # 
        # - `on`: Enabled.
        # - `off`: Disabled.
        self.file_manager = file_manager
        # The file transfer policy for the web client.
        # 
        # - `off`: Transfer is denied.
        # - `upload`: Only upload is allowed.
        # - `download`: Only download is allowed.
        # - `full`: Both upload and download are allowed.
        # 
        # Configure this parameter together with the clipboard policy.
        self.html_5file_transfer = html_5file_transfer
        # The switch for automatic disconnection upon no operation. The value is case-insensitive.
        # 
        # - `on`: Enabled.
        # - `off`: Disabled.
        # 
        # When enabled, use `NoOperationDisconnectTime` to set the wait duration.
        self.no_operation_disconnect = no_operation_disconnect
        # The wait duration before disconnection is triggered after no operation, in seconds. Whether this feature is enabled is indicated by `NoOperationDisconnect`.
        self.no_operation_disconnect_time = no_operation_disconnect_time
        # The ID of the policy associated with the browser instance group.
        self.policy_id = policy_id
        # The policy version.
        # 
        # - `DEFAULT`: Legacy policy.
        # - `CENTER`: Centralized policy.
        self.policy_version = policy_version
        # The video display policy for browser sessions.
        self.video_policy = video_policy
        # The watermark display configuration for browser sessions.
        self.watermark_policy = watermark_policy

    def validate(self):
        if self.authorize_access_policy_rules:
            for v1 in self.authorize_access_policy_rules:
                 if v1:
                    v1.validate()
        if self.client_types:
            for v1 in self.client_types:
                 if v1:
                    v1.validate()
        if self.clipboard_policy:
            self.clipboard_policy.validate()
        if self.video_policy:
            self.video_policy.validate()
        if self.watermark_policy:
            self.watermark_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_content_protection is not None:
            result['AppContentProtection'] = self.app_content_protection

        result['AuthorizeAccessPolicyRules'] = []
        if self.authorize_access_policy_rules is not None:
            for k1 in self.authorize_access_policy_rules:
                result['AuthorizeAccessPolicyRules'].append(k1.to_map() if k1 else None)

        result['ClientTypes'] = []
        if self.client_types is not None:
            for k1 in self.client_types:
                result['ClientTypes'].append(k1.to_map() if k1 else None)

        if self.clipboard_policy is not None:
            result['ClipboardPolicy'] = self.clipboard_policy.to_map()

        if self.disconnect_keep_session is not None:
            result['DisconnectKeepSession'] = self.disconnect_keep_session

        if self.disconnect_keep_session_time is not None:
            result['DisconnectKeepSessionTime'] = self.disconnect_keep_session_time

        if self.file_manager is not None:
            result['FileManager'] = self.file_manager

        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer

        if self.no_operation_disconnect is not None:
            result['NoOperationDisconnect'] = self.no_operation_disconnect

        if self.no_operation_disconnect_time is not None:
            result['NoOperationDisconnectTime'] = self.no_operation_disconnect_time

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.video_policy is not None:
            result['VideoPolicy'] = self.video_policy.to_map()

        if self.watermark_policy is not None:
            result['WatermarkPolicy'] = self.watermark_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')

        self.authorize_access_policy_rules = []
        if m.get('AuthorizeAccessPolicyRules') is not None:
            for k1 in m.get('AuthorizeAccessPolicyRules'):
                temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyAuthorizeAccessPolicyRules()
                self.authorize_access_policy_rules.append(temp_model.from_map(k1))

        self.client_types = []
        if m.get('ClientTypes') is not None:
            for k1 in m.get('ClientTypes'):
                temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyClientTypes()
                self.client_types.append(temp_model.from_map(k1))

        if m.get('ClipboardPolicy') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyClipboardPolicy()
            self.clipboard_policy = temp_model.from_map(m.get('ClipboardPolicy'))

        if m.get('DisconnectKeepSession') is not None:
            self.disconnect_keep_session = m.get('DisconnectKeepSession')

        if m.get('DisconnectKeepSessionTime') is not None:
            self.disconnect_keep_session_time = m.get('DisconnectKeepSessionTime')

        if m.get('FileManager') is not None:
            self.file_manager = m.get('FileManager')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('NoOperationDisconnect') is not None:
            self.no_operation_disconnect = m.get('NoOperationDisconnect')

        if m.get('NoOperationDisconnectTime') is not None:
            self.no_operation_disconnect_time = m.get('NoOperationDisconnectTime')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('VideoPolicy') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyVideoPolicy()
            self.video_policy = temp_model.from_map(m.get('VideoPolicy'))

        if m.get('WatermarkPolicy') is not None:
            temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyWatermarkPolicy()
            self.watermark_policy = temp_model.from_map(m.get('WatermarkPolicy'))

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyWatermarkPolicy(DaraModel):
    def __init__(
        self,
        watermark_switch: str = None,
        watermark_types: List[str] = None,
    ):
        # The watermark switch. The value is case-insensitive.
        # 
        # - `ON`: Watermark enabled.
        # - `OFF`: Watermark disabled.
        # 
        # When disabled, the watermark content type list is not used.
        self.watermark_switch = watermark_switch
        # The list of watermark content types.
        # 
        # - `EndUserId`: User ID.
        # - `InstanceGroupId`: Delivery group ID.
        # - `ClientTime`: Current time on the client.
        # 
        # Use watermark types supported by the browser and client.
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.watermark_switch is not None:
            result['WatermarkSwitch'] = self.watermark_switch

        if self.watermark_types is not None:
            result['WatermarkTypes'] = self.watermark_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkSwitch') is not None:
            self.watermark_switch = m.get('WatermarkSwitch')

        if m.get('WatermarkTypes') is not None:
            self.watermark_types = m.get('WatermarkTypes')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyVideoPolicy(DaraModel):
    def __init__(
        self,
        frame_rate: int = None,
    ):
        # The frame rate of browser sessions.
        self.frame_rate = frame_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyClipboardPolicy(DaraModel):
    def __init__(
        self,
        clipboard: str = None,
        clipboard_read_limit: int = None,
        clipboard_scope: str = None,
        clipboard_size_unit: str = None,
        clipboard_write_limit: int = None,
        file_clipboard: str = None,
        rich_text_clipboard: str = None,
        rich_text_clipboard_limit: int = None,
        rich_text_clipboard_read_limit: int = None,
        rich_text_clipboard_read_size_unit: str = None,
        rich_text_clipboard_size_unit: str = None,
        rich_text_clipboard_write_limit: int = None,
        rich_text_clipboard_write_size_unit: str = None,
        text_clipboard: str = None,
        text_clipboard_read_limit: int = None,
        text_clipboard_read_size_unit: str = None,
        text_clipboard_write_limit: int = None,
        text_clipboard_write_size_unit: str = None,
    ):
        # The clipboard transfer direction. The value is case-insensitive.
        # 
        # - `off`: Bidirectional transfer is denied.
        # - `read`: Copy and paste from the local PC to the cloud browser is allowed.
        # - `write`: Copy and paste from the cloud browser to the local PC is allowed.
        # - `readwrite`: Bidirectional transfer is allowed.
        self.clipboard = clipboard
        # The clipboard size limit for inbound transfer (from the local PC to the cloud browser).
        self.clipboard_read_limit = clipboard_read_limit
        # The clipboard control granularity.
        # 
        # - `global`: Unified control.
        # - `grained`: Separate control by text, rich text, and file.
        self.clipboard_scope = clipboard_scope
        # The unit of the clipboard size.
        # 
        # - `B`: bytes.
        # - `KB`: 1024 bytes.
        self.clipboard_size_unit = clipboard_size_unit
        # The clipboard size limit for outbound transfer (from the cloud browser to the local PC).
        self.clipboard_write_limit = clipboard_write_limit
        # The clipboard transfer direction. The value is case-insensitive.
        # 
        # - `off`: Bidirectional transfer is denied.
        # - `read`: Copy and paste from the local PC to the cloud browser is allowed.
        # - `write`: Copy and paste from the cloud browser to the local PC is allowed.
        # - `readwrite`: Bidirectional transfer is allowed.
        self.file_clipboard = file_clipboard
        # The clipboard transfer direction. The value is case-insensitive.
        # 
        # - `off`: Bidirectional transfer is denied.
        # - `read`: Copy and paste from the local PC to the cloud browser is allowed.
        # - `write`: Copy and paste from the cloud browser to the local PC is allowed.
        # - `readwrite`: Bidirectional transfer is allowed.
        self.rich_text_clipboard = rich_text_clipboard
        # The rich text clipboard size limit.
        self.rich_text_clipboard_limit = rich_text_clipboard_limit
        # The clipboard size limit for inbound transfer (from the local PC to the cloud browser).
        self.rich_text_clipboard_read_limit = rich_text_clipboard_read_limit
        # The unit of the clipboard size.
        # 
        # - `B`: bytes.
        # - `KB`: 1024 bytes.
        self.rich_text_clipboard_read_size_unit = rich_text_clipboard_read_size_unit
        # The unit of the clipboard size.
        # 
        # - `B`: bytes.
        # - `KB`: 1024 bytes.
        self.rich_text_clipboard_size_unit = rich_text_clipboard_size_unit
        # The clipboard size limit for outbound transfer (from the cloud browser to the local PC).
        self.rich_text_clipboard_write_limit = rich_text_clipboard_write_limit
        # The unit of the clipboard size.
        # 
        # - `B`: bytes.
        # - `KB`: 1024 bytes.
        self.rich_text_clipboard_write_size_unit = rich_text_clipboard_write_size_unit
        # The clipboard transfer direction. The value is case-insensitive.
        # 
        # - `off`: Bidirectional transfer is denied.
        # - `read`: Copy and paste from the local PC to the cloud browser is allowed.
        # - `write`: Copy and paste from the cloud browser to the local PC is allowed.
        # - `readwrite`: Bidirectional transfer is allowed.
        self.text_clipboard = text_clipboard
        # The clipboard size limit for inbound transfer (from the local PC to the cloud browser).
        self.text_clipboard_read_limit = text_clipboard_read_limit
        # The unit of the clipboard size.
        # 
        # - `B`: bytes.
        # - `KB`: 1024 bytes.
        self.text_clipboard_read_size_unit = text_clipboard_read_size_unit
        # The clipboard size limit for outbound transfer (from the cloud browser to the local PC).
        self.text_clipboard_write_limit = text_clipboard_write_limit
        # The unit of the clipboard size.
        # 
        # - `B`: bytes.
        # - `KB`: 1024 bytes.
        self.text_clipboard_write_size_unit = text_clipboard_write_size_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        if self.clipboard_read_limit is not None:
            result['ClipboardReadLimit'] = self.clipboard_read_limit

        if self.clipboard_scope is not None:
            result['ClipboardScope'] = self.clipboard_scope

        if self.clipboard_size_unit is not None:
            result['ClipboardSizeUnit'] = self.clipboard_size_unit

        if self.clipboard_write_limit is not None:
            result['ClipboardWriteLimit'] = self.clipboard_write_limit

        if self.file_clipboard is not None:
            result['FileClipboard'] = self.file_clipboard

        if self.rich_text_clipboard is not None:
            result['RichTextClipboard'] = self.rich_text_clipboard

        if self.rich_text_clipboard_limit is not None:
            result['RichTextClipboardLimit'] = self.rich_text_clipboard_limit

        if self.rich_text_clipboard_read_limit is not None:
            result['RichTextClipboardReadLimit'] = self.rich_text_clipboard_read_limit

        if self.rich_text_clipboard_read_size_unit is not None:
            result['RichTextClipboardReadSizeUnit'] = self.rich_text_clipboard_read_size_unit

        if self.rich_text_clipboard_size_unit is not None:
            result['RichTextClipboardSizeUnit'] = self.rich_text_clipboard_size_unit

        if self.rich_text_clipboard_write_limit is not None:
            result['RichTextClipboardWriteLimit'] = self.rich_text_clipboard_write_limit

        if self.rich_text_clipboard_write_size_unit is not None:
            result['RichTextClipboardWriteSizeUnit'] = self.rich_text_clipboard_write_size_unit

        if self.text_clipboard is not None:
            result['TextClipboard'] = self.text_clipboard

        if self.text_clipboard_read_limit is not None:
            result['TextClipboardReadLimit'] = self.text_clipboard_read_limit

        if self.text_clipboard_read_size_unit is not None:
            result['TextClipboardReadSizeUnit'] = self.text_clipboard_read_size_unit

        if self.text_clipboard_write_limit is not None:
            result['TextClipboardWriteLimit'] = self.text_clipboard_write_limit

        if self.text_clipboard_write_size_unit is not None:
            result['TextClipboardWriteSizeUnit'] = self.text_clipboard_write_size_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        if m.get('ClipboardReadLimit') is not None:
            self.clipboard_read_limit = m.get('ClipboardReadLimit')

        if m.get('ClipboardScope') is not None:
            self.clipboard_scope = m.get('ClipboardScope')

        if m.get('ClipboardSizeUnit') is not None:
            self.clipboard_size_unit = m.get('ClipboardSizeUnit')

        if m.get('ClipboardWriteLimit') is not None:
            self.clipboard_write_limit = m.get('ClipboardWriteLimit')

        if m.get('FileClipboard') is not None:
            self.file_clipboard = m.get('FileClipboard')

        if m.get('RichTextClipboard') is not None:
            self.rich_text_clipboard = m.get('RichTextClipboard')

        if m.get('RichTextClipboardLimit') is not None:
            self.rich_text_clipboard_limit = m.get('RichTextClipboardLimit')

        if m.get('RichTextClipboardReadLimit') is not None:
            self.rich_text_clipboard_read_limit = m.get('RichTextClipboardReadLimit')

        if m.get('RichTextClipboardReadSizeUnit') is not None:
            self.rich_text_clipboard_read_size_unit = m.get('RichTextClipboardReadSizeUnit')

        if m.get('RichTextClipboardSizeUnit') is not None:
            self.rich_text_clipboard_size_unit = m.get('RichTextClipboardSizeUnit')

        if m.get('RichTextClipboardWriteLimit') is not None:
            self.rich_text_clipboard_write_limit = m.get('RichTextClipboardWriteLimit')

        if m.get('RichTextClipboardWriteSizeUnit') is not None:
            self.rich_text_clipboard_write_size_unit = m.get('RichTextClipboardWriteSizeUnit')

        if m.get('TextClipboard') is not None:
            self.text_clipboard = m.get('TextClipboard')

        if m.get('TextClipboardReadLimit') is not None:
            self.text_clipboard_read_limit = m.get('TextClipboardReadLimit')

        if m.get('TextClipboardReadSizeUnit') is not None:
            self.text_clipboard_read_size_unit = m.get('TextClipboardReadSizeUnit')

        if m.get('TextClipboardWriteLimit') is not None:
            self.text_clipboard_write_limit = m.get('TextClipboardWriteLimit')

        if m.get('TextClipboardWriteSizeUnit') is not None:
            self.text_clipboard_write_size_unit = m.get('TextClipboardWriteSizeUnit')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyClientTypes(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # The client type.
        # 
        # - `windows`: Windows client.
        # - `macos`: macOS client.
        # - `html5`: Web client.
        # - `linux`: Linux client.
        # - `android`: Android client.
        # - `ios`: iOS client.
        # 
        # This field reflects the existing access configuration and does not indicate that all client types are available for the current product.
        self.client_type = client_type
        # The access policy switch for the client type.
        # 
        # - `on`: Access from this client type is allowed.
        # - `off`: Access from this client type is denied.
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

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelPolicyAuthorizeAccessPolicyRules(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
        policy: str = None,
    ):
        # The client source CIDR block that is allowed to access the browser group.
        self.cidr_ip = cidr_ip
        # The description of the client access rule.
        self.description = description
        # The action of the client access rule.
        # 
        # - `allow`: Access is allowed.
        # - `deny`: Access is denied.
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip

        if self.description is not None:
            result['Description'] = self.description

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNodePool(DaraModel):
    def __init__(
        self,
        node_amount: str = None,
        node_used: str = None,
    ):
        # The total number of nodes. This field does not apply to MAU scenarios.
        self.node_amount = node_amount
        # The number of used nodes. This field does not apply to MAU scenarios.
        self.node_used = node_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount

        if self.node_used is not None:
            result['NodeUsed'] = self.node_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')

        if m.get('NodeUsed') is not None:
            self.node_used = m.get('NodeUsed')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNodeInstanceType(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        memory: int = None,
    ):
        # The CPU configuration of the node. This field does not apply to MAU scenarios.
        self.cpu = cpu
        # The memory configuration of the node. This field does not apply to MAU scenarios.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNetwork(DaraModel):
    def __init__(
        self,
        access_restriction: str = None,
        office_site_id: str = None,
        restricted_urls: List[main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNetworkRestrictedURLs] = None,
        v_switch_ids: List[str] = None,
    ):
        # The website access restriction mode.
        # 
        # - `ALLOW_ALL`: All domain names are allowed.
        # - `ALLOW_LIST`: Only websites in the allowlist are allowed.
        # 
        # The returned value reflects the current configuration of the browser group.
        self.access_restriction = access_restriction
        # The office network ID to which the browser group belongs.
        self.office_site_id = office_site_id
        # The website access restriction list. A maximum of 20 entries are returned. To query the complete list, call `ListBrowserRestrictedURLs`.
        self.restricted_urls = restricted_urls
        # The list of vSwitch IDs used by the browser group. This is available for scenarios with custom network configurations.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.restricted_urls:
            for v1 in self.restricted_urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_restriction is not None:
            result['AccessRestriction'] = self.access_restriction

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        result['RestrictedURLs'] = []
        if self.restricted_urls is not None:
            for k1 in self.restricted_urls:
                result['RestrictedURLs'].append(k1.to_map() if k1 else None)

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRestriction') is not None:
            self.access_restriction = m.get('AccessRestriction')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        self.restricted_urls = []
        if m.get('RestrictedURLs') is not None:
            for k1 in m.get('RestrictedURLs'):
                temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNetworkRestrictedURLs()
                self.restricted_urls.append(temp_model.from_map(k1))

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelNetworkRestrictedURLs(DaraModel):
    def __init__(
        self,
        restricted_urlid: str = None,
        url: str = None,
    ):
        # The ID of the website access restriction entry.
        self.restricted_urlid = restricted_urlid
        # The website URL in the access restriction entry.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.restricted_urlid is not None:
            result['RestrictedURLId'] = self.restricted_urlid

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestrictedURLId') is not None:
            self.restricted_urlid = m.get('RestrictedURLId')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelDuration(DaraModel):
    def __init__(
        self,
        current_pay_stage: str = None,
        period_end_time: str = None,
        period_start_time: str = None,
        total_duration: int = None,
        used_duration: int = None,
    ):
        # The current payment stage of the plan. This field does not apply to MAU scenarios.
        self.current_pay_stage = current_pay_stage
        # The end time of the plan period. This field does not apply to MAU scenarios and is not returned.
        self.period_end_time = period_end_time
        # The start time of the plan period. This field does not apply to MAU scenarios and is not returned.
        self.period_start_time = period_start_time
        # The total duration of the plan, in seconds. This field does not apply to MAU scenarios.
        self.total_duration = total_duration
        # The used duration of the plan, in seconds. This field does not apply to MAU scenarios.
        self.used_duration = used_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_pay_stage is not None:
            result['CurrentPayStage'] = self.current_pay_stage

        if self.period_end_time is not None:
            result['PeriodEndTime'] = self.period_end_time

        if self.period_start_time is not None:
            result['PeriodStartTime'] = self.period_start_time

        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration

        if self.used_duration is not None:
            result['UsedDuration'] = self.used_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPayStage') is not None:
            self.current_pay_stage = m.get('CurrentPayStage')

        if m.get('PeriodEndTime') is not None:
            self.period_end_time = m.get('PeriodEndTime')

        if m.get('PeriodStartTime') is not None:
            self.period_start_time = m.get('PeriodStartTime')

        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')

        if m.get('UsedDuration') is not None:
            self.used_duration = m.get('UsedDuration')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelBrowserConfig(DaraModel):
    def __init__(
        self,
        bookmarks: List[main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelBrowserConfigBookmarks] = None,
        browser_param: str = None,
        cookies_sync: str = None,
        homepage: str = None,
    ):
        # The list of browser bookmarks. A maximum of 20 entries are returned. To query the complete bookmark list, call `ListBrowserBookmarks`.
        self.bookmarks = bookmarks
        # The browser startup parameters. For example, `--incognito` specifies the incognito window mode.
        self.browser_param = browser_param
        # The cookie synchronization configuration. The string `true` indicates that synchronization is enabled. The string `false` indicates that synchronization is disabled.
        self.cookies_sync = cookies_sync
        # The homepage URL that opens when the browser starts.
        self.homepage = homepage

    def validate(self):
        if self.bookmarks:
            for v1 in self.bookmarks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bookmarks'] = []
        if self.bookmarks is not None:
            for k1 in self.bookmarks:
                result['Bookmarks'].append(k1.to_map() if k1 else None)

        if self.browser_param is not None:
            result['BrowserParam'] = self.browser_param

        if self.cookies_sync is not None:
            result['CookiesSync'] = self.cookies_sync

        if self.homepage is not None:
            result['Homepage'] = self.homepage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bookmarks = []
        if m.get('Bookmarks') is not None:
            for k1 in m.get('Bookmarks'):
                temp_model = main_models.GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelBrowserConfigBookmarks()
                self.bookmarks.append(temp_model.from_map(k1))

        if m.get('BrowserParam') is not None:
            self.browser_param = m.get('BrowserParam')

        if m.get('CookiesSync') is not None:
            self.cookies_sync = m.get('CookiesSync')

        if m.get('Homepage') is not None:
            self.homepage = m.get('Homepage')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelBrowserConfigBookmarks(DaraModel):
    def __init__(
        self,
        bookmark_folder: str = None,
        bookmark_id: str = None,
        bookmark_name: str = None,
        bookmark_url: str = None,
    ):
        # The folder in which the bookmark resides.
        self.bookmark_folder = bookmark_folder
        # The bookmark ID.
        self.bookmark_id = bookmark_id
        # The bookmark name.
        self.bookmark_name = bookmark_name
        # The URL of the bookmark.
        self.bookmark_url = bookmark_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bookmark_folder is not None:
            result['BookmarkFolder'] = self.bookmark_folder

        if self.bookmark_id is not None:
            result['BookmarkId'] = self.bookmark_id

        if self.bookmark_name is not None:
            result['BookmarkName'] = self.bookmark_name

        if self.bookmark_url is not None:
            result['BookmarkURL'] = self.bookmark_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BookmarkFolder') is not None:
            self.bookmark_folder = m.get('BookmarkFolder')

        if m.get('BookmarkId') is not None:
            self.bookmark_id = m.get('BookmarkId')

        if m.get('BookmarkName') is not None:
            self.bookmark_name = m.get('BookmarkName')

        if m.get('BookmarkURL') is not None:
            self.bookmark_url = m.get('BookmarkURL')

        return self

class GetBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelAuthorizedUserInfo(DaraModel):
    def __init__(
        self,
        total_count: int = None,
        total_user_group_count: int = None,
    ):
        # The total number of authorized users.
        self.total_count = total_count
        # The total number of authorized user groups.
        self.total_user_group_count = total_user_group_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_user_group_count is not None:
            result['TotalUserGroupCount'] = self.total_user_group_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalUserGroupCount') is not None:
            self.total_user_group_count = m.get('TotalUserGroupCount')

        return self

