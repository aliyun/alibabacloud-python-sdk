# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListBrowserInstanceGroupResponseBody(DaraModel):
    def __init__(
        self,
        browser_instance_group_models: List[main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of browser groups on the current page.
        self.browser_instance_group_models = browser_instance_group_models
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID, which is used for troubleshooting.
        self.request_id = request_id
        # The total number of browser groups that match the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.browser_instance_group_models:
            for v1 in self.browser_instance_group_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BrowserInstanceGroupModels'] = []
        if self.browser_instance_group_models is not None:
            for k1 in self.browser_instance_group_models:
                result['BrowserInstanceGroupModels'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.browser_instance_group_models = []
        if m.get('BrowserInstanceGroupModels') is not None:
            for k1 in m.get('BrowserInstanceGroupModels'):
                temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModels()
                self.browser_instance_group_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModels(DaraModel):
    def __init__(
        self,
        auth_notification_enabled: bool = None,
        authorized_user_info: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsAuthorizedUserInfo = None,
        biz_region_id: str = None,
        browser_config: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsBrowserConfig = None,
        browser_instance_group_id: str = None,
        browser_instance_group_name: str = None,
        browser_instance_group_set_id: str = None,
        charge_type: str = None,
        default_access_url: str = None,
        duration: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsDuration = None,
        expired_time: str = None,
        gmt_create: str = None,
        homepage: str = None,
        image_id: str = None,
        instance_type: str = None,
        network: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsNetwork = None,
        os_type: str = None,
        policy: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicy = None,
        status: str = None,
        sub_pay_type: str = None,
        support_user_group_mixed_auth: bool = None,
        tags: List[main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsTags] = None,
        tier: str = None,
        timers: List[main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsTimers] = None,
        user_group_auth_mode: str = None,
        user_limit: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsUserLimit = None,
    ):
        # Indicates whether authorization and deauthorization notification emails are enabled. `true` indicates enabled. `false` indicates disabled.
        self.auth_notification_enabled = auth_notification_enabled
        # The authorized user statistics of the browser group.
        self.authorized_user_info = authorized_user_info
        # The business region where the browser group is located.
        self.biz_region_id = biz_region_id
        # The current browser configuration.
        self.browser_config = browser_config
        # The ID of the cloud browser group.
        self.browser_instance_group_id = browser_instance_group_id
        # The name of the cloud browser group.
        self.browser_instance_group_name = browser_instance_group_name
        # The ID of the browser group set to which the browser group belongs.
        self.browser_instance_group_set_id = browser_instance_group_set_id
        # The billing type. In MAU scenarios, `PostPaid` is returned, which indicates pay-as-you-go.
        self.charge_type = charge_type
        # The default access URL of the browser group. Use the URL returned by the API for access. The resource identifiers in the example must be replaced.
        self.default_access_url = default_access_url
        # The plan duration information. In MAU scenarios, plan duration does not apply, and an empty object may be returned.
        self.duration = duration
        # The expiration time of the browser group. Not applicable in MAU scenarios. This field is not returned.
        self.expired_time = expired_time
        # The creation time of the browser group.
        # 
        # The time is in RFC 3339 format: `yyyy-MM-dd\\"T\\"HH:mm:ss.SSSXXX`, which includes milliseconds and a time zone offset. The actual POP response uses the UTC offset `+00:00`.
        self.gmt_create = gmt_create
        # The homepage URL of the browser group.
        self.homepage = homepage
        # The image ID used by the browser group.
        self.image_id = image_id
        # The instance type used by the browser group.
        self.instance_type = instance_type
        # The workspace network and website access restriction configuration.
        self.network = network
        # The operating system type of the browser group. The current MAU product scenario uses Windows.
        self.os_type = os_type
        # The policy configuration returned for the browser group. Policy fields are used to view existing settings and do not indicate that all corresponding creation parameters are configurable.
        self.policy = policy
        # The browser group status.
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
        # The sub-payment type. In MAU scenarios, the actual returned value is `mau`, which indicates billing by monthly active users.
        self.sub_pay_type = sub_pay_type
        # Indicates whether mixed authorization of users and user groups is supported. `true` indicates supported, and `false` indicates not supported. Evaluate this value based on the current authorization mode.
        self.support_user_group_mixed_auth = support_user_group_mixed_auth
        # The list of resource tags.
        self.tags = tags
        # The version of the browser. Valid values:
        # 
        # - `Basic`: Basic Edition.
        # - `Pro`: Premium Edition.
        # 
        # In MAU scenarios, the value is `Pro`.
        self.tier = tier
        # The session timer configurations currently returned. This is used to view the effective settings and does not indicate that the create operation supports setting this parameter.
        self.timers = timers
        # The current authorization mode. Valid values:
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
        if self.policy:
            self.policy.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
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

        if self.network is not None:
            result['Network'] = self.network.to_map()

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsAuthorizedUserInfo()
            self.authorized_user_info = temp_model.from_map(m.get('AuthorizedUserInfo'))

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('BrowserConfig') is not None:
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsBrowserConfig()
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
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsDuration()
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

        if m.get('Network') is not None:
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Policy') is not None:
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('SupportUserGroupMixedAuth') is not None:
            self.support_user_group_mixed_auth = m.get('SupportUserGroupMixedAuth')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Tier') is not None:
            self.tier = m.get('Tier')

        self.timers = []
        if m.get('Timers') is not None:
            for k1 in m.get('Timers'):
                temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsTimers()
                self.timers.append(temp_model.from_map(k1))

        if m.get('UserGroupAuthMode') is not None:
            self.user_group_auth_mode = m.get('UserGroupAuthMode')

        if m.get('UserLimit') is not None:
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsUserLimit()
            self.user_limit = temp_model.from_map(m.get('UserLimit'))

        return self

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsUserLimit(DaraModel):
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

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsTimers(DaraModel):
    def __init__(
        self,
        interval: int = None,
        timer_type: str = None,
    ):
        # The session retention duration after disconnection, in minutes. `-1` indicates that the session is not unbound due to this timeout. The session is still subject to authorization and other session release policies.
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

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicy(DaraModel):
    def __init__(
        self,
        app_content_protection: str = None,
        authorize_access_policy_rules: List[main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyAuthorizeAccessPolicyRules] = None,
        client_types: List[main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyClientTypes] = None,
        clipboard_policy: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyClipboardPolicy = None,
        video_policy: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyVideoPolicy = None,
        watermark_policy: main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyWatermarkPolicy = None,
    ):
        # The screenshot protection switch.
        # 
        # - `on`: Screenshot protection is enabled.
        # - `off`: Screenshot protection is disabled.
        self.app_content_protection = app_content_protection
        # The client access IP address whitelist rules.
        self.authorize_access_policy_rules = authorize_access_policy_rules
        # The client access control configuration list.
        self.client_types = client_types
        # The clipboard transfer direction, content type, and size limit settings. read indicates transfer from the local PC to the cloud browser. write indicates transfer from the cloud browser to the local PC.
        self.clipboard_policy = clipboard_policy
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
                temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyAuthorizeAccessPolicyRules()
                self.authorize_access_policy_rules.append(temp_model.from_map(k1))

        self.client_types = []
        if m.get('ClientTypes') is not None:
            for k1 in m.get('ClientTypes'):
                temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyClientTypes()
                self.client_types.append(temp_model.from_map(k1))

        if m.get('ClipboardPolicy') is not None:
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyClipboardPolicy()
            self.clipboard_policy = temp_model.from_map(m.get('ClipboardPolicy'))

        if m.get('VideoPolicy') is not None:
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyVideoPolicy()
            self.video_policy = temp_model.from_map(m.get('VideoPolicy'))

        if m.get('WatermarkPolicy') is not None:
            temp_model = main_models.ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyWatermarkPolicy()
            self.watermark_policy = temp_model.from_map(m.get('WatermarkPolicy'))

        return self

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyWatermarkPolicy(DaraModel):
    def __init__(
        self,
        watermark_switch: str = None,
        watermark_types: List[str] = None,
    ):
        # The watermark switch. The value is case-insensitive. Valid values:
        # 
        # - `ON`: Watermark is enabled.
        # - `OFF`: Watermark is disabled.
        # 
        # When disabled, the watermark content type list is not used.
        self.watermark_switch = watermark_switch
        # The list of watermark content types. Valid values:
        # 
        # - `EndUserId`: The user identifier.
        # - `InstanceGroupId`: The delivery group identifier.
        # - `ClientTime`: The current time on the client.
        # 
        # Use watermark types that are supported by the browser and client.
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

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyVideoPolicy(DaraModel):
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

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyClipboardPolicy(DaraModel):
    def __init__(
        self,
        clipboard: str = None,
    ):
        # The clipboard transfer direction. The value is case-insensitive.
        # 
        # - `off`: Bidirectional transfer is disabled.
        # - `read`: Copy and paste from the local PC to the cloud browser is allowed.
        # - `write`: Copy and paste from the cloud browser to the local PC is allowed.
        # - `readwrite`: Bidirectional transfer is allowed.
        self.clipboard = clipboard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        return self

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyClientTypes(DaraModel):
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
        # The access policy switch for this client type.
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

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsPolicyAuthorizeAccessPolicyRules(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
        policy: str = None,
    ):
        # The source CIDR block of the client that is allowed to access.
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

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsNetwork(DaraModel):
    def __init__(
        self,
        access_restriction: str = None,
        office_site_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        # The website access restriction mode.
        # 
        # - `ALLOW_ALL`: All domain names are allowed.
        # - `ALLOW_LIST`: Only websites in the allowlist are allowed.
        # 
        # The returned value reflects the current configuration of the browser group.
        self.access_restriction = access_restriction
        # The ID of the workspace to which the browser group belongs.
        self.office_site_id = office_site_id
        # The list of vSwitch IDs used by the browser group, available for scenarios with custom network configurations.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_restriction is not None:
            result['AccessRestriction'] = self.access_restriction

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRestriction') is not None:
            self.access_restriction = m.get('AccessRestriction')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsDuration(DaraModel):
    def __init__(
        self,
        current_pay_stage: str = None,
        period_end_time: str = None,
        period_start_time: str = None,
        total_duration: int = None,
        used_duration: int = None,
    ):
        # The current payment stage of the plan. Not applicable in MAU scenarios.
        self.current_pay_stage = current_pay_stage
        # The end time of the plan period. Not applicable in MAU scenarios. This field is not returned.
        self.period_end_time = period_end_time
        # The start time of the plan period. Not applicable in MAU scenarios. This field is not returned.
        self.period_start_time = period_start_time
        # The total duration of the plan, in seconds. Not applicable in MAU scenarios.
        self.total_duration = total_duration
        # The used duration of the plan, in seconds. Not applicable in MAU scenarios.
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

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsBrowserConfig(DaraModel):
    def __init__(
        self,
        browser_param: str = None,
        cookies_sync: str = None,
        homepage: str = None,
    ):
        # The browser startup parameters. For example, `--incognito` indicates an incognito window.
        self.browser_param = browser_param
        # The cookie synchronization configuration. The string `true` indicates enabled. `false` indicates disabled.
        self.cookies_sync = cookies_sync
        # The homepage URL that opens when the browser starts.
        self.homepage = homepage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_param is not None:
            result['BrowserParam'] = self.browser_param

        if self.cookies_sync is not None:
            result['CookiesSync'] = self.cookies_sync

        if self.homepage is not None:
            result['Homepage'] = self.homepage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserParam') is not None:
            self.browser_param = m.get('BrowserParam')

        if m.get('CookiesSync') is not None:
            self.cookies_sync = m.get('CookiesSync')

        if m.get('Homepage') is not None:
            self.homepage = m.get('Homepage')

        return self

class ListBrowserInstanceGroupResponseBodyBrowserInstanceGroupModelsAuthorizedUserInfo(DaraModel):
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

