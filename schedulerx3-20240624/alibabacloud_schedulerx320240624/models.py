# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        app_name: str = None,
        app_type: int = None,
        cluster_id: str = None,
        enable_log: bool = None,
        label_route_strategy: int = None,
        max_concurrency: int = None,
        title: str = None,
    ):
        self.access_token = access_token
        # This parameter is required.
        self.app_name = app_name
        self.app_type = app_type
        # This parameter is required.
        self.cluster_id = cluster_id
        self.enable_log = enable_log
        self.label_route_strategy = label_route_strategy
        self.max_concurrency = max_concurrency
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log
        if self.label_route_strategy is not None:
            result['LabelRouteStrategy'] = self.label_route_strategy
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')
        if m.get('LabelRouteStrategy') is not None:
            self.label_route_strategy = m.get('LabelRouteStrategy')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateAppResponseBodyData(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        app_group_id: int = None,
    ):
        self.access_token = access_token
        self.app_group_id = app_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateAppResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = CreateAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequestTag(TeaModel):
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


class CreateClusterRequestVSwitches(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        duration: int = None,
        engine_type: str = None,
        pricing_cycle: str = None,
        tag: List[CreateClusterRequestTag] = None,
        v_switches: List[CreateClusterRequestVSwitches] = None,
        vpc_id: str = None,
    ):
        self.charge_type = charge_type
        # This parameter is required.
        self.cluster_name = cluster_name
        # This parameter is required.
        self.cluster_spec = cluster_spec
        self.duration = duration
        # This parameter is required.
        self.engine_type = engine_type
        self.pricing_cycle = pricing_cycle
        self.tag = tag
        # This parameter is required.
        self.v_switches = v_switches
        # VPC id
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = CreateClusterRequestVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateClusterShrinkRequestTag(TeaModel):
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


class CreateClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        duration: int = None,
        engine_type: str = None,
        pricing_cycle: str = None,
        tag: List[CreateClusterShrinkRequestTag] = None,
        v_switches_shrink: str = None,
        vpc_id: str = None,
    ):
        self.charge_type = charge_type
        # This parameter is required.
        self.cluster_name = cluster_name
        # This parameter is required.
        self.cluster_spec = cluster_spec
        self.duration = duration
        # This parameter is required.
        self.engine_type = engine_type
        self.pricing_cycle = pricing_cycle
        self.tag = tag
        # This parameter is required.
        self.v_switches_shrink = v_switches_shrink
        # VPC id
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

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
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switches_shrink is not None:
            result['VSwitches'] = self.v_switches_shrink
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitches') is not None:
            self.v_switches_shrink = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        order_id: int = None,
    ):
        self.cluster_id = cluster_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateClusterResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = CreateClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterResponseBody = None,
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequestNoticeConfig(TeaModel):
    def __init__(
        self,
        fail_enable: bool = None,
        fail_limit_times: int = None,
        miss_worker_enable: bool = None,
        send_channel: str = None,
        success_notice: bool = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        self.fail_enable = fail_enable
        self.fail_limit_times = fail_limit_times
        self.miss_worker_enable = miss_worker_enable
        self.send_channel = send_channel
        self.success_notice = success_notice
        self.timeout = timeout
        self.timeout_enable = timeout_enable
        self.timeout_kill_enable = timeout_kill_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable
        if self.fail_limit_times is not None:
            result['FailLimitTimes'] = self.fail_limit_times
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
        if self.success_notice is not None:
            result['SuccessNotice'] = self.success_notice
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable
        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')
        if m.get('FailLimitTimes') is not None:
            self.fail_limit_times = m.get('FailLimitTimes')
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('SuccessNotice') is not None:
            self.success_notice = m.get('SuccessNotice')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
        return self


class CreateJobRequestNoticeContacts(TeaModel):
    def __init__(
        self,
        contact_type: int = None,
        name: str = None,
    ):
        self.contact_type = contact_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        attempt_interval: int = None,
        calendar: str = None,
        child_job_id: str = None,
        cluster_id: str = None,
        description: str = None,
        executor_block_strategy: int = None,
        job_handler: str = None,
        job_type: str = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        name: str = None,
        notice_config: CreateJobRequestNoticeConfig = None,
        notice_contacts: List[CreateJobRequestNoticeContacts] = None,
        parameters: str = None,
        priority: int = None,
        route_strategy: int = None,
        script: str = None,
        start_time: int = None,
        status: int = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
        weight: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.child_job_id = child_job_id
        # This parameter is required.
        self.cluster_id = cluster_id
        self.description = description
        self.executor_block_strategy = executor_block_strategy
        self.job_handler = job_handler
        # This parameter is required.
        self.job_type = job_type
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        # This parameter is required.
        self.name = name
        self.notice_config = notice_config
        self.notice_contacts = notice_contacts
        self.parameters = parameters
        self.priority = priority
        self.route_strategy = route_strategy
        self.script = script
        self.start_time = start_time
        self.status = status
        self.time_expression = time_expression
        # This parameter is required.
        self.time_type = time_type
        self.timezone = timezone
        self.weight = weight

    def validate(self):
        if self.notice_config:
            self.notice_config.validate()
        if self.notice_contacts:
            for k in self.notice_contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.child_job_id is not None:
            result['ChildJobId'] = self.child_job_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.executor_block_strategy is not None:
            result['ExecutorBlockStrategy'] = self.executor_block_strategy
        if self.job_handler is not None:
            result['JobHandler'] = self.job_handler
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.notice_config is not None:
            result['NoticeConfig'] = self.notice_config.to_map()
        result['NoticeContacts'] = []
        if self.notice_contacts is not None:
            for k in self.notice_contacts:
                result['NoticeContacts'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy
        if self.script is not None:
            result['Script'] = self.script
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ChildJobId') is not None:
            self.child_job_id = m.get('ChildJobId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutorBlockStrategy') is not None:
            self.executor_block_strategy = m.get('ExecutorBlockStrategy')
        if m.get('JobHandler') is not None:
            self.job_handler = m.get('JobHandler')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NoticeConfig') is not None:
            temp_model = CreateJobRequestNoticeConfig()
            self.notice_config = temp_model.from_map(m['NoticeConfig'])
        self.notice_contacts = []
        if m.get('NoticeContacts') is not None:
            for k in m.get('NoticeContacts'):
                temp_model = CreateJobRequestNoticeContacts()
                self.notice_contacts.append(temp_model.from_map(k))
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateJobShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        attempt_interval: int = None,
        calendar: str = None,
        child_job_id: str = None,
        cluster_id: str = None,
        description: str = None,
        executor_block_strategy: int = None,
        job_handler: str = None,
        job_type: str = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        name: str = None,
        notice_config_shrink: str = None,
        notice_contacts_shrink: str = None,
        parameters: str = None,
        priority: int = None,
        route_strategy: int = None,
        script: str = None,
        start_time: int = None,
        status: int = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
        weight: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.child_job_id = child_job_id
        # This parameter is required.
        self.cluster_id = cluster_id
        self.description = description
        self.executor_block_strategy = executor_block_strategy
        self.job_handler = job_handler
        # This parameter is required.
        self.job_type = job_type
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        # This parameter is required.
        self.name = name
        self.notice_config_shrink = notice_config_shrink
        self.notice_contacts_shrink = notice_contacts_shrink
        self.parameters = parameters
        self.priority = priority
        self.route_strategy = route_strategy
        self.script = script
        self.start_time = start_time
        self.status = status
        self.time_expression = time_expression
        # This parameter is required.
        self.time_type = time_type
        self.timezone = timezone
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.child_job_id is not None:
            result['ChildJobId'] = self.child_job_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.executor_block_strategy is not None:
            result['ExecutorBlockStrategy'] = self.executor_block_strategy
        if self.job_handler is not None:
            result['JobHandler'] = self.job_handler
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.notice_config_shrink is not None:
            result['NoticeConfig'] = self.notice_config_shrink
        if self.notice_contacts_shrink is not None:
            result['NoticeContacts'] = self.notice_contacts_shrink
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy
        if self.script is not None:
            result['Script'] = self.script
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ChildJobId') is not None:
            self.child_job_id = m.get('ChildJobId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutorBlockStrategy') is not None:
            self.executor_block_strategy = m.get('ExecutorBlockStrategy')
        if m.get('JobHandler') is not None:
            self.job_handler = m.get('JobHandler')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NoticeConfig') is not None:
            self.notice_config_shrink = m.get('NoticeConfig')
        if m.get('NoticeContacts') is not None:
            self.notice_contacts_shrink = m.get('NoticeContacts')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = CreateJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobResponseBody = None,
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
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterResponseBody = None,
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
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_ids: List[int] = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # -\
        self.job_ids = job_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class DeleteJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # -\
        self.job_ids_shrink = job_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_ids_shrink is not None:
            result['JobIds'] = self.job_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobIds') is not None:
            self.job_ids_shrink = m.get('JobIds')
        return self


class DeleteJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteJobsResponseBody = None,
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
            temp_model = DeleteJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportJobsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        export_job_type: int = None,
        job_ids: List[int] = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.export_job_type = export_job_type
        # -\
        self.job_ids = job_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.export_job_type is not None:
            result['ExportJobType'] = self.export_job_type
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ExportJobType') is not None:
            self.export_job_type = m.get('ExportJobType')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class ExportJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        export_job_type: int = None,
        job_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.export_job_type = export_job_type
        # -\
        self.job_ids_shrink = job_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.export_job_type is not None:
            result['ExportJobType'] = self.export_job_type
        if self.job_ids_shrink is not None:
            result['JobIds'] = self.job_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ExportJobType') is not None:
            self.export_job_type = m.get('ExportJobType')
        if m.get('JobIds') is not None:
            self.job_ids_shrink = m.get('JobIds')
        return self


class ExportJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: bytes = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetAppResponseBodyData(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        app_name: str = None,
        app_type: int = None,
        creator: str = None,
        enable_log: bool = None,
        executor_num: int = None,
        id: int = None,
        job_num: int = None,
        label_route_strategy: int = None,
        leader: str = None,
        max_concurrency: int = None,
        max_jobs: int = None,
        title: str = None,
        updater: str = None,
    ):
        # AccessToken。
        self.access_token = access_token
        self.app_name = app_name
        self.app_type = app_type
        self.creator = creator
        self.enable_log = enable_log
        self.executor_num = executor_num
        self.id = id
        self.job_num = job_num
        self.label_route_strategy = label_route_strategy
        self.leader = leader
        self.max_concurrency = max_concurrency
        self.max_jobs = max_jobs
        self.title = title
        self.updater = updater

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log
        if self.executor_num is not None:
            result['ExecutorNum'] = self.executor_num
        if self.id is not None:
            result['Id'] = self.id
        if self.job_num is not None:
            result['JobNum'] = self.job_num
        if self.label_route_strategy is not None:
            result['LabelRouteStrategy'] = self.label_route_strategy
        if self.leader is not None:
            result['Leader'] = self.leader
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.max_jobs is not None:
            result['MaxJobs'] = self.max_jobs
        if self.title is not None:
            result['Title'] = self.title
        if self.updater is not None:
            result['Updater'] = self.updater
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')
        if m.get('ExecutorNum') is not None:
            self.executor_num = m.get('ExecutorNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobNum') is not None:
            self.job_num = m.get('JobNum')
        if m.get('LabelRouteStrategy') is not None:
            self.label_route_strategy = m.get('LabelRouteStrategy')
        if m.get('Leader') is not None:
            self.leader = m.get('Leader')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('MaxJobs') is not None:
            self.max_jobs = m.get('MaxJobs')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Updater') is not None:
            self.updater = m.get('Updater')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAppResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = GetAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppResponseBody = None,
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetClusterResponseBodyDataVSwitches(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        create_time: str = None,
        end_time: str = None,
        engine_type: str = None,
        engine_version: str = None,
        internet_domain: str = None,
        intranet_domain: str = None,
        job_num: int = None,
        kube_config: str = None,
        max_job_num: int = None,
        product_type: int = None,
        spm: int = None,
        status: int = None,
        tags: Dict[str, Any] = None,
        v_switches: List[GetClusterResponseBodyDataVSwitches] = None,
        version_lifecycle: str = None,
        vpc_id: str = None,
        worker_num: int = None,
        zones: List[str] = None,
    ):
        self.charge_type = charge_type
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_spec = cluster_spec
        self.create_time = create_time
        self.end_time = end_time
        self.engine_type = engine_type
        self.engine_version = engine_version
        self.internet_domain = internet_domain
        self.intranet_domain = intranet_domain
        self.job_num = job_num
        self.kube_config = kube_config
        self.max_job_num = max_job_num
        self.product_type = product_type
        self.spm = spm
        self.status = status
        self.tags = tags
        self.v_switches = v_switches
        self.version_lifecycle = version_lifecycle
        # VPC ID
        self.vpc_id = vpc_id
        self.worker_num = worker_num
        self.zones = zones

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.job_num is not None:
            result['JobNum'] = self.job_num
        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config
        if self.max_job_num is not None:
            result['MaxJobNum'] = self.max_job_num
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.spm is not None:
            result['Spm'] = self.spm
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        if self.version_lifecycle is not None:
            result['VersionLifecycle'] = self.version_lifecycle
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('JobNum') is not None:
            self.job_num = m.get('JobNum')
        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')
        if m.get('MaxJobNum') is not None:
            self.max_job_num = m.get('MaxJobNum')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Spm') is not None:
            self.spm = m.get('Spm')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = GetClusterResponseBodyDataVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('VersionLifecycle') is not None:
            self.version_lifecycle = m.get('VersionLifecycle')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetClusterResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = GetClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterResponseBody = None,
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
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDesigateInfoRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_id: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetDesigateInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        designate_type: int = None,
        transferable: bool = None,
    ):
        self.designate_type = designate_type
        self.transferable = transferable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type
        if self.transferable is not None:
            result['Transferable'] = self.transferable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')
        if m.get('Transferable') is not None:
            self.transferable = m.get('Transferable')
        return self


class GetDesigateInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetDesigateInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = GetDesigateInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDesigateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDesigateInfoResponseBody = None,
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
            temp_model = GetDesigateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobExecutionRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_execution_id: str = None,
        mse_session_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_execution_id = job_execution_id
        self.mse_session_id = mse_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.mse_session_id is not None:
            result['MseSessionId'] = self.mse_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('MseSessionId') is not None:
            self.mse_session_id = m.get('MseSessionId')
        return self


class GetJobExecutionResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        attempt: int = None,
        data_time: str = None,
        duration: int = None,
        end_time: str = None,
        executor: str = None,
        job_execution_id: str = None,
        job_id: int = None,
        job_name: str = None,
        job_type: str = None,
        parameters: str = None,
        result: str = None,
        route_strategy: int = None,
        schedule_time: str = None,
        server_ip: str = None,
        start_time: str = None,
        status: int = None,
        time_type: int = None,
        trigger_type: int = None,
    ):
        self.app_name = app_name
        self.attempt = attempt
        self.data_time = data_time
        self.duration = duration
        self.end_time = end_time
        self.executor = executor
        self.job_execution_id = job_execution_id
        self.job_id = job_id
        self.job_name = job_name
        self.job_type = job_type
        self.parameters = parameters
        self.result = result
        self.route_strategy = route_strategy
        self.schedule_time = schedule_time
        self.server_ip = server_ip
        self.start_time = start_time
        self.status = status
        self.time_type = time_type
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.attempt is not None:
            result['Attempt'] = self.attempt
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor is not None:
            result['Executor'] = self.executor
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.result is not None:
            result['Result'] = self.result
        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Attempt') is not None:
            self.attempt = m.get('Attempt')
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Executor') is not None:
            self.executor = m.get('Executor')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class GetJobExecutionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetJobExecutionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
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
            temp_model = GetJobExecutionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobExecutionResponseBody = None,
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
            temp_model = GetJobExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobExecutionProgressRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_execution_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_execution_id = job_execution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        return self


class GetJobExecutionProgressResponseBodyDataRootProgress(TeaModel):
    def __init__(
        self,
        finished: int = None,
        total: int = None,
    ):
        self.finished = finished
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetJobExecutionProgressResponseBodyDataShardingProgressStatusType(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        tips: Dict[str, str] = None,
    ):
        self.code = code
        self.name = name
        # -\
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class GetJobExecutionProgressResponseBodyDataShardingProgress(TeaModel):
    def __init__(
        self,
        id: int = None,
        job_execution_id: str = None,
        result: str = None,
        status: int = None,
        status_type: GetJobExecutionProgressResponseBodyDataShardingProgressStatusType = None,
        worker_addr: str = None,
    ):
        # id
        self.id = id
        self.job_execution_id = job_execution_id
        self.result = result
        self.status = status
        self.status_type = status_type
        self.worker_addr = worker_addr

    def validate(self):
        if self.status_type:
            self.status_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.status_type is not None:
            result['StatusType'] = self.status_type.to_map()
        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusType') is not None:
            temp_model = GetJobExecutionProgressResponseBodyDataShardingProgressStatusType()
            self.status_type = temp_model.from_map(m['StatusType'])
        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')
        return self


class GetJobExecutionProgressResponseBodyDataTaskProgress(TeaModel):
    def __init__(
        self,
        failed: int = None,
        name: str = None,
        pulled: int = None,
        queue: int = None,
        running: int = None,
        success: int = None,
        total: int = None,
    ):
        self.failed = failed
        self.name = name
        self.pulled = pulled
        self.queue = queue
        self.running = running
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.name is not None:
            result['Name'] = self.name
        if self.pulled is not None:
            result['Pulled'] = self.pulled
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.running is not None:
            result['Running'] = self.running
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pulled') is not None:
            self.pulled = m.get('Pulled')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetJobExecutionProgressResponseBodyDataTotalProgress(TeaModel):
    def __init__(
        self,
        finished: int = None,
        total: int = None,
    ):
        self.finished = finished
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetJobExecutionProgressResponseBodyDataWorkerProgress(TeaModel):
    def __init__(
        self,
        failed: int = None,
        pulled: int = None,
        queue: int = None,
        running: int = None,
        success: int = None,
        total: int = None,
        trace_id: str = None,
        worker_addr: str = None,
    ):
        self.failed = failed
        self.pulled = pulled
        self.queue = queue
        self.running = running
        self.success = success
        self.total = total
        self.trace_id = trace_id
        self.worker_addr = worker_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.pulled is not None:
            result['Pulled'] = self.pulled
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.running is not None:
            result['Running'] = self.running
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Pulled') is not None:
            self.pulled = m.get('Pulled')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')
        return self


class GetJobExecutionProgressResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        job_description: str = None,
        root_progress: GetJobExecutionProgressResponseBodyDataRootProgress = None,
        sharding_progress: List[GetJobExecutionProgressResponseBodyDataShardingProgress] = None,
        start_time: str = None,
        task_progress: List[GetJobExecutionProgressResponseBodyDataTaskProgress] = None,
        total_progress: GetJobExecutionProgressResponseBodyDataTotalProgress = None,
        worker_progress: List[GetJobExecutionProgressResponseBodyDataWorkerProgress] = None,
    ):
        self.end_time = end_time
        self.job_description = job_description
        self.root_progress = root_progress
        self.sharding_progress = sharding_progress
        self.start_time = start_time
        self.task_progress = task_progress
        self.total_progress = total_progress
        self.worker_progress = worker_progress

    def validate(self):
        if self.root_progress:
            self.root_progress.validate()
        if self.sharding_progress:
            for k in self.sharding_progress:
                if k:
                    k.validate()
        if self.task_progress:
            for k in self.task_progress:
                if k:
                    k.validate()
        if self.total_progress:
            self.total_progress.validate()
        if self.worker_progress:
            for k in self.worker_progress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.root_progress is not None:
            result['RootProgress'] = self.root_progress.to_map()
        result['ShardingProgress'] = []
        if self.sharding_progress is not None:
            for k in self.sharding_progress:
                result['ShardingProgress'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['TaskProgress'] = []
        if self.task_progress is not None:
            for k in self.task_progress:
                result['TaskProgress'].append(k.to_map() if k else None)
        if self.total_progress is not None:
            result['TotalProgress'] = self.total_progress.to_map()
        result['WorkerProgress'] = []
        if self.worker_progress is not None:
            for k in self.worker_progress:
                result['WorkerProgress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('RootProgress') is not None:
            temp_model = GetJobExecutionProgressResponseBodyDataRootProgress()
            self.root_progress = temp_model.from_map(m['RootProgress'])
        self.sharding_progress = []
        if m.get('ShardingProgress') is not None:
            for k in m.get('ShardingProgress'):
                temp_model = GetJobExecutionProgressResponseBodyDataShardingProgress()
                self.sharding_progress.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.task_progress = []
        if m.get('TaskProgress') is not None:
            for k in m.get('TaskProgress'):
                temp_model = GetJobExecutionProgressResponseBodyDataTaskProgress()
                self.task_progress.append(temp_model.from_map(k))
        if m.get('TotalProgress') is not None:
            temp_model = GetJobExecutionProgressResponseBodyDataTotalProgress()
            self.total_progress = temp_model.from_map(m['TotalProgress'])
        self.worker_progress = []
        if m.get('WorkerProgress') is not None:
            for k in m.get('WorkerProgress'):
                temp_model = GetJobExecutionProgressResponseBodyDataWorkerProgress()
                self.worker_progress.append(temp_model.from_map(k))
        return self


class GetJobExecutionProgressResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetJobExecutionProgressResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = GetJobExecutionProgressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobExecutionProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobExecutionProgressResponseBody = None,
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
            temp_model = GetJobExecutionProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobExecutionThreadDumpRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        executor_addr: str = None,
        job_execution_id: str = None,
    ):
        self.app_name = app_name
        self.cluster_id = cluster_id
        self.executor_addr = executor_addr
        self.job_execution_id = job_execution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.executor_addr is not None:
            result['ExecutorAddr'] = self.executor_addr
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ExecutorAddr') is not None:
            self.executor_addr = m.get('ExecutorAddr')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        return self


class GetJobExecutionThreadDumpResponseBodyData(TeaModel):
    def __init__(
        self,
        dump: str = None,
    ):
        self.dump = dump

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dump is not None:
            result['Dump'] = self.dump
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dump') is not None:
            self.dump = m.get('Dump')
        return self


class GetJobExecutionThreadDumpResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetJobExecutionThreadDumpResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = GetJobExecutionThreadDumpResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobExecutionThreadDumpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobExecutionThreadDumpResponseBody = None,
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
            temp_model = GetJobExecutionThreadDumpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        end_time: int = None,
        job_execution_id: str = None,
        keyword: str = None,
        level: str = None,
        line_num: int = None,
        log_id: int = None,
        offset: int = None,
        reverse: bool = None,
        start_time: int = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.end_time = end_time
        self.job_execution_id = job_execution_id
        self.keyword = keyword
        self.level = level
        # LineNum
        self.line_num = line_num
        self.log_id = log_id
        self.offset = offset
        self.reverse = reverse
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.level is not None:
            result['Level'] = self.level
        if self.line_num is not None:
            result['LineNum'] = self.line_num
        if self.log_id is not None:
            result['LogId'] = self.log_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LineNum') is not None:
            self.line_num = m.get('LineNum')
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetLogResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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


class GetLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLogResponseBody = None,
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
            temp_model = GetLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogEventRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        end_time: int = None,
        event: str = None,
        job_execution_id: int = None,
        job_name: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        reverse: bool = None,
        start_time: int = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.end_time = end_time
        self.event = event
        self.job_execution_id = job_execution_id
        self.job_name = job_name
        self.keyword = keyword
        self.page_num = page_num
        self.page_size = page_size
        self.reverse = reverse
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetLogEventResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        content: str = None,
        event: str = None,
        job_execution_id: str = None,
        job_name: str = None,
        time: str = None,
        worker_addr: str = None,
    ):
        self.app_name = app_name
        self.content = content
        self.event = event
        self.job_execution_id = job_execution_id
        self.job_name = job_name
        self.time = time
        self.worker_addr = worker_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.content is not None:
            result['Content'] = self.content
        if self.event is not None:
            result['Event'] = self.event
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.time is not None:
            result['Time'] = self.time
        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')
        return self


class GetLogEventResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[GetLogEventResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # -\
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetLogEventResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetLogEventResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetLogEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = GetLogEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLogEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLogEventResponseBody = None,
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
            temp_model = GetLogEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportCalendarRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        months: str = None,
        name: str = None,
        year: int = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.months = months
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.months is not None:
            result['Months'] = self.months
        if self.name is not None:
            result['Name'] = self.name
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class ImportCalendarResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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


class ImportCalendarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportCalendarResponseBody = None,
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
            temp_model = ImportCalendarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportJobsRequest(TeaModel):
    def __init__(
        self,
        auto_create_app: bool = None,
        cluster_id: str = None,
        content: str = None,
        overwrite: bool = None,
    ):
        self.auto_create_app = auto_create_app
        # This parameter is required.
        self.cluster_id = cluster_id
        self.content = content
        self.overwrite = overwrite

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_app is not None:
            result['AutoCreateApp'] = self.auto_create_app
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.content is not None:
            result['Content'] = self.content
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateApp') is not None:
            self.auto_create_app = m.get('AutoCreateApp')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        return self


class ImportJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportJobsResponseBody = None,
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
            temp_model = ImportJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmEventRequest(TeaModel):
    def __init__(
        self,
        alarm_channel: str = None,
        alarm_status: str = None,
        alarm_type: str = None,
        app_name: str = None,
        cluster_id: str = None,
        end_time: int = None,
        job_name: str = None,
        page_num: str = None,
        page_size: str = None,
        reverse: bool = None,
        start_time: int = None,
    ):
        self.alarm_channel = alarm_channel
        self.alarm_status = alarm_status
        self.alarm_type = alarm_type
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.end_time = end_time
        self.job_name = job_name
        self.page_num = page_num
        self.page_size = page_size
        self.reverse = reverse
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_channel is not None:
            result['AlarmChannel'] = self.alarm_channel
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmChannel') is not None:
            self.alarm_channel = m.get('AlarmChannel')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAlarmEventResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        alarm_channel: str = None,
        alarm_contacts: str = None,
        alarm_message: str = None,
        alarm_status: str = None,
        alarm_type: str = None,
        app_name: str = None,
        job_name: str = None,
        time: str = None,
    ):
        self.alarm_channel = alarm_channel
        self.alarm_contacts = alarm_contacts
        self.alarm_message = alarm_message
        self.alarm_status = alarm_status
        self.alarm_type = alarm_type
        self.app_name = app_name
        self.job_name = job_name
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_channel is not None:
            result['AlarmChannel'] = self.alarm_channel
        if self.alarm_contacts is not None:
            result['AlarmContacts'] = self.alarm_contacts
        if self.alarm_message is not None:
            result['AlarmMessage'] = self.alarm_message
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmChannel') is not None:
            self.alarm_channel = m.get('AlarmChannel')
        if m.get('AlarmContacts') is not None:
            self.alarm_contacts = m.get('AlarmContacts')
        if m.get('AlarmMessage') is not None:
            self.alarm_message = m.get('AlarmMessage')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class ListAlarmEventResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListAlarmEventResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListAlarmEventResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAlarmEventResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListAlarmEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = ListAlarmEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlarmEventResponseBody = None,
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
            temp_model = ListAlarmEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppNamesRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListAppNamesResponseBodyData(TeaModel):
    def __init__(
        self,
        app_group_id: str = None,
        app_name: str = None,
        app_type: int = None,
        id: int = None,
        title: str = None,
        worker_registry: str = None,
    ):
        self.app_group_id = app_group_id
        self.app_name = app_name
        self.app_type = app_type
        self.id = id
        self.title = title
        self.worker_registry = worker_registry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        if self.worker_registry is not None:
            result['WorkerRegistry'] = self.worker_registry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WorkerRegistry') is not None:
            self.worker_registry = m.get('WorkerRegistry')
        return self


class ListAppNamesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListAppNamesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # .
        self.data = data
        self.message = message
        self.request_id = request_id
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppNamesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppNamesResponseBody = None,
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
            temp_model = ListAppNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        page_num: int = None,
        page_size: int = None,
        title: str = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.page_num = page_num
        self.page_size = page_size
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListAppsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        app_name: str = None,
        app_type: int = None,
        creator: str = None,
        enable_log: bool = None,
        executor_num: int = None,
        id: int = None,
        job_num: int = None,
        label_route_strategy: int = None,
        leader: str = None,
        max_concurrency: int = None,
        max_jobs: int = None,
        title: str = None,
        updater: str = None,
        worker_registry: str = None,
    ):
        # AccessToken
        self.access_token = access_token
        self.app_name = app_name
        self.app_type = app_type
        self.creator = creator
        self.enable_log = enable_log
        self.executor_num = executor_num
        self.id = id
        self.job_num = job_num
        self.label_route_strategy = label_route_strategy
        self.leader = leader
        self.max_concurrency = max_concurrency
        self.max_jobs = max_jobs
        self.title = title
        self.updater = updater
        self.worker_registry = worker_registry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log
        if self.executor_num is not None:
            result['ExecutorNum'] = self.executor_num
        if self.id is not None:
            result['Id'] = self.id
        if self.job_num is not None:
            result['JobNum'] = self.job_num
        if self.label_route_strategy is not None:
            result['LabelRouteStrategy'] = self.label_route_strategy
        if self.leader is not None:
            result['Leader'] = self.leader
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.max_jobs is not None:
            result['MaxJobs'] = self.max_jobs
        if self.title is not None:
            result['Title'] = self.title
        if self.updater is not None:
            result['Updater'] = self.updater
        if self.worker_registry is not None:
            result['WorkerRegistry'] = self.worker_registry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')
        if m.get('ExecutorNum') is not None:
            self.executor_num = m.get('ExecutorNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobNum') is not None:
            self.job_num = m.get('JobNum')
        if m.get('LabelRouteStrategy') is not None:
            self.label_route_strategy = m.get('LabelRouteStrategy')
        if m.get('Leader') is not None:
            self.leader = m.get('Leader')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('MaxJobs') is not None:
            self.max_jobs = m.get('MaxJobs')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Updater') is not None:
            self.updater = m.get('Updater')
        if m.get('WorkerRegistry') is not None:
            self.worker_registry = m.get('WorkerRegistry')
        return self


class ListAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListAppsResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # -\
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListAppsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListAppsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = ListAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppsResponseBody = None,
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
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCalendarNamesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListCalendarNamesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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


class ListCalendarNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCalendarNamesResponseBody = None,
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
            temp_model = ListCalendarNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequestTag(TeaModel):
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


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        page_num: int = None,
        page_size: int = None,
        tag: List[ListClustersRequestTag] = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.page_num = page_num
        self.page_size = page_size
        self.tag = tag

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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListClustersResponseBodyDataRecordsVSwitches(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListClustersResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        create_time: str = None,
        end_time: str = None,
        engine_type: str = None,
        engine_version: str = None,
        internet_domain: str = None,
        intranet_domain: str = None,
        product_type: int = None,
        sp_instance_id: str = None,
        status: int = None,
        tags: Dict[str, Any] = None,
        v_switches: List[ListClustersResponseBodyDataRecordsVSwitches] = None,
        version_lifecycle: str = None,
        vpc_id: str = None,
    ):
        self.charge_type = charge_type
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_spec = cluster_spec
        self.create_time = create_time
        self.end_time = end_time
        self.engine_type = engine_type
        self.engine_version = engine_version
        self.internet_domain = internet_domain
        self.intranet_domain = intranet_domain
        self.product_type = product_type
        self.sp_instance_id = sp_instance_id
        self.status = status
        self.tags = tags
        self.v_switches = v_switches
        self.version_lifecycle = version_lifecycle
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.sp_instance_id is not None:
            result['SpInstanceId'] = self.sp_instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        if self.version_lifecycle is not None:
            result['VersionLifecycle'] = self.version_lifecycle
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SpInstanceId') is not None:
            self.sp_instance_id = m.get('SpInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = ListClustersResponseBodyDataRecordsVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('VersionLifecycle') is not None:
            self.version_lifecycle = m.get('VersionLifecycle')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListClustersResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListClustersResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # -\
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListClustersResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListClustersResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        # This parameter is required.
        self.message = message
        self.request_id = request_id
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
            temp_model = ListClustersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClustersResponseBody = None,
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
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutorsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_id: int = None,
        label: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.job_id = job_id
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ListExecutorsResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        ip: str = None,
        is_designated: bool = None,
        label: str = None,
        online: bool = None,
        port: int = None,
        version: str = None,
        weight: int = None,
    ):
        self.address = address
        self.ip = ip
        self.is_designated = is_designated
        self.label = label
        self.online = online
        self.port = port
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_designated is not None:
            result['IsDesignated'] = self.is_designated
        if self.label is not None:
            result['Label'] = self.label
        if self.online is not None:
            result['Online'] = self.online
        if self.port is not None:
            result['Port'] = self.port
        if self.version is not None:
            result['Version'] = self.version
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsDesignated') is not None:
            self.is_designated = m.get('IsDesignated')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListExecutorsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListExecutorsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListExecutorsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListExecutorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExecutorsResponseBody = None,
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
            temp_model = ListExecutorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobExecutionsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        end_time: str = None,
        job_execution_id: str = None,
        job_id: int = None,
        job_name: str = None,
        page_num: int = None,
        page_size: int = None,
        start_time: str = None,
        status: int = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.end_time = end_time
        self.job_execution_id = job_execution_id
        self.job_id = job_id
        self.job_name = job_name
        self.page_num = page_num
        self.page_size = page_size
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListJobExecutionsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        attempt: int = None,
        data_time: str = None,
        duration: int = None,
        end_time: str = None,
        executor: str = None,
        job_execution_id: str = None,
        job_id: int = None,
        job_name: str = None,
        job_type: str = None,
        parameters: str = None,
        result: str = None,
        route_strategy: int = None,
        schedule_time: str = None,
        server_ip: str = None,
        status: int = None,
        time_type: int = None,
        total_tokens: int = None,
        trigger_type: int = None,
        work_addr: str = None,
    ):
        self.app_name = app_name
        self.attempt = attempt
        self.data_time = data_time
        self.duration = duration
        self.end_time = end_time
        self.executor = executor
        self.job_execution_id = job_execution_id
        self.job_id = job_id
        self.job_name = job_name
        self.job_type = job_type
        self.parameters = parameters
        self.result = result
        self.route_strategy = route_strategy
        self.schedule_time = schedule_time
        self.server_ip = server_ip
        self.status = status
        self.time_type = time_type
        self.total_tokens = total_tokens
        self.trigger_type = trigger_type
        self.work_addr = work_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.attempt is not None:
            result['Attempt'] = self.attempt
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor is not None:
            result['Executor'] = self.executor
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.result is not None:
            result['Result'] = self.result
        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.status is not None:
            result['Status'] = self.status
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Attempt') is not None:
            self.attempt = m.get('Attempt')
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Executor') is not None:
            self.executor = m.get('Executor')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')
        return self


class ListJobExecutionsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListJobExecutionsResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # -\
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListJobExecutionsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListJobExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListJobExecutionsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        # This parameter is required.
        self.message = message
        self.request_id = request_id
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
            temp_model = ListJobExecutionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListJobExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobExecutionsResponseBody = None,
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
            temp_model = ListJobExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobScriptHistoryRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_id: int = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_id = job_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListJobScriptHistoryResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        script_content: str = None,
        version_description: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.script_content = script_content
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.script_content is not None:
            result['ScriptContent'] = self.script_content
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        return self


class ListJobScriptHistoryResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        records: List[ListJobScriptHistoryResponseBodyDataRecords] = None,
        total: str = None,
    ):
        self.next_token = next_token
        # -\
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListJobScriptHistoryResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListJobScriptHistoryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListJobScriptHistoryResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.max_results = max_results
        # This parameter is required.
        self.message = message
        self.request_id = request_id
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
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
            temp_model = ListJobScriptHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListJobScriptHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobScriptHistoryResponseBody = None,
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
            temp_model = ListJobScriptHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        description: str = None,
        job_handler: str = None,
        job_id: int = None,
        job_name: str = None,
        page_num: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.description = description
        self.job_handler = job_handler
        self.job_id = job_id
        self.job_name = job_name
        self.page_num = page_num
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.job_handler is not None:
            result['JobHandler'] = self.job_handler
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobHandler') is not None:
            self.job_handler = m.get('JobHandler')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListJobsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        attempt_interval: int = None,
        calendar: str = None,
        child_job_id: str = None,
        clean_mode: str = None,
        creator: str = None,
        current_execute_status: int = None,
        data_offset: int = None,
        description: str = None,
        executor_block_strategy: str = None,
        job_handler: str = None,
        job_id: int = None,
        job_type: str = None,
        last_execute_end_time: str = None,
        last_execute_status: int = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        name: str = None,
        notice_config: str = None,
        notice_contacts: str = None,
        parameters: str = None,
        priority: int = None,
        route_strategy: int = None,
        script: str = None,
        status: int = None,
        time_expression: str = None,
        time_type: int = None,
        time_zone: str = None,
        timezone: str = None,
        updater: str = None,
        weight: int = None,
        xattrs: str = None,
    ):
        self.app_name = app_name
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.child_job_id = child_job_id
        self.clean_mode = clean_mode
        self.creator = creator
        self.current_execute_status = current_execute_status
        self.data_offset = data_offset
        self.description = description
        self.executor_block_strategy = executor_block_strategy
        self.job_handler = job_handler
        self.job_id = job_id
        self.job_type = job_type
        self.last_execute_end_time = last_execute_end_time
        self.last_execute_status = last_execute_status
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        self.name = name
        self.notice_config = notice_config
        self.notice_contacts = notice_contacts
        self.parameters = parameters
        self.priority = priority
        self.route_strategy = route_strategy
        self.script = script
        self.status = status
        self.time_expression = time_expression
        self.time_type = time_type
        self.time_zone = time_zone
        self.timezone = timezone
        self.updater = updater
        self.weight = weight
        self.xattrs = xattrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.child_job_id is not None:
            result['ChildJobId'] = self.child_job_id
        if self.clean_mode is not None:
            result['CleanMode'] = self.clean_mode
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.current_execute_status is not None:
            result['CurrentExecuteStatus'] = self.current_execute_status
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.description is not None:
            result['Description'] = self.description
        if self.executor_block_strategy is not None:
            result['ExecutorBlockStrategy'] = self.executor_block_strategy
        if self.job_handler is not None:
            result['JobHandler'] = self.job_handler
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.last_execute_end_time is not None:
            result['LastExecuteEndTime'] = self.last_execute_end_time
        if self.last_execute_status is not None:
            result['LastExecuteStatus'] = self.last_execute_status
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.notice_config is not None:
            result['NoticeConfig'] = self.notice_config
        if self.notice_contacts is not None:
            result['NoticeContacts'] = self.notice_contacts
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy
        if self.script is not None:
            result['Script'] = self.script
        if self.status is not None:
            result['Status'] = self.status
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.updater is not None:
            result['Updater'] = self.updater
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.xattrs is not None:
            result['Xattrs'] = self.xattrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ChildJobId') is not None:
            self.child_job_id = m.get('ChildJobId')
        if m.get('CleanMode') is not None:
            self.clean_mode = m.get('CleanMode')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CurrentExecuteStatus') is not None:
            self.current_execute_status = m.get('CurrentExecuteStatus')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutorBlockStrategy') is not None:
            self.executor_block_strategy = m.get('ExecutorBlockStrategy')
        if m.get('JobHandler') is not None:
            self.job_handler = m.get('JobHandler')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('LastExecuteEndTime') is not None:
            self.last_execute_end_time = m.get('LastExecuteEndTime')
        if m.get('LastExecuteStatus') is not None:
            self.last_execute_status = m.get('LastExecuteStatus')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NoticeConfig') is not None:
            self.notice_config = m.get('NoticeConfig')
        if m.get('NoticeContacts') is not None:
            self.notice_contacts = m.get('NoticeContacts')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Updater') is not None:
            self.updater = m.get('Updater')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Xattrs') is not None:
            self.xattrs = m.get('Xattrs')
        return self


class ListJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListJobsResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # -\
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListJobsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListJobsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = ListJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
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
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLablesRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_id: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class ListLablesResponseBodyData(TeaModel):
    def __init__(
        self,
        is_designated: bool = None,
        label: str = None,
        online: bool = None,
        size: int = None,
    ):
        self.is_designated = is_designated
        self.label = label
        self.online = online
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_designated is not None:
            result['IsDesignated'] = self.is_designated
        if self.label is not None:
            result['Label'] = self.label
        if self.online is not None:
            result['Online'] = self.online
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDesignated') is not None:
            self.is_designated = m.get('IsDesignated')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListLablesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListLablesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListLablesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListLablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLablesResponseBody = None,
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
            temp_model = ListLablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionZoneResponseBodyData(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        # zone id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListRegionZoneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListRegionZoneResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRegionZoneResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRegionZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionZoneResponseBody = None,
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
            temp_model = ListRegionZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        # endpoint
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        regions: List[ListRegionsResponseBodyRegions] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        # -\
        self.regions = regions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.regions:
            for k in self.regions:
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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class ListScheduleEventRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        end_time: int = None,
        event: str = None,
        event_type: str = None,
        job_execution_id: str = None,
        job_name: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        reverse: bool = None,
        start_time: int = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.end_time = end_time
        self.event = event
        self.event_type = event_type
        self.job_execution_id = job_execution_id
        self.job_name = job_name
        self.keyword = keyword
        self.page_num = page_num
        self.page_size = page_size
        self.reverse = reverse
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListScheduleEventResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        content: str = None,
        event: str = None,
        job_execution_id: str = None,
        job_name: str = None,
        time: str = None,
        worker_addr: str = None,
    ):
        self.app_name = app_name
        self.content = content
        self.event = event
        # 130
        self.job_execution_id = job_execution_id
        self.job_name = job_name
        self.time = time
        self.worker_addr = worker_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.content is not None:
            result['Content'] = self.content
        if self.event is not None:
            result['Event'] = self.event
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.time is not None:
            result['Time'] = self.time
        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')
        return self


class ListScheduleEventResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[ListScheduleEventResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListScheduleEventResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListScheduleEventResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListScheduleEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = ListScheduleEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListScheduleEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScheduleEventResponseBody = None,
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
            temp_model = ListScheduleEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduleTimesRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        calendar: str = None,
        cluster_id: str = None,
        time_expression: str = None,
        time_type: int = None,
        time_zone: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.calendar = calendar
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.time_expression = time_expression
        # This parameter is required.
        self.time_type = time_type
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class ListScheduleTimesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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


class ListScheduleTimesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScheduleTimesResponseBody = None,
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
            temp_model = ListScheduleTimesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateDesignateExecutorsRequest(TeaModel):
    def __init__(
        self,
        address_list: List[str] = None,
        app_name: str = None,
        cluster_id: str = None,
        designate_type: int = None,
        job_id: int = None,
        transferable: bool = None,
    ):
        # This parameter is required.
        self.address_list = address_list
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.designate_type = designate_type
        # This parameter is required.
        self.job_id = job_id
        self.transferable = transferable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.transferable is not None:
            result['Transferable'] = self.transferable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Transferable') is not None:
            self.transferable = m.get('Transferable')
        return self


class OperateDesignateExecutorsShrinkRequest(TeaModel):
    def __init__(
        self,
        address_list_shrink: str = None,
        app_name: str = None,
        cluster_id: str = None,
        designate_type: int = None,
        job_id: int = None,
        transferable: bool = None,
    ):
        # This parameter is required.
        self.address_list_shrink = address_list_shrink
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.designate_type = designate_type
        # This parameter is required.
        self.job_id = job_id
        self.transferable = transferable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_list_shrink is not None:
            result['AddressList'] = self.address_list_shrink
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.transferable is not None:
            result['Transferable'] = self.transferable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list_shrink = m.get('AddressList')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Transferable') is not None:
            self.transferable = m.get('Transferable')
        return self


class OperateDesignateExecutorsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateDesignateExecutorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateDesignateExecutorsResponseBody = None,
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
            temp_model = OperateDesignateExecutorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateDisableJobsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_ids: List[int] = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # -\
        self.job_ids = job_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class OperateDisableJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # -\
        self.job_ids_shrink = job_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_ids_shrink is not None:
            result['JobIds'] = self.job_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobIds') is not None:
            self.job_ids_shrink = m.get('JobIds')
        return self


class OperateDisableJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateDisableJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateDisableJobsResponseBody = None,
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
            temp_model = OperateDisableJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateEnableJobsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_ids: List[int] = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # -\
        self.job_ids = job_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class OperateEnableJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # -\
        self.job_ids_shrink = job_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_ids_shrink is not None:
            result['JobIds'] = self.job_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobIds') is not None:
            self.job_ids_shrink = m.get('JobIds')
        return self


class OperateEnableJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateEnableJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateEnableJobsResponseBody = None,
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
            temp_model = OperateEnableJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateExecuteJobRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        instance_parameters: str = None,
        job_id: int = None,
        label: str = None,
        worker: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.instance_parameters = instance_parameters
        # This parameter is required.
        self.job_id = job_id
        self.label = label
        self.worker = worker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_parameters is not None:
            result['InstanceParameters'] = self.instance_parameters
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.label is not None:
            result['Label'] = self.label
        if self.worker is not None:
            result['Worker'] = self.worker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceParameters') is not None:
            self.instance_parameters = m.get('InstanceParameters')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Worker') is not None:
            self.worker = m.get('Worker')
        return self


class OperateExecuteJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_execution_id: str = None,
    ):
        self.job_execution_id = job_execution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        return self


class OperateExecuteJobResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: OperateExecuteJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = OperateExecuteJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateExecuteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateExecuteJobResponseBody = None,
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
            temp_model = OperateExecuteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateRerunJobRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        data_time: str = None,
        end_date: int = None,
        job_id: int = None,
        start_date: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.data_time = data_time
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class OperateRerunJobResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateRerunJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateRerunJobResponseBody = None,
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
            temp_model = OperateRerunJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateRetryJobExecutionRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_execution_id: str = None,
        task_list: List[str] = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_execution_id = job_execution_id
        self.task_list = task_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.task_list is not None:
            result['TaskList'] = self.task_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('TaskList') is not None:
            self.task_list = m.get('TaskList')
        return self


class OperateRetryJobExecutionShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_execution_id: str = None,
        task_list_shrink: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_execution_id = job_execution_id
        self.task_list_shrink = task_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.task_list_shrink is not None:
            result['TaskList'] = self.task_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('TaskList') is not None:
            self.task_list_shrink = m.get('TaskList')
        return self


class OperateRetryJobExecutionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateRetryJobExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateRetryJobExecutionResponseBody = None,
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
            temp_model = OperateRetryJobExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateStopJobExecutionRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_execution_id: str = None,
        task_list: List[str] = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_execution_id = job_execution_id
        self.task_list = task_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.task_list is not None:
            result['TaskList'] = self.task_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('TaskList') is not None:
            self.task_list = m.get('TaskList')
        return self


class OperateStopJobExecutionShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_execution_id: str = None,
        task_list_shrink: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_execution_id = job_execution_id
        self.task_list_shrink = task_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id
        if self.task_list_shrink is not None:
            result['TaskList'] = self.task_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')
        if m.get('TaskList') is not None:
            self.task_list_shrink = m.get('TaskList')
        return self


class OperateStopJobExecutionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateStopJobExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateStopJobExecutionResponseBody = None,
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
            temp_model = OperateStopJobExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        app_name: str = None,
        cluster_id: str = None,
        enable_log: bool = None,
        label_route_strategy: int = None,
        max_concurrency: int = None,
        title: str = None,
    ):
        self.access_token = access_token
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.enable_log = enable_log
        self.label_route_strategy = label_route_strategy
        self.max_concurrency = max_concurrency
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log
        if self.label_route_strategy is not None:
            result['LabelRouteStrategy'] = self.label_route_strategy
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')
        if m.get('LabelRouteStrategy') is not None:
            self.label_route_strategy = m.get('LabelRouteStrategy')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppResponseBody = None,
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
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class UpdateClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClusterResponseBody = None,
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
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateJobRequestNoticeConfig(TeaModel):
    def __init__(
        self,
        fail_enable: bool = None,
        fail_limit_times: int = None,
        miss_worker_enable: bool = None,
        send_channel: str = None,
        success_notice: bool = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        self.fail_enable = fail_enable
        self.fail_limit_times = fail_limit_times
        self.miss_worker_enable = miss_worker_enable
        self.send_channel = send_channel
        self.success_notice = success_notice
        self.timeout = timeout
        self.timeout_enable = timeout_enable
        self.timeout_kill_enable = timeout_kill_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable
        if self.fail_limit_times is not None:
            result['FailLimitTimes'] = self.fail_limit_times
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
        if self.success_notice is not None:
            result['SuccessNotice'] = self.success_notice
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable
        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')
        if m.get('FailLimitTimes') is not None:
            self.fail_limit_times = m.get('FailLimitTimes')
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('SuccessNotice') is not None:
            self.success_notice = m.get('SuccessNotice')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
        return self


class UpdateJobRequestNoticeContacts(TeaModel):
    def __init__(
        self,
        contact_type: int = None,
        name: str = None,
    ):
        self.contact_type = contact_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateJobRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        attempt_interval: int = None,
        calendar: str = None,
        child_job_id: str = None,
        cluster_id: str = None,
        description: str = None,
        executor_block_strategy: int = None,
        job_handler: str = None,
        job_id: int = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        name: str = None,
        notice_config: UpdateJobRequestNoticeConfig = None,
        notice_contacts: List[UpdateJobRequestNoticeContacts] = None,
        parameters: str = None,
        priority: int = None,
        route_strategy: int = None,
        script: str = None,
        start_time: int = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
        weight: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.child_job_id = child_job_id
        # This parameter is required.
        self.cluster_id = cluster_id
        self.description = description
        self.executor_block_strategy = executor_block_strategy
        self.job_handler = job_handler
        # This parameter is required.
        self.job_id = job_id
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        self.name = name
        self.notice_config = notice_config
        self.notice_contacts = notice_contacts
        self.parameters = parameters
        self.priority = priority
        self.route_strategy = route_strategy
        self.script = script
        self.start_time = start_time
        self.time_expression = time_expression
        self.time_type = time_type
        self.timezone = timezone
        self.weight = weight

    def validate(self):
        if self.notice_config:
            self.notice_config.validate()
        if self.notice_contacts:
            for k in self.notice_contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.child_job_id is not None:
            result['ChildJobId'] = self.child_job_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.executor_block_strategy is not None:
            result['ExecutorBlockStrategy'] = self.executor_block_strategy
        if self.job_handler is not None:
            result['JobHandler'] = self.job_handler
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.notice_config is not None:
            result['NoticeConfig'] = self.notice_config.to_map()
        result['NoticeContacts'] = []
        if self.notice_contacts is not None:
            for k in self.notice_contacts:
                result['NoticeContacts'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy
        if self.script is not None:
            result['Script'] = self.script
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ChildJobId') is not None:
            self.child_job_id = m.get('ChildJobId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutorBlockStrategy') is not None:
            self.executor_block_strategy = m.get('ExecutorBlockStrategy')
        if m.get('JobHandler') is not None:
            self.job_handler = m.get('JobHandler')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NoticeConfig') is not None:
            temp_model = UpdateJobRequestNoticeConfig()
            self.notice_config = temp_model.from_map(m['NoticeConfig'])
        self.notice_contacts = []
        if m.get('NoticeContacts') is not None:
            for k in m.get('NoticeContacts'):
                temp_model = UpdateJobRequestNoticeContacts()
                self.notice_contacts.append(temp_model.from_map(k))
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateJobShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        attempt_interval: int = None,
        calendar: str = None,
        child_job_id: str = None,
        cluster_id: str = None,
        description: str = None,
        executor_block_strategy: int = None,
        job_handler: str = None,
        job_id: int = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        name: str = None,
        notice_config_shrink: str = None,
        notice_contacts_shrink: str = None,
        parameters: str = None,
        priority: int = None,
        route_strategy: int = None,
        script: str = None,
        start_time: int = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
        weight: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.child_job_id = child_job_id
        # This parameter is required.
        self.cluster_id = cluster_id
        self.description = description
        self.executor_block_strategy = executor_block_strategy
        self.job_handler = job_handler
        # This parameter is required.
        self.job_id = job_id
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        self.name = name
        self.notice_config_shrink = notice_config_shrink
        self.notice_contacts_shrink = notice_contacts_shrink
        self.parameters = parameters
        self.priority = priority
        self.route_strategy = route_strategy
        self.script = script
        self.start_time = start_time
        self.time_expression = time_expression
        self.time_type = time_type
        self.timezone = timezone
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.child_job_id is not None:
            result['ChildJobId'] = self.child_job_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.executor_block_strategy is not None:
            result['ExecutorBlockStrategy'] = self.executor_block_strategy
        if self.job_handler is not None:
            result['JobHandler'] = self.job_handler
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.notice_config_shrink is not None:
            result['NoticeConfig'] = self.notice_config_shrink
        if self.notice_contacts_shrink is not None:
            result['NoticeContacts'] = self.notice_contacts_shrink
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy
        if self.script is not None:
            result['Script'] = self.script
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ChildJobId') is not None:
            self.child_job_id = m.get('ChildJobId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutorBlockStrategy') is not None:
            self.executor_block_strategy = m.get('ExecutorBlockStrategy')
        if m.get('JobHandler') is not None:
            self.job_handler = m.get('JobHandler')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NoticeConfig') is not None:
            self.notice_config_shrink = m.get('NoticeConfig')
        if m.get('NoticeContacts') is not None:
            self.notice_contacts_shrink = m.get('NoticeContacts')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateJobResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateJobResponseBody = None,
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
            temp_model = UpdateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateJobScriptRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_id: int = None,
        script_content: str = None,
        version_description: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_id = job_id
        self.script_content = script_content
        # This parameter is required.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.script_content is not None:
            result['ScriptContent'] = self.script_content
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        return self


class UpdateJobScriptResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateJobScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateJobScriptResponseBody = None,
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
            temp_model = UpdateJobScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


