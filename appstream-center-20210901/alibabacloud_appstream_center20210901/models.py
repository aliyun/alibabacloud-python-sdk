# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ApproveOtaTaskRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        ota_type: str = None,
        start_time: str = None,
        task_id: str = None,
    ):
        # The ID of the delivery group. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the region where the delivery group resides. You can call the [ListRegions](https://help.aliyun.com/document_detail/428500.html) operation to query the list of regions supported by App Streaming.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The type of the OTA update task.
        # 
        # Valid values:
        # 
        # *   Fota: update of the system components of Alibaba Cloud Workspace
        # *   AppUpdate
        # *   ImageUpdate
        # 
        # This parameter is required.
        self.ota_type = ota_type
        # The start time of the OTA update task. The time follows the ISO 8601 standard.
        # 
        # This parameter is required.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.start_time = start_time
        # The ID of the OTA update task. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # >  Each successful call to the `ApproveOtaTask` operation causes a value change of this parameter.`` Before you call this operation, call the `ListAppInstanceGroup` operation again to obtain the latest value of this parameter.``
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ApproveOtaTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The execution result. If the request was successful, `success` is returned. If the request failed, an error message is returned.
        self.code = code
        # The error message. If the value of `Code` is `success`, this parameter is not returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApproveOtaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApproveOtaTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApproveOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeInstanceGroupRequestUserMeta(TeaModel):
    def __init__(
        self,
        ad_domain: str = None,
        type: str = None,
    ):
        # The AD domain name.
        self.ad_domain = ad_domain
        # The user type.
        # 
        # Valid values:
        # 
        # *   ad: Active Directory (AD) account
        # *   simple: convenience account
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AuthorizeInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_persistent_id: str = None,
        authorize_user_group_ids: List[str] = None,
        authorize_user_ids: List[str] = None,
        avatar_id: str = None,
        product_type: str = None,
        un_authorize_user_group_ids: List[str] = None,
        un_authorize_user_ids: List[str] = None,
        user_meta: AuthorizeInstanceGroupRequestUserMeta = None,
    ):
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # 持久会话ID。
        self.app_instance_persistent_id = app_instance_persistent_id
        self.authorize_user_group_ids = authorize_user_group_ids
        # The IDs of the users that you want to add to the authorization list of the delivery group. You can specify 1 to 100 user IDs.
        self.authorize_user_ids = authorize_user_ids
        self.avatar_id = avatar_id
        # This parameter is required.
        self.product_type = product_type
        self.un_authorize_user_group_ids = un_authorize_user_group_ids
        # The IDs of the users that you want to remove from the authorization list of the delivery group. You can specify 1 to 100 user IDs.
        self.un_authorize_user_ids = un_authorize_user_ids
        # The user information.
        self.user_meta = user_meta

    def validate(self):
        if self.user_meta:
            self.user_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.authorize_user_group_ids is not None:
            result['AuthorizeUserGroupIds'] = self.authorize_user_group_ids
        if self.authorize_user_ids is not None:
            result['AuthorizeUserIds'] = self.authorize_user_ids
        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.un_authorize_user_group_ids is not None:
            result['UnAuthorizeUserGroupIds'] = self.un_authorize_user_group_ids
        if self.un_authorize_user_ids is not None:
            result['UnAuthorizeUserIds'] = self.un_authorize_user_ids
        if self.user_meta is not None:
            result['UserMeta'] = self.user_meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('AuthorizeUserGroupIds') is not None:
            self.authorize_user_group_ids = m.get('AuthorizeUserGroupIds')
        if m.get('AuthorizeUserIds') is not None:
            self.authorize_user_ids = m.get('AuthorizeUserIds')
        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UnAuthorizeUserGroupIds') is not None:
            self.un_authorize_user_group_ids = m.get('UnAuthorizeUserGroupIds')
        if m.get('UnAuthorizeUserIds') is not None:
            self.un_authorize_user_ids = m.get('UnAuthorizeUserIds')
        if m.get('UserMeta') is not None:
            temp_model = AuthorizeInstanceGroupRequestUserMeta()
            self.user_meta = temp_model.from_map(m['UserMeta'])
        return self


class AuthorizeInstanceGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_persistent_id: str = None,
        authorize_user_group_ids: List[str] = None,
        authorize_user_ids: List[str] = None,
        avatar_id: str = None,
        product_type: str = None,
        un_authorize_user_group_ids: List[str] = None,
        un_authorize_user_ids: List[str] = None,
        user_meta_shrink: str = None,
    ):
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # 持久会话ID。
        self.app_instance_persistent_id = app_instance_persistent_id
        self.authorize_user_group_ids = authorize_user_group_ids
        # The IDs of the users that you want to add to the authorization list of the delivery group. You can specify 1 to 100 user IDs.
        self.authorize_user_ids = authorize_user_ids
        self.avatar_id = avatar_id
        # This parameter is required.
        self.product_type = product_type
        self.un_authorize_user_group_ids = un_authorize_user_group_ids
        # The IDs of the users that you want to remove from the authorization list of the delivery group. You can specify 1 to 100 user IDs.
        self.un_authorize_user_ids = un_authorize_user_ids
        # The user information.
        self.user_meta_shrink = user_meta_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.authorize_user_group_ids is not None:
            result['AuthorizeUserGroupIds'] = self.authorize_user_group_ids
        if self.authorize_user_ids is not None:
            result['AuthorizeUserIds'] = self.authorize_user_ids
        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.un_authorize_user_group_ids is not None:
            result['UnAuthorizeUserGroupIds'] = self.un_authorize_user_group_ids
        if self.un_authorize_user_ids is not None:
            result['UnAuthorizeUserIds'] = self.un_authorize_user_ids
        if self.user_meta_shrink is not None:
            result['UserMeta'] = self.user_meta_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('AuthorizeUserGroupIds') is not None:
            self.authorize_user_group_ids = m.get('AuthorizeUserGroupIds')
        if m.get('AuthorizeUserIds') is not None:
            self.authorize_user_ids = m.get('AuthorizeUserIds')
        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UnAuthorizeUserGroupIds') is not None:
            self.un_authorize_user_group_ids = m.get('UnAuthorizeUserGroupIds')
        if m.get('UnAuthorizeUserIds') is not None:
            self.un_authorize_user_ids = m.get('UnAuthorizeUserIds')
        if m.get('UserMeta') is not None:
            self.user_meta_shrink = m.get('UserMeta')
        return self


class AuthorizeInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AuthorizeInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppInstanceGroupRequestNetworkDomainRules(TeaModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The policy used for the domain name.
        # 
        # Valid values:
        # 
        # *   allow
        # *   block
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppInstanceGroupRequestNetworkRoutes(TeaModel):
    def __init__(
        self,
        destination: str = None,
        mode: str = None,
    ):
        # The destination. The value is a CIDR block.
        self.destination = destination
        # The network egress mode.
        # 
        # Valid value:
        # 
        # *   Shared: accesses the network by using NAT Gateway.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppInstanceGroupRequestNetwork(TeaModel):
    def __init__(
        self,
        domain_rules: List[CreateAppInstanceGroupRequestNetworkDomainRules] = None,
        ip_expire_minutes: int = None,
        office_site_id: str = None,
        routes: List[CreateAppInstanceGroupRequestNetworkRoutes] = None,
        strategy_type: str = None,
        v_switch_ids: List[str] = None,
    ):
        # The domain name rules.
        self.domain_rules = domain_rules
        # The validity period of the public IP address. If the specified value is exceeded, the IP address is updated at next logon. Minimum value: 60. Unit: minutes.
        self.ip_expire_minutes = ip_expire_minutes
        # Office Network ID.
        self.office_site_id = office_site_id
        # The route settings. This parameter is available only if you set `StrategyType` to `Mixed`.
        self.routes = routes
        # The type of the network policy.
        # 
        # Valid values:
        # 
        # *   Mixed: the hybrid mode. In this mode, a device is deployed in one virtual private cloud (VPC). Two NICs are provided and an independent public IP address is configured for the device.
        # *   Shared: the shared mode. In this mode, a single NIC is provided for a device and the network is accessed by using NAT Gateway.
        self.strategy_type = strategy_type
        # List of virtual switch IDs.
        # - Valid only for custom office networks.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.domain_rules:
            for k in self.domain_rules:
                if k:
                    k.validate()
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainRules'] = []
        if self.domain_rules is not None:
            for k in self.domain_rules:
                result['DomainRules'].append(k.to_map() if k else None)
        if self.ip_expire_minutes is not None:
            result['IpExpireMinutes'] = self.ip_expire_minutes
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        result['Routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['Routes'].append(k.to_map() if k else None)
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_rules = []
        if m.get('DomainRules') is not None:
            for k in m.get('DomainRules'):
                temp_model = CreateAppInstanceGroupRequestNetworkDomainRules()
                self.domain_rules.append(temp_model.from_map(k))
        if m.get('IpExpireMinutes') is not None:
            self.ip_expire_minutes = m.get('IpExpireMinutes')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        self.routes = []
        if m.get('Routes') is not None:
            for k in m.get('Routes'):
                temp_model = CreateAppInstanceGroupRequestNetworkRoutes()
                self.routes.append(temp_model.from_map(k))
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The number of resources.
        self.amount = amount
        # The end time of the time period. Format: HH:mm.
        self.end_time = end_time
        # The start time of the time period. Format: HH:mm.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules(TeaModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        # The schedule type of the scaling policy. This parameter must be configured together with `RecurrenceValues`.``
        # 
        # Valid value:
        # 
        # *   Weekly: The scaling policy is executed on specific days each week.
        self.recurrence_type = recurrence_type
        # The days of each week on which the scaling policy is executed.
        self.recurrence_values = recurrence_values
        # The time periods during which the scaling policy can be executed. The time periods must meet the following requirements:
        # 
        # *   Up to three time periods can be added.
        # *   Time periods cannot be overlapped.
        # *   The interval between two consecutive time periods must be greater than or equal to 5 minutes.
        # *   Each time period must be greater than or equal to 15 minutes.
        # *   The total length of the time periods that you specify cannot be greater than a day.
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class CreateAppInstanceGroupRequestNodePool(TeaModel):
    def __init__(
        self,
        max_idle_app_instance_amount: int = None,
        max_scaling_amount: int = None,
        node_amount: int = None,
        node_capacity: int = None,
        node_instance_type: str = None,
        recurrence_schedules: List[CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        # Maximum number of idle sessions. When this value is specified, auto-scaling is triggered only if the session utilization exceeds `ScalingUsageThreshold` and the current number of idle sessions in the delivery group is less than `MaxIdleAppInstanceAmount`. Otherwise, it is considered that sufficient idle sessions are available, and no auto-scaling will occur. This parameter allows flexible control over elastic scaling behavior and helps reduce usage costs.
        self.max_idle_app_instance_amount = max_idle_app_instance_amount
        # The maximum number of resources that can be created for scale-out. This parameter is required if you set `StrategyType` to `NODE_SCALING_BY_USAGE`.
        self.max_scaling_amount = max_scaling_amount
        # The number of resources that you want to purchase. Valid values: 1 to 100.
        # 
        # > 
        # 
        # *   This parameter is required if the resources are subscription resources.
        # 
        # *   If the resources are pay-as-you-go resources, this parameter is required only if you set `StrategyType` to `NODE_FIXED` or `NODE_SCALING_BY_USAGE`.
        self.node_amount = node_amount
        # The maximum number of sessions to which a resource can connect at the same time. If a resource connects to a large number of sessions at the same time, the user experience can be compromised. The value range varies based on the resource type. The following items describe the value ranges of different resource types:
        # 
        # *   appstreaming.general.4c8g: 1 to 2
        # *   appstreaming.general.8c16g: 1 to 4
        # *   appstreaming.vgpu.8c16g.4g: 1 to 4
        # *   appstreaming.vgpu.8c31g.16g: 1 to 4
        # *   appstreaming.vgpu.14c93g.12g: 1 to 6
        self.node_capacity = node_capacity
        # The ID of the resource type that you want to purchase. You can call the [ListNodeInstanceType](https://help.aliyun.com/document_detail/428502.html) operation to obtain the ID.
        # 
        # Valid values:
        # 
        # *   appstreaming.vgpu.8c16g.4g: WUYING - Graphics_8 vCPUs, 16 GiB Memory, 4 GiB GPU Memory
        # *   appstreaming.general.8c16g: WUYING - General_8 vCPUs, 16 GiB Memory
        # *   appstreaming.general.4c8g: WUYING - General_4 vCPUs, 8 GiB Memory
        # *   appstreaming.vgpu.14c93g.12g: WUYING - Graphics_14 vCPUs, 93 GiB Memory, 12 GiB GPU Memory.
        # *   appstreaming.vgpu.8c31g.16g: WUYING - Graphics_8 vCPUs, 31 GiB Memory, 16 GiB GPU Memory
        self.node_instance_type = node_instance_type
        # The schedules of the scaling policy. This parameter is required if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.recurrence_schedules = recurrence_schedules
        # The maximum retention period of a resource to which no session is connected. If no session is connected to a resource, the resource is automatically scaled in after the specified retention period elapses. Valid values: 5 to 120. Default value: 5. Unit: minutes. If one of the following situations occurs, the resource is not scaled in.
        # 
        # *   If automatic scale-out is triggered after the resource is scaled in, the scale-in is not executed. This prevents repeated scale-in and scale-out.
        # *   If automatic scale-out is triggered due to an increase in the number of sessions during the specified period of time, the resource is not scaled in and the countdown restarts.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The number of resources that are created each time resources are scaled out. Valid values: 1 to 10. This parameter is required if you set `StrategyType` to `NODE_SCALING_BY_USAGE`.
        self.scaling_step = scaling_step
        # The upper limit of session usage. If the session usage exceeds the specified upper limit, auto scaling is automatically triggered. The session usage is calculated by using the following formula: `Session usage = Number of current sessions/(Total number of resources × Number of concurrent sessions) × 100%`. This parameter is required if you set `StrategyType` to `NODE_SCALING_BY_USAGE`. Valid values: 0 to 100. Default value: 85.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The expiration date of the scaling policy. Format: yyyy-MM-dd. The interval between the expiration date and the effective date must be from 7 days to 1 year. This parameter is required if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.strategy_disable_date = strategy_disable_date
        # The effective date of the scaling policy. Format: yyyy-MM-dd. The date must be the same as or later than the current date. This parameter is required if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.strategy_enable_date = strategy_enable_date
        # The scaling policy of resources.
        # 
        # > 
        # 
        # *   `NODE_FIXED`: fixed number of resources. This value is applicable to pay-as-you-go resources and subscription resources.
        # 
        # *   `NODE_SCALING_BY_USAGE`: auto scaling. This value is applicable to pay-as-you-go resources and subscription resources.
        # 
        # *   `NODE_SCALING_BY_SCHEDULE`: scheduled scaling. This value is applicable only to pay-as-you-go resources.
        # 
        # Valid values:
        # 
        # *   NODE_FIXED: fixed number of resources
        # *   NODE_SCALING_BY_SCHEDULE: scheduled scaling
        # *   NODE_SCALING_BY_USAGE: auto scaling
        self.strategy_type = strategy_type
        # Specifies whether to enable the warmup policy for resources. This parameter is required if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
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
            for k in m.get('RecurrenceSchedules'):
                temp_model = CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
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


class CreateAppInstanceGroupRequestRuntimePolicy(TeaModel):
    def __init__(
        self,
        debug_mode: str = None,
        per_session_per_app: bool = None,
        persistent_app_instance_schedule_mode: str = None,
        session_pre_open: str = None,
        session_type: str = None,
        session_user_generation_mode: str = None,
    ):
        # Specifies whether to enable the debugging mode. If you want to call the `GetDebugAppInstance` and `CreateImageFromAppInstanceGroup` operations, you must set this parameter to `ON`.
        # 
        # Valid values:
        # 
        # *   OFF
        # *   ON
        self.debug_mode = debug_mode
        # Only one application is allowed to be opened within a single session.
        # 
        # - When enabled, launching multiple applications from the delivery group will allocate a separate session for each application, resulting in higher session consumption.
        self.per_session_per_app = per_session_per_app
        # Persistent session scheduling mode.
        self.persistent_app_instance_schedule_mode = persistent_app_instance_schedule_mode
        # Session pre-launch toggle.
        # 
        # - If not specified, the default value is true.
        self.session_pre_open = session_pre_open
        # The session type.
        # 
        # Valid values:
        # 
        # *   CONSOLE: console session
        # *   NORMAL: Remote Desktop Protocol (RDP)-based O\\&M session
        self.session_type = session_type
        # The generation mode of the session users. Valid value:
        # - wyid. In this case, you must set sessionPreOpen to false.
        self.session_user_generation_mode = session_user_generation_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppInstanceGroupRequestSecurityPolicy(TeaModel):
    def __init__(
        self,
        reset_after_unbind: bool = None,
        skip_user_auth_check: bool = None,
    ):
        # Specifies whether to reset after unbinding from a delivery group.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.reset_after_unbind = reset_after_unbind
        # Specifies whether to skip user permission verification.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: This is the default value.
        self.skip_user_auth_check = skip_user_auth_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppInstanceGroupRequestStoragePolicyUserProfile(TeaModel):
    def __init__(
        self,
        remote_storage_path: str = None,
        remote_storage_type: str = None,
        user_profile_switch: bool = None,
    ):
        # Remote storage path for user data roaming.
        # 
        # - If left empty, the default value is the delivery group ID.
        # - For cross-delivery-group (within the same VPC) user data roaming, the same value must be configured for all participating delivery groups.
        self.remote_storage_path = remote_storage_path
        # Remote storage type used for user data roaming.
        self.remote_storage_type = remote_storage_type
        # User data roaming toggle.
        self.user_profile_switch = user_profile_switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppInstanceGroupRequestStoragePolicy(TeaModel):
    def __init__(
        self,
        storage_type_list: List[str] = None,
        user_profile: CreateAppInstanceGroupRequestStoragePolicyUserProfile = None,
    ):
        # The storage types.
        self.storage_type_list = storage_type_list
        # User data roaming configuration.
        self.user_profile = user_profile

    def validate(self):
        if self.user_profile:
            self.user_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateAppInstanceGroupRequestStoragePolicyUserProfile()
            self.user_profile = temp_model.from_map(m['UserProfile'])
        return self


class CreateAppInstanceGroupRequestUserDefinePolicy(TeaModel):
    def __init__(
        self,
        custom_config: str = None,
    ):
        # The content of the custom policy. The content must meet the specifications of image versions. To use this parameter, submit a ticket to apply to enable the whitelist feature.
        self.custom_config = custom_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_config is not None:
            result['CustomConfig'] = self.custom_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomConfig') is not None:
            self.custom_config = m.get('CustomConfig')
        return self


class CreateAppInstanceGroupRequestUserInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The account type of the user.
        # 
        # Valid value:
        # 
        # *   Simple: convenience account
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppInstanceGroupRequestVideoPolicy(TeaModel):
    def __init__(
        self,
        frame_rate: int = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        streaming_mode: str = None,
        terminal_resolution_adaptive: bool = None,
        webrtc: bool = None,
    ):
        # Frame rate (FPS).
        self.frame_rate = frame_rate
        # Resolution height, in pixels.
        self.session_resolution_height = session_resolution_height
        # Resolution width, in pixels.
        self.session_resolution_width = session_resolution_width
        # Streaming mode. Combined with the Webrtc parameter, it indicates the protocol type.
        # 
        # - When Webrtc=true and StreamingMode=video, it indicates a WebRTC stream.
        # - When Webrtc=false and StreamingMode=video, it indicates a video stream.
        # - When Webrtc=false and StreamingMode=mix, it indicates a mixed stream.
        self.streaming_mode = streaming_mode
        # Whether to use adaptive resolution.
        # 
        # - true: The session resolution follows changes in the terminal\\"s display area. In this case, SessionResolutionWidth and SessionResolutionHeight represent the maximum values for resolution adjustment.
        # 
        # - false: The session resolution does not follow changes in the terminal\\"s display area. In this case, the resolution is fixed to the values of SessionResolutionWidth and SessionResolutionHeight.
        self.terminal_resolution_adaptive = terminal_resolution_adaptive
        # Whether to enable WebRTC. Combined with the StreamingMode parameter, it indicates the protocol type.
        # 
        # - When Webrtc=true and StreamingMode=video, it indicates a WebRTC stream.
        # - When Webrtc=false and StreamingMode=video, it indicates a video stream.
        # - When Webrtc=false and StreamingMode=mix, it indicates a mixed stream.
        self.webrtc = webrtc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppInstanceGroupRequest(TeaModel):
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
        network: CreateAppInstanceGroupRequestNetwork = None,
        node_pool: CreateAppInstanceGroupRequestNodePool = None,
        period: int = None,
        period_unit: str = None,
        pre_open_app_id: str = None,
        product_type: str = None,
        promotion_id: str = None,
        runtime_policy: CreateAppInstanceGroupRequestRuntimePolicy = None,
        security_policy: CreateAppInstanceGroupRequestSecurityPolicy = None,
        session_timeout: int = None,
        storage_policy: CreateAppInstanceGroupRequestStoragePolicy = None,
        sub_pay_type: str = None,
        user_define_policy: CreateAppInstanceGroupRequestUserDefinePolicy = None,
        user_group_ids: List[str] = None,
        user_info: CreateAppInstanceGroupRequestUserInfo = None,
        users: List[str] = None,
        video_policy: CreateAppInstanceGroupRequestVideoPolicy = None,
    ):
        # The image ID of the application. To obtain the image ID, log on to the [App Streaming console](https://appstreaming.console.aliyun.com/). In the left-side navigation pane, choose **Maintenance** > **Custom Images** or Maintenance > **System Images**.
        # 
        # This parameter is required.
        self.app_center_image_id = app_center_image_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # Package type.
        self.app_package_type = app_package_type
        # Policy ID.
        self.app_policy_id = app_policy_id
        # The authentication mode of the delivery group.
        self.auth_mode = auth_mode
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_renew = auto_renew
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-hangzhou: China (Hangzhou)
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The sales mode.
        # 
        # Valid value:
        # 
        # *   Node: by resource
        # 
        # This parameter is required.
        self.charge_resource_mode = charge_resource_mode
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # Cluster ID.
        self.cluster_id = cluster_id
        # The network settings.
        # 
        # >  If you want to use this parameter, submit a ticket.
        self.network = network
        # The node pool object.
        self.node_pool = node_pool
        # The subscription duration of resources. This parameter is required if you set `ChargeType` to `PrePaid`. The unit of this parameter is specified by `PeriodUnit`.
        # 
        # *   Valid value if you set `PeriodUnit` to `Week`:
        # 
        #     *   1
        # 
        # *   Valid values if you set `PeriodUnit` to `Month`:
        # 
        #     *   1
        #     *   2
        #     *   3
        #     *   6
        # 
        # *   Valid values if you set `PeriodUnit` to `Year`:
        # 
        #     *   1
        #     *   2
        #     *   3
        # 
        # >  If you set `ChargeType` to `PostPaid`, set this parameter to 1.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration. This parameter is available if you set `ChargeType` to `PrePaid`.
        # 
        # >  The value of this parameter is case-insensitive. For example, `Week` is valid and `week` is invalid. If you specify an invalid value combination for Period and PeriodUnit, such as `2 Week`, the operation can still be called. However, an error occurs when you place the order.
        # 
        # >  If you set `ChargeType` to `PostPaid`, set this parameter to `Month`.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Week
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The ID of the pre-open application.
        self.pre_open_app_id = pre_open_app_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The promotion ID. You can call the [GetResourcePrice](https://help.aliyun.com/document_detail/428503.html) operation to obtain the ID.
        self.promotion_id = promotion_id
        # The runtime policy.
        self.runtime_policy = runtime_policy
        # The security policy.
        self.security_policy = security_policy
        # The period of time during which the application can be recycled. The recycling period is the period of time between the time when the end user disconnects from the application and the time when processes exit the application. If you do not want to recycle the application, set this parameter to `-1`. Valid values:-1 and 3 to 300. The value must be an integer. Default value: `15`. Unit: minutes.
        # 
        # This parameter is required.
        self.session_timeout = session_timeout
        # The storage policy.
        self.storage_policy = storage_policy
        # Payment method subtype.
        self.sub_pay_type = sub_pay_type
        # The custom policy.
        self.user_define_policy = user_define_policy
        # List of authorized user group IDs.
        self.user_group_ids = user_group_ids
        # The information about the user that you want to add to the assigned user list of the delivery group. This parameter is required if you configure `Users`.
        self.user_info = user_info
        # The users that you want to add to the assigned user list of the delivery group.
        self.users = users
        # Display policy.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateAppInstanceGroupRequestNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('NodePool') is not None:
            temp_model = CreateAppInstanceGroupRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
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
            temp_model = CreateAppInstanceGroupRequestRuntimePolicy()
            self.runtime_policy = temp_model.from_map(m['RuntimePolicy'])
        if m.get('SecurityPolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m['SecurityPolicy'])
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m['StoragePolicy'])
        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')
        if m.get('UserDefinePolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestUserDefinePolicy()
            self.user_define_policy = temp_model.from_map(m['UserDefinePolicy'])
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserInfo') is not None:
            temp_model = CreateAppInstanceGroupRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('Users') is not None:
            self.users = m.get('Users')
        if m.get('VideoPolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestVideoPolicy()
            self.video_policy = temp_model.from_map(m['VideoPolicy'])
        return self


class CreateAppInstanceGroupShrinkRequest(TeaModel):
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
        network_shrink: str = None,
        node_pool_shrink: str = None,
        period: int = None,
        period_unit: str = None,
        pre_open_app_id: str = None,
        product_type: str = None,
        promotion_id: str = None,
        runtime_policy_shrink: str = None,
        security_policy_shrink: str = None,
        session_timeout: int = None,
        storage_policy_shrink: str = None,
        sub_pay_type: str = None,
        user_define_policy_shrink: str = None,
        user_group_ids: List[str] = None,
        user_info_shrink: str = None,
        users: List[str] = None,
        video_policy_shrink: str = None,
    ):
        # The image ID of the application. To obtain the image ID, log on to the [App Streaming console](https://appstreaming.console.aliyun.com/). In the left-side navigation pane, choose **Maintenance** > **Custom Images** or Maintenance > **System Images**.
        # 
        # This parameter is required.
        self.app_center_image_id = app_center_image_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # Package type.
        self.app_package_type = app_package_type
        # Policy ID.
        self.app_policy_id = app_policy_id
        # The authentication mode of the delivery group.
        self.auth_mode = auth_mode
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_renew = auto_renew
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-hangzhou: China (Hangzhou)
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The sales mode.
        # 
        # Valid value:
        # 
        # *   Node: by resource
        # 
        # This parameter is required.
        self.charge_resource_mode = charge_resource_mode
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # Cluster ID.
        self.cluster_id = cluster_id
        # The network settings.
        # 
        # >  If you want to use this parameter, submit a ticket.
        self.network_shrink = network_shrink
        # The node pool object.
        self.node_pool_shrink = node_pool_shrink
        # The subscription duration of resources. This parameter is required if you set `ChargeType` to `PrePaid`. The unit of this parameter is specified by `PeriodUnit`.
        # 
        # *   Valid value if you set `PeriodUnit` to `Week`:
        # 
        #     *   1
        # 
        # *   Valid values if you set `PeriodUnit` to `Month`:
        # 
        #     *   1
        #     *   2
        #     *   3
        #     *   6
        # 
        # *   Valid values if you set `PeriodUnit` to `Year`:
        # 
        #     *   1
        #     *   2
        #     *   3
        # 
        # >  If you set `ChargeType` to `PostPaid`, set this parameter to 1.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration. This parameter is available if you set `ChargeType` to `PrePaid`.
        # 
        # >  The value of this parameter is case-insensitive. For example, `Week` is valid and `week` is invalid. If you specify an invalid value combination for Period and PeriodUnit, such as `2 Week`, the operation can still be called. However, an error occurs when you place the order.
        # 
        # >  If you set `ChargeType` to `PostPaid`, set this parameter to `Month`.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Week
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The ID of the pre-open application.
        self.pre_open_app_id = pre_open_app_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The promotion ID. You can call the [GetResourcePrice](https://help.aliyun.com/document_detail/428503.html) operation to obtain the ID.
        self.promotion_id = promotion_id
        # The runtime policy.
        self.runtime_policy_shrink = runtime_policy_shrink
        # The security policy.
        self.security_policy_shrink = security_policy_shrink
        # The period of time during which the application can be recycled. The recycling period is the period of time between the time when the end user disconnects from the application and the time when processes exit the application. If you do not want to recycle the application, set this parameter to `-1`. Valid values:-1 and 3 to 300. The value must be an integer. Default value: `15`. Unit: minutes.
        # 
        # This parameter is required.
        self.session_timeout = session_timeout
        # The storage policy.
        self.storage_policy_shrink = storage_policy_shrink
        # Payment method subtype.
        self.sub_pay_type = sub_pay_type
        # The custom policy.
        self.user_define_policy_shrink = user_define_policy_shrink
        # List of authorized user group IDs.
        self.user_group_ids = user_group_ids
        # The information about the user that you want to add to the assigned user list of the delivery group. This parameter is required if you configure `Users`.
        self.user_info_shrink = user_info_shrink
        # The users that you want to add to the assigned user list of the delivery group.
        self.users = users
        # Display policy.
        self.video_policy_shrink = video_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.network_shrink is not None:
            result['Network'] = self.network_shrink
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
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
        if self.runtime_policy_shrink is not None:
            result['RuntimePolicy'] = self.runtime_policy_shrink
        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink
        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type
        if self.user_define_policy_shrink is not None:
            result['UserDefinePolicy'] = self.user_define_policy_shrink
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        if self.users is not None:
            result['Users'] = self.users
        if self.video_policy_shrink is not None:
            result['VideoPolicy'] = self.video_policy_shrink
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
            self.network_shrink = m.get('Network')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
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
            self.runtime_policy_shrink = m.get('RuntimePolicy')
        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')
        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')
        if m.get('UserDefinePolicy') is not None:
            self.user_define_policy_shrink = m.get('UserDefinePolicy')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        if m.get('VideoPolicy') is not None:
            self.video_policy_shrink = m.get('VideoPolicy')
        return self


class CreateAppInstanceGroupResponseBodyAppInstanceGroupModel(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        node_pool_id: str = None,
        order_id: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the resource group. This parameter is returned if a resource group was created.
        self.node_pool_id = node_pool_id
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_model: CreateAppInstanceGroupResponseBodyAppInstanceGroupModel = None,
        request_id: str = None,
    ):
        # The delivery group.
        self.app_instance_group_model = app_instance_group_model
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_instance_group_model:
            self.app_instance_group_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_model is not None:
            result['AppInstanceGroupModel'] = self.app_instance_group_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupModel') is not None:
            temp_model = CreateAppInstanceGroupResponseBodyAppInstanceGroupModel()
            self.app_instance_group_model = temp_model.from_map(m['AppInstanceGroupModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageByInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_clean_userdata: bool = None,
        biz_type: int = None,
        description: str = None,
        disk_type: str = None,
        image_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        product_type: str = None,
        sub_instance_id: str = None,
    ):
        # This parameter is applicable only to scenarios in which the instance type is Cloud Desktop. Specifies whether to clear private data of users. If this parameter is set to true, the created image clears data in directories other than Administrator and Public in the C:\\Users directory.
        # 
        # Valid values:
        # 
        # *   true: cleanup.
        # *   false: does not clear.
        self.auto_clean_userdata = auto_clean_userdata
        # This parameter is not publicly available.
        self.biz_type = biz_type
        # The description of the image.
        self.description = description
        # The type of disk data contained in the image. By default, the system disk and data disk of the instance are included.
        # 
        # Valid values:
        # 
        # *   SYSTEM: only system disk.
        # *   ALL: system disk + data disk
        self.disk_type = disk_type
        # The name of the image.
        self.image_name = image_name
        # The ID of the RDS instance. The instance can be a CloudDesktop instance, a workstation instance. To ensure data consistency in the image, we recommend that you shut down the instance before you create an image.
        self.instance_id = instance_id
        # The instance type.
        # 
        # Valid values:
        # 
        # *   CloudDesktop: Cloud Desktop.
        # *   WuyingServer: Workstation
        self.instance_type = instance_type
        # This parameter is not publicly available.
        self.product_type = product_type
        # The ID of the child instance. This parameter is not used in cloud computing scenarios. Workstation scenarios, you need to specify a persistent session ID to ensure that a specific instance is located.
        self.sub_instance_id = sub_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_clean_userdata is not None:
            result['AutoCleanUserdata'] = self.auto_clean_userdata
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.description is not None:
            result['Description'] = self.description
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.sub_instance_id is not None:
            result['SubInstanceId'] = self.sub_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanUserdata') is not None:
            self.auto_clean_userdata = m.get('AutoCleanUserdata')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubInstanceId') is not None:
            self.sub_instance_id = m.get('SubInstanceId')
        return self


class CreateImageByInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        task_id: str = None,
        version_id: str = None,
    ):
        # The ID of the RDS image.
        self.image_id = image_id
        # The ID of the image creation task.
        self.task_id = task_id
        # The version of the image.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateImageByInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateImageByInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateImageByInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateImageByInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageByInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateImageByInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageFromAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_center_image_name: str = None,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        # The image name.
        # 
        # This parameter is required.
        self.app_center_image_name = app_center_image_name
        # The ID of the delivery group. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_name is not None:
            result['AppCenterImageName'] = self.app_center_image_name
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageName') is not None:
            self.app_center_image_name = m.get('AppCenterImageName')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class CreateImageFromAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageFromAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageFromAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateImageFromAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWuyingServerRequestDataDisk(TeaModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_performance_level: str = None,
        data_disk_size: int = None,
    ):
        # The data disk category.
        # 
        # Valid values:
        # 
        # *   cloud_auto.
        self.data_disk_category = data_disk_category
        # The PL of the data disk.
        self.data_disk_performance_level = data_disk_performance_level
        # The data disk size.
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_performance_level is not None:
            result['DataDiskPerformanceLevel'] = self.data_disk_performance_level
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('DataDiskPerformanceLevel')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        return self


class CreateWuyingServerRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bandwidth: int = None,
        biz_region_id: str = None,
        charge_type: str = None,
        data_disk: List[CreateWuyingServerRequestDataDisk] = None,
        host_name: str = None,
        idempotence_token: str = None,
        image_id: str = None,
        network_strategy_type: str = None,
        office_site_id: str = None,
        password: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        saving_plan_id: str = None,
        server_instance_type: str = None,
        server_port_range: str = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        v_switch_ids: List[str] = None,
        virtual_node_pool_id: str = None,
        wuying_server_name: str = None,
    ):
        # Quantity.
        self.amount = amount
        # Auto payment.
        self.auto_pay = auto_pay
        # Auto-renewal.
        self.auto_renew = auto_renew
        # bandwidth value, the NetworkStrategyType is valid for DirectIp. Unit: Mbps, range 2~100
        self.bandwidth = bandwidth
        # Region.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PrePaid: subscription
        self.charge_type = charge_type
        # The list of data disks.
        self.data_disk = data_disk
        self.host_name = host_name
        # Idempotence token to ensure operation uniqueness
        self.idempotence_token = idempotence_token
        # The ID of the image.
        self.image_id = image_id
        # The type of the network policy (in invitational preview).
        self.network_strategy_type = network_strategy_type
        # The office network IDs.
        self.office_site_id = office_site_id
        # Workstation login password.
        self.password = password
        # The subscription period.
        self.period = period
        # The time unit.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        self.period_unit = period_unit
        # The ID of the discount.
        # 
        # >  If PromotionId is set, it will try to apply the corresponding discount.
        self.promotion_id = promotion_id
        self.saving_plan_id = saving_plan_id
        # Workstation specifications.
        self.server_instance_type = server_instance_type
        self.server_port_range = server_port_range
        # The system disk category.
        # 
        # Valid values:
        # 
        # *   cloud_auto.
        self.system_disk_category = system_disk_category
        # The performance level (PL) of the system disk.
        self.system_disk_performance_level = system_disk_performance_level
        # The size of the system disk. Unit: GB.
        self.system_disk_size = system_disk_size
        # The list of office network vSwitches.
        self.v_switch_ids = v_switch_ids
        self.virtual_node_pool_id = virtual_node_pool_id
        # The name of the workstation. The numeric suffix is automatically added when multiple workstations are created.
        self.wuying_server_name = wuying_server_name

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.idempotence_token is not None:
            result['IdempotenceToken'] = self.idempotence_token
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.network_strategy_type is not None:
            result['NetworkStrategyType'] = self.network_strategy_type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.saving_plan_id is not None:
            result['SavingPlanId'] = self.saving_plan_id
        if self.server_instance_type is not None:
            result['ServerInstanceType'] = self.server_instance_type
        if self.server_port_range is not None:
            result['ServerPortRange'] = self.server_port_range
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.virtual_node_pool_id is not None:
            result['VirtualNodePoolId'] = self.virtual_node_pool_id
        if self.wuying_server_name is not None:
            result['WuyingServerName'] = self.wuying_server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = CreateWuyingServerRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IdempotenceToken') is not None:
            self.idempotence_token = m.get('IdempotenceToken')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('NetworkStrategyType') is not None:
            self.network_strategy_type = m.get('NetworkStrategyType')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('SavingPlanId') is not None:
            self.saving_plan_id = m.get('SavingPlanId')
        if m.get('ServerInstanceType') is not None:
            self.server_instance_type = m.get('ServerInstanceType')
        if m.get('ServerPortRange') is not None:
            self.server_port_range = m.get('ServerPortRange')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VirtualNodePoolId') is not None:
            self.virtual_node_pool_id = m.get('VirtualNodePoolId')
        if m.get('WuyingServerName') is not None:
            self.wuying_server_name = m.get('WuyingServerName')
        return self


class CreateWuyingServerResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        wuying_server_id_list: List[str] = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')
        return self


class CreateWuyingServerResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateWuyingServerResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateWuyingServerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWuyingServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWuyingServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWuyingServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DeleteAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstancesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_ids: List[str] = None,
        product_type: str = None,
    ):
        # The ID of the delivery group. You can call the [listAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The IDs of application instances.
        # 
        # This parameter is required.
        self.app_instance_ids = app_instance_ids
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_ids is not None:
            result['AppInstanceIds'] = self.app_instance_ids
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceIds') is not None:
            self.app_instance_ids = m.get('AppInstanceIds')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DeleteAppInstancesResponseBodyDeleteAppInstanceModels(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # Specifies whether the application instance is deleted.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppInstancesResponseBody(TeaModel):
    def __init__(
        self,
        delete_app_instance_models: List[DeleteAppInstancesResponseBodyDeleteAppInstanceModels] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.delete_app_instance_models = delete_app_instance_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.delete_app_instance_models:
            for k in self.delete_app_instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeleteAppInstanceModels'] = []
        if self.delete_app_instance_models is not None:
            for k in self.delete_app_instance_models:
                result['DeleteAppInstanceModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delete_app_instance_models = []
        if m.get('DeleteAppInstanceModels') is not None:
            for k in m.get('DeleteAppInstanceModels'):
                temp_model = DeleteAppInstancesResponseBodyDeleteAppInstanceModels()
                self.delete_app_instance_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
    ):
        # The ID of the RDS image.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code:
        # 
        # *   `200`: Success.
        # *   `400`: An error occurred.
        self.code = code
        # Whether the deletion is successful.
        # 
        # Enumerated values:
        # 
        # *   true:Deleted successfully.
        # *   false:Deletion failure.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWuyingServerRequest(TeaModel):
    def __init__(
        self,
        wuying_server_id: str = None,
    ):
        # The ID of the workstation.
        # 
        # This parameter is required.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')
        return self


class DeleteWuyingServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWuyingServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWuyingServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWuyingServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWuyingServerEipInfoRequest(TeaModel):
    def __init__(
        self,
        isp: str = None,
        wuying_server_id: str = None,
    ):
        # The Internet service provider (ISP). Valid values:
        # 
        # *   ChinaMobile: China Mobile
        # *   ChinaTelecom: China Telecom
        # *   ChinaUnicom: China Unicom
        self.isp = isp
        # The ID of the workstation.
        # 
        # This parameter is required.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')
        return self


class DescribeWuyingServerEipInfoResponseBodyEipInfoModel(TeaModel):
    def __init__(
        self,
        eip_id: str = None,
        ip_address: str = None,
        network_interface_id: str = None,
        server_port_range: str = None,
    ):
        self.eip_id = eip_id
        # The public IP address.
        self.ip_address = ip_address
        # The ID of the elastic network interface (ENI).
        self.network_interface_id = network_interface_id
        # The port range.
        self.server_port_range = server_port_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_id is not None:
            result['EipId'] = self.eip_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.server_port_range is not None:
            result['ServerPortRange'] = self.server_port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('ServerPortRange') is not None:
            self.server_port_range = m.get('ServerPortRange')
        return self


class DescribeWuyingServerEipInfoResponseBody(TeaModel):
    def __init__(
        self,
        eip_info_model: DescribeWuyingServerEipInfoResponseBodyEipInfoModel = None,
        request_id: str = None,
    ):
        # The information about the associated EIP.
        self.eip_info_model = eip_info_model
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.eip_info_model:
            self.eip_info_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_info_model is not None:
            result['EipInfoModel'] = self.eip_info_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipInfoModel') is not None:
            temp_model = DescribeWuyingServerEipInfoResponseBodyEipInfoModel()
            self.eip_info_model = temp_model.from_map(m['EipInfoModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWuyingServerEipInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWuyingServerEipInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWuyingServerEipInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        # The ID of the delivery group. You can call the [listAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(TeaModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        # The schedule type of the scaling policy. This parameter must be configured together with `RecurrenceValues`.``
        self.recurrence_type = recurrence_type
        # The days of each week on which the scaling policy is executed.
        self.recurrence_values = recurrence_values
        # The time periods during which the scaling policy can be executed.
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(TeaModel):
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
        recurrence_schedules: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules] = None,
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
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
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
            for k in m.get('RecurrenceSchedules'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
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


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetAppInstanceGroupResponseBodyAppInstanceGroupModels(TeaModel):
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
        apps: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps] = None,
        auth_mode: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        max_amount: int = None,
        min_amount: int = None,
        node_pool: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool] = None,
        office_site_id: str = None,
        os_type: str = None,
        ota_info: GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo = None,
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
        tags: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsTags] = None,
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
            for k in self.apps:
                if k:
                    k.validate()
        if self.node_pool:
            for k in self.node_pool:
                if k:
                    k.validate()
        if self.ota_info:
            self.ota_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
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
            for k in self.node_pool:
                result['NodePool'].append(k.to_map() if k else None)
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
            for k in m.get('Apps'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k))
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
            for k in m.get('NodePool'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k))
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaInfo') is not None:
            temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m['OtaInfo'])
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
            for k in m.get('Tags'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UserGroupAuthMode') is not None:
            self.user_group_auth_mode = m.get('UserGroupAuthMode')
        return self


class GetAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_models: GetAppInstanceGroupResponseBodyAppInstanceGroupModels = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_models is not None:
            result['AppInstanceGroupModels'] = self.app_instance_group_models.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupModels') is not None:
            temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModels()
            self.app_instance_group_models = temp_model.from_map(m['AppInstanceGroupModels'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        app_id: str = None,
        app_instance_group_id_list: List[str] = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        app_policy_id: str = None,
        app_start_param: str = None,
        app_version: str = None,
        biz_region_id: str = None,
        end_user_id: str = None,
        environment_config: str = None,
        product_type: str = None,
        task_id: str = None,
    ):
        self.access_type = access_type
        # The application ID.
        # 
        # >  This parameter is required for the first call to this operation and optional for subsequent calls to the operation.
        self.app_id = app_id
        # The delivery groups.
        # 
        # > *   If you configure this parameter, the system assigns application instances only among the specified authorized delivery groups. 
        # > *   This parameter is required if you configure `AppInstanceId` or `AppInstancePersistentId`.
        self.app_instance_group_id_list = app_instance_group_id_list
        # The ID of the application instance.
        # 
        # > *   If you configure this parameter, the system attempts to assign only the specified application instance.
        # > *   If you configure this parameter, you must also configure `AppInstanceGroupIdList` and the number of delivery groups specified by `AppInstanceGroupIdList` must be 1.
        self.app_instance_id = app_instance_id
        # The ID of the persistent session.
        self.app_instance_persistent_id = app_instance_persistent_id
        self.app_policy_id = app_policy_id
        # The parameters that are configured to start the application. For information about how to obtain these parameters, see [Obtain parameters configured to install and start an application](https://help.aliyun.com/document_detail/426045.html).
        self.app_start_param = app_start_param
        # The application version. If you configure this parameter, only an application of the specified version is started. If you do not configure this parameter, an application of a random authorized version is started.
        self.app_version = app_version
        # The region ID.
        # 
        # >  If you configure this parameter, the system assigns application instances only among the delivery groups that reside in the specified region.
        self.biz_region_id = biz_region_id
        # The ID of the convenience account.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The environment configuration.
        self.environment_config = environment_config
        # The product type.
        # 
        # Valid values:
        # 
        # *   CloudApp: App Streaming
        # *   AndroidCloud: Cloud Phone
        # 
        # This parameter is required.
        self.product_type = product_type
        # The task ID.
        # 
        # >  This parameter is required for calls other than the first call to this operation. You can use this parameter to query the task status and connection credential.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id_list is not None:
            result['AppInstanceGroupIdList'] = self.app_instance_group_id_list
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id
        if self.app_start_param is not None:
            result['AppStartParam'] = self.app_start_param
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.environment_config is not None:
            result['EnvironmentConfig'] = self.environment_config
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupIdList') is not None:
            self.app_instance_group_id_list = m.get('AppInstanceGroupIdList')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')
        if m.get('AppStartParam') is not None:
            self.app_start_param = m.get('AppStartParam')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EnvironmentConfig') is not None:
            self.environment_config = m.get('EnvironmentConfig')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        avatar_id: str = None,
        biz_region_id: str = None,
        os_type: str = None,
        request_id: str = None,
        task_id: str = None,
        task_status: str = None,
        tenant_id: int = None,
        ticket: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The ID of the persistent session.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The avatar ID.
        self.avatar_id = avatar_id
        # The region ID.
        self.biz_region_id = biz_region_id
        # The operating system.
        # 
        # Valid value:
        # 
        # *   Windows: the Windows operating system
        self.os_type = os_type
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id
        # The task status.
        # 
        # Valid values:
        # 
        # *   Finished: The task is complete.
        # *   Failed: The task failed.
        # *   Running: The task is being executed.
        self.task_status = task_status
        # The ID of the Alibaba Cloud account.
        self.tenant_id = tenant_id
        # The credential that is used to connect to App Streaming.
        # 
        # >  This parameter is displayed for calls other than the first call to this operation.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConnectionTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDebugAppInstanceRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        # The ID of the delivery group. You can call the `listAppInstanceGroup` operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetDebugAppInstanceResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_version: str = None,
        auth_code: str = None,
        request_id: str = None,
        user_id: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The ID of the application version.
        self.app_version = app_version
        # The authorization code. This authorization code is valid for 3 minutes and can be used only once, regardless of whether the authentication succeeds. If multiple authentication codes are generated for a user, only the latest authentication code takes effect.
        self.auth_code = auth_code
        # The request ID.
        self.request_id = request_id
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetDebugAppInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDebugAppInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDebugAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOtaTaskByTaskIdRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The ID of the OTA update task. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetOtaTaskByTaskIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        ota_version: str = None,
        release_note: str = None,
        request_id: str = None,
        task_start_time: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The OTA version.
        self.ota_version = ota_version
        # The version description.
        self.release_note = release_note
        # The request ID.
        self.request_id = request_id
        # The execution time of the OTA update task. The time follows the ISO 8601 standard.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.task_start_time = task_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        return self


class GetOtaTaskByTaskIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOtaTaskByTaskIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOtaTaskByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePriceRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        app_instance_type: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        node_instance_type: str = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
    ):
        # The number of resources to purchase.
        # 
        # This parameter is required.
        self.amount = amount
        # The type ID of the sessions that you purchase. You can call the `ListAppInstanceType` operation to obtain the ID.
        # 
        # You must specify one of AppInstanceType and NodeInstanceType. If you specify both of the parameters, the value of NodeInstanceType takes effect.
        self.app_instance_type = app_instance_type
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai).
        # *   cn-hangzhou: China (Hangzhou)
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The ID of the resource type that you purchase. You can call the [ListNodeInstanceType](https://help.aliyun.com/document_detail/428502.html) to obtain the ID.
        # 
        # You must specify one of AppInstanceType and NodeInstanceType. If you specify both of the parameters, the value of NodeInstanceType takes effect.
        # 
        # Valid values:
        # 
        # *   appstreaming.vgpu.8c16g.4g: WUYING - Graphics - 8 vCPUs, 16 GiB Memory, 4 GiB GPU Memory
        # *   appstreaming.general.8c16g: WUYING - General - 8 vCPUs, 16 GiB Memory
        # *   appstreaming.general.4c8g: WUYING - General - 4 vCPUs, 8 GiB Memory
        # *   appstreaming.vgpu.14c93g.12g: WUYING - Graphics - 14 vCPUs, 93 GiB Memory, 12 GiB GPU Memory.
        # *   appstreaming.vgpu.8c31g.16g: WUYING - Graphics - 8 vCPUs, 31 GiB Memory, 16 GiB GPU Memory
        self.node_instance_type = node_instance_type
        # The subscription duration of resources. This parameter must be configured together with `PeriodUnit`.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration. This parameter must be configured together with `Period`. The following items describe valid values for the combinations of `Period` and `PeriodUnit`:
        # 
        # *   1 Week
        # *   1 Month
        # *   2 Month
        # *   3 Month
        # *   6 Month
        # *   1 Year
        # *   2 Year
        # *   3 Year
        # 
        # >  The value of this parameter is case-insensitive. For example, `Week` is valid and `week` is invalid. If you specify a value combination other than the preceding combinations, such as `2 Week`, the operation can still be called. However, an error occurs when you place the order.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetResourcePriceResponseBodyPriceListPricePromotions(TeaModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        # The coupon code.
        self.option_code = option_code
        # The coupon description.
        self.promotion_desc = promotion_desc
        # The coupon ID.
        self.promotion_id = promotion_id
        # The coupon name.
        self.promotion_name = promotion_name
        # Indicates whether the coupon was used.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourcePriceResponseBodyPriceListPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        promotions: List[GetResourcePriceResponseBodyPriceListPricePromotions] = None,
        trade_price: str = None,
    ):
        # The currency type.
        self.currency = currency
        # The discount. The actual price is calculated based on the following formula: Actual price = Original price - Discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The coupon metadata.
        self.promotions = promotions
        # The actual price. The actual price is calculated based on the following formula: Actual price = Original price - Discount.
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourcePriceResponseBodyPriceListPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourcePriceResponseBodyPriceListRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the price calculation rule.
        self.description = description
        # The ID of the price calculation rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourcePriceResponseBodyPriceList(TeaModel):
    def __init__(
        self,
        price: GetResourcePriceResponseBodyPriceListPrice = None,
        price_type: str = None,
        rules: List[GetResourcePriceResponseBodyPriceListRules] = None,
    ):
        # The price details.
        self.price = price
        # The price type.
        # 
        # Valid values:
        # 
        # *   Connected: in use
        # *   Standby: pending for use.
        self.price_type = price_type
        # The price calculation rules.
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourcePriceResponseBodyPriceListPrice()
            self.price = temp_model.from_map(m['Price'])
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourcePriceResponseBodyPriceListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourcePriceResponseBodyPriceModelPricePromotions(TeaModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        # The coupon code.
        self.option_code = option_code
        # The coupon description.
        self.promotion_desc = promotion_desc
        # The coupon ID.
        self.promotion_id = promotion_id
        # The coupon name.
        self.promotion_name = promotion_name
        # Indicates whether the coupon was used.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourcePriceResponseBodyPriceModelPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        promotions: List[GetResourcePriceResponseBodyPriceModelPricePromotions] = None,
        trade_price: str = None,
    ):
        # The currency type.
        self.currency = currency
        # The discount. The actual price is calculated based on the following formula: Actual price = Original price - Discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The coupon metadata.
        self.promotions = promotions
        # The actual price. The actual price is calculated based on the following formula: Actual price = Original price - Discount.
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourcePriceResponseBodyPriceModelPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourcePriceResponseBodyPriceModelRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the price calculation rule.
        self.description = description
        # The ID of the price calculation rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourcePriceResponseBodyPriceModel(TeaModel):
    def __init__(
        self,
        price: GetResourcePriceResponseBodyPriceModelPrice = None,
        rules: List[GetResourcePriceResponseBodyPriceModelRules] = None,
    ):
        # The price details.
        self.price = price
        # The price calculation rules.
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourcePriceResponseBodyPriceModelPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourcePriceResponseBodyPriceModelRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourcePriceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        price_list: List[GetResourcePriceResponseBodyPriceList] = None,
        price_model: GetResourcePriceResponseBodyPriceModel = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The price objects.
        # 
        # This parameter is returned only if a value is specified for AppInstanceType.
        self.price_list = price_list
        # The price object.
        # 
        # This parameter is returned only if a value is specified for NodeInstanceType.
        self.price_model = price_model
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()
        if self.price_model:
            self.price_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.price_model is not None:
            result['PriceModel'] = self.price_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = GetResourcePriceResponseBodyPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('PriceModel') is not None:
            temp_model = GetResourcePriceResponseBodyPriceModel()
            self.price_model = temp_model.from_map(m['PriceModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourcePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourcePriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourcePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRenewPriceRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
    ):
        # The ID of the delivery group. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The subscription duration of resources. This parameter must be configured together with `PeriodUnit`.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration. This parameter must be configured together with `Period`. The following items describe valid values for the combinations of `Period` and `PeriodUnit`:
        # 
        # *   1 Week
        # *   1 Month
        # *   2 Month
        # *   3 Month
        # *   6 Month
        # *   1 Year
        # *   2 Year
        # *   3 Year
        # 
        # >  The value of this parameter is case-insensitive. For example, `Week` is valid and `week` is invalid. If you specify a value combination other than the preceding combinations, such as `2 Week`, the operation can still be called. However, an error occurs when you place the order.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetResourceRenewPriceResponseBodyDataPricePromotions(TeaModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        # The coupon code.
        self.option_code = option_code
        # The coupon description.
        self.promotion_desc = promotion_desc
        # The coupon ID.
        self.promotion_id = promotion_id
        # The coupon name.
        self.promotion_name = promotion_name
        # Indicates whether the coupon was used.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourceRenewPriceResponseBodyDataPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        promotions: List[GetResourceRenewPriceResponseBodyDataPricePromotions] = None,
        trade_price: str = None,
    ):
        # The currency type.
        self.currency = currency
        # The discount. The actual price is calculated based on the following formula: Actual price = Original price - Discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The coupon description.
        self.promotions = promotions
        # The actual price. The actual price is calculated based on the following formula: Actual price = Original price - Discount.
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourceRenewPriceResponseBodyDataPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourceRenewPriceResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the price calculation rule.
        self.description = description
        # The ID of the price calculation rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourceRenewPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        price: GetResourceRenewPriceResponseBodyDataPrice = None,
        rules: List[GetResourceRenewPriceResponseBodyDataRules] = None,
    ):
        # The price details.
        self.price = price
        # The price calculation rules.
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourceRenewPriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourceRenewPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourceRenewPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: GetResourceRenewPriceResponseBodyData = None,
        request_id: str = None,
    ):
        # The price object.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetResourceRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceRenewPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceRenewPriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstanceGroupRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        biz_region_id: str = None,
        excluded_user_group_ids: List[str] = None,
        node_instance_type: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        region_id: str = None,
        status: List[str] = None,
        tag: List[ListAppInstanceGroupRequestTag] = None,
        user_group_ids: List[str] = None,
    ):
        # The image ID of the app. You can obtain the ID from the Images page in the App Streaming console.
        self.app_center_image_id = app_center_image_id
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery groups to query. Fuzzy match is used for queries. For example, if you set this parameter to `Office App`, all delivery groups whose names contain `Office App` are queried, such as `My Office Apps` and `Office App A`.
        self.app_instance_group_name = app_instance_group_name
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-hangzhou: China (Hangzhou)
        self.biz_region_id = biz_region_id
        self.excluded_user_group_ids = excluded_user_group_ids
        # The ID of the resource specification that you purchase. You can call the [ListNodeInstanceType](~~ListNodeInstanceType~~) operation to obtain the ID.
        self.node_instance_type = node_instance_type
        self.office_site_id = office_site_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. The value cannot be greater than `100`.
        self.page_size = page_size
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The region ID
        self.region_id = region_id
        # The status of the delivery groups.
        self.status = status
        self.tag = tag
        self.user_group_ids = user_group_ids

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.excluded_user_group_ids is not None:
            result['ExcludedUserGroupIds'] = self.excluded_user_group_ids
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ExcludedUserGroupIds') is not None:
            self.excluded_user_group_ids = m.get('ExcludedUserGroupIds')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAppInstanceGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(TeaModel):
    def __init__(
        self,
        app_icon: str = None,
        app_id: str = None,
        app_name: str = None,
        app_version: str = None,
        app_version_name: str = None,
    ):
        # The app icon.
        self.app_icon = app_icon
        # The app ID.
        self.app_id = app_id
        # The app name.
        self.app_name = app_name
        # The app version.
        self.app_version = app_version
        # The name of the app version.
        self.app_version_name = app_version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The number of destination resources.
        self.amount = amount
        # The time when the scaling policy ends. Format: HH:mm.
        self.end_time = end_time
        # The time when the scaling policy starts. Format: HH:mm.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(TeaModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        # The schedule type of the scaling policy. This parameter must be configured together with `RecurrenceValues`.``
        # 
        # Valid value:
        # 
        # *   weekly: The scaling policy is executed on specific days each week.
        self.recurrence_type = recurrence_type
        # The days of each week on which the scaling policy is executed.
        self.recurrence_values = recurrence_values
        # The time periods during which the scaling policy can be executed.
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(TeaModel):
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
        recurrence_schedules: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules] = None,
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
        # The maximum number of idle sessions. After you specify a value for this parameter, auto scale-out is triggered only if the number of idle sessions in the delivery group is smaller than the specified value and the session usage exceeds the value specified for `ScalingUsageThreshold`. Otherwise, the system determines that idle sessions in the delivery group are sufficient and does not perform auto scale-out.`` You can use this parameter to flexibly manage auto scaling and reduce costs.
        self.max_idle_app_instance_amount = max_idle_app_instance_amount
        # The maximum number of resources that can be created for scale-out.
        self.max_scaling_amount = max_scaling_amount
        # The total number of subscription resources.
        self.node_amount = node_amount
        # The maximum number of sessions that can be connected to a resource at the same time. If a resource connects to a large number of sessions at the same time, user experience can be compromised. The value range varies based on the resource specification. The following items describe the value ranges of different resource types:
        # 
        # *   appstreaming.general.4c8g: 1 to 2
        # *   appstreaming.general.8c16g: 1 to 4
        # *   appstreaming.vgpu.8c16g.4g: 1 to 4
        # *   appstreaming.vgpu.8c31g.16g: 1 to 4
        # *   appstreaming.vgpu.14c93g.12g: 1 to 6
        self.node_capacity = node_capacity
        # The ID of the resource specification that you purchase.
        self.node_instance_type = node_instance_type
        # The ID of the resource group.
        self.node_pool_id = node_pool_id
        # The name of the resource specification.
        self.node_type_name = node_type_name
        # The number of subscription resources that are in use.
        self.node_used = node_used
        # The intervals at which the scaling policy is executed.
        self.recurrence_schedules = recurrence_schedules
        # The duration for which no session is connected. Unit: minutes. If no session is connected in the resources after the specified duration elapses, auto scale-in is triggered. Default value: 5.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The total number of scalable resources.
        self.scaling_node_amount = scaling_node_amount
        # The number of scalable resources that are in use.
        self.scaling_node_used = scaling_node_used
        # The number of resources that are created each time resources are scaled out. Valid values: 1 to 10.
        self.scaling_step = scaling_step
        # The upper limit of session usage. If the session usage exceeds the specified upper limit, auto scale-out is triggered. The session usage is calculated by using the following formula: `Session usage = Number of current sessions/(Total number of resources × Number of concurrent sessions) × 100%`.
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
        # Indicates whether resource prefetch is enabled.
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
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
            for k in m.get('RecurrenceSchedules'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
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


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsResourceTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag type. Valid values: Custom System
        self.scope = scope
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        self.key = key
        self.scope = scope
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListAppInstanceGroupResponseBodyAppInstanceGroupModels(TeaModel):
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
        apps: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps] = None,
        auth_mode: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        max_amount: int = None,
        min_amount: int = None,
        node_pool: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool] = None,
        office_site_id: str = None,
        os_type: str = None,
        ota_info: ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo = None,
        product_type: str = None,
        region_id: str = None,
        reserve_amount_ratio: str = None,
        reserve_max_amount: int = None,
        reserve_min_amount: int = None,
        resource_status: str = None,
        resource_tags: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsResourceTags] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        session_timeout: str = None,
        skip_user_auth_check: bool = None,
        spec_id: str = None,
        status: str = None,
        support_user_group_mixed_auth: bool = None,
        tags: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsTags] = None,
        user_group_auth_mode: str = None,
    ):
        self.access_type = access_type
        # The number of subscription resources. Minimum value: 1.
        self.amount = amount
        # The image ID of the app.
        self.app_center_image_id = app_center_image_id
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # The resource type of the delivery group.
        self.app_instance_type = app_instance_type
        # The policy ID.
        self.app_policy_id = app_policy_id
        self.app_policy_image_check = app_policy_image_check
        self.app_policy_version = app_policy_version
        # The apps.
        self.apps = apps
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
        # The resource groups.
        self.node_pool = node_pool
        self.office_site_id = office_site_id
        # The type of the operating system.
        # 
        # Valid value:
        # 
        # *   Windows
        self.os_type = os_type
        # The information about the over-the-air (OTA) update task.
        self.ota_info = ota_info
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
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
        # 
        # Valid values:
        # 
        # *   AVAILABLE
        # *   RELEASED
        # *   EXPIRED_IN_7_DAYS
        # *   UNAVAILABLE
        # *   UPGRADING
        # *   CREATING
        self.resource_status = resource_status
        # The resource tags.
        self.resource_tags = resource_tags
        # The duration for which no session is connected. Unit: minutes. If no session is connected in the resources after the specified duration elapses, auto scale-in is triggered. Minimum value: 0.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The number of sessions that are created each time the delivery group is scaled out. Minimum value: 1.
        self.scaling_step = scaling_step
        # The upper limit of session usage. If the session usage exceeds the specified upper limit, auto scale-out is triggered. The session usage rate is calculated by using the following formula: Session usage rate = Number of sessions in use/Total number of sessions × 100%. Valid values: 0 to 99.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The duration for which sessions are retained after disconnection. Unit: minutes. After an end user disconnects from a session, the session is closed only after the specified duration elapses. If you want to permanently retain sessions, set this parameter to `-1`. Valid values:-1 and 3 to 300. Default value: `15`.
        self.session_timeout = session_timeout
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
        self.tags = tags
        self.user_group_auth_mode = user_group_auth_mode

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()
        if self.node_pool:
            for k in self.node_pool:
                if k:
                    k.validate()
        if self.ota_info:
            self.ota_info.validate()
        if self.resource_tags:
            for k in self.resource_tags:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
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
            for k in self.node_pool:
                result['NodePool'].append(k.to_map() if k else None)
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
            for k in self.resource_tags:
                result['ResourceTags'].append(k.to_map() if k else None)
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
            for k in m.get('Apps'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k))
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
            for k in m.get('NodePool'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k))
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaInfo') is not None:
            temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m['OtaInfo'])
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
            for k in m.get('ResourceTags'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsResourceTags()
                self.resource_tags.append(temp_model.from_map(k))
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
            for k in m.get('Tags'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UserGroupAuthMode') is not None:
            self.user_group_auth_mode = m.get('UserGroupAuthMode')
        return self


class ListAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_models: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The delivery groups.
        self.app_instance_group_models = app_instance_group_models
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.app_instance_group_models:
            for k in self.app_instance_group_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInstanceGroupModels'] = []
        if self.app_instance_group_models is not None:
            for k in self.app_instance_group_models:
                result['AppInstanceGroupModels'].append(k.to_map() if k else None)
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
            for k in m.get('AppInstanceGroupModels'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModels()
                self.app_instance_group_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstancesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_id_list: List[str] = None,
        include_deleted: bool = None,
        page_number: int = None,
        page_size: int = None,
        status: List[str] = None,
        user_id_list: List[str] = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The IDs of the application instances. Up to 100 IDs can be specified.
        self.app_instance_id_list = app_instance_id_list
        # Specifies whether to query the information about deleted app instances. If you set this parameter to true, you must configure AppInstanceIdList. Otherwise, a parameter error is reported.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.include_deleted = include_deleted
        # The page number. Default value: `1`. We recommend that you specify this parameter.
        self.page_number = page_number
        # The number of entries per page. The value cannot be greater than `100`. Default value: `20`. We recommend that you specify this parameter.
        self.page_size = page_size
        # The status of the application instances.
        self.status = status
        # The user IDs. You can specify up to 100 IDs.
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_id_list is not None:
            result['AppInstanceIdList'] = self.app_instance_id_list
        if self.include_deleted is not None:
            result['IncludeDeleted'] = self.include_deleted
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstanceIdList') is not None:
            self.app_instance_id_list = m.get('AppInstanceIdList')
        if m.get('IncludeDeleted') is not None:
            self.include_deleted = m.get('IncludeDeleted')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class ListAppInstancesResponseBodyAppInstanceModelsBindInfo(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        usage_duration: int = None,
    ):
        # The ID of the end user that is bound to the application instance.
        self.end_user_id = end_user_id
        # The use duration of the application instance. Unit: seconds.
        self.usage_duration = usage_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.usage_duration is not None:
            result['UsageDuration'] = self.usage_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('UsageDuration') is not None:
            self.usage_duration = m.get('UsageDuration')
        return self


class ListAppInstancesResponseBodyAppInstanceModels(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        bind_info: ListAppInstancesResponseBodyAppInstanceModelsBindInfo = None,
        charge_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        main_eth_public_ip: str = None,
        network_interface_id: str = None,
        network_interface_ip: str = None,
        node_id: str = None,
        session_status: str = None,
        status: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The information about the binding between the application instance and end users.
        self.bind_info = bind_info
        # The billing method of the app instance. Valid values:
        # 
        # *   **PrePaid**: subscription.
        # *   **PostPaid**: pay-as-you-go
        # 
        # >  This parameter is returned only if the ChargeResourceMode parameter of the delivery group to which the app instance belongs is set to Node.
        self.charge_type = charge_type
        # The time when the application instance was created.
        self.gmt_create = gmt_create
        # The time when the application instance was updated.
        self.gmt_modified = gmt_modified
        # The public IP address associated with the primary NIC. This value is returned only if `StrategyType` is set to `Mixed`.
        self.main_eth_public_ip = main_eth_public_ip
        self.network_interface_id = network_interface_id
        self.network_interface_ip = network_interface_ip
        # The ID of the node on which the app instance runs.
        # 
        # >  This parameter is returned only if the ChargeResourceMode parameter of the delivery group to which the app instance belongs is set to Node.
        self.node_id = node_id
        # The session status. This parameter is returned only if the application instance is in the `RUNNING` state.
        # 
        # Valid values:
        # 
        # *   disconnect: disconnected
        # *   connect: connected
        self.session_status = session_status
        # The status of the application instance.
        self.status = status

    def validate(self):
        if self.bind_info:
            self.bind_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.bind_info is not None:
            result['BindInfo'] = self.bind_info.to_map()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.main_eth_public_ip is not None:
            result['MainEthPublicIp'] = self.main_eth_public_ip
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('BindInfo') is not None:
            temp_model = ListAppInstancesResponseBodyAppInstanceModelsBindInfo()
            self.bind_info = temp_model.from_map(m['BindInfo'])
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MainEthPublicIp') is not None:
            self.main_eth_public_ip = m.get('MainEthPublicIp')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstancesResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_models: List[ListAppInstancesResponseBodyAppInstanceModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The app instances.
        self.app_instance_models = app_instance_models
        # The page number of the returned page. We recommend that you configure this parameter.
        self.page_number = page_number
        # The number of entries returned on each page. The value cannot be greater than `100`. We recommend that you configure this parameter.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.app_instance_models:
            for k in self.app_instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInstanceModels'] = []
        if self.app_instance_models is not None:
            for k in self.app_instance_models:
                result['AppInstanceModels'].append(k.to_map() if k else None)
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
        self.app_instance_models = []
        if m.get('AppInstanceModels') is not None:
            for k in m.get('AppInstanceModels'):
                temp_model = ListAppInstancesResponseBodyAppInstanceModels()
                self.app_instance_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizedUserGroupsRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        group_id: str = None,
        group_name: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the user group (exact match).
        self.group_id = group_id
        # The name of the user group (fuzzy match).
        self.group_name = group_name
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The maximum number of entries returned per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type.
        # 
        # Valid values:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ListAuthorizedUserGroupsResponseBodyUserGroups(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        auth_mode: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The authorization mode.
        # 
        # Valid values:
        # 
        # *   App: authorizes access to apps.
        # *   AppInstanceGroup: authorizes access to delivery groups.
        # *   Session: authorizes access to sessions.
        self.auth_mode = auth_mode
        # The ID of the user group.
        self.group_id = group_id
        # The name of the user group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.auth_mode is not None:
            result['AuthMode'] = self.auth_mode
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AuthMode') is not None:
            self.auth_mode = m.get('AuthMode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class ListAuthorizedUserGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        user_groups: List[ListAuthorizedUserGroupsResponseBodyUserGroups] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The maximum number of entries returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the user groups.
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListAuthorizedUserGroupsResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListAuthorizedUserGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAuthorizedUserGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAuthorizedUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindInfoRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        app_instance_group_id_list: List[str] = None,
        app_instance_id_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        user_id_list: List[str] = None,
        wy_id_list: List[str] = None,
    ):
        # The app IDs. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified apps are returned.
        self.app_id_list = app_id_list
        # The IDs of the delivery groups. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified delivery groups are returned.
        self.app_instance_group_id_list = app_instance_group_id_list
        # The IDs of app instances. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified app instances are returned.
        self.app_instance_id_list = app_instance_id_list
        # The page number. Default value: `1`. We recommend that you specify this parameter.
        self.page_number = page_number
        # The number of entries per page. The value cannot be greater than `100`. Default value: `20`. We recommend that you specify this parameter.
        self.page_size = page_size
        # The user IDs. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified users are returned.
        self.user_id_list = user_id_list
        # The IDs of the Alibaba Cloud Workspace users. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified Alibaba Cloud Workspace users are returned.
        self.wy_id_list = wy_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        if self.app_instance_group_id_list is not None:
            result['AppInstanceGroupIdList'] = self.app_instance_group_id_list
        if self.app_instance_id_list is not None:
            result['AppInstanceIdList'] = self.app_instance_id_list
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        if self.wy_id_list is not None:
            result['WyIdList'] = self.wy_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        if m.get('AppInstanceGroupIdList') is not None:
            self.app_instance_group_id_list = m.get('AppInstanceGroupIdList')
        if m.get('AppInstanceIdList') is not None:
            self.app_instance_id_list = m.get('AppInstanceIdList')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        if m.get('WyIdList') is not None:
            self.wy_id_list = m.get('WyIdList')
        return self


class ListBindInfoResponseBodyBindInfoModels(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_version: str = None,
        product_type: str = None,
        region_id: str = None,
        user_id: str = None,
        wy_id: str = None,
    ):
        # The account type.
        # 
        # Valid values:
        # 
        # *   ad: Active Directory (AD) account
        # *   simple: convenience account
        self.account_type = account_type
        # The app ID.
        self.app_id = app_id
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the app instance.
        self.app_instance_id = app_instance_id
        # The app version.
        self.app_version = app_version
        # The product type.
        # 
        # Valid values:
        # 
        # *   CloudApp: App Streaming
        # *   CloudBrowser: Cloud-based Browser
        # *   AndroidCloud: Cloud Phone
        self.product_type = product_type
        # The region ID.
        self.region_id = region_id
        # The user ID.
        self.user_id = user_id
        # The ID of the Alibaba Cloud Workspace user.
        self.wy_id = wy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.wy_id is not None:
            result['WyId'] = self.wy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')
        return self


class ListBindInfoResponseBody(TeaModel):
    def __init__(
        self,
        bind_info_models: List[ListBindInfoResponseBodyBindInfoModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The bindings.
        self.bind_info_models = bind_info_models
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.bind_info_models:
            for k in self.bind_info_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindInfoModels'] = []
        if self.bind_info_models is not None:
            for k in self.bind_info_models:
                result['BindInfoModels'].append(k.to_map() if k else None)
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
        self.bind_info_models = []
        if m.get('BindInfoModels') is not None:
            for k in m.get('BindInfoModels'):
                temp_model = ListBindInfoResponseBodyBindInfoModels()
                self.bind_info_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBindInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBindInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBindInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageRequestTagList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the custom tag.
        self.key = key
        # The value of the custom tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListImageRequest(TeaModel):
    def __init__(
        self,
        biz_region_id_list: List[str] = None,
        biz_type: int = None,
        biz_type_list: List[int] = None,
        feature_list: List[str] = None,
        fota_version: str = None,
        image_id: str = None,
        image_name: str = None,
        image_type: str = None,
        language_type: str = None,
        os_type: str = None,
        package_type: str = None,
        page_number: int = None,
        page_size: int = None,
        platform_name: str = None,
        platform_name_list: List[str] = None,
        product_type: str = None,
        product_type_list: List[str] = None,
        protocol_type: str = None,
        resource_instance_type: str = None,
        status: str = None,
        tag_list: List[ListImageRequestTagList] = None,
    ):
        # The regions that are supported. The EDS images are centralized. Use this parameter to query the regions where the image is deployed.
        self.biz_region_id_list = biz_region_id_list
        # The service type. This parameter is not available publicly.
        # 
        # Valid value:
        # 
        # *   1 (default)
        self.biz_type = biz_type
        # The list of all service types. It is not available publicly.
        self.biz_type_list = biz_type_list
        # The features supported by the image.
        self.feature_list = feature_list
        # The image version.
        self.fota_version = fota_version
        # The image ID.
        self.image_id = image_id
        # The image name. Fuzzy match is supported.
        self.image_name = image_name
        # The type of the images.
        # 
        # Valid values:
        # 
        # *   User: a custom image.
        # *   Shared: a shared image.
        # *   System: a system image.
        # *   Community: a community image.
        self.image_type = image_type
        # The language.
        # 
        # Valid values:
        # 
        # *   en-US: English.
        # *   zh-HK: Chinese, Traditional (Hong Kong, China).
        # *   zh-CN: Simplified Chinese.
        # *   ja-JP: Japanese.
        self.language_type = language_type
        # The OS type of the image.
        # 
        # Valid values:
        # 
        # *   Linux
        # *   Unknown
        # *   Windows
        # *   Android
        self.os_type = os_type
        # The image encapsulation type.
        # 
        # Valid values:
        # 
        # *   Ecs_Container: ECS and Docker image
        # *   Ecs: ECS image
        self.package_type = package_type
        # The current page number.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The name of the operating system platform.
        # 
        # Valid values:
        # 
        # *   Ubuntu
        # *   Debian
        # *   Windows Server 2022
        # *   Windows Server 2019
        # *   Windows Server 2016
        # *   Windows 11
        # *   Windows 10
        self.platform_name = platform_name
        # The list of supported platform types. For valid values, refer to PlatformName above.
        self.platform_name_list = platform_name_list
        # The product type.
        # 
        # Valid values:
        # 
        # *   CloudDesktop: Elastic Desktop Service
        # *   CloudApp: App Streaming
        # *   WuyingServer: Workstation
        self.product_type = product_type
        # The list of products that are supported when the image supports multiple products.
        self.product_type_list = product_type_list
        # The protocol type of the image.
        # 
        # Valid values:
        # 
        # *   HDX: the High-definition Experience (HDX) protocol
        # *   ASP: the Alibaba Cloud-developed ASP protocol
        self.protocol_type = protocol_type
        # Find images with certain fixed specifications.
        self.resource_instance_type = resource_instance_type
        # The status of the image. You can query images in the specified status. By default, all images in the Not Deleted state are queried.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The image is available.
        # *   INIT: The image is being initialized.
        # *   CREATE_FAILED: The image failed to be created.
        # *   CREATING: The image is being created.
        self.status = status
        # The tags to query.
        self.tag_list = tag_list

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id_list is not None:
            result['BizRegionIdList'] = self.biz_region_id_list
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list
        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.language_type is not None:
            result['LanguageType'] = self.language_type
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.platform_name_list is not None:
            result['PlatformNameList'] = self.platform_name_list
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.product_type_list is not None:
            result['ProductTypeList'] = self.product_type_list
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.resource_instance_type is not None:
            result['ResourceInstanceType'] = self.resource_instance_type
        if self.status is not None:
            result['Status'] = self.status
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionIdList') is not None:
            self.biz_region_id_list = m.get('BizRegionIdList')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')
        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('LanguageType') is not None:
            self.language_type = m.get('LanguageType')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('PlatformNameList') is not None:
            self.platform_name_list = m.get('PlatformNameList')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProductTypeList') is not None:
            self.product_type_list = m.get('ProductTypeList')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ResourceInstanceType') is not None:
            self.resource_instance_type = m.get('ResourceInstanceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = ListImageRequestTagList()
                self.tag_list.append(temp_model.from_map(k))
        return self


class ListImageResponseBodyDataAppList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ListImageResponseBodyDataImageRegionDistributeList(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        progress: str = None,
        region_id: str = None,
        status: str = None,
        version_id: str = None,
    ):
        # System image IDs follow a descriptive, human-readable format, while custom image IDs are automatically generated by the system.
        self.image_id = image_id
        # The progress.
        self.progress = progress
        # The supported region.
        self.region_id = region_id
        # The status.
        self.status = status
        # The version of the image.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListImageResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_list: List[ListImageResponseBodyDataAppList] = None,
        base_image_id: str = None,
        base_image_version: str = None,
        biz_type: int = None,
        compatible_mode: bool = None,
        data_disk_size: int = None,
        description: str = None,
        distro: str = None,
        driver_list: List[str] = None,
        feature_list: List[str] = None,
        fota_channel: str = None,
        fota_version: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_create_mode: str = None,
        image_id: str = None,
        image_name: str = None,
        image_region_distribute_list: List[ListImageResponseBodyDataImageRegionDistributeList] = None,
        image_region_list: List[str] = None,
        image_type: str = None,
        language: str = None,
        latest_version_id: str = None,
        online_version: bool = None,
        online_version_id: str = None,
        os_type: str = None,
        package_type: str = None,
        parent_image_id: str = None,
        parent_image_version: str = None,
        platform: int = None,
        platform_name: str = None,
        product_type: str = None,
        protocol_type: str = None,
        resource_instance_category: str = None,
        scene: str = None,
        session_type: str = None,
        status: str = None,
        supported_language_list: List[str] = None,
        system_disk_size: int = None,
        version_id: str = None,
        version_name: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        # The tenant ID.
        self.ali_uid = ali_uid
        # The application configuration.
        self.app_list = app_list
        # The base image ID.
        self.base_image_id = base_image_id
        # The version of the base image.
        self.base_image_version = base_image_version
        # The service type.
        self.biz_type = biz_type
        # Specifies whether to use the compatibility mode.
        self.compatible_mode = compatible_mode
        # The size of the data disk. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The description of the image.
        self.description = description
        # The name of the release.
        self.distro = distro
        # The information about each driver.
        self.driver_list = driver_list
        # The image feature tags.
        self.feature_list = feature_list
        # >  This parameter is not available for public use.
        self.fota_channel = fota_channel
        # The FOTA version.
        self.fota_version = fota_version
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The image creation type.
        # 
        # Valid values:
        # 
        # *   BY_SNAPSHOT_ID: The image is created from the snapshot or contains only a system disk.
        # *   BUILDER_MANUAL: The image is manually generated.
        # *   INSTANCE_AUTO: The image is automatically generated based on an instance.
        # *   BY_INSTANCE_ID: The image is created from an instance or contains both a system disk and data disks.
        self.image_create_mode = image_create_mode
        # System image IDs follow a descriptive, human-readable format, while custom image IDs are automatically generated by the system.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # Layered supported regions information.
        self.image_region_distribute_list = image_region_distribute_list
        # The region ID.
        self.image_region_list = image_region_list
        # The type of the image.
        self.image_type = image_type
        # The image language. When the packaging type is VHD or Container, the image inherits its properties from the ECS-type image within the same image bundle.
        self.language = language
        # The latest sub-version of the image. (An image consists of multiple sub-versions.)
        self.latest_version_id = latest_version_id
        # Indicates whether the current version is the active version.
        self.online_version = online_version
        # This image tag currently points to the specified sub-version of the parent image. (An image consists of multiple sub-versions.)
        self.online_version_id = online_version_id
        # The type of the image.
        self.os_type = os_type
        # The image encapsulation type.
        self.package_type = package_type
        # The ID of the parent image from which this image is derived. Note: This field is only applicable to custom images, as system images do not have a parent.
        self.parent_image_id = parent_image_id
        # The version of the parent image.
        self.parent_image_version = parent_image_version
        # The operating system platform of the image.
        # 
        # >  When the packaging type is VHD or Container, the image inherits its properties from the ECS-type image within the same image bundle.
        self.platform = platform
        # The name of the operating system platform.
        self.platform_name = platform_name
        # The product type.
        self.product_type = product_type
        # The protocol type.
        self.protocol_type = protocol_type
        # The types of resources that are supported by the images.
        self.resource_instance_category = resource_instance_category
        self.scene = scene
        # The type of the session.
        # 
        # Valid values:
        # 
        # *   SINGLE_SESSION
        # *   MULTIPLE_SESSION
        self.session_type = session_type
        # The state of the image.
        self.status = status
        # The supported languages.
        self.supported_language_list = supported_language_list
        # The size of the system disk. Unit: GiB.
        # 
        # >  The system disk must be at least as large as the image.
        self.system_disk_size = system_disk_size
        # The version of the image.
        self.version_id = version_id
        # The version number.
        self.version_name = version_name
        # Specifies whether to enable disk encryption.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key that is used to encrypt the disk.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        if self.app_list:
            for k in self.app_list:
                if k:
                    k.validate()
        if self.image_region_distribute_list:
            for k in self.image_region_distribute_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        if self.base_image_id is not None:
            result['BaseImageId'] = self.base_image_id
        if self.base_image_version is not None:
            result['BaseImageVersion'] = self.base_image_version
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.compatible_mode is not None:
            result['CompatibleMode'] = self.compatible_mode
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.description is not None:
            result['Description'] = self.description
        if self.distro is not None:
            result['Distro'] = self.distro
        if self.driver_list is not None:
            result['DriverList'] = self.driver_list
        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list
        if self.fota_channel is not None:
            result['FotaChannel'] = self.fota_channel
        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_create_mode is not None:
            result['ImageCreateMode'] = self.image_create_mode
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        result['ImageRegionDistributeList'] = []
        if self.image_region_distribute_list is not None:
            for k in self.image_region_distribute_list:
                result['ImageRegionDistributeList'].append(k.to_map() if k else None)
        if self.image_region_list is not None:
            result['ImageRegionList'] = self.image_region_list
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.language is not None:
            result['Language'] = self.language
        if self.latest_version_id is not None:
            result['LatestVersionId'] = self.latest_version_id
        if self.online_version is not None:
            result['OnlineVersion'] = self.online_version
        if self.online_version_id is not None:
            result['OnlineVersionId'] = self.online_version_id
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.parent_image_id is not None:
            result['ParentImageId'] = self.parent_image_id
        if self.parent_image_version is not None:
            result['ParentImageVersion'] = self.parent_image_version
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.resource_instance_category is not None:
            result['ResourceInstanceCategory'] = self.resource_instance_category
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supported_language_list is not None:
            result['SupportedLanguageList'] = self.supported_language_list
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.app_list = []
        if m.get('AppList') is not None:
            for k in m.get('AppList'):
                temp_model = ListImageResponseBodyDataAppList()
                self.app_list.append(temp_model.from_map(k))
        if m.get('BaseImageId') is not None:
            self.base_image_id = m.get('BaseImageId')
        if m.get('BaseImageVersion') is not None:
            self.base_image_version = m.get('BaseImageVersion')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CompatibleMode') is not None:
            self.compatible_mode = m.get('CompatibleMode')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Distro') is not None:
            self.distro = m.get('Distro')
        if m.get('DriverList') is not None:
            self.driver_list = m.get('DriverList')
        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')
        if m.get('FotaChannel') is not None:
            self.fota_channel = m.get('FotaChannel')
        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageCreateMode') is not None:
            self.image_create_mode = m.get('ImageCreateMode')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        self.image_region_distribute_list = []
        if m.get('ImageRegionDistributeList') is not None:
            for k in m.get('ImageRegionDistributeList'):
                temp_model = ListImageResponseBodyDataImageRegionDistributeList()
                self.image_region_distribute_list.append(temp_model.from_map(k))
        if m.get('ImageRegionList') is not None:
            self.image_region_list = m.get('ImageRegionList')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LatestVersionId') is not None:
            self.latest_version_id = m.get('LatestVersionId')
        if m.get('OnlineVersion') is not None:
            self.online_version = m.get('OnlineVersion')
        if m.get('OnlineVersionId') is not None:
            self.online_version_id = m.get('OnlineVersionId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('ParentImageId') is not None:
            self.parent_image_id = m.get('ParentImageId')
        if m.get('ParentImageVersion') is not None:
            self.parent_image_version = m.get('ParentImageVersion')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ResourceInstanceCategory') is not None:
            self.resource_instance_category = m.get('ResourceInstanceCategory')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportedLanguageList') is not None:
            self.supported_language_list = m.get('SupportedLanguageList')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')
        return self


class ListImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[ListImageResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The total number of entries.
        self.count = count
        # The returned data.
        self.data = data
        # The message that is returned for the request.
        self.message = message
        # The page number returned.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true: The request is successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListImageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeInstanceTypeRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        cpu: float = None,
        gpu: float = None,
        gpu_memory: int = None,
        language: str = None,
        memory: int = None,
        node_instance_type: str = None,
        node_instance_type_family: str = None,
        order_by: str = None,
        os_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        sort_type: str = None,
    ):
        # The ID of the region where the resource resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-hangzhou: China (Hangzhou)
        self.biz_region_id = biz_region_id
        self.cpu = cpu
        self.gpu = gpu
        self.gpu_memory = gpu_memory
        # The language that you want to use.
        # 
        # Valid values:
        # 
        # *   en-US: English (US)
        # *   zh-CN: Simplified Chinese
        self.language = language
        self.memory = memory
        # The resource type that you want to query. If you do not configure this parameter, all resource types are returned.
        self.node_instance_type = node_instance_type
        self.node_instance_type_family = node_instance_type_family
        self.order_by = order_by
        # The operating system that is supported.
        # 
        # Valid value:
        # 
        # *   Windows: the Windows operating system
        self.os_type = os_type
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.language is not None:
            result['Language'] = self.language
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_instance_type_family is not None:
            result['NodeInstanceTypeFamily'] = self.node_instance_type_family
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodeInstanceTypeFamily') is not None:
            self.node_instance_type_family = m.get('NodeInstanceTypeFamily')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        return self


class ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gpu_memory: int = None,
        max_capacity: int = None,
        memory: int = None,
        node_instance_type: str = None,
        node_instance_type_family: str = None,
        node_type_name: str = None,
    ):
        # The number of vCPUs.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU size. Unit: MB.
        self.gpu_memory = gpu_memory
        # The maximum number of sessions to which a resource can connect at the same time. If a resource connects to a large number of sessions at the same time, user experience can be compromised. The value range varies based on the resource type. The following items describe the value ranges of different resource types:
        # 
        # *   appstreaming.general.4c8g: 1 to 2
        # *   appstreaming.general.8c16g: 1 to 4
        # *   appstreaming.vgpu.8c16g.4g: 1 to 4
        # *   appstreaming.vgpu.8c31g.16g: 1 to 4
        # *   appstreaming.vgpu.14c93g.12g: 1 to 6
        self.max_capacity = max_capacity
        # The memory size. Unit: MB.
        self.memory = memory
        # The ID of the resource type.
        self.node_instance_type = node_instance_type
        # The resource type family.
        # 
        # Valid values:
        # 
        # *   appstreaming.general: WUYING - General
        # *   appstreaming.vgpu: WUYING - Graphics
        self.node_instance_type_family = node_instance_type_family
        # The name of the resource type.
        self.node_type_name = node_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_instance_type_family is not None:
            result['NodeInstanceTypeFamily'] = self.node_instance_type_family
        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodeInstanceTypeFamily') is not None:
            self.node_instance_type_family = m.get('NodeInstanceTypeFamily')
        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')
        return self


class ListNodeInstanceTypeResponseBody(TeaModel):
    def __init__(
        self,
        node_instance_type_models: List[ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The resource types.
        self.node_instance_type_models = node_instance_type_models
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.node_instance_type_models:
            for k in self.node_instance_type_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInstanceTypeModels'] = []
        if self.node_instance_type_models is not None:
            for k in self.node_instance_type_models:
                result['NodeInstanceTypeModels'].append(k.to_map() if k else None)
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
        self.node_instance_type_models = []
        if m.get('NodeInstanceTypeModels') is not None:
            for k in m.get('NodeInstanceTypeModels'):
                temp_model = ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels()
                self.node_instance_type_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeInstanceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeInstanceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodeInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 200.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ListNodesResponseBodyNodeModels(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        node_id: str = None,
    ):
        # The billing method of the resource node.
        # 
        # >  This parameter is returned only if the ChargeResourceMode parameter of the delivery group to which the resource node belongs is set to Node.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   Prepaid: subscription
        self.charge_type = charge_type
        # The ID of the resource node.
        # 
        # >  This parameter is returned only if the ChargeResourceMode parameter of the delivery group to which the resource node belongs is set to Node.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        node_models: List[ListNodesResponseBodyNodeModels] = None,
        per_page_size: int = None,
        request_id: str = None,
        to_page: int = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The resource nodes.
        self.node_models = node_models
        # The number of entries per page.
        self.per_page_size = per_page_size
        # The request ID.
        self.request_id = request_id
        # The page number.
        self.to_page = to_page

    def validate(self):
        if self.node_models:
            for k in self.node_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['NodeModels'] = []
        if self.node_models is not None:
            for k in self.node_models:
                result['NodeModels'].append(k.to_map() if k else None)
        if self.per_page_size is not None:
            result['PerPageSize'] = self.per_page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.to_page is not None:
            result['ToPage'] = self.to_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.node_models = []
        if m.get('NodeModels') is not None:
            for k in m.get('NodeModels'):
                temp_model = ListNodesResponseBodyNodeModels()
                self.node_models.append(temp_model.from_map(k))
        if m.get('PerPageSize') is not None:
            self.per_page_size = m.get('PerPageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ToPage') is not None:
            self.to_page = m.get('ToPage')
        return self


class ListNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOtaTaskRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        ota_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The type of the OTA update task.
        # 
        # Valid values:
        # 
        # *   Fota: update of the system components of Alibaba Cloud Workspace
        # 
        # This parameter is required.
        self.ota_type = ota_type
        # The page number of the page to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOtaTaskResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        ota_version: str = None,
        task_display_status: str = None,
        task_id: str = None,
        task_start_time: str = None,
    ):
        # The OTA version.
        self.ota_version = ota_version
        # The task status.
        # 
        # Valid values:
        # 
        # *   FAILED
        # *   RUNNING
        # *   TERMINATED
        # *   PART_FINISHED
        # *   STANDBY
        # *   FINISHED
        self.task_display_status = task_display_status
        # The task ID.
        self.task_id = task_id
        # The start time of the OTA update task. The time follows the ISO 8601 standard.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.task_start_time = task_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_display_status is not None:
            result['TaskDisplayStatus'] = self.task_display_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskDisplayStatus') is not None:
            self.task_display_status = m.get('TaskDisplayStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        return self


class ListOtaTaskResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        task_list: List[ListOtaTaskResponseBodyTaskList] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The OTA update tasks.
        self.task_list = task_list
        # The total number of OTA update tasks.
        self.total_count = total_count

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListOtaTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOtaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOtaTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersistentAppInstancesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_persistent_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The IDs of the persistent sessions.
        self.app_instance_persistent_ids = app_instance_persistent_ids
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. The value cannot be greater than **100**. Default value: **20**.
        self.page_size = page_size
        # The product type.
        # 
        # Valid values:
        # 
        # *   CloudApp: App Streaming
        # *   CloudBrowser: Cloud-based Browser
        # *   AndroidCloud: Cloud Phone
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_persistent_ids is not None:
            result['AppInstancePersistentIds'] = self.app_instance_persistent_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstancePersistentIds') is not None:
            self.app_instance_persistent_ids = m.get('AppInstancePersistentIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ListPersistentAppInstancesResponseBodyPersistentAppInstanceModels(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        app_instance_persistent_name: str = None,
        app_instance_persistent_status: str = None,
        app_instance_status: str = None,
        authorized_users: List[str] = None,
        gmt_create: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the app instance.
        self.app_instance_id = app_instance_id
        # The ID of the app instance of the persistent session type.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The name of the app instance of the persistent session type.
        self.app_instance_persistent_name = app_instance_persistent_name
        # The status of the app instance of the persistent session type.
        # 
        # Valid values:
        # 
        # *   STARTING
        # *   RUNNING
        # *   STOPPED
        # *   UNAVAILABLE
        # *   DELETING
        # *   PENDING
        # *   STOPPING
        # *   DELETED
        # *   REBUILDING
        self.app_instance_persistent_status = app_instance_persistent_status
        # The status of the app instance.
        # 
        # Valid values:
        # 
        # *   INIT: The app instance is being initialized.
        # *   STARTING: The app instance is being started.
        # *   CLOSING: The app instance is being stopped.
        # *   CLOSED: The app instance is closed.
        # *   RUNNING: The app instance is running.
        # *   idle: The app instance is idle.
        # *   BOUND: The app instance is bound to an app instance group.
        # *   UNAVAILABLE: The app instance is unavailable.
        # *   DELETED: The app instance is deleted.
        self.app_instance_status = app_instance_status
        # The authorized users.
        self.authorized_users = authorized_users
        # The time when the app instance was created.
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.app_instance_persistent_name is not None:
            result['AppInstancePersistentName'] = self.app_instance_persistent_name
        if self.app_instance_persistent_status is not None:
            result['AppInstancePersistentStatus'] = self.app_instance_persistent_status
        if self.app_instance_status is not None:
            result['AppInstanceStatus'] = self.app_instance_status
        if self.authorized_users is not None:
            result['AuthorizedUsers'] = self.authorized_users
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('AppInstancePersistentName') is not None:
            self.app_instance_persistent_name = m.get('AppInstancePersistentName')
        if m.get('AppInstancePersistentStatus') is not None:
            self.app_instance_persistent_status = m.get('AppInstancePersistentStatus')
        if m.get('AppInstanceStatus') is not None:
            self.app_instance_status = m.get('AppInstanceStatus')
        if m.get('AuthorizedUsers') is not None:
            self.authorized_users = m.get('AuthorizedUsers')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class ListPersistentAppInstancesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        persistent_app_instance_models: List[ListPersistentAppInstancesResponseBodyPersistentAppInstanceModels] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The app instances of the persistent session type.
        self.persistent_app_instance_models = persistent_app_instance_models
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.persistent_app_instance_models:
            for k in self.persistent_app_instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PersistentAppInstanceModels'] = []
        if self.persistent_app_instance_models is not None:
            for k in self.persistent_app_instance_models:
                result['PersistentAppInstanceModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.persistent_app_instance_models = []
        if m.get('PersistentAppInstanceModels') is not None:
            for k in m.get('PersistentAppInstanceModels'):
                temp_model = ListPersistentAppInstancesResponseBodyPersistentAppInstanceModels()
                self.persistent_app_instance_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPersistentAppInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPersistentAppInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPersistentAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(
        self,
        biz_source: str = None,
        product_type: str = None,
    ):
        # >  This parameter is not publicly available.
        self.biz_source = biz_source
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_source is not None:
            result['BizSource'] = self.biz_source
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizSource') is not None:
            self.biz_source = m.get('BizSource')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ListRegionsResponseBodyRegionModels(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        region_models: List[ListRegionsResponseBodyRegionModels] = None,
        request_id: str = None,
    ):
        # The region IDs.
        self.region_models = region_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.region_models:
            for k in self.region_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionModels'] = []
        if self.region_models is not None:
            for k in self.region_models:
                result['RegionModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_models = []
        if m.get('RegionModels') is not None:
            for k in m.get('RegionModels'):
                temp_model = ListRegionsResponseBodyRegionModels()
                self.region_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagCloudResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        scope: str = None,
    ):
        # The number of entries per page. Maximum value: 1000. Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The resource IDs. You can specify up to 50 resource IDs. You do not need to specify this parameter if you set ResourceType to AliUid.
        self.resource_ids = resource_ids
        # The type of the cloud resource.
        # 
        # Valid values:
        # 
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag type.
        # 
        # Valid values:
        # 
        # *   All (default): all tags.
        # *   Custom: custom tag.
        # *   System: system tag.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ListTagCloudResourcesResponseBodyResourceTagsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag type.
        # 
        # Valid values:
        # 
        # *   Custom: custom tag.
        # *   System: system tag.
        self.scope = scope
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagCloudResourcesResponseBodyResourceTags(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tags: List[ListTagCloudResourcesResponseBodyResourceTagsTags] = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The type of the cloud resource.
        # 
        # Valid values:
        # 
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        self.resource_type = resource_type
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagCloudResourcesResponseBodyResourceTagsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagCloudResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_tags: List[ListTagCloudResourcesResponseBodyResourceTags] = None,
        total_count: int = None,
    ):
        # Indicates whether the next query is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tags added to the cloud resources.
        self.resource_tags = resource_tags
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.resource_tags:
            for k in self.resource_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceTags'] = []
        if self.resource_tags is not None:
            for k in self.resource_tags:
                result['ResourceTags'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_tags = []
        if m.get('ResourceTags') is not None:
            for k in m.get('ResourceTags'):
                temp_model = ListTagCloudResourcesResponseBodyResourceTags()
                self.resource_tags.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagCloudResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagCloudResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagCloudResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantConfigResponseBodyTenantConfigModel(TeaModel):
    def __init__(
        self,
        app_instance_group_expire_remind: bool = None,
    ):
        # Indicates whether the resource expiration reminder feature is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.app_instance_group_expire_remind = app_instance_group_expire_remind

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')
        return self


class ListTenantConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_config_model: ListTenantConfigResponseBodyTenantConfigModel = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The user configurations.
        self.tenant_config_model = tenant_config_model

    def validate(self):
        if self.tenant_config_model:
            self.tenant_config_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_config_model is not None:
            result['TenantConfigModel'] = self.tenant_config_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantConfigModel') is not None:
            temp_model = ListTenantConfigResponseBodyTenantConfigModel()
            self.tenant_config_model = temp_model.from_map(m['TenantConfigModel'])
        return self


class ListTenantConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTenantConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTenantConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWuyingServerRequest(TeaModel):
    def __init__(
        self,
        add_virtual_node_pool_status_list: List[str] = None,
        biz_region_id: str = None,
        charge_type: str = None,
        image_id: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        server_instance_type: str = None,
        status: str = None,
        virtual_node_pool_id: str = None,
        wuying_server_id_list: List[str] = None,
        wuying_server_name_or_id: str = None,
    ):
        self.add_virtual_node_pool_status_list = add_virtual_node_pool_status_list
        # The region ID.
        self.biz_region_id = biz_region_id
        # The billing method of the Internet access package.
        self.charge_type = charge_type
        # The image ID.
        self.image_id = image_id
        # The office network IDs.
        self.office_site_id = office_site_id
        # The page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # Workstation specifications.
        self.server_instance_type = server_instance_type
        # The status of the workstation.
        self.status = status
        self.virtual_node_pool_id = virtual_node_pool_id
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list
        # The workstation name or workstation ID.
        self.wuying_server_name_or_id = wuying_server_name_or_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_virtual_node_pool_status_list is not None:
            result['AddVirtualNodePoolStatusList'] = self.add_virtual_node_pool_status_list
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.server_instance_type is not None:
            result['ServerInstanceType'] = self.server_instance_type
        if self.status is not None:
            result['Status'] = self.status
        if self.virtual_node_pool_id is not None:
            result['VirtualNodePoolId'] = self.virtual_node_pool_id
        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list
        if self.wuying_server_name_or_id is not None:
            result['WuyingServerNameOrId'] = self.wuying_server_name_or_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddVirtualNodePoolStatusList') is not None:
            self.add_virtual_node_pool_status_list = m.get('AddVirtualNodePoolStatusList')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServerInstanceType') is not None:
            self.server_instance_type = m.get('ServerInstanceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VirtualNodePoolId') is not None:
            self.virtual_node_pool_id = m.get('VirtualNodePoolId')
        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')
        if m.get('WuyingServerNameOrId') is not None:
            self.wuying_server_name_or_id = m.get('WuyingServerNameOrId')
        return self


class ListWuyingServerResponseBodyWuyingServerListDataDisk(TeaModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_performance_level: str = None,
        data_disk_size: int = None,
    ):
        # The category of data disk.
        self.data_disk_category = data_disk_category
        # The PL of the data disk.
        self.data_disk_performance_level = data_disk_performance_level
        # The size of the data disk. Unit: GB.
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_performance_level is not None:
            result['DataDiskPerformanceLevel'] = self.data_disk_performance_level
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('DataDiskPerformanceLevel')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        return self


class ListWuyingServerResponseBodyWuyingServerListInstanceInfoList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        network_interface_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the ENI.
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class ListWuyingServerResponseBodyWuyingServerListServerInstanceTypeInfo(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gpu_memory: int = None,
        memory: int = None,
        server_instance_type: str = None,
    ):
        # The number of vCPUs.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The memory size. Unit: MB.
        self.gpu_memory = gpu_memory
        # The memory size. Unit: MB.
        self.memory = memory
        # Workstation specifications.
        self.server_instance_type = server_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.server_instance_type is not None:
            result['ServerInstanceType'] = self.server_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('ServerInstanceType') is not None:
            self.server_instance_type = m.get('ServerInstanceType')
        return self


class ListWuyingServerResponseBodyWuyingServerList(TeaModel):
    def __init__(
        self,
        add_virtual_node_pool_status: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        create_time: str = None,
        data_disk: List[ListWuyingServerResponseBodyWuyingServerListDataDisk] = None,
        expired_time: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_info_list: List[ListWuyingServerResponseBodyWuyingServerListInstanceInfoList] = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        os_type: str = None,
        security_group_ids: List[str] = None,
        server_instance_type_info: ListWuyingServerResponseBodyWuyingServerListServerInstanceTypeInfo = None,
        status: str = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        virtual_node_pool_id: str = None,
        wuying_server_id: str = None,
        wuying_server_name: str = None,
    ):
        self.add_virtual_node_pool_status = add_virtual_node_pool_status
        # Region.
        self.biz_region_id = biz_region_id
        # The billing method.
        self.charge_type = charge_type
        # The time when the storage resource was created.
        self.create_time = create_time
        # The data disks.
        self.data_disk = data_disk
        # The time when the subscription instance expires.
        self.expired_time = expired_time
        # The ID of the custom image.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The list of information about the workstation instance.
        self.instance_info_list = instance_info_list
        # The private IP address.
        self.network_interface_ip = network_interface_ip
        # The ID of the office network.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The type of the office network.
        self.office_site_type = office_site_type
        # The OS type.
        self.os_type = os_type
        self.security_group_ids = security_group_ids
        # The specifications.
        self.server_instance_type_info = server_instance_type_info
        # The status of the workstation.
        self.status = status
        # The type of the system disk.
        self.system_disk_category = system_disk_category
        # The performance level (PL) of the system disk.
        self.system_disk_performance_level = system_disk_performance_level
        # The size of the system disk. Unit: GiB.
        self.system_disk_size = system_disk_size
        self.virtual_node_pool_id = virtual_node_pool_id
        # The ID of the workstation.
        self.wuying_server_id = wuying_server_id
        # The name of the workstation.
        self.wuying_server_name = wuying_server_name

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.instance_info_list:
            for k in self.instance_info_list:
                if k:
                    k.validate()
        if self.server_instance_type_info:
            self.server_instance_type_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_virtual_node_pool_status is not None:
            result['AddVirtualNodePoolStatus'] = self.add_virtual_node_pool_status
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        result['InstanceInfoList'] = []
        if self.instance_info_list is not None:
            for k in self.instance_info_list:
                result['InstanceInfoList'].append(k.to_map() if k else None)
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.server_instance_type_info is not None:
            result['ServerInstanceTypeInfo'] = self.server_instance_type_info.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.virtual_node_pool_id is not None:
            result['VirtualNodePoolId'] = self.virtual_node_pool_id
        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id
        if self.wuying_server_name is not None:
            result['WuyingServerName'] = self.wuying_server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddVirtualNodePoolStatus') is not None:
            self.add_virtual_node_pool_status = m.get('AddVirtualNodePoolStatus')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = ListWuyingServerResponseBodyWuyingServerListDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        self.instance_info_list = []
        if m.get('InstanceInfoList') is not None:
            for k in m.get('InstanceInfoList'):
                temp_model = ListWuyingServerResponseBodyWuyingServerListInstanceInfoList()
                self.instance_info_list.append(temp_model.from_map(k))
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('ServerInstanceTypeInfo') is not None:
            temp_model = ListWuyingServerResponseBodyWuyingServerListServerInstanceTypeInfo()
            self.server_instance_type_info = temp_model.from_map(m['ServerInstanceTypeInfo'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('VirtualNodePoolId') is not None:
            self.virtual_node_pool_id = m.get('VirtualNodePoolId')
        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')
        if m.get('WuyingServerName') is not None:
            self.wuying_server_name = m.get('WuyingServerName')
        return self


class ListWuyingServerResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        wuying_server_list: List[ListWuyingServerResponseBodyWuyingServerList] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The list of workstation information.
        self.wuying_server_list = wuying_server_list

    def validate(self):
        if self.wuying_server_list:
            for k in self.wuying_server_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WuyingServerList'] = []
        if self.wuying_server_list is not None:
            for k in self.wuying_server_list:
                result['WuyingServerList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.wuying_server_list = []
        if m.get('WuyingServerList') is not None:
            for k in m.get('WuyingServerList'):
                temp_model = ListWuyingServerResponseBodyWuyingServerList()
                self.wuying_server_list.append(temp_model.from_map(k))
        return self


class ListWuyingServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWuyingServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWuyingServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogOffAllSessionsInAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class LogOffAllSessionsInAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LogOffAllSessionsInAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LogOffAllSessionsInAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LogOffAllSessionsInAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppInstanceGroupAttributeRequestNetworkDomainRules(TeaModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The policy used for the domain name.
        # 
        # Valid values:
        # 
        # *   allow
        # *   block
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyAppInstanceGroupAttributeRequestNetwork(TeaModel):
    def __init__(
        self,
        domain_rules: List[ModifyAppInstanceGroupAttributeRequestNetworkDomainRules] = None,
    ):
        # The domain name rules.
        self.domain_rules = domain_rules

    def validate(self):
        if self.domain_rules:
            for k in self.domain_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainRules'] = []
        if self.domain_rules is not None:
            for k in self.domain_rules:
                result['DomainRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_rules = []
        if m.get('DomainRules') is not None:
            for k in m.get('DomainRules'):
                temp_model = ModifyAppInstanceGroupAttributeRequestNetworkDomainRules()
                self.domain_rules.append(temp_model.from_map(k))
        return self


class ModifyAppInstanceGroupAttributeRequestNodePool(TeaModel):
    def __init__(
        self,
        node_capacity: int = None,
        node_pool_id: str = None,
    ):
        # The maximum number of sessions to which a resource can connect at the same time. If a resource connects to a large number of sessions at the same time, user experience can be compromised. The value range varies based on the resource type. The following items describe the value ranges of different resource types:
        # 
        # *   appstreaming.general.4c8g: 1 to 2
        # *   appstreaming.general.8c16g: 1 to 4
        # *   appstreaming.vgpu.8c16g.4g: 1 to 4
        # *   appstreaming.vgpu.8c31g.16g: 1 to 4
        # *   appstreaming.vgpu.14c93g.12g: 1 to 6
        self.node_capacity = node_capacity
        # The ID of the resource group.
        self.node_pool_id = node_pool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        return self


class ModifyAppInstanceGroupAttributeRequestSecurityPolicy(TeaModel):
    def __init__(
        self,
        reset_after_unbind: bool = None,
        skip_user_auth_check: bool = None,
    ):
        # Specifies whether to reset after unbinding from a delivery group.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.reset_after_unbind = reset_after_unbind
        # Specifies whether to skip user permission verification.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: This is the default value.
        self.skip_user_auth_check = skip_user_auth_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfile(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        user_profile_switch: bool = None,
    ):
        # The ID of the File Storage NAS (NAS) file system used to store user data.
        self.file_system_id = file_system_id
        # Specifies whether user data roaming is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.user_profile_switch = user_profile_switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.user_profile_switch is not None:
            result['UserProfileSwitch'] = self.user_profile_switch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('UserProfileSwitch') is not None:
            self.user_profile_switch = m.get('UserProfileSwitch')
        return self


class ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfileFollow(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        profile_follow_switch: bool = None,
    ):
        self.file_system_id = file_system_id
        self.profile_follow_switch = profile_follow_switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.profile_follow_switch is not None:
            result['ProfileFollowSwitch'] = self.profile_follow_switch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProfileFollowSwitch') is not None:
            self.profile_follow_switch = m.get('ProfileFollowSwitch')
        return self


class ModifyAppInstanceGroupAttributeRequestStoragePolicy(TeaModel):
    def __init__(
        self,
        storage_type_list: List[str] = None,
        user_profile: ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfile = None,
        user_profile_follow: ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfileFollow = None,
    ):
        # The storage types.
        self.storage_type_list = storage_type_list
        # The configurations of user data roaming.
        self.user_profile = user_profile
        self.user_profile_follow = user_profile_follow

    def validate(self):
        if self.user_profile:
            self.user_profile.validate()
        if self.user_profile_follow:
            self.user_profile_follow.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type_list is not None:
            result['StorageTypeList'] = self.storage_type_list
        if self.user_profile is not None:
            result['UserProfile'] = self.user_profile.to_map()
        if self.user_profile_follow is not None:
            result['UserProfileFollow'] = self.user_profile_follow.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageTypeList') is not None:
            self.storage_type_list = m.get('StorageTypeList')
        if m.get('UserProfile') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfile()
            self.user_profile = temp_model.from_map(m['UserProfile'])
        if m.get('UserProfileFollow') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfileFollow()
            self.user_profile_follow = temp_model.from_map(m['UserProfileFollow'])
        return self


class ModifyAppInstanceGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        network: ModifyAppInstanceGroupAttributeRequestNetwork = None,
        node_pool: ModifyAppInstanceGroupAttributeRequestNodePool = None,
        per_session_per_app: bool = None,
        pre_open_app_id: str = None,
        pre_open_mode: str = None,
        product_type: str = None,
        security_policy: ModifyAppInstanceGroupAttributeRequestSecurityPolicy = None,
        session_timeout: int = None,
        storage_policy: ModifyAppInstanceGroupAttributeRequestStoragePolicy = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # The network settings.
        # 
        # >  If you want to use this parameter, submit a ticket.
        self.network = network
        # The information about the resource group.
        self.node_pool = node_pool
        # Specifies whether only one application can be opened in a session.
        # 
        # *   After you enable this feature, the system assigns a session to each application if you open multiple applications in a delivery group. This consumes a larger number of sessions.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.per_session_per_app = per_session_per_app
        # The application ID of the pre-open application. If you set `PreOpenMode` to `SINGLE_APP`, you cannot leave this parameter empty.``
        self.pre_open_app_id = pre_open_app_id
        # The pre-open mode.
        # 
        # Valid values:
        # 
        # *   SINGLE_APP: enables the pre-open mode for a single application.
        # *   OFF: disables the pre-open mode. This is the default value.
        self.pre_open_mode = pre_open_mode
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The security policy.
        self.security_policy = security_policy
        # The duration for which sessions are retained after disconnection. Unit: minutes. After an end user disconnects from a session, the session is closed only after the specified duration elapses. If you want to permanently retain sessions, set this parameter to `-1`. Valid values:-1 and 3 to 300. Default value: `15`.
        self.session_timeout = session_timeout
        # The storage policy.
        self.storage_policy = storage_policy

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.per_session_per_app is not None:
            result['PerSessionPerApp'] = self.per_session_per_app
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.pre_open_mode is not None:
            result['PreOpenMode'] = self.pre_open_mode
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('Network') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('NodePool') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('PerSessionPerApp') is not None:
            self.per_session_per_app = m.get('PerSessionPerApp')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('PreOpenMode') is not None:
            self.pre_open_mode = m.get('PreOpenMode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SecurityPolicy') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m['SecurityPolicy'])
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m['StoragePolicy'])
        return self


class ModifyAppInstanceGroupAttributeShrinkRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        network_shrink: str = None,
        node_pool_shrink: str = None,
        per_session_per_app: bool = None,
        pre_open_app_id: str = None,
        pre_open_mode: str = None,
        product_type: str = None,
        security_policy_shrink: str = None,
        session_timeout: int = None,
        storage_policy_shrink: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # The network settings.
        # 
        # >  If you want to use this parameter, submit a ticket.
        self.network_shrink = network_shrink
        # The information about the resource group.
        self.node_pool_shrink = node_pool_shrink
        # Specifies whether only one application can be opened in a session.
        # 
        # *   After you enable this feature, the system assigns a session to each application if you open multiple applications in a delivery group. This consumes a larger number of sessions.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.per_session_per_app = per_session_per_app
        # The application ID of the pre-open application. If you set `PreOpenMode` to `SINGLE_APP`, you cannot leave this parameter empty.``
        self.pre_open_app_id = pre_open_app_id
        # The pre-open mode.
        # 
        # Valid values:
        # 
        # *   SINGLE_APP: enables the pre-open mode for a single application.
        # *   OFF: disables the pre-open mode. This is the default value.
        self.pre_open_mode = pre_open_mode
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The security policy.
        self.security_policy_shrink = security_policy_shrink
        # The duration for which sessions are retained after disconnection. Unit: minutes. After an end user disconnects from a session, the session is closed only after the specified duration elapses. If you want to permanently retain sessions, set this parameter to `-1`. Valid values:-1 and 3 to 300. Default value: `15`.
        self.session_timeout = session_timeout
        # The storage policy.
        self.storage_policy_shrink = storage_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.network_shrink is not None:
            result['Network'] = self.network_shrink
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.per_session_per_app is not None:
            result['PerSessionPerApp'] = self.per_session_per_app
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.pre_open_mode is not None:
            result['PreOpenMode'] = self.pre_open_mode
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('PerSessionPerApp') is not None:
            self.per_session_per_app = m.get('PerSessionPerApp')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('PreOpenMode') is not None:
            self.pre_open_mode = m.get('PreOpenMode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')
        return self


class ModifyAppInstanceGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppInstanceGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppInstanceGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAppInstanceGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppPolicyRequestVideoPolicy(TeaModel):
    def __init__(
        self,
        frame_rate: int = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        streaming_mode: str = None,
        terminal_resolution_adaptive: bool = None,
        visual_quality_strategy: str = None,
        webrtc: bool = None,
    ):
        # The frame rate (FPS).
        # 
        # Enumerated values:
        # 
        # *   30: 30 FPS
        # *   60: 60 FPS
        self.frame_rate = frame_rate
        # The height of the resolution, in pixels.
        self.session_resolution_height = session_resolution_height
        # The width of the resolution, in pixels.
        self.session_resolution_width = session_resolution_width
        # The stream mode. This parameter is used together with `Webrtc` to specify the protocol type.
        # 
        # *   If you set `Webrtc` to `true` and `StreamingMode` to `video`, Web Real-Time Communications (WebRTC) streams are used.
        # *   If you set `Webrtc` to `false` and `StreamingMode` to `video`, video streams are used.
        # *   If you set `Webrtc` to `false` and `StreamingMode` to `mix`, mixed streams are used.
        self.streaming_mode = streaming_mode
        # Whether to use adaptive resolution.
        # 
        # *   `true`: The session resolution changes with the display area of the terminal. In this case, `SessionResolutionWidth` indicates the maximum resolution width and `SessionResolutionHeight` indicates the maximum resolution height.
        # *   `false`: The session resolution does not change with the display area of the terminal. In this case, `SessionResolutionWidth` specifies the fixed resolution width and `SessionResolutionHeight` specifies the fixed resolution height.
        self.terminal_resolution_adaptive = terminal_resolution_adaptive
        # The image quality policy.
        # 
        # Enumerated values:
        # 
        # *   adaptive: adaptive.
        # *   smooth: smooth first.
        # *   quality: quality first.
        self.visual_quality_strategy = visual_quality_strategy
        # Specifies whether to enable WebRTC. This parameter is used together with `StreamingMode` to specify the protocol type.
        # 
        # *   If you set `Webrtc` to `true` and `StreamingMode` to `video`, WebRTC streams are used.
        # *   If you set `Webrtc` to `false` and `StreamingMode` to `video`, video streams are used.
        # *   If you set `Webrtc` to `false` and `StreamingMode` to `mix`, mixed streams are used.
        self.webrtc = webrtc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.visual_quality_strategy is not None:
            result['VisualQualityStrategy'] = self.visual_quality_strategy
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
        if m.get('VisualQualityStrategy') is not None:
            self.visual_quality_strategy = m.get('VisualQualityStrategy')
        if m.get('Webrtc') is not None:
            self.webrtc = m.get('Webrtc')
        return self


class ModifyAppPolicyRequest(TeaModel):
    def __init__(
        self,
        app_policy_id: str = None,
        product_type: str = None,
        video_policy: ModifyAppPolicyRequestVideoPolicy = None,
    ):
        # The policy ID.
        # 
        # This parameter is required.
        self.app_policy_id = app_policy_id
        # The product type.
        # 
        # Enumerated values:
        # 
        # *   CloudApp: RDS Cloud App
        # 
        # This parameter is required.
        self.product_type = product_type
        # Displays the policy.
        self.video_policy = video_policy

    def validate(self):
        if self.video_policy:
            self.video_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.video_policy is not None:
            result['VideoPolicy'] = self.video_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('VideoPolicy') is not None:
            temp_model = ModifyAppPolicyRequestVideoPolicy()
            self.video_policy = temp_model.from_map(m['VideoPolicy'])
        return self


class ModifyAppPolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        app_policy_id: str = None,
        product_type: str = None,
        video_policy_shrink: str = None,
    ):
        # The policy ID.
        # 
        # This parameter is required.
        self.app_policy_id = app_policy_id
        # The product type.
        # 
        # Enumerated values:
        # 
        # *   CloudApp: RDS Cloud App
        # 
        # This parameter is required.
        self.product_type = product_type
        # Displays the policy.
        self.video_policy_shrink = video_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.video_policy_shrink is not None:
            result['VideoPolicy'] = self.video_policy_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('VideoPolicy') is not None:
            self.video_policy_shrink = m.get('VideoPolicy')
        return self


class ModifyAppPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAppPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBrowserInstanceGroupRequestBrowserConfigBookmarks(TeaModel):
    def __init__(
        self,
        bookmark_folder: str = None,
        bookmark_id: str = None,
        bookmark_name: str = None,
        bookmark_url: str = None,
    ):
        # The folder where the bookmark is located.
        self.bookmark_folder = bookmark_folder
        # The ID of the bookmark. This parameter needs to be specified only to modify the bookmark.
        self.bookmark_id = bookmark_id
        # The name of the bookmark.
        # 
        # This parameter is required.
        self.bookmark_name = bookmark_name
        # The URL of the bookmark.
        # 
        # This parameter is required.
        self.bookmark_url = bookmark_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyBrowserInstanceGroupRequestBrowserConfig(TeaModel):
    def __init__(
        self,
        bookmarks: List[ModifyBrowserInstanceGroupRequestBrowserConfigBookmarks] = None,
        browser_param: str = None,
        homepage: str = None,
        remove_bookmarks: List[str] = None,
    ):
        # The bookmark.
        self.bookmarks = bookmarks
        # The startup parameter.
        self.browser_param = browser_param
        # The home page.
        self.homepage = homepage
        # The removed bookmarks.
        self.remove_bookmarks = remove_bookmarks

    def validate(self):
        if self.bookmarks:
            for k in self.bookmarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bookmarks'] = []
        if self.bookmarks is not None:
            for k in self.bookmarks:
                result['Bookmarks'].append(k.to_map() if k else None)
        if self.browser_param is not None:
            result['BrowserParam'] = self.browser_param
        if self.homepage is not None:
            result['Homepage'] = self.homepage
        if self.remove_bookmarks is not None:
            result['RemoveBookmarks'] = self.remove_bookmarks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bookmarks = []
        if m.get('Bookmarks') is not None:
            for k in m.get('Bookmarks'):
                temp_model = ModifyBrowserInstanceGroupRequestBrowserConfigBookmarks()
                self.bookmarks.append(temp_model.from_map(k))
        if m.get('BrowserParam') is not None:
            self.browser_param = m.get('BrowserParam')
        if m.get('Homepage') is not None:
            self.homepage = m.get('Homepage')
        if m.get('RemoveBookmarks') is not None:
            self.remove_bookmarks = m.get('RemoveBookmarks')
        return self


class ModifyBrowserInstanceGroupRequestNetworkRestrictedURLs(TeaModel):
    def __init__(
        self,
        restricted_urlid: str = None,
        url: str = None,
    ):
        # The ID of the domain name. This parameter is required only when you want to modify the domain restriction configuration.
        self.restricted_urlid = restricted_urlid
        # The restricted domain name.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyBrowserInstanceGroupRequestNetwork(TeaModel):
    def __init__(
        self,
        access_restriction: str = None,
        remove_restricted_urlids: List[str] = None,
        restricted_urls: List[ModifyBrowserInstanceGroupRequestNetworkRestrictedURLs] = None,
    ):
        # The type of the access control list.
        # 
        # Valid value:
        # 
        # *   ALLOW_LIST: The whitelist.
        self.access_restriction = access_restriction
        # The domain names to be removed.
        self.remove_restricted_urlids = remove_restricted_urlids
        # The domain restriction configurations.
        self.restricted_urls = restricted_urls

    def validate(self):
        if self.restricted_urls:
            for k in self.restricted_urls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_restriction is not None:
            result['AccessRestriction'] = self.access_restriction
        if self.remove_restricted_urlids is not None:
            result['RemoveRestrictedURLIds'] = self.remove_restricted_urlids
        result['RestrictedURLs'] = []
        if self.restricted_urls is not None:
            for k in self.restricted_urls:
                result['RestrictedURLs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRestriction') is not None:
            self.access_restriction = m.get('AccessRestriction')
        if m.get('RemoveRestrictedURLIds') is not None:
            self.remove_restricted_urlids = m.get('RemoveRestrictedURLIds')
        self.restricted_urls = []
        if m.get('RestrictedURLs') is not None:
            for k in m.get('RestrictedURLs'):
                temp_model = ModifyBrowserInstanceGroupRequestNetworkRestrictedURLs()
                self.restricted_urls.append(temp_model.from_map(k))
        return self


class ModifyBrowserInstanceGroupRequestPolicyClipboardPolicy(TeaModel):
    def __init__(
        self,
        clipboard: str = None,
        clipboard_read_limit: int = None,
        clipboard_scope: str = None,
        clipboard_write_limit: int = None,
        file_clipboard: str = None,
        rich_text_clipboard: str = None,
        text_clipboard: str = None,
    ):
        # The clipboard policy.
        # 
        # Valid values:
        # 
        # *   read: Allows copying from the local device to the cloud browser.
        # *   readwrite: Allows copying in both directions.
        # *   write: Allows copying from the cloud browser to the local device.
        # *   off: Blocks copying in both directions.
        self.clipboard = clipboard
        # The maximum number of characters allowed when copying from the clipboard.
        self.clipboard_read_limit = clipboard_read_limit
        # The clipboard control scope.
        # 
        # Valid values:
        # 
        # *   grained: fine-grained control
        # *   global: global control
        self.clipboard_scope = clipboard_scope
        # The maximum number of characters allowed when copying to the clipboard.
        self.clipboard_write_limit = clipboard_write_limit
        # The file clipboard policy.
        # 
        # Valid values:
        # 
        # *   read: Allows copying from the local device to the cloud browser.
        # *   readwrite: Allows copying in both directions.
        # *   write: Allows copying from the cloud browser to the local device.
        # *   off: Blocks copying in both directions.
        self.file_clipboard = file_clipboard
        # The rich text clipboard policy.
        # 
        # Valid values:
        # 
        # *   read: Allows copying from the local device to the cloud browser.
        # *   readwrite: Allows copying in both directions.
        # *   write: Allows copying from the cloud browser to the local device.
        # *   off: Blocks copying in both directions.
        self.rich_text_clipboard = rich_text_clipboard
        # The text clipboard policy.
        # 
        # Valid values:
        # 
        # *   read: Allows copying from the local device to the cloud browser.
        # *   readwrite: Allows copying in both directions.
        # *   write: Allows copying from the cloud browser to the local device.
        # *   off: Blocks copying in both directions.
        self.text_clipboard = text_clipboard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.clipboard_read_limit is not None:
            result['ClipboardReadLimit'] = self.clipboard_read_limit
        if self.clipboard_scope is not None:
            result['ClipboardScope'] = self.clipboard_scope
        if self.clipboard_write_limit is not None:
            result['ClipboardWriteLimit'] = self.clipboard_write_limit
        if self.file_clipboard is not None:
            result['FileClipboard'] = self.file_clipboard
        if self.rich_text_clipboard is not None:
            result['RichTextClipboard'] = self.rich_text_clipboard
        if self.text_clipboard is not None:
            result['TextClipboard'] = self.text_clipboard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('ClipboardReadLimit') is not None:
            self.clipboard_read_limit = m.get('ClipboardReadLimit')
        if m.get('ClipboardScope') is not None:
            self.clipboard_scope = m.get('ClipboardScope')
        if m.get('ClipboardWriteLimit') is not None:
            self.clipboard_write_limit = m.get('ClipboardWriteLimit')
        if m.get('FileClipboard') is not None:
            self.file_clipboard = m.get('FileClipboard')
        if m.get('RichTextClipboard') is not None:
            self.rich_text_clipboard = m.get('RichTextClipboard')
        if m.get('TextClipboard') is not None:
            self.text_clipboard = m.get('TextClipboard')
        return self


class ModifyBrowserInstanceGroupRequestPolicyVideoPolicy(TeaModel):
    def __init__(
        self,
        frame_rate: int = None,
    ):
        # The frame rate.
        self.frame_rate = frame_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        return self


class ModifyBrowserInstanceGroupRequestPolicyWatermarkPolicy(TeaModel):
    def __init__(
        self,
        watermark_switch: str = None,
        watermark_types: List[str] = None,
    ):
        # Specifies whether to enable the watermark.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.watermark_switch = watermark_switch
        # The watermark types.
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyBrowserInstanceGroupRequestPolicy(TeaModel):
    def __init__(
        self,
        clipboard_policy: ModifyBrowserInstanceGroupRequestPolicyClipboardPolicy = None,
        disconnect_keep_session: str = None,
        disconnect_keep_session_time: int = None,
        html_5file_transfer: str = None,
        no_operation_disconnect: str = None,
        no_operation_disconnect_time: int = None,
        policy_id: str = None,
        policy_version: str = None,
        video_policy: ModifyBrowserInstanceGroupRequestPolicyVideoPolicy = None,
        watermark_policy: ModifyBrowserInstanceGroupRequestPolicyWatermarkPolicy = None,
    ):
        # The settings related to clipboard control.
        self.clipboard_policy = clipboard_policy
        # Defines what happens to a session when a user disconnects.
        # 
        # Valid values:
        # 
        # *   customTime: The session will be terminated after a custom-defined timeout.
        # *   persistent: The session will never be automatically terminated..
        self.disconnect_keep_session = disconnect_keep_session
        # The session persistence duration.
        self.disconnect_keep_session_time = disconnect_keep_session_time
        # The file transfer policy on the web client.
        self.html_5file_transfer = html_5file_transfer
        self.no_operation_disconnect = no_operation_disconnect
        self.no_operation_disconnect_time = no_operation_disconnect_time
        # The ID of the policy.
        self.policy_id = policy_id
        # The policy version.
        # 
        # Valid value:
        # 
        # *   Center: center policy
        self.policy_version = policy_version
        # The display policy.
        self.video_policy = video_policy
        # The watermark configuration.
        self.watermark_policy = watermark_policy

    def validate(self):
        if self.clipboard_policy:
            self.clipboard_policy.validate()
        if self.video_policy:
            self.video_policy.validate()
        if self.watermark_policy:
            self.watermark_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard_policy is not None:
            result['ClipboardPolicy'] = self.clipboard_policy.to_map()
        if self.disconnect_keep_session is not None:
            result['DisconnectKeepSession'] = self.disconnect_keep_session
        if self.disconnect_keep_session_time is not None:
            result['DisconnectKeepSessionTime'] = self.disconnect_keep_session_time
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
        if m.get('ClipboardPolicy') is not None:
            temp_model = ModifyBrowserInstanceGroupRequestPolicyClipboardPolicy()
            self.clipboard_policy = temp_model.from_map(m['ClipboardPolicy'])
        if m.get('DisconnectKeepSession') is not None:
            self.disconnect_keep_session = m.get('DisconnectKeepSession')
        if m.get('DisconnectKeepSessionTime') is not None:
            self.disconnect_keep_session_time = m.get('DisconnectKeepSessionTime')
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
            temp_model = ModifyBrowserInstanceGroupRequestPolicyVideoPolicy()
            self.video_policy = temp_model.from_map(m['VideoPolicy'])
        if m.get('WatermarkPolicy') is not None:
            temp_model = ModifyBrowserInstanceGroupRequestPolicyWatermarkPolicy()
            self.watermark_policy = temp_model.from_map(m['WatermarkPolicy'])
        return self


class ModifyBrowserInstanceGroupRequestTimers(TeaModel):
    def __init__(
        self,
        interval: int = None,
        timer_type: str = None,
    ):
        # The interval.
        self.interval = interval
        # The timer type:
        # 
        # Valid value:
        # 
        # *   SESSION_TIMEOUT: Defines the timeout period before a disconnected session is terminated.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyBrowserInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        browser_config: ModifyBrowserInstanceGroupRequestBrowserConfig = None,
        browser_instance_group_id: str = None,
        cloud_browser_name: str = None,
        network: ModifyBrowserInstanceGroupRequestNetwork = None,
        policy: ModifyBrowserInstanceGroupRequestPolicy = None,
        timers: List[ModifyBrowserInstanceGroupRequestTimers] = None,
    ):
        # The browser settings.
        self.browser_config = browser_config
        # The ID of the cloud browser to be modified.
        # 
        # This parameter is required.
        self.browser_instance_group_id = browser_instance_group_id
        # The name of the cloud browser.
        self.cloud_browser_name = cloud_browser_name
        # The network configurations.
        self.network = network
        # The access policy.
        self.policy = policy
        # The timer.
        self.timers = timers

    def validate(self):
        if self.browser_config:
            self.browser_config.validate()
        if self.network:
            self.network.validate()
        if self.policy:
            self.policy.validate()
        if self.timers:
            for k in self.timers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.browser_config is not None:
            result['BrowserConfig'] = self.browser_config.to_map()
        if self.browser_instance_group_id is not None:
            result['BrowserInstanceGroupId'] = self.browser_instance_group_id
        if self.cloud_browser_name is not None:
            result['CloudBrowserName'] = self.cloud_browser_name
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['Timers'] = []
        if self.timers is not None:
            for k in self.timers:
                result['Timers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserConfig') is not None:
            temp_model = ModifyBrowserInstanceGroupRequestBrowserConfig()
            self.browser_config = temp_model.from_map(m['BrowserConfig'])
        if m.get('BrowserInstanceGroupId') is not None:
            self.browser_instance_group_id = m.get('BrowserInstanceGroupId')
        if m.get('CloudBrowserName') is not None:
            self.cloud_browser_name = m.get('CloudBrowserName')
        if m.get('Network') is not None:
            temp_model = ModifyBrowserInstanceGroupRequestNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('Policy') is not None:
            temp_model = ModifyBrowserInstanceGroupRequestPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.timers = []
        if m.get('Timers') is not None:
            for k in m.get('Timers'):
                temp_model = ModifyBrowserInstanceGroupRequestTimers()
                self.timers.append(temp_model.from_map(k))
        return self


class ModifyBrowserInstanceGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        browser_config_shrink: str = None,
        browser_instance_group_id: str = None,
        cloud_browser_name: str = None,
        network_shrink: str = None,
        policy_shrink: str = None,
        timers_shrink: str = None,
    ):
        # The browser settings.
        self.browser_config_shrink = browser_config_shrink
        # The ID of the cloud browser to be modified.
        # 
        # This parameter is required.
        self.browser_instance_group_id = browser_instance_group_id
        # The name of the cloud browser.
        self.cloud_browser_name = cloud_browser_name
        # The network configurations.
        self.network_shrink = network_shrink
        # The access policy.
        self.policy_shrink = policy_shrink
        # The timer.
        self.timers_shrink = timers_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.browser_config_shrink is not None:
            result['BrowserConfig'] = self.browser_config_shrink
        if self.browser_instance_group_id is not None:
            result['BrowserInstanceGroupId'] = self.browser_instance_group_id
        if self.cloud_browser_name is not None:
            result['CloudBrowserName'] = self.cloud_browser_name
        if self.network_shrink is not None:
            result['Network'] = self.network_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.timers_shrink is not None:
            result['Timers'] = self.timers_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserConfig') is not None:
            self.browser_config_shrink = m.get('BrowserConfig')
        if m.get('BrowserInstanceGroupId') is not None:
            self.browser_instance_group_id = m.get('BrowserInstanceGroupId')
        if m.get('CloudBrowserName') is not None:
            self.cloud_browser_name = m.get('CloudBrowserName')
        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('Timers') is not None:
            self.timers_shrink = m.get('Timers')
        return self


class ModifyBrowserInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBrowserInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBrowserInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBrowserInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodePoolAmountRequestNodePool(TeaModel):
    def __init__(
        self,
        node_amount: int = None,
        pre_paid_node_amount_modify_mode: str = None,
        pre_paid_node_amount_modify_node_ids: List[str] = None,
    ):
        # The total number of subscription nodes after the change.
        # 
        # This parameter is required.
        self.node_amount = node_amount
        # The change mode of subscription nodes.
        # 
        # Valid value:
        # 
        # *   EXPAND_FROM_POST_PAID_EXPLICIT: changes from specified pay-as-you-go nodes
        self.pre_paid_node_amount_modify_mode = pre_paid_node_amount_modify_mode
        # The nodes for which you want to change the billing method.
        self.pre_paid_node_amount_modify_node_ids = pre_paid_node_amount_modify_node_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.pre_paid_node_amount_modify_mode is not None:
            result['PrePaidNodeAmountModifyMode'] = self.pre_paid_node_amount_modify_mode
        if self.pre_paid_node_amount_modify_node_ids is not None:
            result['PrePaidNodeAmountModifyNodeIds'] = self.pre_paid_node_amount_modify_node_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('PrePaidNodeAmountModifyMode') is not None:
            self.pre_paid_node_amount_modify_mode = m.get('PrePaidNodeAmountModifyMode')
        if m.get('PrePaidNodeAmountModifyNodeIds') is not None:
            self.pre_paid_node_amount_modify_node_ids = m.get('PrePaidNodeAmountModifyNodeIds')
        return self


class ModifyNodePoolAmountRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        node_pool: ModifyNodePoolAmountRequestNodePool = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The parameters related to the configuration change of the node pool.
        # 
        # This parameter is required.
        self.node_pool = node_pool
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        if self.node_pool:
            self.node_pool.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('NodePool') is not None:
            temp_model = ModifyNodePoolAmountRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAmountShrinkRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        node_pool_shrink: str = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The parameters related to the configuration change of the node pool.
        # 
        # This parameter is required.
        self.node_pool_shrink = node_pool_shrink
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAmountResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyNodePoolAmountResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyNodePoolAmountResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyNodePoolAmountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNodePoolAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNodePoolAmountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyNodePoolAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The number of resources.
        self.amount = amount
        # The end of the time period during which the scaling policy is executed. Format: HH:mm.
        self.end_time = end_time
        # The beginning of the time period during which the scaling policy is executed. Format: HH:mm.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules(TeaModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods] = None,
    ):
        # The schedule type of the scaling policy. This parameter must be configured together with `RecurrenceValues`.``
        # 
        # Valid values:
        # 
        # *   weekly: The scaling policy is executed on specific days each week.
        self.recurrence_type = recurrence_type
        # The days of each week on which the scaling policy is executed.
        self.recurrence_values = recurrence_values
        # The time periods during which the scaling policy can be executed. The time periods must meet the following requirements:
        # 
        # *   Up to three time periods can be added.
        # *   Time periods cannot be overlapped.
        # *   The interval between two consecutive time periods must be greater than or equal to 5 minutes.
        # *   Each time period must be greater than or equal to 15 minutes.
        # *   The total length of the time periods that you specify cannot be greater than a day.
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategy(TeaModel):
    def __init__(
        self,
        max_idle_app_instance_amount: int = None,
        max_scaling_amount: int = None,
        node_amount: int = None,
        recurrence_schedules: List[ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        # The maximum number of idle sessions. After you specify a value for this parameter, auto scaling is triggered only if the number of idle sessions in the delivery group is smaller than the specified value and the session usage exceeds the value specified for `ScalingUsageThreshold`. Otherwise, the system determines that the idle sessions in the delivery group are sufficient and does not perform auto scaling.`` You can use this parameter to flexibly manage auto scaling and reduce costs.
        self.max_idle_app_instance_amount = max_idle_app_instance_amount
        # The maximum number of resources that can be created for scale-out. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_USAGE`.
        self.max_scaling_amount = max_scaling_amount
        # The number of resources to purchase. Valid values: 1 to 100.
        # 
        # > 
        # 
        # *   If you use subscription resources, you cannot modify this parameter.
        # *   If you use pay-as-you-go resources, you can modify this parameter only if you set `StrategyType` to `NODE_FIXED` or `NODE_SCALING_BY_USAGE`.
        self.node_amount = node_amount
        # The intervals at which the scaling policy is executed. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.recurrence_schedules = recurrence_schedules
        # The maximum retention period of a resource to which no session is connected. If no session is connected to a resource, the resource is automatically scaled in after the specified retention period elapses. Valid values: 5 to 120. Default value: 5. Unit: minutes. If one of the following situations occurs, the resource is not scaled in.
        # 
        # *   If a scale-out is automatically triggered after the resource is scaled in, the scale-in is not executed. This prevents repeated scale-in and scale-out.
        # *   If a scale-out is automatically triggered due to an increase in the number of sessions during the specified period of time, the resource is not scaled in and the countdown restarts.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The number of resources that are created each time resources are scaled out. Valid values: 1 to 10. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_USAGE`.
        self.scaling_step = scaling_step
        # The upper limit of session usage. If the session usage exceeds the specified upper limit, auto scaling is automatically triggered. The session usage is calculated by using the following formula: `Session usage = Number of current sessions/(Total number of resources × Number of concurrent sessions) × 100%`. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_USAGE`. Valid values: 0 to 100. Default value: 85.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The expiration date of the scaling policy. Format: yyyy-MM-dd. The interval between the expiration date and the effective date must be from 7 days to 1 year. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.strategy_disable_date = strategy_disable_date
        # The effective date of the scaling policy. Format: yyyy-MM-dd. The date must be the same as or later than the current date. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.strategy_enable_date = strategy_enable_date
        # The scaling mode.
        # 
        # > 
        # 
        # *   `NODE_FIXED`: no scaling. This value is applicable to pay-as-you-go resources and subscription resources.
        # *   `NODE_SCALING_BY_USAGE`: auto scaling. This value is applicable to pay-as-you-go resources and subscription resources.
        # *   `NODE_SCALING_BY_SCHEDULE`: scheduled scaling. This value is applicable only to pay-as-you-go resources.
        # 
        # Valid values:
        # 
        # *   NODE_FIXED: no scaling
        # *   NODE_SCALING_BY_SCHEDULE: scheduled scaling
        # *   NODE_SCALING_BY_USAGE: auto scaling
        self.strategy_type = strategy_type
        # Specifies whether to enable the warmup policy for resources. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_idle_app_instance_amount is not None:
            result['MaxIdleAppInstanceAmount'] = self.max_idle_app_instance_amount
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
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
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
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


class ModifyNodePoolAttributeRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        node_capacity: int = None,
        node_pool_strategy: ModifyNodePoolAttributeRequestNodePoolStrategy = None,
        pool_id: str = None,
        product_type: str = None,
    ):
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-hangzhou: China (Hangzhou)
        self.biz_region_id = biz_region_id
        self.node_capacity = node_capacity
        # The auto scaling policy used by the delivery group.
        self.node_pool_strategy = node_pool_strategy
        self.pool_id = pool_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        self.product_type = product_type

    def validate(self):
        if self.node_pool_strategy:
            self.node_pool_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_strategy is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy.to_map()
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolStrategy') is not None:
            temp_model = ModifyNodePoolAttributeRequestNodePoolStrategy()
            self.node_pool_strategy = temp_model.from_map(m['NodePoolStrategy'])
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAttributeShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        node_capacity: int = None,
        node_pool_strategy_shrink: str = None,
        pool_id: str = None,
        product_type: str = None,
    ):
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-hangzhou: China (Hangzhou)
        self.biz_region_id = biz_region_id
        self.node_capacity = node_capacity
        # The auto scaling policy used by the delivery group.
        self.node_pool_strategy_shrink = node_pool_strategy_shrink
        self.pool_id = pool_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_strategy_shrink is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy_shrink
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolStrategy') is not None:
            self.node_pool_strategy_shrink = m.get('NodePoolStrategy')
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNodePoolAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNodePoolAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyNodePoolAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantConfigRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_expire_remind: bool = None,
    ):
        # Specifies whether to enable the resource expiration reminder feature.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.app_instance_group_expire_remind = app_instance_group_expire_remind

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')
        return self


class ModifyTenantConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTenantConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTenantConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWuyingServerAttributeRequest(TeaModel):
    def __init__(
        self,
        password: str = None,
        wuying_server_id: str = None,
        wuying_server_name: str = None,
    ):
        # Workstation login password.
        self.password = password
        # The ID of the workstation.
        self.wuying_server_id = wuying_server_id
        # The name.
        self.wuying_server_name = wuying_server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id
        if self.wuying_server_name is not None:
            result['WuyingServerName'] = self.wuying_server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')
        if m.get('WuyingServerName') is not None:
            self.wuying_server_name = m.get('WuyingServerName')
        return self


class ModifyWuyingServerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWuyingServerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyWuyingServerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyWuyingServerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageListAppInstanceGroupUserRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The number of the page to return. We recommend that you configure this parameter.
        self.page_number = page_number
        # The number of entries to be return on each page. The value cannot be greater than `100`. We recommend that you configure this parameter.
        self.page_size = page_size
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class PageListAppInstanceGroupUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        users: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The users.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class PageListAppInstanceGroupUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageListAppInstanceGroupUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PageListAppInstanceGroupUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        auto_pay: bool = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
        promotion_id: str = None,
        renew_amount: int = None,
        renew_mode: str = None,
        renew_nodes: List[str] = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_pay = auto_pay
        # The subscription duration of resources. This parameter must be configured together with `PeriodUnit`.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration. This parameter must be configured together with `Period`. The following items describe valid values for the combinations of `Period` and `PeriodUnit`:
        # 
        # *   1 Week
        # *   1 Month
        # *   2 Month
        # *   3 Month
        # *   6 Month
        # *   1 Year
        # *   2 Year
        # *   3 Year
        # 
        # >  The value of this parameter is case-insensitive. For example, `Week` is valid and `week` is invalid. If you specify a value combination other than the preceding combinations, such as `2 Week`, the operation can still be called. However, an error occurs when you place the order.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The promotion ID. You can call the [GetResourcePrice](https://help.aliyun.com/document_detail/428503.html) operation to obtain the ID.
        self.promotion_id = promotion_id
        self.renew_amount = renew_amount
        self.renew_mode = renew_mode
        self.renew_nodes = renew_nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.renew_amount is not None:
            result['RenewAmount'] = self.renew_amount
        if self.renew_mode is not None:
            result['RenewMode'] = self.renew_mode
        if self.renew_nodes is not None:
            result['RenewNodes'] = self.renew_nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RenewAmount') is not None:
            self.renew_amount = m.get('RenewAmount')
        if m.get('RenewMode') is not None:
            self.renew_mode = m.get('RenewMode')
        if m.get('RenewNodes') is not None:
            self.renew_nodes = m.get('RenewNodes')
        return self


class RenewAppInstanceGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        auto_pay: bool = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
        promotion_id: str = None,
        renew_amount: int = None,
        renew_mode: str = None,
        renew_nodes_shrink: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_pay = auto_pay
        # The subscription duration of resources. This parameter must be configured together with `PeriodUnit`.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration. This parameter must be configured together with `Period`. The following items describe valid values for the combinations of `Period` and `PeriodUnit`:
        # 
        # *   1 Week
        # *   1 Month
        # *   2 Month
        # *   3 Month
        # *   6 Month
        # *   1 Year
        # *   2 Year
        # *   3 Year
        # 
        # >  The value of this parameter is case-insensitive. For example, `Week` is valid and `week` is invalid. If you specify a value combination other than the preceding combinations, such as `2 Week`, the operation can still be called. However, an error occurs when you place the order.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The promotion ID. You can call the [GetResourcePrice](https://help.aliyun.com/document_detail/428503.html) operation to obtain the ID.
        self.promotion_id = promotion_id
        self.renew_amount = renew_amount
        self.renew_mode = renew_mode
        self.renew_nodes_shrink = renew_nodes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.renew_amount is not None:
            result['RenewAmount'] = self.renew_amount
        if self.renew_mode is not None:
            result['RenewMode'] = self.renew_mode
        if self.renew_nodes_shrink is not None:
            result['RenewNodes'] = self.renew_nodes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RenewAmount') is not None:
            self.renew_amount = m.get('RenewAmount')
        if m.get('RenewMode') is not None:
            self.renew_mode = m.get('RenewMode')
        if m.get('RenewNodes') is not None:
            self.renew_nodes_shrink = m.get('RenewNodes')
        return self


class RenewAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenewAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewWuyingServerRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        wuying_server_id: str = None,
    ):
        # Automatic payment.
        self.auto_pay = auto_pay
        # The renewal duration.
        self.period = period
        # The unit of the renewal time.
        # 
        # Valid values:
        # 
        # *   Month: month.
        # *   Year: year.
        self.period_unit = period_unit
        # The discount ID.
        self.promotion_id = promotion_id
        # The ID of the workstation.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')
        return self


class RenewWuyingServerResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewWuyingServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewWuyingServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenewWuyingServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartWuyingServerRequest(TeaModel):
    def __init__(
        self,
        wuying_server_id_list: List[str] = None,
    ):
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')
        return self


class RestartWuyingServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartWuyingServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartWuyingServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartWuyingServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTaskForDistributeImageRequest(TeaModel):
    def __init__(
        self,
        destination_region_list: List[str] = None,
        image_id: str = None,
        product_type: str = None,
        retry_type: str = None,
        source_region: str = None,
        version_id: str = None,
    ):
        # The regions to which you want to replicate the image.
        self.destination_region_list = destination_region_list
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The product type.
        # 
        # Valid values:
        # 
        # *   CloudDesktop: Elastic Desktop Service
        # *   CloudApp: App Streaming
        # *   WuyingServer: Workstation
        self.product_type = product_type
        # This parameter is not publicly available.
        self.retry_type = retry_type
        # The region where the source image is located. If you leave this parameter empty, a random region is selected.
        self.source_region = source_region
        # The ID of the image version. If you do not specify this parameter, the latest image version is used by default.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_region_list is not None:
            result['DestinationRegionList'] = self.destination_region_list
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.retry_type is not None:
            result['RetryType'] = self.retry_type
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionList') is not None:
            self.destination_region_list = m.get('DestinationRegionList')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RetryType') is not None:
            self.retry_type = m.get('RetryType')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class StartTaskForDistributeImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code if an error occurred.
        self.code = code
        # The ID of the image replication task.
        self.data = data
        # The error message if an error occurred.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the task is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartTaskForDistributeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTaskForDistributeImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartTaskForDistributeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartWuyingServerRequest(TeaModel):
    def __init__(
        self,
        wuying_server_id_list: List[str] = None,
    ):
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')
        return self


class StartWuyingServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartWuyingServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartWuyingServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartWuyingServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopWuyingServerRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        wuying_server_id_list: List[str] = None,
    ):
        # Force restart.
        # 
        # Valid values:
        # 
        # *   True.
        # *   False
        self.force = force
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')
        return self


class StopWuyingServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopWuyingServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopWuyingServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopWuyingServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagCloudResourcesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of a tag. The value must be 1 to 128 characters in length and is case-sensitive. The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.key = key
        # The value of a tag. The value must be 1 to 128 characters in length and is case-sensitive. The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagCloudResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[TagCloudResourcesRequestTags] = None,
    ):
        # The resource IDs. You can specify up to 50 resource IDs. You do not need to specify this parameter if you set ResourceType to AliUid.
        self.resource_ids = resource_ids
        # The type of the cloud resource.
        # 
        # Valid values:
        # 
        # *   CenterImageId: center image ID.
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to remove from the cloud resources. System and custom tags are supported.
        # 
        # *   Valid values for system tags:
        # 
        #     *   `System/Scheduler/GRAYSCALE`: canary tags.
        #     *   `System/Scheduler/STOP_NEW_USER_CONNECTION`: tags used to stop new users bound to the delivery group from establishing a connection.
        # 
        # *   You can create up to 20 custom tags.
        # 
        # > Each tag key on a resource can have only one tag value. If you create a tag that has the same key as an existing tag, the value of the existing tag is overwritten.
        # 
        # This parameter is required.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = TagCloudResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TagCloudResourcesResponseBodyFailedResourcesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        self.key = key
        self.scope = scope
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagCloudResourcesResponseBodyFailedResources(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tags: List[TagCloudResourcesResponseBodyFailedResourcesTags] = None,
    ):
        self.code = code
        self.message = message
        self.resource_id = resource_id
        # The type of the cloud resource.
        # 
        # Valid values:
        # 
        # *   CenterImageId: center image ID.
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = TagCloudResourcesResponseBodyFailedResourcesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TagCloudResourcesResponseBody(TeaModel):
    def __init__(
        self,
        failed_resources: List[TagCloudResourcesResponseBodyFailedResources] = None,
        request_id: str = None,
    ):
        # The cloud resources on which the operation failed and the corresponding tags.
        self.failed_resources = failed_resources
        self.request_id = request_id

    def validate(self):
        if self.failed_resources:
            for k in self.failed_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedResources'] = []
        if self.failed_resources is not None:
            for k in self.failed_resources:
                result['FailedResources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_resources = []
        if m.get('FailedResources') is not None:
            for k in m.get('FailedResources'):
                temp_model = TagCloudResourcesResponseBodyFailedResources()
                self.failed_resources.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagCloudResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagCloudResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagCloudResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        end_user_id: str = None,
        product_type: str = None,
    ):
        # The ID of the delivery group. You can call the [GetConnectionTicket](~~GetConnectionTicket~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The session ID. You can call the [GetConnectionTicket](~~GetConnectionTicket~~) operation to obtain the ID.
        self.app_instance_id = app_instance_id
        # The ID of the persistent session. You can call the [GetConnectionTicket](~~GetConnectionTicket~~) operation to obtain the ID.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The username.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class UnbindResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagCloudResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tag_keys: List[str] = None,
    ):
        # The resource IDs. You can specify up to 50 resource IDs. You do not need to specify this parameter if you set ResourceType to AliUid.
        self.resource_ids = resource_ids
        # The type of the resource from which you want to remove tags.
        # 
        # Valid values:
        # 
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to remove from the cloud resources. System and custom tags are supported. You can specify up to 10 tags.
        # 
        # Valid values for system tags:
        # 
        # *   `System/Scheduler/GRAYSCALE`: canary tags.
        # *   `System/Scheduler/STOP_NEW_USER_CONNECTION`: tags used to stop new users bound to the delivery group from establishing a connection.
        # 
        # This parameter is required.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagCloudResourcesResponseBodyFailedResourcesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag type.
        # 
        # Valid values:
        # 
        # *   Custom: custom tag.
        # *   System: system tag.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class UntagCloudResourcesResponseBodyFailedResources(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tags: List[UntagCloudResourcesResponseBodyFailedResourcesTags] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The resource IDs.
        self.resource_id = resource_id
        # The type of the cloud resource.
        # 
        # Valid values:
        # 
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        self.resource_type = resource_type
        # The tags that failed to be removed from the cloud resources.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UntagCloudResourcesResponseBodyFailedResourcesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class UntagCloudResourcesResponseBody(TeaModel):
    def __init__(
        self,
        failed_resources: List[UntagCloudResourcesResponseBodyFailedResources] = None,
        request_id: str = None,
    ):
        # The cloud resources whose tags failed to be removed and the corresponding tags.
        self.failed_resources = failed_resources
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.failed_resources:
            for k in self.failed_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedResources'] = []
        if self.failed_resources is not None:
            for k in self.failed_resources:
                result['FailedResources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_resources = []
        if m.get('FailedResources') is not None:
            for k in m.get('FailedResources'):
                temp_model = UntagCloudResourcesResponseBodyFailedResources()
                self.failed_resources.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagCloudResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagCloudResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagCloudResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppInstanceGroupImageRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        product_type: str = None,
    ):
        # The image ID of the application. You can obtain the ID from the Images page in the App Streaming console.
        # 
        # This parameter is required.
        self.app_center_image_id = app_center_image_id
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai).
        # *   cn-hangzhou: China (Hangzhou)
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class UpdateAppInstanceGroupImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppInstanceGroupImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppInstanceGroupImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppInstanceGroupImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWuyingServerImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        product_type: str = None,
        wuying_server_id: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The product type. Set this parameter to WuyingServer.
        self.product_type = product_type
        # The ID of the workstation.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')
        return self


class UpdateWuyingServerImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the update task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateWuyingServerImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWuyingServerImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWuyingServerImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


