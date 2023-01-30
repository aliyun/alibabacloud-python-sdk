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
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        self.ota_type = ota_type
        self.start_time = start_time
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class AuthorizeInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        authorize_user_ids: List[str] = None,
        product_type: str = None,
        un_authorize_user_ids: List[str] = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.authorize_user_ids = authorize_user_ids
        self.product_type = product_type
        self.un_authorize_user_ids = un_authorize_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.authorize_user_ids is not None:
            result['AuthorizeUserIds'] = self.authorize_user_ids
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.un_authorize_user_ids is not None:
            result['UnAuthorizeUserIds'] = self.un_authorize_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AuthorizeUserIds') is not None:
            self.authorize_user_ids = m.get('AuthorizeUserIds')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UnAuthorizeUserIds') is not None:
            self.un_authorize_user_ids = m.get('UnAuthorizeUserIds')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CancelOtaTaskRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        task_id: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelOtaTaskResponseBody(TeaModel):
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


class CancelOtaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelOtaTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CancelOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppInstanceGroupRequestNetworkRoutes(TeaModel):
    def __init__(
        self,
        destination: str = None,
        mode: str = None,
    ):
        self.destination = destination
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
        routes: List[CreateAppInstanceGroupRequestNetworkRoutes] = None,
        strategy_type: str = None,
    ):
        self.routes = routes
        self.strategy_type = strategy_type

    def validate(self):
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['Routes'].append(k.to_map() if k else None)
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.routes = []
        if m.get('Routes') is not None:
            for k in m.get('Routes'):
                temp_model = CreateAppInstanceGroupRequestNetworkRoutes()
                self.routes.append(temp_model.from_map(k))
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        return self


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.amount = amount
        self.end_time = end_time
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
        self.recurrence_type = recurrence_type
        self.recurrence_values = recurrence_values
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
        self.max_scaling_amount = max_scaling_amount
        self.node_amount = node_amount
        self.node_capacity = node_capacity
        self.node_instance_type = node_instance_type
        self.recurrence_schedules = recurrence_schedules
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        self.strategy_disable_date = strategy_disable_date
        self.strategy_enable_date = strategy_enable_date
        self.strategy_type = strategy_type
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


class CreateAppInstanceGroupRequestUserInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class CreateAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_name: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        network: CreateAppInstanceGroupRequestNetwork = None,
        node_pool: CreateAppInstanceGroupRequestNodePool = None,
        period: int = None,
        period_unit: str = None,
        pre_open_app_id: str = None,
        product_type: str = None,
        promotion_id: str = None,
        session_timeout: int = None,
        user_info: CreateAppInstanceGroupRequestUserInfo = None,
        users: List[str] = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_name = app_instance_group_name
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.biz_region_id = biz_region_id
        self.charge_resource_mode = charge_resource_mode
        self.charge_type = charge_type
        self.network = network
        self.node_pool = node_pool
        self.period = period
        self.period_unit = period_unit
        self.pre_open_app_id = pre_open_app_id
        self.product_type = product_type
        self.promotion_id = promotion_id
        self.session_timeout = session_timeout
        self.user_info = user_info
        self.users = users

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
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
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
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
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('UserInfo') is not None:
            temp_model = CreateAppInstanceGroupRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateAppInstanceGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_name: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        network_shrink: str = None,
        node_pool_shrink: str = None,
        period: int = None,
        period_unit: str = None,
        pre_open_app_id: str = None,
        product_type: str = None,
        promotion_id: str = None,
        session_timeout: int = None,
        user_info_shrink: str = None,
        users: List[str] = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_name = app_instance_group_name
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.biz_region_id = biz_region_id
        self.charge_resource_mode = charge_resource_mode
        self.charge_type = charge_type
        self.network_shrink = network_shrink
        self.node_pool_shrink = node_pool_shrink
        self.period = period
        self.period_unit = period_unit
        self.pre_open_app_id = pre_open_app_id
        self.product_type = product_type
        self.promotion_id = promotion_id
        self.session_timeout = session_timeout
        self.user_info_shrink = user_info_shrink
        self.users = users

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
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
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
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateAppInstanceGroupResponseBodyAppInstanceGroupModel(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        node_pool_id: str = None,
        order_id: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.node_pool_id = node_pool_id
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
        self.app_instance_group_model = app_instance_group_model
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DeleteAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetOtaTaskByTaskIdRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
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
        self.code = code
        self.message = message
        self.ota_version = ota_version
        self.release_note = release_note
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        biz_region_id: str = None,
        charge_type: str = None,
        node_instance_type: str = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
    ):
        self.amount = amount
        self.biz_region_id = biz_region_id
        self.charge_type = charge_type
        self.node_instance_type = node_instance_type
        self.period = period
        self.period_unit = period_unit
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


class GetResourcePriceResponseBodyPriceModelPricePromotions(TeaModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        self.option_code = option_code
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name
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
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.promotions = promotions
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
        self.description = description
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
        self.price = price
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
        price_model: GetResourcePriceResponseBodyPriceModel = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.price_model = price_model
        self.request_id = request_id

    def validate(self):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.app_instance_group_id = app_instance_group_id
        self.period = period
        self.period_unit = period_unit
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
        self.option_code = option_code
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name
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
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.promotions = promotions
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
        self.description = description
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
        self.price = price
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
        self.data = data
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        region_id: str = None,
        status: List[str] = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.page_number = page_number
        self.page_size = page_size
        self.product_type = product_type
        self.region_id = region_id
        self.status = status

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
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
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
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        self.app_id = app_id
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


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.amount = amount
        self.end_time = end_time
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
        self.recurrence_type = recurrence_type
        self.recurrence_values = recurrence_values
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
        max_scaling_amount: int = None,
        node_amount: int = None,
        node_capacity: int = None,
        node_instance_type: str = None,
        node_pool_id: str = None,
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
        self.amount = amount
        self.max_scaling_amount = max_scaling_amount
        self.node_amount = node_amount
        self.node_capacity = node_capacity
        self.node_instance_type = node_instance_type
        self.node_pool_id = node_pool_id
        self.node_used = node_used
        self.recurrence_schedules = recurrence_schedules
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_node_amount = scaling_node_amount
        self.scaling_node_used = scaling_node_used
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        self.strategy_disable_date = strategy_disable_date
        self.strategy_enable_date = strategy_enable_date
        self.strategy_type = strategy_type
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
        self.new_ota_version = new_ota_version
        self.ota_version = ota_version
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


class ListAppInstanceGroupResponseBodyAppInstanceGroupModels(TeaModel):
    def __init__(
        self,
        amount: int = None,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_instance_type: str = None,
        apps: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps] = None,
        charge_type: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        node_pool: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool] = None,
        os_type: str = None,
        ota_info: ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo = None,
        product_type: str = None,
        region_id: str = None,
        resource_status: str = None,
        session_timeout: str = None,
        spec_id: str = None,
        status: str = None,
    ):
        self.amount = amount
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.app_instance_type = app_instance_type
        self.apps = apps
        self.charge_type = charge_type
        self.expired_time = expired_time
        self.gmt_create = gmt_create
        self.node_pool = node_pool
        self.os_type = os_type
        self.ota_info = ota_info
        self.product_type = product_type
        self.region_id = region_id
        self.resource_status = resource_status
        self.session_timeout = session_timeout
        self.spec_id = spec_id
        self.status = status

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

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        result['NodePool'] = []
        if self.node_pool is not None:
            for k in self.node_pool:
                result['NodePool'].append(k.to_map() if k else None)
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.ota_info is not None:
            result['OtaInfo'] = self.ota_info.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        self.node_pool = []
        if m.get('NodePool') is not None:
            for k in m.get('NodePool'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k))
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaInfo') is not None:
            temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m['OtaInfo'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
        self.app_instance_group_models = app_instance_group_models
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListNodeInstanceTypeRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        language: str = None,
        os_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        self.biz_region_id = biz_region_id
        self.language = language
        self.os_type = os_type
        self.page_number = page_number
        self.page_size = page_size
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
        if self.language is not None:
            result['Language'] = self.language
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
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
        self.cpu = cpu
        self.gpu = gpu
        self.gpu_memory = gpu_memory
        self.max_capacity = max_capacity
        self.memory = memory
        self.node_instance_type = node_instance_type
        self.node_instance_type_family = node_instance_type_family
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
        self.node_instance_type_models = node_instance_type_models
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListOtaTaskRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        ota_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.ota_type = ota_type
        self.page_number = page_number
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
        self.ota_version = ota_version
        self.task_display_status = task_display_status
        self.task_id = task_id
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
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.task_list = task_list
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListRegionsResponseBodyRegionModels(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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
        self.region_models = region_models
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListTenantConfigResponseBodyTenantConfigModel(TeaModel):
    def __init__(
        self,
        app_instance_group_expire_remind: bool = None,
    ):
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
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class LogOffAllSessionsInAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ModifyAppInstanceGroupAttributeRequestNodePool(TeaModel):
    def __init__(
        self,
        node_capacity: int = None,
        node_pool_id: str = None,
    ):
        self.node_capacity = node_capacity
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


class ModifyAppInstanceGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        node_pool: ModifyAppInstanceGroupAttributeRequestNodePool = None,
        product_type: str = None,
        session_timeout: int = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.node_pool = node_pool
        self.product_type = product_type
        self.session_timeout = session_timeout

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
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('NodePool') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        return self


class ModifyAppInstanceGroupAttributeShrinkRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        node_pool_shrink: str = None,
        product_type: str = None,
        session_timeout: int = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.node_pool_shrink = node_pool_shrink
        self.product_type = product_type
        self.session_timeout = session_timeout

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
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        return self


class ModifyAppInstanceGroupAttributeResponseBody(TeaModel):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ModifyNodePoolAttributeRequestNodePoolStrategy(TeaModel):
    def __init__(
        self,
        max_scaling_amount: int = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_type: str = None,
    ):
        self.max_scaling_amount = max_scaling_amount
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        self.strategy_type = strategy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
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
        self.biz_region_id = biz_region_id
        self.node_capacity = node_capacity
        self.node_pool_strategy = node_pool_strategy
        self.pool_id = pool_id
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
        self.biz_region_id = biz_region_id
        self.node_capacity = node_capacity
        self.node_pool_strategy_shrink = node_pool_strategy_shrink
        self.pool_id = pool_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class PageListAppInstanceGroupUserRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.page_number = page_number
        self.page_size = page_size
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
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
    ):
        self.app_instance_group_id = app_instance_group_id
        self.auto_pay = auto_pay
        self.period = period
        self.period_unit = period_unit
        self.product_type = product_type
        self.promotion_id = promotion_id

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
        return self


class RenewAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.order_id = order_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UpdateAppInstanceGroupImageRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        product_type: str = None,
        update_mode: str = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        self.product_type = product_type
        self.update_mode = update_mode

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
        if self.update_mode is not None:
            result['UpdateMode'] = self.update_mode
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
        if m.get('UpdateMode') is not None:
            self.update_mode = m.get('UpdateMode')
        return self


class UpdateAppInstanceGroupImageResponseBody(TeaModel):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


