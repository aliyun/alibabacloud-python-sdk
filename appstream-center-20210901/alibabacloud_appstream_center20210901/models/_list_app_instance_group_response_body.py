# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListAppInstanceGroupResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_group_models: List[main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The delivery group information.
        self.app_instance_group_models = app_instance_group_models
        # The page number of the query results currently displayed.
        self.page_number = page_number
        # The number of query results per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of query results.
        self.total_count = total_count

    def validate(self):
        if self.app_instance_group_models:
            for v1 in self.app_instance_group_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppInstanceGroupModels'] = []
        if self.app_instance_group_models is not None:
            for k1 in self.app_instance_group_models:
                result['AppInstanceGroupModels'].append(k1.to_map() if k1 else None)

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
        self.app_instance_group_models = []
        if m.get('AppInstanceGroupModels') is not None:
            for k1 in m.get('AppInstanceGroupModels'):
                temp_model = main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModels()
                self.app_instance_group_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAppInstanceGroupResponseBodyAppInstanceGroupModels(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        amount: int = None,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_instance_type: str = None,
        app_policy_id: str = None,
        app_policy_image_check: bool = None,
        app_policy_version: str = None,
        apps: List[main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps] = None,
        auth_mode: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        max_amount: int = None,
        min_amount: int = None,
        node_pool: List[main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool] = None,
        office_site_id: str = None,
        os_type: str = None,
        ota_info: main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo = None,
        product_type: str = None,
        region_id: str = None,
        reserve_amount_ratio: str = None,
        reserve_max_amount: int = None,
        reserve_min_amount: int = None,
        resource_status: str = None,
        resource_tags: List[main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsResourceTags] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        session_timeout: str = None,
        skip_user_auth_check: bool = None,
        spec_id: str = None,
        status: str = None,
        support_user_group_mixed_auth: bool = None,
        tags: List[main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsTags] = None,
        user_group_auth_mode: str = None,
    ):
        # The access type.
        self.access_type = access_type
        # The number of subscription resources configured by the user. Minimum value: 1.
        self.amount = amount
        # The application image ID.
        self.app_center_image_id = app_center_image_id
        # The delivery group ID.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name.
        self.app_instance_group_name = app_instance_group_name
        # The specification type of the delivery group.
        self.app_instance_type = app_instance_type
        # The policy ID.
        self.app_policy_id = app_policy_id
        # Indicates whether the current image supports the unified policy.
        self.app_policy_image_check = app_policy_image_check
        # The policy version.
        self.app_policy_version = app_policy_version
        # The application information.
        self.apps = apps
        # The authorization mode.
        self.auth_mode = auth_mode
        # The sales mode.
        self.charge_resource_mode = charge_resource_mode
        # The billing method.
        self.charge_type = charge_type
        # The expiration time of the delivery group.
        self.expired_time = expired_time
        # The creation time.
        self.gmt_create = gmt_create
        # The maximum number of instances. Minimum value: 1.
        self.max_amount = max_amount
        # The minimum number of instances. Minimum value: 1.
        self.min_amount = min_amount
        # The resource group information.
        self.node_pool = node_pool
        # The office network ID.
        self.office_site_id = office_site_id
        # The operating system type.
        self.os_type = os_type
        # The over-the-air update task information.
        self.ota_info = ota_info
        # The product type.
        self.product_type = product_type
        # The region ID of the delivery group. For more information about supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        self.region_id = region_id
        # The percentage of reserved instances, which represents the ratio of unused sessions in the delivery group. Valid values: 0 to 99.
        self.reserve_amount_ratio = reserve_amount_ratio
        # The maximum number of reserved instances, which represents the maximum number of unused sessions in the delivery group. Minimum value: 1.
        self.reserve_max_amount = reserve_max_amount
        # The minimum number of reserved instances, which represents the minimum number of unused sessions in the delivery group. Minimum value: 1.
        self.reserve_min_amount = reserve_min_amount
        # The resource status.
        self.resource_status = resource_status
        # The list of resource tags.
        self.resource_tags = resource_tags
        # The duration of no session connections, in minutes. When a resource remains in a no-session-connection state for the specified duration, automatic scale-in is triggered. Minimum value: 0.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The number of sessions created during each scale-out event. Minimum value: 1.
        self.scaling_step = scaling_step
        # The upper threshold of session usage (%). When the session usage exceeds this threshold, automatic scale-out is triggered. The formula for session usage is: Session usage = Number of sessions in use ÷ Total number of sessions × 100%. Valid values: 0 to 99.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The session disconnection retention duration, in minutes. After an end user session is disconnected, the session is retained for the specified duration before being logged off. Set this parameter to `-1` to retain the session indefinitely. Valid values: -1 and 3 to 300. Default value: `15`.
        self.session_timeout = session_timeout
        # Indicates whether user authorization verification is skipped.
        self.skip_user_auth_check = skip_user_auth_check
        # The ID that uniquely corresponds to the delivery group ID.
        self.spec_id = spec_id
        # The delivery group status.
        self.status = status
        self.support_user_group_mixed_auth = support_user_group_mixed_auth
        # The list of resource tags.
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
        if self.resource_tags:
            for v1 in self.resource_tags:
                 if v1:
                    v1.validate()
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

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type

        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id

        if self.app_policy_image_check is not None:
            result['AppPolicyImageCheck'] = self.app_policy_image_check

        if self.app_policy_version is not None:
            result['AppPolicyVersion'] = self.app_policy_version

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

        result['ResourceTags'] = []
        if self.resource_tags is not None:
            for k1 in self.resource_tags:
                result['ResourceTags'].append(k1.to_map() if k1 else None)

        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes

        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step

        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

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

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')

        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')

        if m.get('AppPolicyImageCheck') is not None:
            self.app_policy_image_check = m.get('AppPolicyImageCheck')

        if m.get('AppPolicyVersion') is not None:
            self.app_policy_version = m.get('AppPolicyVersion')

        self.apps = []
        if m.get('Apps') is not None:
            for k1 in m.get('Apps'):
                temp_model = main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
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
                temp_model = main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k1))

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OtaInfo') is not None:
            temp_model = main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
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

        self.resource_tags = []
        if m.get('ResourceTags') is not None:
            for k1 in m.get('ResourceTags'):
                temp_model = main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')

        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')

        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

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
                temp_model = main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserGroupAuthMode') is not None:
            self.user_group_auth_mode = m.get('UserGroupAuthMode')

        return self

class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag type.
        self.scope = scope
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

class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsResourceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag type.
        self.scope = scope
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

class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(DaraModel):
    def __init__(
        self,
        new_ota_version: str = None,
        ota_version: str = None,
        task_id: str = None,
    ):
        # The new OTA version. An empty value indicates that no new version is available.
        self.new_ota_version = new_ota_version
        # The current OTA version.
        self.ota_version = ota_version
        # The OTA upgrade task ID.
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

class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(DaraModel):
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
        recurrence_schedules: List[main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules] = None,
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
        # The upper limit of idle sessions. When this value is specified, automatic scale-out is triggered only when the session usage exceeds `ScalingUsageThreshold` and the number of idle sessions in the delivery group is less than `MaxIdleAppInstanceAmount`. Otherwise, the delivery group is considered to have sufficient idle sessions and no automatic scale-out is performed. This parameter allows you to flexibly control elastic scaling behavior and reduce costs.
        self.max_idle_app_instance_amount = max_idle_app_instance_amount
        # The maximum number of resources that can be created during scale-out.
        self.max_scaling_amount = max_scaling_amount
        # The total number of current subscription resources.
        self.node_amount = node_amount
        # The number of concurrent sessions, which is the number of sessions that a single resource can handle simultaneously. Too many simultaneous sessions may degrade the application experience. The valid values vary depending on the resource specification.
        self.node_capacity = node_capacity
        # The specification type ID of the purchased resources.
        self.node_instance_type = node_instance_type
        # The resource group ID.
        self.node_pool_id = node_pool_id
        # The resource specification name.
        self.node_type_name = node_type_name
        # The resource count of subscription resources in use.
        self.node_used = node_used
        # The list of policy execution cycles.
        self.recurrence_schedules = recurrence_schedules
        # The duration of no session connections, in minutes. When a resource remains in a no-session-connection state for the specified duration, automatic scale-in is triggered. Default value: 5.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The total number of elastic resources.
        self.scaling_node_amount = scaling_node_amount
        # The resource count of elastic resources in use.
        self.scaling_node_used = scaling_node_used
        # The number of resources created during each scale-out event. Valid values: 1 to 10.
        self.scaling_step = scaling_step
        # The upper threshold of session usage (%). When the session usage exceeds this threshold, automatic scale-out is triggered. The formula for session usage is: `Session usage = Number of current sessions ÷ (Total number of resources × Concurrent sessions per resource) × 100%`.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The date when the policy expires. Format: yyyy-MM-dd.
        self.strategy_disable_date = strategy_disable_date
        # The date when the policy takes effect. Format: yyyy-MM-dd.
        self.strategy_enable_date = strategy_enable_date
        # The elastic policy type.
        # 
        # > `NODE_SCALING_BY_USAGE` (usage-based scaling policy) applies only to `PrePaid` (subscription) resources. `NODE_SCALING_BY_SCHEDULE` (scheduled scaling policy) applies only to `PostPaid` (pay-as-you-go) resources.
        self.strategy_type = strategy_type
        # Indicates whether the resource prefetch policy is enabled.
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
                temp_model = main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
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

class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(DaraModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        # The type of the policy execution cycle. You must specify both `RecurrenceType` and `RecurrenceValues`.
        self.recurrence_type = recurrence_type
        # The list of values for the policy execution cycle.
        self.recurrence_values = recurrence_values
        # The list of time periods for the policy execution cycle.
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
                temp_model = main_models.ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k1))

        return self

class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(DaraModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The target resource count.
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

class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(DaraModel):
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
        # The application version name.
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

