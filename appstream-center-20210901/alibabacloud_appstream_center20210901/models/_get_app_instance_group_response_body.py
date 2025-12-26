# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetAppInstanceGroupResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_group_models: main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModels = None,
        request_id: str = None,
    ):
        # AppInstanceGroupModels
        self.app_instance_group_models = app_instance_group_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_instance_group_models:
            self.app_instance_group_models.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_models is not None:
            result['AppInstanceGroupModels'] = self.app_instance_group_models.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupModels') is not None:
            temp_model = main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModels()
            self.app_instance_group_models = temp_model.from_map(m.get('AppInstanceGroupModels'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAppInstanceGroupResponseBodyAppInstanceGroupModels(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        amount: int = None,
        app_center_image_id: str = None,
        app_center_image_name: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_instance_type: str = None,
        app_instance_type_name: str = None,
        app_policy_id: str = None,
        apps: List[main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps] = None,
        auth_mode: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        max_amount: int = None,
        min_amount: int = None,
        node_pool: List[main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool] = None,
        office_site_id: str = None,
        os_type: str = None,
        ota_info: main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo = None,
        product_type: str = None,
        region_id: str = None,
        reserve_amount_ratio: str = None,
        reserve_max_amount: int = None,
        reserve_min_amount: int = None,
        resource_status: str = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        session_timeout: str = None,
        session_type: str = None,
        skip_user_auth_check: bool = None,
        spec_id: str = None,
        status: str = None,
        support_user_group_mixed_auth: bool = None,
        tags: List[main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsTags] = None,
        user_group_auth_mode: str = None,
    ):
        # 接入类型。
        self.access_type = access_type
        # The number of subscription resources. Minimum value: 1.
        self.amount = amount
        # The image ID of the application.
        self.app_center_image_id = app_center_image_id
        # The image name of the application.
        self.app_center_image_name = app_center_image_name
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # The resource type of the delivery group.
        self.app_instance_type = app_instance_type
        # The name of the resource type of the delivery group.
        self.app_instance_type_name = app_instance_type_name
        # The policy ID of the application.
        self.app_policy_id = app_policy_id
        # The applications.
        self.apps = apps
        # 授权模式。
        self.auth_mode = auth_mode
        # The sales mode.
        # 
        # Valid values:
        # 
        # *   AppInstance: by session
        # *   Node: by resource
        self.charge_resource_mode = charge_resource_mode
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        self.charge_type = charge_type
        # The time when the delivery group expires.
        self.expired_time = expired_time
        # The time when the delivery group was created.
        self.gmt_create = gmt_create
        # The maximum number of instances. Minimum value: 1.
        self.max_amount = max_amount
        # The minimum number of instances. Minimum value: 1.
        self.min_amount = min_amount
        # The information about the resource group.
        self.node_pool = node_pool
        # 办公网络ID。
        self.office_site_id = office_site_id
        # The type of the operating system.
        self.os_type = os_type
        # The information about the over-the-air (OTA) update task.
        self.ota_info = ota_info
        # The product type.
        self.product_type = product_type
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        self.region_id = region_id
        # The percentage of reserved instances. The value indicates the percentage of unused sessions in the delivery group. Valid values: 0 to 99.
        self.reserve_amount_ratio = reserve_amount_ratio
        # The maximum number of reserved instances. The value indicates the maximum number of unused sessions in the delivery group. Minimum value: 1.
        self.reserve_max_amount = reserve_max_amount
        # The minimum number of reserved instances. The value indicates the minimum number of unused sessions in the delivery group. Minimum value: 1.
        self.reserve_min_amount = reserve_min_amount
        # The resource status.
        self.resource_status = resource_status
        # The duration for which no session is connected. Unit: minutes. If no session is connected in the resources after the specified duration elapses, automatic scale-in is triggered. Minimum value: 0.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The number of sessions that are created each time the delivery group is scaled out. Minimum value: 1.
        self.scaling_step = scaling_step
        # The upper limit of session usage. If the session usage exceeds the specified upper limit, auto scaling is automatically triggered. The session usage rate is calculated by using the following formula: Session usage rate = Number of sessions in use/Total number of sessions × 100%. Valid values: 0 to 99.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The duration for which sessions are retained after disconnection. Unit: minutes. After an end user disconnects from a session, the session is closed only after the specified duration elapses. If you want to permanently retain sessions, set this parameter to `-1`. Valid values:-1 and 3 to 300. Default value: `15`.
        self.session_timeout = session_timeout
        # 会话类型。
        self.session_type = session_type
        # Indicates whether user permission verification is skipped.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: This is the default value.
        self.skip_user_auth_check = skip_user_auth_check
        # The specification ID that uniquely corresponds to the ID of the delivery group.
        self.spec_id = spec_id
        # The status of the delivery group.
        # 
        # Valid values:
        # 
        # *   PUBLISHED: The delivery group is published.
        # *   FAILED: The delivery group failed to be published.
        # *   MAINTAIN_FAILED: The delivery group failed to be updated.
        # *   EXPIRED: The delivery group is expired.
        # *   MAINTAINING: The delivery group is being updated.
        # *   CEASED: The delivery group has overdue payments.
        # *   EXPIRED_RECYCLING: The delivery group is expired and being recycled.
        # *   DEPLOYING: The delivery group is being published.
        self.status = status
        self.support_user_group_mixed_auth = support_user_group_mixed_auth
        # 资源标签列表。
        self.tags = tags
        self.user_group_auth_mode = user_group_auth_mode

    def validate(self):
        if self.apps:
            for v1 in self.apps:
                 if v1:
                    v1.validate()
        if self.node_pool:
            for v1 in self.node_pool:
                 if v1:
                    v1.validate()
        if self.ota_info:
            self.ota_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id

        if self.app_center_image_name is not None:
            result['AppCenterImageName'] = self.app_center_image_name

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type

        if self.app_instance_type_name is not None:
            result['AppInstanceTypeName'] = self.app_instance_type_name

        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id

        result['Apps'] = []
        if self.apps is not None:
            for k1 in self.apps:
                result['Apps'].append(k1.to_map() if k1 else None)

        if self.auth_mode is not None:
            result['AuthMode'] = self.auth_mode

        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.max_amount is not None:
            result['MaxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['MinAmount'] = self.min_amount

        result['NodePool'] = []
        if self.node_pool is not None:
            for k1 in self.node_pool:
                result['NodePool'].append(k1.to_map() if k1 else None)

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.ota_info is not None:
            result['OtaInfo'] = self.ota_info.to_map()

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserve_amount_ratio is not None:
            result['ReserveAmountRatio'] = self.reserve_amount_ratio

        if self.reserve_max_amount is not None:
            result['ReserveMaxAmount'] = self.reserve_max_amount

        if self.reserve_min_amount is not None:
            result['ReserveMinAmount'] = self.reserve_min_amount

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes

        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step

        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        if self.status is not None:
            result['Status'] = self.status

        if self.support_user_group_mixed_auth is not None:
            result['SupportUserGroupMixedAuth'] = self.support_user_group_mixed_auth

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_group_auth_mode is not None:
            result['UserGroupAuthMode'] = self.user_group_auth_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')

        if m.get('AppCenterImageName') is not None:
            self.app_center_image_name = m.get('AppCenterImageName')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')

        if m.get('AppInstanceTypeName') is not None:
            self.app_instance_type_name = m.get('AppInstanceTypeName')

        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')

        self.apps = []
        if m.get('Apps') is not None:
            for k1 in m.get('Apps'):
                temp_model = main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k1))

        if m.get('AuthMode') is not None:
            self.auth_mode = m.get('AuthMode')

        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('MaxAmount') is not None:
            self.max_amount = m.get('MaxAmount')

        if m.get('MinAmount') is not None:
            self.min_amount = m.get('MinAmount')

        self.node_pool = []
        if m.get('NodePool') is not None:
            for k1 in m.get('NodePool'):
                temp_model = main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k1))

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OtaInfo') is not None:
            temp_model = main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m.get('OtaInfo'))

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReserveAmountRatio') is not None:
            self.reserve_amount_ratio = m.get('ReserveAmountRatio')

        if m.get('ReserveMaxAmount') is not None:
            self.reserve_max_amount = m.get('ReserveMaxAmount')

        if m.get('ReserveMinAmount') is not None:
            self.reserve_min_amount = m.get('ReserveMinAmount')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')

        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')

        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportUserGroupMixedAuth') is not None:
            self.support_user_group_mixed_auth = m.get('SupportUserGroupMixedAuth')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserGroupAuthMode') is not None:
            self.user_group_auth_mode = m.get('UserGroupAuthMode')

        return self

class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        # 标签键。
        self.key = key
        # 标签类型。
        self.scope = scope
        # 标签值。
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

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(DaraModel):
    def __init__(
        self,
        new_ota_version: str = None,
        ota_version: str = None,
        task_id: str = None,
    ):
        # The new OTA version. A null value indicates that no new version is available.
        self.new_ota_version = new_ota_version
        # The current OTA version.
        self.ota_version = ota_version
        # The ID of the OTA update task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_ota_version is not None:
            result['NewOtaVersion'] = self.new_ota_version

        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewOtaVersion') is not None:
            self.new_ota_version = m.get('NewOtaVersion')

        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(DaraModel):
    def __init__(
        self,
        amount: int = None,
        max_idle_app_instance_amount: int = None,
        max_scaling_amount: int = None,
        node_amount: int = None,
        node_capacity: int = None,
        node_instance_type: str = None,
        node_pool_id: str = None,
        node_type_name: str = None,
        node_used: int = None,
        recurrence_schedules: List[main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_node_amount: int = None,
        scaling_node_used: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        # The number of resources purchased when the delivery group was created.
        self.amount = amount
        # 空闲会话数上限。指定该值时，当会话使用率超过`ScalingUsageThreshold`且当前交付组空闲会话数小于`MaxIdleAppInstanceAmount`时，才会触发自动扩容，否则认为交付组空闲会话已足够使用，不自动扩容。该参数可用于灵活控制弹性扩容行为和降低使用成本。
        self.max_idle_app_instance_amount = max_idle_app_instance_amount
        # The maximum number of resources that can be created for scale-out.
        self.max_scaling_amount = max_scaling_amount
        # The total number of subscription resources.
        self.node_amount = node_amount
        # The maximum number of sessions to which a resource can connect at the same time. If a resource connects to a large number of sessions at the same time, user experience can be compromised. The value range varies based on the resource type. The following items describe the value ranges of different resource types:
        # 
        # *   appstreaming.general.4c8g: 1 to 2
        # *   appstreaming.general.8c16g: 1 to 4
        # *   appstreaming.vgpu.8c16g.4g: 1 to 4
        # *   appstreaming.vgpu.8c31g.16g: 1 to 4
        # *   appstreaming.vgpu.14c93g.12g: 1 to 6
        self.node_capacity = node_capacity
        # The ID of the resource type that you purchase.
        self.node_instance_type = node_instance_type
        # The ID of the resource group.
        self.node_pool_id = node_pool_id
        # The name of the resource type.
        self.node_type_name = node_type_name
        # The number of subscription resources that are in use.
        self.node_used = node_used
        # The schedules of the scaling policy.
        self.recurrence_schedules = recurrence_schedules
        # The duration for which no session is connected. Unit: minutes. If no session is connected in the resources after the specified duration elapses, automatic scale-in is triggered. Default value: 5.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The total number of scalable resources.
        self.scaling_node_amount = scaling_node_amount
        # The number of scalable resources that are in use.
        self.scaling_node_used = scaling_node_used
        # The number of resources that are created each time resources are scaled out. Valid values: 1 to 10.
        self.scaling_step = scaling_step
        # The upper limit of session usage. If the session usage exceeds the specified upper limit, auto scaling is automatically triggered. The session usage is calculated by using the following formula: `Session usage = Number of current sessions/(Total number of resources × Number of concurrent sessions) × 100%`.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The expiration date of the scaling policy. Format: yyyy-MM-dd.
        self.strategy_disable_date = strategy_disable_date
        # The effective date of the scaling policy. Format: yyyy-MM-dd.
        self.strategy_enable_date = strategy_enable_date
        # The type of the scaling policy.
        # 
        # >  `NODE_SCALING_BY_USAGE` is returned for this parameter only if ChargeType is set to `PrePaid`. `NODE_SCALING_BY_SCHEDULE` is returned for this parameter only if ChargeType is set to `PostPaid`.
        # 
        # Valid values:
        # 
        # *   NODE_FIXED: No scalable resources are used.
        # *   NODE_SCALING_BY_SCHEDULE: Scheduled scaling is used.
        # *   NODE_SCALING_BY_USAGE: Resources are scaled based on usage.
        self.strategy_type = strategy_type
        # Indicates whether the warmup policy is enabled for resources.
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
        if self.amount is not None:
            result['Amount'] = self.amount

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

        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id

        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name

        if self.node_used is not None:
            result['NodeUsed'] = self.node_used

        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k1 in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k1.to_map() if k1 else None)

        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes

        if self.scaling_node_amount is not None:
            result['ScalingNodeAmount'] = self.scaling_node_amount

        if self.scaling_node_used is not None:
            result['ScalingNodeUsed'] = self.scaling_node_used

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
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

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

        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')

        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')

        if m.get('NodeUsed') is not None:
            self.node_used = m.get('NodeUsed')

        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k1 in m.get('RecurrenceSchedules'):
                temp_model = main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k1))

        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')

        if m.get('ScalingNodeAmount') is not None:
            self.scaling_node_amount = m.get('ScalingNodeAmount')

        if m.get('ScalingNodeUsed') is not None:
            self.scaling_node_used = m.get('ScalingNodeUsed')

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

class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(DaraModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        # The schedule type of the scaling policy. This parameter must be configured together with `RecurrenceValues`.``
        self.recurrence_type = recurrence_type
        # The days of each week on which the scaling policy is executed.
        self.recurrence_values = recurrence_values
        # The time periods during which the scaling policy can be executed.
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
                temp_model = main_models.GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k1))

        return self

class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(DaraModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The number of destination resources.
        self.amount = amount
        # The end time of the scaling policy. Format: HH:mm.
        self.end_time = end_time
        # The start time of the scaling policy. Format: HH:mm.
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

class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(DaraModel):
    def __init__(
        self,
        app_icon: str = None,
        app_id: str = None,
        app_name: str = None,
        app_version: str = None,
        app_version_name: str = None,
    ):
        # The application icon.
        self.app_icon = app_icon
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application version.
        self.app_version = app_version
        # The name of the application version.
        self.app_version_name = app_version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')

        return self

