# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AccessKeyGetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        user_id: int = None,
    ):
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AccessKeyGetResponseBody(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
        secret_key: str = None,
        success: bool = None,
        user_id: int = None,
    ):
        self.access_key = access_key
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.secret_key = secret_key
        self.success = success
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.success is not None:
            result['Success'] = self.success
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AccessKeyGetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AccessKeyGetResponseBody = None,
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
            temp_model = AccessKeyGetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMyGroupInstancesRequest(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        instances: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.group_id = group_id
        self.instances = instances
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instances is not None:
            result['Instances'] = self.instances
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddMyGroupInstancesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddMyGroupInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMyGroupInstancesResponseBody = None,
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
            temp_model = AddMyGroupInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmRequest(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        dry_run: bool = None,
        end_time: int = None,
        evaluation_count: int = None,
        metric_name: str = None,
        name: str = None,
        namespace: str = None,
        notify_type: int = None,
        period: int = None,
        region_id: str = None,
        silence_time: int = None,
        start_time: int = None,
        statistics: str = None,
        threshold: str = None,
        webhook: str = None,
    ):
        # This parameter is required.
        self.comparison_operator = comparison_operator
        self.contact_groups = contact_groups
        # This parameter is required.
        self.dimensions = dimensions
        self.dry_run = dry_run
        self.end_time = end_time
        self.evaluation_count = evaluation_count
        # This parameter is required.
        self.metric_name = metric_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.namespace = namespace
        self.notify_type = notify_type
        self.period = period
        self.region_id = region_id
        self.silence_time = silence_time
        self.start_time = start_time
        # This parameter is required.
        self.statistics = statistics
        # This parameter is required.
        self.threshold = threshold
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class CreateAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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


class CreateAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAlarmResponseBody = None,
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
            temp_model = CreateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHybridDoubleWriteRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        source_namespace: str = None,
        source_user_id: int = None,
        user_id: int = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.source_namespace = source_namespace
        # This parameter is required.
        self.source_user_id = source_user_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.source_namespace is not None:
            result['SourceNamespace'] = self.source_namespace
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SourceNamespace') is not None:
            self.source_namespace = m.get('SourceNamespace')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateHybridDoubleWriteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class CreateHybridDoubleWriteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHybridDoubleWriteResponseBody = None,
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
            temp_model = CreateHybridDoubleWriteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMonitoringTemplateRequest(TeaModel):
    def __init__(
        self,
        alert_templates_json: str = None,
        description: str = None,
        host_availability_template: str = None,
        name: str = None,
        namespace: str = None,
        process_monitor_templates: str = None,
        region_id: str = None,
        system_event_templates: str = None,
    ):
        # This parameter is required.
        self.alert_templates_json = alert_templates_json
        self.description = description
        self.host_availability_template = host_availability_template
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.namespace = namespace
        self.process_monitor_templates = process_monitor_templates
        self.region_id = region_id
        self.system_event_templates = system_event_templates

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_templates_json is not None:
            result['AlertTemplatesJson'] = self.alert_templates_json
        if self.description is not None:
            result['Description'] = self.description
        if self.host_availability_template is not None:
            result['HostAvailabilityTemplate'] = self.host_availability_template
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.process_monitor_templates is not None:
            result['ProcessMonitorTemplates'] = self.process_monitor_templates
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_event_templates is not None:
            result['SystemEventTemplates'] = self.system_event_templates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTemplatesJson') is not None:
            self.alert_templates_json = m.get('AlertTemplatesJson')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostAvailabilityTemplate') is not None:
            self.host_availability_template = m.get('HostAvailabilityTemplate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ProcessMonitorTemplates') is not None:
            self.process_monitor_templates = m.get('ProcessMonitorTemplates')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemEventTemplates') is not None:
            self.system_event_templates = m.get('SystemEventTemplates')
        return self


class CreateMonitoringTemplateResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.id = id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMonitoringTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMonitoringTemplateResponseBody = None,
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
            temp_model = CreateMonitoringTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMyGroupsRequest(TeaModel):
    def __init__(
        self,
        bind_url: str = None,
        contact_groups: str = None,
        group_name: str = None,
        options: str = None,
        region_id: str = None,
        service_id: int = None,
        type: str = None,
    ):
        self.bind_url = bind_url
        self.contact_groups = contact_groups
        self.group_name = group_name
        self.options = options
        self.region_id = region_id
        self.service_id = service_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_url is not None:
            result['BindUrl'] = self.bind_url
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.options is not None:
            result['Options'] = self.options
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrl') is not None:
            self.bind_url = m.get('BindUrl')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateMyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        group_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.group_id = group_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMyGroupsResponseBody = None,
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
            temp_model = CreateMyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        alert_ids: str = None,
        alert_rule: str = None,
        interval: str = None,
        interval_unit: str = None,
        isp_city: str = None,
        options: str = None,
        region_id: str = None,
        task_name: str = None,
        task_type: str = None,
        caller: str = None,
    ):
        # This parameter is required.
        self.address = address
        self.alert_ids = alert_ids
        self.alert_rule = alert_rule
        self.interval = interval
        self.interval_unit = interval_unit
        # This parameter is required.
        self.isp_city = isp_city
        self.options = options
        self.region_id = region_id
        # This parameter is required.
        self.task_name = task_name
        # 1.http
        # 2.ping
        # 3.tcp
        # 4.udp
        # 5.dns
        # 6.smtp
        # 7.pop3
        # 8.ftp
        # 
        # This parameter is required.
        self.task_type = task_type
        self.caller = caller

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.interval_unit is not None:
            result['IntervalUnit'] = self.interval_unit
        if self.isp_city is not None:
            result['IspCity'] = self.isp_city
        if self.options is not None:
            result['Options'] = self.options
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.caller is not None:
            result['caller'] = self.caller
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')
        if m.get('AlertRule') is not None:
            self.alert_rule = m.get('AlertRule')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IntervalUnit') is not None:
            self.interval_unit = m.get('IntervalUnit')
        if m.get('IspCity') is not None:
            self.isp_city = m.get('IspCity')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('caller') is not None:
            self.caller = m.get('caller')
        return self


class CreateTaskResponseBodyCreateResultListContact(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        task_name: str = None,
    ):
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateTaskResponseBodyCreateResultList(TeaModel):
    def __init__(
        self,
        contact: List[CreateTaskResponseBodyCreateResultListContact] = None,
    ):
        self.contact = contact

    def validate(self):
        if self.contact:
            for k in self.contact:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contact'] = []
        if self.contact is not None:
            for k in self.contact:
                result['Contact'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact = []
        if m.get('Contact') is not None:
            for k in m.get('Contact'):
                temp_model = CreateTaskResponseBodyCreateResultListContact()
                self.contact.append(temp_model.from_map(k))
        return self


class CreateTaskResponseBody(TeaModel):
    def __init__(
        self,
        alert_rule: str = None,
        code: str = None,
        create_result_list: CreateTaskResponseBodyCreateResultList = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.alert_rule = alert_rule
        self.code = code
        self.create_result_list = create_result_list
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.create_result_list:
            self.create_result_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule
        if self.code is not None:
            result['Code'] = self.code
        if self.create_result_list is not None:
            result['CreateResultList'] = self.create_result_list.to_map()
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
        if m.get('AlertRule') is not None:
            self.alert_rule = m.get('AlertRule')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateResultList') is not None:
            temp_model = CreateTaskResponseBodyCreateResultList()
            self.create_result_list = temp_model.from_map(m['CreateResultList'])
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskResponseBody = None,
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
            temp_model = CreateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class DeleteAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAlarmResponseBody = None,
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
            temp_model = DeleteAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomMetricRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        md_5: str = None,
        metric_name: str = None,
        region_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.group_id = group_id
        self.md_5 = md_5
        self.metric_name = metric_name
        self.region_id = region_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class DeleteCustomMetricResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteCustomMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomMetricResponseBody = None,
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
            temp_model = DeleteCustomMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHybridDoubleWriteRequest(TeaModel):
    def __init__(
        self,
        source_namespace: str = None,
        source_user_id: int = None,
    ):
        # This parameter is required.
        self.source_namespace = source_namespace
        # This parameter is required.
        self.source_user_id = source_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_namespace is not None:
            result['SourceNamespace'] = self.source_namespace
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceNamespace') is not None:
            self.source_namespace = m.get('SourceNamespace')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        return self


class DeleteHybridDoubleWriteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class DeleteHybridDoubleWriteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHybridDoubleWriteResponseBody = None,
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
            temp_model = DeleteHybridDoubleWriteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMetricRuleTargetsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        rule_id: str = None,
        target_ids: List[str] = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.rule_id = rule_id
        self.target_ids = target_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')
        return self


class DeleteMetricRuleTargetsResponseBodyFailIdsTargetIds(TeaModel):
    def __init__(
        self,
        target_id: List[str] = None,
    ):
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class DeleteMetricRuleTargetsResponseBodyFailIds(TeaModel):
    def __init__(
        self,
        target_ids: DeleteMetricRuleTargetsResponseBodyFailIdsTargetIds = None,
    ):
        self.target_ids = target_ids

    def validate(self):
        if self.target_ids:
            self.target_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetIds') is not None:
            temp_model = DeleteMetricRuleTargetsResponseBodyFailIdsTargetIds()
            self.target_ids = temp_model.from_map(m['TargetIds'])
        return self


class DeleteMetricRuleTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        fail_ids: DeleteMetricRuleTargetsResponseBodyFailIds = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.fail_ids = fail_ids
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.fail_ids:
            self.fail_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.fail_ids is not None:
            result['FailIds'] = self.fail_ids.to_map()
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
        if m.get('FailIds') is not None:
            temp_model = DeleteMetricRuleTargetsResponseBodyFailIds()
            self.fail_ids = temp_model.from_map(m['FailIds'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMetricRuleTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMetricRuleTargetsResponseBody = None,
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
            temp_model = DeleteMetricRuleTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMetricRulesRequest(TeaModel):
    def __init__(
        self,
        id: List[str] = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteMetricRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class DeleteMetricRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMetricRulesResponseBody = None,
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
            temp_model = DeleteMetricRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMyGroupInstancesRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        group_id: int = None,
        instance_id_list: str = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.group_id = group_id
        self.instance_id_list = instance_id_list
        self.instance_ids = instance_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteMyGroupInstancesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMyGroupInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMyGroupInstancesResponseBody = None,
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
            temp_model = DeleteMyGroupInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMyGroupsRequest(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteMyGroupsResponseBodyGroupContactGroupsContactGroup(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteMyGroupsResponseBodyGroupContactGroups(TeaModel):
    def __init__(
        self,
        contact_group: List[DeleteMyGroupsResponseBodyGroupContactGroupsContactGroup] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        if self.contact_group:
            for k in self.contact_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactGroup'] = []
        if self.contact_group is not None:
            for k in self.contact_group:
                result['ContactGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_group = []
        if m.get('ContactGroup') is not None:
            for k in m.get('ContactGroup'):
                temp_model = DeleteMyGroupsResponseBodyGroupContactGroupsContactGroup()
                self.contact_group.append(temp_model.from_map(k))
        return self


class DeleteMyGroupsResponseBodyGroup(TeaModel):
    def __init__(
        self,
        bind_urls: str = None,
        contact_groups: DeleteMyGroupsResponseBodyGroupContactGroups = None,
        group_id: int = None,
        group_name: str = None,
        service_id: str = None,
        type: str = None,
    ):
        self.bind_urls = bind_urls
        self.contact_groups = contact_groups
        self.group_id = group_id
        self.group_name = group_name
        self.service_id = service_id
        self.type = type

    def validate(self):
        if self.contact_groups:
            self.contact_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_urls is not None:
            result['BindUrls'] = self.bind_urls
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrls') is not None:
            self.bind_urls = m.get('BindUrls')
        if m.get('ContactGroups') is not None:
            temp_model = DeleteMyGroupsResponseBodyGroupContactGroups()
            self.contact_groups = temp_model.from_map(m['ContactGroups'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteMyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        group: DeleteMyGroupsResponseBodyGroup = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.group = group
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Group') is not None:
            temp_model = DeleteMyGroupsResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMyGroupsResponseBody = None,
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
            temp_model = DeleteMyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTasksRequest(TeaModel):
    def __init__(
        self,
        is_delete_alarms: int = None,
        region_id: str = None,
        task_ids: str = None,
    ):
        self.is_delete_alarms = is_delete_alarms
        self.region_id = region_id
        # This parameter is required.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_delete_alarms is not None:
            result['IsDeleteAlarms'] = self.is_delete_alarms
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDeleteAlarms') is not None:
            self.is_delete_alarms = m.get('IsDeleteAlarms')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class DeleteTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class DeleteTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTasksResponseBody = None,
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
            temp_model = DeleteTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmHistoryRequest(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        ascending: bool = None,
        end_time: str = None,
        group_id: str = None,
        metric_name: str = None,
        namespace: str = None,
        only_count: bool = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        rule_name: str = None,
        start_time: str = None,
        state: str = None,
        status: str = None,
    ):
        self.alert_name = alert_name
        self.ascending = ascending
        self.end_time = end_time
        self.group_id = group_id
        self.metric_name = metric_name
        self.namespace = namespace
        self.only_count = only_count
        self.page = page
        self.page_size = page_size
        self.region_id = region_id
        self.rule_name = rule_name
        self.start_time = start_time
        self.state = state
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.ascending is not None:
            result['Ascending'] = self.ascending
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.only_count is not None:
            result['OnlyCount'] = self.only_count
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Ascending') is not None:
            self.ascending = m.get('Ascending')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OnlyCount') is not None:
            self.only_count = m.get('OnlyCount')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs(TeaModel):
    def __init__(
        self,
        contact_aliim: List[str] = None,
    ):
        self.contact_aliim = contact_aliim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_aliim is not None:
            result['ContactALIIM'] = self.contact_aliim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactALIIM') is not None:
            self.contact_aliim = m.get('ContactALIIM')
        return self


class DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactGroups(TeaModel):
    def __init__(
        self,
        contact_group: List[str] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')
        return self


class DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactMails(TeaModel):
    def __init__(
        self,
        contact_mail: List[str] = None,
    ):
        self.contact_mail = contact_mail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')
        return self


class DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactSmses(TeaModel):
    def __init__(
        self,
        contact_sms: List[str] = None,
    ):
        self.contact_sms = contact_sms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_sms is not None:
            result['ContactSms'] = self.contact_sms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactSms') is not None:
            self.contact_sms = m.get('ContactSms')
        return self


class DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContacts(TeaModel):
    def __init__(
        self,
        contact: List[str] = None,
    ):
        self.contact = contact

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['Contact'] = self.contact
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        return self


class DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistory(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_time: int = None,
        contact_aliims: DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs = None,
        contact_groups: DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactGroups = None,
        contact_mails: DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactMails = None,
        contact_smses: DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactSmses = None,
        contacts: DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContacts = None,
        dimensions: str = None,
        evaluation_count: int = None,
        expression: str = None,
        group_id: str = None,
        id: str = None,
        instance_name: str = None,
        last_time: int = None,
        level: str = None,
        metric_name: str = None,
        namespace: str = None,
        pre_level: str = None,
        rule_name: str = None,
        state: str = None,
        status: int = None,
        user_id: str = None,
        value: str = None,
        webhooks: str = None,
    ):
        self.alert_name = alert_name
        self.alert_time = alert_time
        self.contact_aliims = contact_aliims
        self.contact_groups = contact_groups
        self.contact_mails = contact_mails
        self.contact_smses = contact_smses
        self.contacts = contacts
        self.dimensions = dimensions
        self.evaluation_count = evaluation_count
        self.expression = expression
        self.group_id = group_id
        self.id = id
        self.instance_name = instance_name
        self.last_time = last_time
        self.level = level
        self.metric_name = metric_name
        self.namespace = namespace
        self.pre_level = pre_level
        self.rule_name = rule_name
        self.state = state
        self.status = status
        self.user_id = user_id
        self.value = value
        self.webhooks = webhooks

    def validate(self):
        if self.contact_aliims:
            self.contact_aliims.validate()
        if self.contact_groups:
            self.contact_groups.validate()
        if self.contact_mails:
            self.contact_mails.validate()
        if self.contact_smses:
            self.contact_smses.validate()
        if self.contacts:
            self.contacts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.contact_aliims is not None:
            result['ContactALIIMs'] = self.contact_aliims.to_map()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()
        if self.contact_mails is not None:
            result['ContactMails'] = self.contact_mails.to_map()
        if self.contact_smses is not None:
            result['ContactSmses'] = self.contact_smses.to_map()
        if self.contacts is not None:
            result['Contacts'] = self.contacts.to_map()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.level is not None:
            result['Level'] = self.level
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.pre_level is not None:
            result['PreLevel'] = self.pre_level
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.value is not None:
            result['Value'] = self.value
        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('ContactALIIMs') is not None:
            temp_model = DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs()
            self.contact_aliims = temp_model.from_map(m['ContactALIIMs'])
        if m.get('ContactGroups') is not None:
            temp_model = DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactGroups()
            self.contact_groups = temp_model.from_map(m['ContactGroups'])
        if m.get('ContactMails') is not None:
            temp_model = DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactMails()
            self.contact_mails = temp_model.from_map(m['ContactMails'])
        if m.get('ContactSmses') is not None:
            temp_model = DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContactSmses()
            self.contact_smses = temp_model.from_map(m['ContactSmses'])
        if m.get('Contacts') is not None:
            temp_model = DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistoryContacts()
            self.contacts = temp_model.from_map(m['Contacts'])
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PreLevel') is not None:
            self.pre_level = m.get('PreLevel')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')
        return self


class DescribeAlarmHistoryResponseBodyAlarmHistoryList(TeaModel):
    def __init__(
        self,
        alarm_history: List[DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistory] = None,
    ):
        self.alarm_history = alarm_history

    def validate(self):
        if self.alarm_history:
            for k in self.alarm_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmHistory'] = []
        if self.alarm_history is not None:
            for k in self.alarm_history:
                result['AlarmHistory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_history = []
        if m.get('AlarmHistory') is not None:
            for k in m.get('AlarmHistory'):
                temp_model = DescribeAlarmHistoryResponseBodyAlarmHistoryListAlarmHistory()
                self.alarm_history.append(temp_model.from_map(k))
        return self


class DescribeAlarmHistoryResponseBody(TeaModel):
    def __init__(
        self,
        alarm_history_list: DescribeAlarmHistoryResponseBodyAlarmHistoryList = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: str = None,
    ):
        self.alarm_history_list = alarm_history_list
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.alarm_history_list:
            self.alarm_history_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_history_list is not None:
            result['AlarmHistoryList'] = self.alarm_history_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmHistoryList') is not None:
            temp_model = DescribeAlarmHistoryResponseBodyAlarmHistoryList()
            self.alarm_history_list = temp_model.from_map(m['AlarmHistoryList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAlarmHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlarmHistoryResponseBody = None,
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
            temp_model = DescribeAlarmHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmsRequest(TeaModel):
    def __init__(
        self,
        alert_state: str = None,
        display_name: str = None,
        enable_state: bool = None,
        group_by: str = None,
        group_id: str = None,
        metric_name: str = None,
        name_keyword: str = None,
        names: str = None,
        namespace: str = None,
        page: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.alert_state = alert_state
        self.display_name = display_name
        self.enable_state = enable_state
        self.group_by = group_by
        self.group_id = group_id
        self.metric_name = metric_name
        self.name_keyword = name_keyword
        self.names = names
        self.namespace = namespace
        self.page = page
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.enable_state is not None:
            result['EnableState'] = self.enable_state
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.name_keyword is not None:
            result['NameKeyword'] = self.name_keyword
        if self.names is not None:
            result['Names'] = self.names
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('NameKeyword') is not None:
            self.name_keyword = m.get('NameKeyword')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlarmsResponseBodyDatapointsAlarmEscalationsCritical(TeaModel):
    def __init__(
        self,
        alert_sensitivity: str = None,
        comparison_operator: str = None,
        history_data_range: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.alert_sensitivity = alert_sensitivity
        self.comparison_operator = comparison_operator
        self.history_data_range = history_data_range
        self.pre_condition = pre_condition
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_sensitivity is not None:
            result['AlertSensitivity'] = self.alert_sensitivity
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.history_data_range is not None:
            result['HistoryDataRange'] = self.history_data_range
        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSensitivity') is not None:
            self.alert_sensitivity = m.get('AlertSensitivity')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('HistoryDataRange') is not None:
            self.history_data_range = m.get('HistoryDataRange')
        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeAlarmsResponseBodyDatapointsAlarmEscalationsInfo(TeaModel):
    def __init__(
        self,
        alert_sensitivity: str = None,
        comparison_operator: str = None,
        history_data_range: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.alert_sensitivity = alert_sensitivity
        self.comparison_operator = comparison_operator
        self.history_data_range = history_data_range
        self.pre_condition = pre_condition
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_sensitivity is not None:
            result['AlertSensitivity'] = self.alert_sensitivity
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.history_data_range is not None:
            result['HistoryDataRange'] = self.history_data_range
        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSensitivity') is not None:
            self.alert_sensitivity = m.get('AlertSensitivity')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('HistoryDataRange') is not None:
            self.history_data_range = m.get('HistoryDataRange')
        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeAlarmsResponseBodyDatapointsAlarmEscalationsWarn(TeaModel):
    def __init__(
        self,
        alert_sensitivity: str = None,
        comparison_operator: str = None,
        history_data_range: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.alert_sensitivity = alert_sensitivity
        self.comparison_operator = comparison_operator
        self.history_data_range = history_data_range
        self.pre_condition = pre_condition
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_sensitivity is not None:
            result['AlertSensitivity'] = self.alert_sensitivity
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.history_data_range is not None:
            result['HistoryDataRange'] = self.history_data_range
        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSensitivity') is not None:
            self.alert_sensitivity = m.get('AlertSensitivity')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('HistoryDataRange') is not None:
            self.history_data_range = m.get('HistoryDataRange')
        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeAlarmsResponseBodyDatapointsAlarmEscalations(TeaModel):
    def __init__(
        self,
        critical: DescribeAlarmsResponseBodyDatapointsAlarmEscalationsCritical = None,
        info: DescribeAlarmsResponseBodyDatapointsAlarmEscalationsInfo = None,
        warn: DescribeAlarmsResponseBodyDatapointsAlarmEscalationsWarn = None,
    ):
        self.critical = critical
        self.info = info
        self.warn = warn

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.info:
            self.info.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()
        if self.info is not None:
            result['Info'] = self.info.to_map()
        if self.warn is not None:
            result['Warn'] = self.warn.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = DescribeAlarmsResponseBodyDatapointsAlarmEscalationsCritical()
            self.critical = temp_model.from_map(m['Critical'])
        if m.get('Info') is not None:
            temp_model = DescribeAlarmsResponseBodyDatapointsAlarmEscalationsInfo()
            self.info = temp_model.from_map(m['Info'])
        if m.get('Warn') is not None:
            temp_model = DescribeAlarmsResponseBodyDatapointsAlarmEscalationsWarn()
            self.warn = temp_model.from_map(m['Warn'])
        return self


class DescribeAlarmsResponseBodyDatapointsAlarm(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        display_name: str = None,
        effective_interval: str = None,
        enable: bool = None,
        escalations: DescribeAlarmsResponseBodyDatapointsAlarmEscalations = None,
        evaluation_count: str = None,
        group_id: str = None,
        group_name: str = None,
        level: str = None,
        metric_name: str = None,
        name: str = None,
        namespace: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        rule_name: str = None,
        rule_type: str = None,
        silence_time: str = None,
        state: str = None,
        statistics: str = None,
        subject: str = None,
        threshold: str = None,
        uuid: str = None,
        webhook: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.contact_groups = contact_groups
        self.dimensions = dimensions
        self.display_name = display_name
        self.effective_interval = effective_interval
        self.enable = enable
        self.escalations = escalations
        self.evaluation_count = evaluation_count
        self.group_id = group_id
        self.group_name = group_name
        self.level = level
        self.metric_name = metric_name
        self.name = name
        self.namespace = namespace
        self.no_effective_interval = no_effective_interval
        self.period = period
        self.resources = resources
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.silence_time = silence_time
        self.state = state
        self.statistics = statistics
        self.subject = subject
        self.threshold = threshold
        self.uuid = uuid
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.level is not None:
            result['Level'] = self.level
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval
        if self.period is not None:
            result['Period'] = self.period
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.state is not None:
            result['State'] = self.state
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Escalations') is not None:
            temp_model = DescribeAlarmsResponseBodyDatapointsAlarmEscalations()
            self.escalations = temp_model.from_map(m['Escalations'])
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class DescribeAlarmsResponseBodyDatapoints(TeaModel):
    def __init__(
        self,
        alarm: List[DescribeAlarmsResponseBodyDatapointsAlarm] = None,
    ):
        self.alarm = alarm

    def validate(self):
        if self.alarm:
            for k in self.alarm:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarm'] = []
        if self.alarm is not None:
            for k in self.alarm:
                result['Alarm'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm = []
        if m.get('Alarm') is not None:
            for k in m.get('Alarm'):
                temp_model = DescribeAlarmsResponseBodyDatapointsAlarm()
                self.alarm.append(temp_model.from_map(k))
        return self


class DescribeAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        datapoints: DescribeAlarmsResponseBodyDatapoints = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.datapoints = datapoints
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total
        self.trace_id = trace_id

    def validate(self):
        if self.datapoints:
            self.datapoints.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Datapoints') is not None:
            temp_model = DescribeAlarmsResponseBodyDatapoints()
            self.datapoints = temp_model.from_map(m['Datapoints'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlarmsResponseBody = None,
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
            temp_model = DescribeAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmsForResourcesRequest(TeaModel):
    def __init__(
        self,
        alert_state: str = None,
        dimensions: str = None,
        enable_state: bool = None,
        group_id: str = None,
        metric_name: str = None,
        namespace: str = None,
        page: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.alert_state = alert_state
        # This parameter is required.
        self.dimensions = dimensions
        self.enable_state = enable_state
        self.group_id = group_id
        self.metric_name = metric_name
        # This parameter is required.
        self.namespace = namespace
        self.page = page
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.enable_state is not None:
            result['EnableState'] = self.enable_state
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsCritical(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsInfo(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsWarn(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalations(TeaModel):
    def __init__(
        self,
        critical: DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsCritical = None,
        info: DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsInfo = None,
        warn: DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsWarn = None,
    ):
        self.critical = critical
        self.info = info
        self.warn = warn

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.info:
            self.info.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()
        if self.info is not None:
            result['Info'] = self.info.to_map()
        if self.warn is not None:
            result['Warn'] = self.warn.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsCritical()
            self.critical = temp_model.from_map(m['Critical'])
        if m.get('Info') is not None:
            temp_model = DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsInfo()
            self.info = temp_model.from_map(m['Info'])
        if m.get('Warn') is not None:
            temp_model = DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalationsWarn()
            self.warn = temp_model.from_map(m['Warn'])
        return self


class DescribeAlarmsForResourcesResponseBodyDatapointsAlarm(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        contact_groups: str = None,
        display_name: str = None,
        effective_interval: str = None,
        enable: bool = None,
        escalations: DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalations = None,
        evaluation_count: str = None,
        group_id: str = None,
        group_name: str = None,
        level: str = None,
        metric_name: str = None,
        name: str = None,
        namespace: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        silence_time: str = None,
        state: str = None,
        statistics: str = None,
        subject: str = None,
        threshold: str = None,
        uuid: str = None,
        webhook: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.contact_groups = contact_groups
        self.display_name = display_name
        self.effective_interval = effective_interval
        self.enable = enable
        self.escalations = escalations
        self.evaluation_count = evaluation_count
        self.group_id = group_id
        self.group_name = group_name
        self.level = level
        self.metric_name = metric_name
        self.name = name
        self.namespace = namespace
        self.no_effective_interval = no_effective_interval
        self.period = period
        self.resources = resources
        self.silence_time = silence_time
        self.state = state
        self.statistics = statistics
        self.subject = subject
        self.threshold = threshold
        self.uuid = uuid
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.level is not None:
            result['Level'] = self.level
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval
        if self.period is not None:
            result['Period'] = self.period
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.state is not None:
            result['State'] = self.state
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Escalations') is not None:
            temp_model = DescribeAlarmsForResourcesResponseBodyDatapointsAlarmEscalations()
            self.escalations = temp_model.from_map(m['Escalations'])
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class DescribeAlarmsForResourcesResponseBodyDatapoints(TeaModel):
    def __init__(
        self,
        alarm: List[DescribeAlarmsForResourcesResponseBodyDatapointsAlarm] = None,
    ):
        self.alarm = alarm

    def validate(self):
        if self.alarm:
            for k in self.alarm:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarm'] = []
        if self.alarm is not None:
            for k in self.alarm:
                result['Alarm'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm = []
        if m.get('Alarm') is not None:
            for k in m.get('Alarm'):
                temp_model = DescribeAlarmsForResourcesResponseBodyDatapointsAlarm()
                self.alarm.append(temp_model.from_map(k))
        return self


class DescribeAlarmsForResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        datapoints: DescribeAlarmsForResourcesResponseBodyDatapoints = None,
        dimensions: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.datapoints = datapoints
        self.dimensions = dimensions
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total
        self.trace_id = trace_id

    def validate(self):
        if self.datapoints:
            self.datapoints.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints.to_map()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Datapoints') is not None:
            temp_model = DescribeAlarmsForResourcesResponseBodyDatapoints()
            self.datapoints = temp_model.from_map(m['Datapoints'])
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeAlarmsForResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlarmsForResourcesResponseBody = None,
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
            temp_model = DescribeAlarmsForResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertHistoryListRequest(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        ascending: bool = None,
        end_time: str = None,
        group_id: str = None,
        metric_name: str = None,
        namespace: str = None,
        only_count: bool = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        rule_name: str = None,
        start_time: str = None,
        state: str = None,
        status: str = None,
    ):
        self.alert_name = alert_name
        self.ascending = ascending
        self.end_time = end_time
        self.group_id = group_id
        self.metric_name = metric_name
        self.namespace = namespace
        self.only_count = only_count
        self.page = page
        self.page_size = page_size
        self.region_id = region_id
        self.rule_name = rule_name
        self.start_time = start_time
        self.state = state
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.ascending is not None:
            result['Ascending'] = self.ascending
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.only_count is not None:
            result['OnlyCount'] = self.only_count
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Ascending') is not None:
            self.ascending = m.get('Ascending')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OnlyCount') is not None:
            self.only_count = m.get('OnlyCount')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs(TeaModel):
    def __init__(
        self,
        contact_aliim: List[str] = None,
    ):
        self.contact_aliim = contact_aliim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_aliim is not None:
            result['ContactALIIM'] = self.contact_aliim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactALIIM') is not None:
            self.contact_aliim = m.get('ContactALIIM')
        return self


class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactGroups(TeaModel):
    def __init__(
        self,
        contact_group: List[str] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')
        return self


class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactMails(TeaModel):
    def __init__(
        self,
        contact_mail: List[str] = None,
    ):
        self.contact_mail = contact_mail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')
        return self


class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactSmses(TeaModel):
    def __init__(
        self,
        contact_sms: List[str] = None,
    ):
        self.contact_sms = contact_sms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_sms is not None:
            result['ContactSms'] = self.contact_sms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactSms') is not None:
            self.contact_sms = m.get('ContactSms')
        return self


class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContacts(TeaModel):
    def __init__(
        self,
        contact: List[str] = None,
    ):
        self.contact = contact

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['Contact'] = self.contact
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        return self


class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistory(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_time: int = None,
        contact_aliims: DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs = None,
        contact_groups: DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactGroups = None,
        contact_mails: DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactMails = None,
        contact_smses: DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactSmses = None,
        contacts: DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContacts = None,
        dimensions: str = None,
        evaluation_count: int = None,
        expression: str = None,
        group_id: str = None,
        id: str = None,
        instance_name: str = None,
        last_time: int = None,
        level: str = None,
        metric_name: str = None,
        namespace: str = None,
        pre_level: str = None,
        rule_name: str = None,
        state: str = None,
        status: int = None,
        user_id: str = None,
        value: str = None,
        webhooks: str = None,
    ):
        self.alert_name = alert_name
        self.alert_time = alert_time
        self.contact_aliims = contact_aliims
        self.contact_groups = contact_groups
        self.contact_mails = contact_mails
        self.contact_smses = contact_smses
        self.contacts = contacts
        self.dimensions = dimensions
        self.evaluation_count = evaluation_count
        self.expression = expression
        self.group_id = group_id
        self.id = id
        self.instance_name = instance_name
        self.last_time = last_time
        self.level = level
        self.metric_name = metric_name
        self.namespace = namespace
        self.pre_level = pre_level
        self.rule_name = rule_name
        self.state = state
        self.status = status
        self.user_id = user_id
        self.value = value
        self.webhooks = webhooks

    def validate(self):
        if self.contact_aliims:
            self.contact_aliims.validate()
        if self.contact_groups:
            self.contact_groups.validate()
        if self.contact_mails:
            self.contact_mails.validate()
        if self.contact_smses:
            self.contact_smses.validate()
        if self.contacts:
            self.contacts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.contact_aliims is not None:
            result['ContactALIIMs'] = self.contact_aliims.to_map()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()
        if self.contact_mails is not None:
            result['ContactMails'] = self.contact_mails.to_map()
        if self.contact_smses is not None:
            result['ContactSmses'] = self.contact_smses.to_map()
        if self.contacts is not None:
            result['Contacts'] = self.contacts.to_map()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.level is not None:
            result['Level'] = self.level
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.pre_level is not None:
            result['PreLevel'] = self.pre_level
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.value is not None:
            result['Value'] = self.value
        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('ContactALIIMs') is not None:
            temp_model = DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs()
            self.contact_aliims = temp_model.from_map(m['ContactALIIMs'])
        if m.get('ContactGroups') is not None:
            temp_model = DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactGroups()
            self.contact_groups = temp_model.from_map(m['ContactGroups'])
        if m.get('ContactMails') is not None:
            temp_model = DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactMails()
            self.contact_mails = temp_model.from_map(m['ContactMails'])
        if m.get('ContactSmses') is not None:
            temp_model = DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactSmses()
            self.contact_smses = temp_model.from_map(m['ContactSmses'])
        if m.get('Contacts') is not None:
            temp_model = DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContacts()
            self.contacts = temp_model.from_map(m['Contacts'])
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PreLevel') is not None:
            self.pre_level = m.get('PreLevel')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')
        return self


class DescribeAlertHistoryListResponseBodyAlarmHistoryList(TeaModel):
    def __init__(
        self,
        alarm_history: List[DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistory] = None,
    ):
        self.alarm_history = alarm_history

    def validate(self):
        if self.alarm_history:
            for k in self.alarm_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmHistory'] = []
        if self.alarm_history is not None:
            for k in self.alarm_history:
                result['AlarmHistory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_history = []
        if m.get('AlarmHistory') is not None:
            for k in m.get('AlarmHistory'):
                temp_model = DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistory()
                self.alarm_history.append(temp_model.from_map(k))
        return self


class DescribeAlertHistoryListResponseBody(TeaModel):
    def __init__(
        self,
        alarm_history_list: DescribeAlertHistoryListResponseBodyAlarmHistoryList = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: str = None,
    ):
        self.alarm_history_list = alarm_history_list
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.alarm_history_list:
            self.alarm_history_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_history_list is not None:
            result['AlarmHistoryList'] = self.alarm_history_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmHistoryList') is not None:
            temp_model = DescribeAlertHistoryListResponseBodyAlarmHistoryList()
            self.alarm_history_list = temp_model.from_map(m['AlarmHistoryList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAlertHistoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertHistoryListResponseBody = None,
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
            temp_model = DescribeAlertHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContactRequest(TeaModel):
    def __init__(
        self,
        contact_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.contact_name = contact_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeContactResponseBodyDatapointsChannelsChannel(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeContactResponseBodyDatapointsChannels(TeaModel):
    def __init__(
        self,
        channel: List[DescribeContactResponseBodyDatapointsChannelsChannel] = None,
    ):
        self.channel = channel

    def validate(self):
        if self.channel:
            for k in self.channel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Channel'] = []
        if self.channel is not None:
            for k in self.channel:
                result['Channel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel = []
        if m.get('Channel') is not None:
            for k in m.get('Channel'):
                temp_model = DescribeContactResponseBodyDatapointsChannelsChannel()
                self.channel.append(temp_model.from_map(k))
        return self


class DescribeContactResponseBodyDatapoints(TeaModel):
    def __init__(
        self,
        channels: DescribeContactResponseBodyDatapointsChannels = None,
        name: str = None,
    ):
        self.channels = channels
        self.name = name

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = DescribeContactResponseBodyDatapointsChannels()
            self.channels = temp_model.from_map(m['Channels'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContactResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        datapoints: DescribeContactResponseBodyDatapoints = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.datapoints = datapoints
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.datapoints:
            self.datapoints.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints.to_map()
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
        if m.get('Datapoints') is not None:
            temp_model = DescribeContactResponseBodyDatapoints()
            self.datapoints = temp_model.from_map(m['Datapoints'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContactResponseBody = None,
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
            temp_model = DescribeContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHybridDoubleWriteRequest(TeaModel):
    def __init__(
        self,
        source_namespace: str = None,
        source_user_id: str = None,
        target_namespace: str = None,
        target_user_id: str = None,
    ):
        self.source_namespace = source_namespace
        self.source_user_id = source_user_id
        self.target_namespace = target_namespace
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_namespace is not None:
            result['SourceNamespace'] = self.source_namespace
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.target_namespace is not None:
            result['TargetNamespace'] = self.target_namespace
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceNamespace') is not None:
            self.source_namespace = m.get('SourceNamespace')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('TargetNamespace') is not None:
            self.target_namespace = m.get('TargetNamespace')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        return self


class DescribeHybridDoubleWriteResponseBodyResult(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        source_namespace: str = None,
        source_user_id: int = None,
        user_id: int = None,
    ):
        self.namespace = namespace
        self.source_namespace = source_namespace
        self.source_user_id = source_user_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.source_namespace is not None:
            result['SourceNamespace'] = self.source_namespace
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SourceNamespace') is not None:
            self.source_namespace = m.get('SourceNamespace')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeHybridDoubleWriteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[DescribeHybridDoubleWriteResponseBodyResult] = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeHybridDoubleWriteResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHybridDoubleWriteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHybridDoubleWriteResponseBody = None,
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
            temp_model = DescribeHybridDoubleWriteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeISPAreaCityRequest(TeaModel):
    def __init__(
        self,
        city: str = None,
        isp: str = None,
    ):
        self.city = city
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeISPAreaCityResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class DescribeISPAreaCityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeISPAreaCityResponseBody = None,
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
            temp_model = DescribeISPAreaCityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMetricRuleListRequest(TeaModel):
    def __init__(
        self,
        alert_state: str = None,
        dimensions: str = None,
        enable_state: bool = None,
        group_id: str = None,
        metric_name: str = None,
        namespace: str = None,
        page: str = None,
        page_size: str = None,
        region_id: str = None,
        rule_ids: str = None,
        rule_name: str = None,
    ):
        self.alert_state = alert_state
        self.dimensions = dimensions
        self.enable_state = enable_state
        self.group_id = group_id
        self.metric_name = metric_name
        self.namespace = namespace
        self.page = page
        self.page_size = page_size
        self.region_id = region_id
        self.rule_ids = rule_ids
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.enable_state is not None:
            result['EnableState'] = self.enable_state
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsCritical(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsInfo(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsWarn(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class DescribeMetricRuleListResponseBodyAlarmsAlarmEscalations(TeaModel):
    def __init__(
        self,
        critical: DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsCritical = None,
        info: DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsInfo = None,
        warn: DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsWarn = None,
    ):
        self.critical = critical
        self.info = info
        self.warn = warn

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.info:
            self.info.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()
        if self.info is not None:
            result['Info'] = self.info.to_map()
        if self.warn is not None:
            result['Warn'] = self.warn.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsCritical()
            self.critical = temp_model.from_map(m['Critical'])
        if m.get('Info') is not None:
            temp_model = DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsInfo()
            self.info = temp_model.from_map(m['Info'])
        if m.get('Warn') is not None:
            temp_model = DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsWarn()
            self.warn = temp_model.from_map(m['Warn'])
        return self


class DescribeMetricRuleListResponseBodyAlarmsAlarm(TeaModel):
    def __init__(
        self,
        alert_state: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        effective_interval: str = None,
        enable_state: bool = None,
        escalations: DescribeMetricRuleListResponseBodyAlarmsAlarmEscalations = None,
        group_id: str = None,
        group_name: str = None,
        mail_subject: str = None,
        metric_name: str = None,
        namespace: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: str = None,
        source_type: str = None,
        webhook: str = None,
    ):
        self.alert_state = alert_state
        self.contact_groups = contact_groups
        self.dimensions = dimensions
        self.effective_interval = effective_interval
        self.enable_state = enable_state
        self.escalations = escalations
        self.group_id = group_id
        self.group_name = group_name
        self.mail_subject = mail_subject
        self.metric_name = metric_name
        self.namespace = namespace
        self.no_effective_interval = no_effective_interval
        self.period = period
        self.resources = resources
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.silence_time = silence_time
        self.source_type = source_type
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval
        if self.enable_state is not None:
            result['EnableState'] = self.enable_state
        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.mail_subject is not None:
            result['MailSubject'] = self.mail_subject
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval
        if self.period is not None:
            result['Period'] = self.period
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')
        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')
        if m.get('Escalations') is not None:
            temp_model = DescribeMetricRuleListResponseBodyAlarmsAlarmEscalations()
            self.escalations = temp_model.from_map(m['Escalations'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('MailSubject') is not None:
            self.mail_subject = m.get('MailSubject')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class DescribeMetricRuleListResponseBodyAlarms(TeaModel):
    def __init__(
        self,
        alarm: List[DescribeMetricRuleListResponseBodyAlarmsAlarm] = None,
    ):
        self.alarm = alarm

    def validate(self):
        if self.alarm:
            for k in self.alarm:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarm'] = []
        if self.alarm is not None:
            for k in self.alarm:
                result['Alarm'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm = []
        if m.get('Alarm') is not None:
            for k in m.get('Alarm'):
                temp_model = DescribeMetricRuleListResponseBodyAlarmsAlarm()
                self.alarm.append(temp_model.from_map(k))
        return self


class DescribeMetricRuleListResponseBody(TeaModel):
    def __init__(
        self,
        alarms: DescribeMetricRuleListResponseBodyAlarms = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: str = None,
    ):
        self.alarms = alarms
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.alarms:
            self.alarms.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarms is not None:
            result['Alarms'] = self.alarms.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarms') is not None:
            temp_model = DescribeMetricRuleListResponseBodyAlarms()
            self.alarms = temp_model.from_map(m['Alarms'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeMetricRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMetricRuleListResponseBody = None,
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
            temp_model = DescribeMetricRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskDetailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class DescribeTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskDetailResponseBody = None,
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
            temp_model = DescribeTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.keyword = keyword
        self.page = page
        self.page_size = page_size
        self.region_id = region_id
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
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
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTasksResponseBody = None,
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
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAlarmRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class DisableAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAlarmResponseBody = None,
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
            temp_model = DisableAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAlarmRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class EnableAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAlarmResponseBody = None,
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
            temp_model = EnableAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContactsRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetContactsResponseBodyDatapointsContacts(TeaModel):
    def __init__(
        self,
        contact: List[str] = None,
    ):
        self.contact = contact

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['Contact'] = self.contact
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        return self


class GetContactsResponseBodyDatapoints(TeaModel):
    def __init__(
        self,
        contacts: GetContactsResponseBodyDatapointsContacts = None,
        name: str = None,
    ):
        self.contacts = contacts
        self.name = name

    def validate(self):
        if self.contacts:
            self.contacts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contacts is not None:
            result['Contacts'] = self.contacts.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contacts') is not None:
            temp_model = GetContactsResponseBodyDatapointsContacts()
            self.contacts = temp_model.from_map(m['Contacts'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetContactsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        datapoints: GetContactsResponseBodyDatapoints = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.datapoints = datapoints
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.datapoints:
            self.datapoints.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Datapoints') is not None:
            temp_model = GetContactsResponseBodyDatapoints()
            self.datapoints = temp_model.from_map(m['Datapoints'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetContactsResponseBody = None,
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
            temp_model = GetContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLineSplitResultRequest(TeaModel):
    def __init__(
        self,
        line: str = None,
        prefix: str = None,
        regex: str = None,
        select_content: str = None,
        split_type: str = None,
    ):
        self.line = line
        self.prefix = prefix
        self.regex = regex
        self.select_content = select_content
        self.split_type = split_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.select_content is not None:
            result['SelectContent'] = self.select_content
        if self.split_type is not None:
            result['SplitType'] = self.split_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('SelectContent') is not None:
            self.select_content = m.get('SelectContent')
        if m.get('SplitType') is not None:
            self.split_type = m.get('SplitType')
        return self


class GetLineSplitResultResponseBodyResource(TeaModel):
    def __init__(
        self,
        additional_regex: str = None,
        end_split_symbol: str = None,
        regex: str = None,
        regex_split_result: List[str] = None,
        start_split_symbol: str = None,
        start_split_symbol_index: int = None,
    ):
        self.additional_regex = additional_regex
        self.end_split_symbol = end_split_symbol
        self.regex = regex
        self.regex_split_result = regex_split_result
        self.start_split_symbol = start_split_symbol
        self.start_split_symbol_index = start_split_symbol_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_regex is not None:
            result['AdditionalRegex'] = self.additional_regex
        if self.end_split_symbol is not None:
            result['EndSplitSymbol'] = self.end_split_symbol
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.regex_split_result is not None:
            result['RegexSplitResult'] = self.regex_split_result
        if self.start_split_symbol is not None:
            result['StartSplitSymbol'] = self.start_split_symbol
        if self.start_split_symbol_index is not None:
            result['StartSplitSymbolIndex'] = self.start_split_symbol_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalRegex') is not None:
            self.additional_regex = m.get('AdditionalRegex')
        if m.get('EndSplitSymbol') is not None:
            self.end_split_symbol = m.get('EndSplitSymbol')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('RegexSplitResult') is not None:
            self.regex_split_result = m.get('RegexSplitResult')
        if m.get('StartSplitSymbol') is not None:
            self.start_split_symbol = m.get('StartSplitSymbol')
        if m.get('StartSplitSymbolIndex') is not None:
            self.start_split_symbol_index = m.get('StartSplitSymbolIndex')
        return self


class GetLineSplitResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
        resource: GetLineSplitResultResponseBodyResource = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.resource = resource
        self.success = success

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resource') is not None:
            temp_model = GetLineSplitResultResponseBodyResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLineSplitResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLineSplitResultResponseBody = None,
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
            temp_model = GetLineSplitResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogColumnTranslateResultRequest(TeaModel):
    def __init__(
        self,
        column_value: str = None,
        translate_config: str = None,
    ):
        self.column_value = column_value
        self.translate_config = translate_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_value is not None:
            result['ColumnValue'] = self.column_value
        if self.translate_config is not None:
            result['TranslateConfig'] = self.translate_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnValue') is not None:
            self.column_value = m.get('ColumnValue')
        if m.get('TranslateConfig') is not None:
            self.translate_config = m.get('TranslateConfig')
        return self


class GetLogColumnTranslateResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        error_code: int = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        resource: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.resource = resource
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLogColumnTranslateResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLogColumnTranslateResultResponseBody = None,
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
            temp_model = GetLogColumnTranslateResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMonitoringTemplateRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.id = id
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetMonitoringTemplateResponseBodyResource(TeaModel):
    def __init__(
        self,
        alert_templates_json: str = None,
        description: str = None,
        host_availability_template: str = None,
        id: str = None,
        name: str = None,
        namespace: str = None,
        process_monitor_templates: str = None,
        rest_version: str = None,
        system_event_templates: str = None,
    ):
        self.alert_templates_json = alert_templates_json
        self.description = description
        self.host_availability_template = host_availability_template
        self.id = id
        self.name = name
        self.namespace = namespace
        self.process_monitor_templates = process_monitor_templates
        self.rest_version = rest_version
        self.system_event_templates = system_event_templates

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_templates_json is not None:
            result['AlertTemplatesJson'] = self.alert_templates_json
        if self.description is not None:
            result['Description'] = self.description
        if self.host_availability_template is not None:
            result['HostAvailabilityTemplate'] = self.host_availability_template
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.process_monitor_templates is not None:
            result['ProcessMonitorTemplates'] = self.process_monitor_templates
        if self.rest_version is not None:
            result['RestVersion'] = self.rest_version
        if self.system_event_templates is not None:
            result['SystemEventTemplates'] = self.system_event_templates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTemplatesJson') is not None:
            self.alert_templates_json = m.get('AlertTemplatesJson')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostAvailabilityTemplate') is not None:
            self.host_availability_template = m.get('HostAvailabilityTemplate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ProcessMonitorTemplates') is not None:
            self.process_monitor_templates = m.get('ProcessMonitorTemplates')
        if m.get('RestVersion') is not None:
            self.rest_version = m.get('RestVersion')
        if m.get('SystemEventTemplates') is not None:
            self.system_event_templates = m.get('SystemEventTemplates')
        return self


class GetMonitoringTemplateResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
        resource: GetMonitoringTemplateResponseBodyResource = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.resource = resource
        self.success = success

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resource') is not None:
            temp_model = GetMonitoringTemplateResponseBodyResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMonitoringTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMonitoringTemplateResponseBody = None,
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
            temp_model = GetMonitoringTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMyGroupsRequest(TeaModel):
    def __init__(
        self,
        bind_url: str = None,
        group_id: int = None,
        group_name: str = None,
        instance_id: str = None,
        region_id: str = None,
        select_contact_groups: bool = None,
        type: str = None,
    ):
        self.bind_url = bind_url
        self.group_id = group_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.region_id = region_id
        self.select_contact_groups = select_contact_groups
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_url is not None:
            result['BindUrl'] = self.bind_url
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.select_contact_groups is not None:
            result['SelectContactGroups'] = self.select_contact_groups
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrl') is not None:
            self.bind_url = m.get('BindUrl')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SelectContactGroups') is not None:
            self.select_contact_groups = m.get('SelectContactGroups')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMyGroupsResponseBodyGroupContactGroupsContactGroup(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetMyGroupsResponseBodyGroupContactGroups(TeaModel):
    def __init__(
        self,
        contact_group: List[GetMyGroupsResponseBodyGroupContactGroupsContactGroup] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        if self.contact_group:
            for k in self.contact_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactGroup'] = []
        if self.contact_group is not None:
            for k in self.contact_group:
                result['ContactGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_group = []
        if m.get('ContactGroup') is not None:
            for k in m.get('ContactGroup'):
                temp_model = GetMyGroupsResponseBodyGroupContactGroupsContactGroup()
                self.contact_group.append(temp_model.from_map(k))
        return self


class GetMyGroupsResponseBodyGroup(TeaModel):
    def __init__(
        self,
        bind_url: str = None,
        contact_groups: GetMyGroupsResponseBodyGroupContactGroups = None,
        group_id: int = None,
        group_name: str = None,
        service_id: int = None,
        type: str = None,
    ):
        self.bind_url = bind_url
        self.contact_groups = contact_groups
        self.group_id = group_id
        self.group_name = group_name
        self.service_id = service_id
        self.type = type

    def validate(self):
        if self.contact_groups:
            self.contact_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_url is not None:
            result['BindUrl'] = self.bind_url
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrl') is not None:
            self.bind_url = m.get('BindUrl')
        if m.get('ContactGroups') is not None:
            temp_model = GetMyGroupsResponseBodyGroupContactGroups()
            self.contact_groups = temp_model.from_map(m['ContactGroups'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        group: GetMyGroupsResponseBodyGroup = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.group = group
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Group') is not None:
            temp_model = GetMyGroupsResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMyGroupsResponseBody = None,
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
            temp_model = GetMyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmRequest(TeaModel):
    def __init__(
        self,
        dimension: str = None,
        id: str = None,
        is_enable: bool = None,
        name: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        state: str = None,
    ):
        self.dimension = dimension
        self.id = id
        self.is_enable = is_enable
        self.name = name
        self.namespace = namespace
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.id is not None:
            result['Id'] = self.id
        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAlarmResponseBodyAlarmListAlarm(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        enable: bool = None,
        end_time: int = None,
        evaluation_count: int = None,
        id: str = None,
        metric_name: str = None,
        name: str = None,
        namespace: str = None,
        notify_type: int = None,
        period: int = None,
        silence_time: int = None,
        start_time: int = None,
        state: str = None,
        statistics: str = None,
        threshold: str = None,
        webhook: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.contact_groups = contact_groups
        self.dimensions = dimensions
        self.enable = enable
        self.end_time = end_time
        self.evaluation_count = evaluation_count
        self.id = id
        self.metric_name = metric_name
        self.name = name
        self.namespace = namespace
        self.notify_type = notify_type
        self.period = period
        self.silence_time = silence_time
        self.start_time = start_time
        self.state = state
        self.statistics = statistics
        self.threshold = threshold
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.id is not None:
            result['Id'] = self.id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.period is not None:
            result['Period'] = self.period
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class ListAlarmResponseBodyAlarmList(TeaModel):
    def __init__(
        self,
        alarm: List[ListAlarmResponseBodyAlarmListAlarm] = None,
    ):
        self.alarm = alarm

    def validate(self):
        if self.alarm:
            for k in self.alarm:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarm'] = []
        if self.alarm is not None:
            for k in self.alarm:
                result['Alarm'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm = []
        if m.get('Alarm') is not None:
            for k in m.get('Alarm'):
                temp_model = ListAlarmResponseBodyAlarmListAlarm()
                self.alarm.append(temp_model.from_map(k))
        return self


class ListAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_list: ListAlarmResponseBodyAlarmList = None,
        code: str = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.alarm_list = alarm_list
        self.code = code
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.alarm_list:
            self.alarm_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_list is not None:
            result['AlarmList'] = self.alarm_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmList') is not None:
            temp_model = ListAlarmResponseBodyAlarmList()
            self.alarm_list = temp_model.from_map(m['AlarmList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlarmResponseBody = None,
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
            temp_model = ListAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmHistoryRequest(TeaModel):
    def __init__(
        self,
        cursor: str = None,
        end_time: str = None,
        id: str = None,
        region_id: str = None,
        size: int = None,
        start_time: str = None,
    ):
        self.cursor = cursor
        self.end_time = end_time
        self.id = id
        self.region_id = region_id
        self.size = size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAlarmHistoryResponseBodyAlarmHistoryListAlarmHistory(TeaModel):
    def __init__(
        self,
        alarm_time: int = None,
        contact_groups: str = None,
        dimension: str = None,
        evaluation_count: int = None,
        id: str = None,
        instance_name: str = None,
        last_time: int = None,
        metric_name: str = None,
        name: str = None,
        namespace: str = None,
        state: str = None,
        status: int = None,
        value: str = None,
    ):
        self.alarm_time = alarm_time
        self.contact_groups = contact_groups
        self.dimension = dimension
        self.evaluation_count = evaluation_count
        self.id = id
        self.instance_name = instance_name
        self.last_time = last_time
        self.metric_name = metric_name
        self.name = name
        self.namespace = namespace
        self.state = state
        self.status = status
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAlarmHistoryResponseBodyAlarmHistoryList(TeaModel):
    def __init__(
        self,
        alarm_history: List[ListAlarmHistoryResponseBodyAlarmHistoryListAlarmHistory] = None,
    ):
        self.alarm_history = alarm_history

    def validate(self):
        if self.alarm_history:
            for k in self.alarm_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmHistory'] = []
        if self.alarm_history is not None:
            for k in self.alarm_history:
                result['AlarmHistory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_history = []
        if m.get('AlarmHistory') is not None:
            for k in m.get('AlarmHistory'):
                temp_model = ListAlarmHistoryResponseBodyAlarmHistoryListAlarmHistory()
                self.alarm_history.append(temp_model.from_map(k))
        return self


class ListAlarmHistoryResponseBody(TeaModel):
    def __init__(
        self,
        alarm_history_list: ListAlarmHistoryResponseBodyAlarmHistoryList = None,
        code: str = None,
        cursor: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.alarm_history_list = alarm_history_list
        self.code = code
        self.cursor = cursor
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.alarm_history_list:
            self.alarm_history_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_history_list is not None:
            result['AlarmHistoryList'] = self.alarm_history_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmHistoryList') is not None:
            temp_model = ListAlarmHistoryResponseBodyAlarmHistoryList()
            self.alarm_history_list = temp_model.from_map(m['AlarmHistoryList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlarmHistoryResponseBody = None,
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
            temp_model = ListAlarmHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContactGroupRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListContactGroupResponseBodyContactGroups(TeaModel):
    def __init__(
        self,
        contact_group: List[str] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')
        return self


class ListContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        contact_groups: ListContactGroupResponseBodyContactGroups = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.contact_groups = contact_groups
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.contact_groups:
            self.contact_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContactGroups') is not None:
            temp_model = ListContactGroupResponseBodyContactGroups()
            self.contact_groups = temp_model.from_map(m['ContactGroups'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListContactGroupResponseBody = None,
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
            temp_model = ListContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventRulesRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        name_prefix: str = None,
        page: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.name_prefix = name_prefix
        self.page = page
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternEventTypeList(TeaModel):
    def __init__(
        self,
        event_type_list: List[str] = None,
    ):
        self.event_type_list = event_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        return self


class ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternLevelList(TeaModel):
    def __init__(
        self,
        level_list: List[str] = None,
    ):
        self.level_list = level_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level_list is not None:
            result['LevelList'] = self.level_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LevelList') is not None:
            self.level_list = m.get('LevelList')
        return self


class ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternNameList(TeaModel):
    def __init__(
        self,
        name_list: List[str] = None,
    ):
        self.name_list = name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_list is not None:
            result['NameList'] = self.name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')
        return self


class ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternStatusList(TeaModel):
    def __init__(
        self,
        status_list: List[str] = None,
    ):
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPattern(TeaModel):
    def __init__(
        self,
        event_type_list: ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternEventTypeList = None,
        level_list: ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternLevelList = None,
        name_list: ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternNameList = None,
        product: str = None,
        status_list: ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternStatusList = None,
    ):
        self.event_type_list = event_type_list
        self.level_list = level_list
        self.name_list = name_list
        self.product = product
        self.status_list = status_list

    def validate(self):
        if self.event_type_list:
            self.event_type_list.validate()
        if self.level_list:
            self.level_list.validate()
        if self.name_list:
            self.name_list.validate()
        if self.status_list:
            self.status_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list.to_map()
        if self.level_list is not None:
            result['LevelList'] = self.level_list.to_map()
        if self.name_list is not None:
            result['NameList'] = self.name_list.to_map()
        if self.product is not None:
            result['Product'] = self.product
        if self.status_list is not None:
            result['StatusList'] = self.status_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypeList') is not None:
            temp_model = ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternEventTypeList()
            self.event_type_list = temp_model.from_map(m['EventTypeList'])
        if m.get('LevelList') is not None:
            temp_model = ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternLevelList()
            self.level_list = temp_model.from_map(m['LevelList'])
        if m.get('NameList') is not None:
            temp_model = ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternNameList()
            self.name_list = temp_model.from_map(m['NameList'])
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('StatusList') is not None:
            temp_model = ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPatternStatusList()
            self.status_list = temp_model.from_map(m['StatusList'])
        return self


class ListEventRulesResponseBodyDatapointsEventRuleEventPattern(TeaModel):
    def __init__(
        self,
        event_pattern: List[ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPattern] = None,
    ):
        self.event_pattern = event_pattern

    def validate(self):
        if self.event_pattern:
            for k in self.event_pattern:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventPattern'] = []
        if self.event_pattern is not None:
            for k in self.event_pattern:
                result['EventPattern'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_pattern = []
        if m.get('EventPattern') is not None:
            for k in m.get('EventPattern'):
                temp_model = ListEventRulesResponseBodyDatapointsEventRuleEventPatternEventPattern()
                self.event_pattern.append(temp_model.from_map(k))
        return self


class ListEventRulesResponseBodyDatapointsEventRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_pattern: ListEventRulesResponseBodyDatapointsEventRuleEventPattern = None,
        event_type: str = None,
        group_id: str = None,
        name: str = None,
        state: str = None,
    ):
        self.description = description
        self.event_pattern = event_pattern
        self.event_type = event_type
        self.group_id = group_id
        self.name = name
        self.state = state

    def validate(self):
        if self.event_pattern:
            self.event_pattern.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_pattern is not None:
            result['EventPattern'] = self.event_pattern.to_map()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventPattern') is not None:
            temp_model = ListEventRulesResponseBodyDatapointsEventRuleEventPattern()
            self.event_pattern = temp_model.from_map(m['EventPattern'])
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListEventRulesResponseBodyDatapoints(TeaModel):
    def __init__(
        self,
        event_rule: List[ListEventRulesResponseBodyDatapointsEventRule] = None,
    ):
        self.event_rule = event_rule

    def validate(self):
        if self.event_rule:
            for k in self.event_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventRule'] = []
        if self.event_rule is not None:
            for k in self.event_rule:
                result['EventRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_rule = []
        if m.get('EventRule') is not None:
            for k in m.get('EventRule'):
                temp_model = ListEventRulesResponseBodyDatapointsEventRule()
                self.event_rule.append(temp_model.from_map(k))
        return self


class ListEventRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        datapoints: ListEventRulesResponseBodyDatapoints = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.datapoints = datapoints
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.datapoints:
            self.datapoints.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Datapoints') is not None:
            temp_model = ListEventRulesResponseBodyDatapoints()
            self.datapoints = temp_model.from_map(m['Datapoints'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventRulesResponseBody = None,
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
            temp_model = ListEventRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyGroupInstancesRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        group_id: int = None,
        instance_ids: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        total: bool = None,
    ):
        self.category = category
        # This parameter is required.
        self.group_id = group_id
        self.instance_ids = instance_ids
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMyGroupInstancesResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        category: str = None,
        id: int = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.category = category
        self.id = id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListMyGroupInstancesResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[ListMyGroupInstancesResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = ListMyGroupInstancesResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class ListMyGroupInstancesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: ListMyGroupInstancesResponseBodyResources = None,
        success: bool = None,
        total: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.resources = resources
        self.success = success
        self.total = total

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = ListMyGroupInstancesResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMyGroupInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMyGroupInstancesResponseBody = None,
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
            temp_model = ListMyGroupInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyGroupsRequest(TeaModel):
    def __init__(
        self,
        bind_urls: str = None,
        group_name: str = None,
        instance_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        select_contact_groups: bool = None,
        type: str = None,
    ):
        self.bind_urls = bind_urls
        self.group_name = group_name
        self.instance_id = instance_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.select_contact_groups = select_contact_groups
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_urls is not None:
            result['BindUrls'] = self.bind_urls
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.select_contact_groups is not None:
            result['SelectContactGroups'] = self.select_contact_groups
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrls') is not None:
            self.bind_urls = m.get('BindUrls')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SelectContactGroups') is not None:
            self.select_contact_groups = m.get('SelectContactGroups')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListMyGroupsResponseBodyResourcesResourceContactGroupsContactGroup(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListMyGroupsResponseBodyResourcesResourceContactGroups(TeaModel):
    def __init__(
        self,
        contact_group: List[ListMyGroupsResponseBodyResourcesResourceContactGroupsContactGroup] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        if self.contact_group:
            for k in self.contact_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactGroup'] = []
        if self.contact_group is not None:
            for k in self.contact_group:
                result['ContactGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_group = []
        if m.get('ContactGroup') is not None:
            for k in m.get('ContactGroup'):
                temp_model = ListMyGroupsResponseBodyResourcesResourceContactGroupsContactGroup()
                self.contact_group.append(temp_model.from_map(k))
        return self


class ListMyGroupsResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        bind_url: str = None,
        bind_urls: str = None,
        contact_groups: ListMyGroupsResponseBodyResourcesResourceContactGroups = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_id: int = None,
        group_name: str = None,
        service_id: str = None,
        type: str = None,
    ):
        self.bind_url = bind_url
        self.bind_urls = bind_urls
        self.contact_groups = contact_groups
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_id = group_id
        self.group_name = group_name
        self.service_id = service_id
        self.type = type

    def validate(self):
        if self.contact_groups:
            self.contact_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_url is not None:
            result['BindUrl'] = self.bind_url
        if self.bind_urls is not None:
            result['BindUrls'] = self.bind_urls
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrl') is not None:
            self.bind_url = m.get('BindUrl')
        if m.get('BindUrls') is not None:
            self.bind_urls = m.get('BindUrls')
        if m.get('ContactGroups') is not None:
            temp_model = ListMyGroupsResponseBodyResourcesResourceContactGroups()
            self.contact_groups = temp_model.from_map(m['ContactGroups'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListMyGroupsResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[ListMyGroupsResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = ListMyGroupsResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class ListMyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: ListMyGroupsResponseBodyResources = None,
        success: bool = None,
        total: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.resources = resources
        self.success = success
        self.total = total

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = ListMyGroupsResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMyGroupsResponseBody = None,
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
            temp_model = ListMyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTaskRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        alert_ids: str = None,
        alert_rule: str = None,
        interval: str = None,
        interval_unit: str = None,
        isp_city: str = None,
        options: str = None,
        region_id: str = None,
        task_id: str = None,
        task_name: str = None,
        caller: str = None,
    ):
        self.address = address
        self.alert_ids = alert_ids
        self.alert_rule = alert_rule
        self.interval = interval
        self.interval_unit = interval_unit
        self.isp_city = isp_city
        self.options = options
        self.region_id = region_id
        # This parameter is required.
        self.task_id = task_id
        self.task_name = task_name
        self.caller = caller

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.interval_unit is not None:
            result['IntervalUnit'] = self.interval_unit
        if self.isp_city is not None:
            result['IspCity'] = self.isp_city
        if self.options is not None:
            result['Options'] = self.options
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.caller is not None:
            result['caller'] = self.caller
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')
        if m.get('AlertRule') is not None:
            self.alert_rule = m.get('AlertRule')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IntervalUnit') is not None:
            self.interval_unit = m.get('IntervalUnit')
        if m.get('IspCity') is not None:
            self.isp_city = m.get('IspCity')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('caller') is not None:
            self.caller = m.get('caller')
        return self


class ModifyTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class ModifyTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTaskResponseBody = None,
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
            temp_model = ModifyTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NodeListRequest(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        instance_ids: str = None,
        instance_region_id: str = None,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        serial_numbers: str = None,
        status: str = None,
        user_id: int = None,
    ):
        self.host_name = host_name
        self.instance_ids = instance_ids
        self.instance_region_id = instance_region_id
        self.key_word = key_word
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.serial_numbers = serial_numbers
        self.status = status
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_numbers is not None:
            result['SerialNumbers'] = self.serial_numbers
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumbers') is not None:
            self.serial_numbers = m.get('SerialNumbers')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class NodeListResponseBodyNodesNode(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        aliyun_host: bool = None,
        eip_address: str = None,
        eip_id: str = None,
        host_name: str = None,
        instance_id: str = None,
        instance_type_family: str = None,
        ip_group: str = None,
        nat_ip: str = None,
        network_type: str = None,
        operating_system: str = None,
        region: str = None,
        serial_number: str = None,
        tianjimon_version: str = None,
    ):
        self.ali_uid = ali_uid
        self.aliyun_host = aliyun_host
        self.eip_address = eip_address
        self.eip_id = eip_id
        self.host_name = host_name
        self.instance_id = instance_id
        self.instance_type_family = instance_type_family
        self.ip_group = ip_group
        self.nat_ip = nat_ip
        self.network_type = network_type
        self.operating_system = operating_system
        self.region = region
        self.serial_number = serial_number
        self.tianjimon_version = tianjimon_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.aliyun_host is not None:
            result['AliyunHost'] = self.aliyun_host
        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address
        if self.eip_id is not None:
            result['EipId'] = self.eip_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.ip_group is not None:
            result['IpGroup'] = self.ip_group
        if self.nat_ip is not None:
            result['NatIp'] = self.nat_ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.operating_system is not None:
            result['OperatingSystem'] = self.operating_system
        if self.region is not None:
            result['Region'] = self.region
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.tianjimon_version is not None:
            result['TianjimonVersion'] = self.tianjimon_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AliyunHost') is not None:
            self.aliyun_host = m.get('AliyunHost')
        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')
        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('IpGroup') is not None:
            self.ip_group = m.get('IpGroup')
        if m.get('NatIp') is not None:
            self.nat_ip = m.get('NatIp')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('OperatingSystem') is not None:
            self.operating_system = m.get('OperatingSystem')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('TianjimonVersion') is not None:
            self.tianjimon_version = m.get('TianjimonVersion')
        return self


class NodeListResponseBodyNodes(TeaModel):
    def __init__(
        self,
        node: List[NodeListResponseBodyNodesNode] = None,
    ):
        self.node = node

    def validate(self):
        if self.node:
            for k in self.node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Node'] = []
        if self.node is not None:
            for k in self.node:
                result['Node'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k in m.get('Node'):
                temp_model = NodeListResponseBodyNodesNode()
                self.node.append(temp_model.from_map(k))
        return self


class NodeListResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        nodes: NodeListResponseBodyNodes = None,
        page_number: int = None,
        page_size: int = None,
        page_total: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.nodes = nodes
        self.page_number = page_number
        self.page_size = page_size
        self.page_total = page_total
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Nodes') is not None:
            temp_model = NodeListResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class NodeListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NodeListResponseBody = None,
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
            temp_model = NodeListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NodeProcessCreateRequest(TeaModel):
    def __init__(
        self,
        command: str = None,
        instance_id: str = None,
        name: str = None,
        process_name: str = None,
        process_user: str = None,
        region_id: str = None,
    ):
        self.command = command
        # This parameter is required.
        self.instance_id = instance_id
        self.name = name
        self.process_name = process_name
        self.process_user = process_user
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.process_user is not None:
            result['ProcessUser'] = self.process_user
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('ProcessUser') is not None:
            self.process_user = m.get('ProcessUser')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class NodeProcessCreateResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.id = id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class NodeProcessCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NodeProcessCreateResponseBody = None,
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
            temp_model = NodeProcessCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NodeProcessesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class NodeProcessesResponseBodyNodeProcessesNodeProcess(TeaModel):
    def __init__(
        self,
        command: str = None,
        id: int = None,
        instance_id: str = None,
        name: str = None,
        process_name: str = None,
        process_user: str = None,
    ):
        self.command = command
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.process_name = process_name
        self.process_user = process_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.process_user is not None:
            result['ProcessUser'] = self.process_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('ProcessUser') is not None:
            self.process_user = m.get('ProcessUser')
        return self


class NodeProcessesResponseBodyNodeProcesses(TeaModel):
    def __init__(
        self,
        node_process: List[NodeProcessesResponseBodyNodeProcessesNodeProcess] = None,
    ):
        self.node_process = node_process

    def validate(self):
        if self.node_process:
            for k in self.node_process:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeProcess'] = []
        if self.node_process is not None:
            for k in self.node_process:
                result['NodeProcess'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_process = []
        if m.get('NodeProcess') is not None:
            for k in m.get('NodeProcess'):
                temp_model = NodeProcessesResponseBodyNodeProcessesNodeProcess()
                self.node_process.append(temp_model.from_map(k))
        return self


class NodeProcessesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        node_processes: NodeProcessesResponseBodyNodeProcesses = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.node_processes = node_processes
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_processes:
            self.node_processes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.node_processes is not None:
            result['NodeProcesses'] = self.node_processes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NodeProcesses') is not None:
            temp_model = NodeProcessesResponseBodyNodeProcesses()
            self.node_processes = temp_model.from_map(m['NodeProcesses'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class NodeProcessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NodeProcessesResponseBody = None,
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
            temp_model = NodeProcessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NodeStatusListRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_ids = instance_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class NodeStatusListResponseBodyNodeStatusListNodeStatus(TeaModel):
    def __init__(
        self,
        auto_install: bool = None,
        instance_id: str = None,
        status: str = None,
    ):
        self.auto_install = auto_install
        self.instance_id = instance_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class NodeStatusListResponseBodyNodeStatusList(TeaModel):
    def __init__(
        self,
        node_status: List[NodeStatusListResponseBodyNodeStatusListNodeStatus] = None,
    ):
        self.node_status = node_status

    def validate(self):
        if self.node_status:
            for k in self.node_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeStatus'] = []
        if self.node_status is not None:
            for k in self.node_status:
                result['NodeStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_status = []
        if m.get('NodeStatus') is not None:
            for k in m.get('NodeStatus'):
                temp_model = NodeStatusListResponseBodyNodeStatusListNodeStatus()
                self.node_status.append(temp_model.from_map(k))
        return self


class NodeStatusListResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        node_status_list: NodeStatusListResponseBodyNodeStatusList = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.node_status_list = node_status_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_status_list:
            self.node_status_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.node_status_list is not None:
            result['NodeStatusList'] = self.node_status_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NodeStatusList') is not None:
            temp_model = NodeStatusListResponseBodyNodeStatusList()
            self.node_status_list = temp_model.from_map(m['NodeStatusList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class NodeStatusListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NodeStatusListResponseBody = None,
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
            temp_model = NodeStatusListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NodeUninstallRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class NodeUninstallResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class NodeUninstallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NodeUninstallResponseBody = None,
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
            temp_model = NodeUninstallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutCustomMetricRequest(TeaModel):
    def __init__(
        self,
        metric_list: str = None,
        region_id: str = None,
    ):
        self.metric_list = metric_list
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_list is not None:
            result['MetricList'] = self.metric_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricList') is not None:
            self.metric_list = m.get('MetricList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class PutCustomMetricResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        return self


class PutCustomMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutCustomMetricResponseBody = None,
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
            temp_model = PutCustomMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEventRequest(TeaModel):
    def __init__(
        self,
        event_info: str = None,
        region_id: str = None,
    ):
        self.event_info = event_info
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_info is not None:
            result['EventInfo'] = self.event_info
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class PutEventResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        return self


class PutEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutEventResponseBody = None,
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
            temp_model = PutEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEventRuleRequestEventPattern(TeaModel):
    def __init__(
        self,
        event_type_list: List[str] = None,
        level_list: List[str] = None,
        name_list: List[str] = None,
        product: str = None,
        status_list: List[str] = None,
    ):
        self.event_type_list = event_type_list
        self.level_list = level_list
        self.name_list = name_list
        self.product = product
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        if self.level_list is not None:
            result['LevelList'] = self.level_list
        if self.name_list is not None:
            result['NameList'] = self.name_list
        if self.product is not None:
            result['Product'] = self.product
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        if m.get('LevelList') is not None:
            self.level_list = m.get('LevelList')
        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class PutEventRuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_pattern: List[PutEventRuleRequestEventPattern] = None,
        event_type: str = None,
        group_id: str = None,
        name: str = None,
        region_id: str = None,
        state: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.event_pattern = event_pattern
        self.event_type = event_type
        self.group_id = group_id
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.state = state

    def validate(self):
        if self.event_pattern:
            for k in self.event_pattern:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['EventPattern'] = []
        if self.event_pattern is not None:
            for k in self.event_pattern:
                result['EventPattern'].append(k.to_map() if k else None)
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.event_pattern = []
        if m.get('EventPattern') is not None:
            for k in m.get('EventPattern'):
                temp_model = PutEventRuleRequestEventPattern()
                self.event_pattern.append(temp_model.from_map(k))
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class PutEventRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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


class PutEventRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutEventRuleResponseBody = None,
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
            temp_model = PutEventRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEventTargetsRequestContactParameters(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        id: str = None,
        level: str = None,
    ):
        self.contact_group_name = contact_group_name
        self.id = id
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class PutEventTargetsRequestFcParameters(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        id: str = None,
        region: str = None,
        service_name: str = None,
    ):
        self.function_name = function_name
        self.id = id
        self.region = region
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.id is not None:
            result['Id'] = self.id
        if self.region is not None:
            result['Region'] = self.region
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class PutEventTargetsRequestMnsParameters(TeaModel):
    def __init__(
        self,
        id: str = None,
        queue: str = None,
        region: str = None,
    ):
        self.id = id
        self.queue = queue
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class PutEventTargetsRequestSlsParameters(TeaModel):
    def __init__(
        self,
        id: str = None,
        log_store: str = None,
        project: str = None,
        region: str = None,
    ):
        self.id = id
        self.log_store = log_store
        self.project = project
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class PutEventTargetsRequestWebhookParameters(TeaModel):
    def __init__(
        self,
        id: str = None,
        method: str = None,
        protocol: str = None,
        url: str = None,
    ):
        self.id = id
        self.method = method
        self.protocol = protocol
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.method is not None:
            result['Method'] = self.method
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PutEventTargetsRequest(TeaModel):
    def __init__(
        self,
        contact_parameters: List[PutEventTargetsRequestContactParameters] = None,
        fc_parameters: List[PutEventTargetsRequestFcParameters] = None,
        mns_parameters: List[PutEventTargetsRequestMnsParameters] = None,
        region_id: str = None,
        rule_name: str = None,
        sls_parameters: List[PutEventTargetsRequestSlsParameters] = None,
        webhook_parameters: List[PutEventTargetsRequestWebhookParameters] = None,
    ):
        self.contact_parameters = contact_parameters
        self.fc_parameters = fc_parameters
        self.mns_parameters = mns_parameters
        self.region_id = region_id
        # This parameter is required.
        self.rule_name = rule_name
        self.sls_parameters = sls_parameters
        self.webhook_parameters = webhook_parameters

    def validate(self):
        if self.contact_parameters:
            for k in self.contact_parameters:
                if k:
                    k.validate()
        if self.fc_parameters:
            for k in self.fc_parameters:
                if k:
                    k.validate()
        if self.mns_parameters:
            for k in self.mns_parameters:
                if k:
                    k.validate()
        if self.sls_parameters:
            for k in self.sls_parameters:
                if k:
                    k.validate()
        if self.webhook_parameters:
            for k in self.webhook_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactParameters'] = []
        if self.contact_parameters is not None:
            for k in self.contact_parameters:
                result['ContactParameters'].append(k.to_map() if k else None)
        result['FcParameters'] = []
        if self.fc_parameters is not None:
            for k in self.fc_parameters:
                result['FcParameters'].append(k.to_map() if k else None)
        result['MnsParameters'] = []
        if self.mns_parameters is not None:
            for k in self.mns_parameters:
                result['MnsParameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        result['SlsParameters'] = []
        if self.sls_parameters is not None:
            for k in self.sls_parameters:
                result['SlsParameters'].append(k.to_map() if k else None)
        result['WebhookParameters'] = []
        if self.webhook_parameters is not None:
            for k in self.webhook_parameters:
                result['WebhookParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_parameters = []
        if m.get('ContactParameters') is not None:
            for k in m.get('ContactParameters'):
                temp_model = PutEventTargetsRequestContactParameters()
                self.contact_parameters.append(temp_model.from_map(k))
        self.fc_parameters = []
        if m.get('FcParameters') is not None:
            for k in m.get('FcParameters'):
                temp_model = PutEventTargetsRequestFcParameters()
                self.fc_parameters.append(temp_model.from_map(k))
        self.mns_parameters = []
        if m.get('MnsParameters') is not None:
            for k in m.get('MnsParameters'):
                temp_model = PutEventTargetsRequestMnsParameters()
                self.mns_parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        self.sls_parameters = []
        if m.get('SlsParameters') is not None:
            for k in m.get('SlsParameters'):
                temp_model = PutEventTargetsRequestSlsParameters()
                self.sls_parameters.append(temp_model.from_map(k))
        self.webhook_parameters = []
        if m.get('WebhookParameters') is not None:
            for k in m.get('WebhookParameters'):
                temp_model = PutEventTargetsRequestWebhookParameters()
                self.webhook_parameters.append(temp_model.from_map(k))
        return self


class PutEventTargetsResponseBodyContactParametersContactParameter(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        id: int = None,
        level: str = None,
    ):
        self.contact_group_name = contact_group_name
        self.id = id
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class PutEventTargetsResponseBodyContactParameters(TeaModel):
    def __init__(
        self,
        contact_parameter: List[PutEventTargetsResponseBodyContactParametersContactParameter] = None,
    ):
        self.contact_parameter = contact_parameter

    def validate(self):
        if self.contact_parameter:
            for k in self.contact_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactParameter'] = []
        if self.contact_parameter is not None:
            for k in self.contact_parameter:
                result['ContactParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_parameter = []
        if m.get('ContactParameter') is not None:
            for k in m.get('ContactParameter'):
                temp_model = PutEventTargetsResponseBodyContactParametersContactParameter()
                self.contact_parameter.append(temp_model.from_map(k))
        return self


class PutEventTargetsResponseBodyFailedContactParametersContactParameter(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        id: int = None,
        level: str = None,
    ):
        self.contact_group_name = contact_group_name
        self.id = id
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class PutEventTargetsResponseBodyFailedContactParameters(TeaModel):
    def __init__(
        self,
        contact_parameter: List[PutEventTargetsResponseBodyFailedContactParametersContactParameter] = None,
    ):
        self.contact_parameter = contact_parameter

    def validate(self):
        if self.contact_parameter:
            for k in self.contact_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactParameter'] = []
        if self.contact_parameter is not None:
            for k in self.contact_parameter:
                result['ContactParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_parameter = []
        if m.get('ContactParameter') is not None:
            for k in m.get('ContactParameter'):
                temp_model = PutEventTargetsResponseBodyFailedContactParametersContactParameter()
                self.contact_parameter.append(temp_model.from_map(k))
        return self


class PutEventTargetsResponseBodyFailedFcParametersFcParameter(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        id: int = None,
        region: str = None,
        service_name: str = None,
    ):
        self.function_name = function_name
        self.id = id
        self.region = region
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.id is not None:
            result['Id'] = self.id
        if self.region is not None:
            result['Region'] = self.region
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class PutEventTargetsResponseBodyFailedFcParameters(TeaModel):
    def __init__(
        self,
        fc_parameter: List[PutEventTargetsResponseBodyFailedFcParametersFcParameter] = None,
    ):
        self.fc_parameter = fc_parameter

    def validate(self):
        if self.fc_parameter:
            for k in self.fc_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FcParameter'] = []
        if self.fc_parameter is not None:
            for k in self.fc_parameter:
                result['FcParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fc_parameter = []
        if m.get('FcParameter') is not None:
            for k in m.get('FcParameter'):
                temp_model = PutEventTargetsResponseBodyFailedFcParametersFcParameter()
                self.fc_parameter.append(temp_model.from_map(k))
        return self


class PutEventTargetsResponseBodyFailedMnsParametersMnsParameter(TeaModel):
    def __init__(
        self,
        id: int = None,
        queue: str = None,
        region: str = None,
    ):
        self.id = id
        self.queue = queue
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class PutEventTargetsResponseBodyFailedMnsParameters(TeaModel):
    def __init__(
        self,
        mns_parameter: List[PutEventTargetsResponseBodyFailedMnsParametersMnsParameter] = None,
    ):
        self.mns_parameter = mns_parameter

    def validate(self):
        if self.mns_parameter:
            for k in self.mns_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MnsParameter'] = []
        if self.mns_parameter is not None:
            for k in self.mns_parameter:
                result['MnsParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mns_parameter = []
        if m.get('MnsParameter') is not None:
            for k in m.get('MnsParameter'):
                temp_model = PutEventTargetsResponseBodyFailedMnsParametersMnsParameter()
                self.mns_parameter.append(temp_model.from_map(k))
        return self


class PutEventTargetsResponseBodyFailedSlsParametersFailedSlsParameter(TeaModel):
    def __init__(
        self,
        id: str = None,
        log_store: str = None,
        project: str = None,
        region: str = None,
    ):
        self.id = id
        self.log_store = log_store
        self.project = project
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class PutEventTargetsResponseBodyFailedSlsParameters(TeaModel):
    def __init__(
        self,
        failed_sls_parameter: List[PutEventTargetsResponseBodyFailedSlsParametersFailedSlsParameter] = None,
    ):
        self.failed_sls_parameter = failed_sls_parameter

    def validate(self):
        if self.failed_sls_parameter:
            for k in self.failed_sls_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedSlsParameter'] = []
        if self.failed_sls_parameter is not None:
            for k in self.failed_sls_parameter:
                result['FailedSlsParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_sls_parameter = []
        if m.get('FailedSlsParameter') is not None:
            for k in m.get('FailedSlsParameter'):
                temp_model = PutEventTargetsResponseBodyFailedSlsParametersFailedSlsParameter()
                self.failed_sls_parameter.append(temp_model.from_map(k))
        return self


class PutEventTargetsResponseBodyFcParametersFcParameter(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        id: int = None,
        region: str = None,
        service_name: str = None,
    ):
        self.function_name = function_name
        self.id = id
        self.region = region
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.id is not None:
            result['Id'] = self.id
        if self.region is not None:
            result['Region'] = self.region
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class PutEventTargetsResponseBodyFcParameters(TeaModel):
    def __init__(
        self,
        fc_parameter: List[PutEventTargetsResponseBodyFcParametersFcParameter] = None,
    ):
        self.fc_parameter = fc_parameter

    def validate(self):
        if self.fc_parameter:
            for k in self.fc_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FcParameter'] = []
        if self.fc_parameter is not None:
            for k in self.fc_parameter:
                result['FcParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fc_parameter = []
        if m.get('FcParameter') is not None:
            for k in m.get('FcParameter'):
                temp_model = PutEventTargetsResponseBodyFcParametersFcParameter()
                self.fc_parameter.append(temp_model.from_map(k))
        return self


class PutEventTargetsResponseBodyMnsParametersMnsParameter(TeaModel):
    def __init__(
        self,
        id: int = None,
        queue: str = None,
        region: str = None,
    ):
        self.id = id
        self.queue = queue
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class PutEventTargetsResponseBodyMnsParameters(TeaModel):
    def __init__(
        self,
        mns_parameter: List[PutEventTargetsResponseBodyMnsParametersMnsParameter] = None,
    ):
        self.mns_parameter = mns_parameter

    def validate(self):
        if self.mns_parameter:
            for k in self.mns_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MnsParameter'] = []
        if self.mns_parameter is not None:
            for k in self.mns_parameter:
                result['MnsParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mns_parameter = []
        if m.get('MnsParameter') is not None:
            for k in m.get('MnsParameter'):
                temp_model = PutEventTargetsResponseBodyMnsParametersMnsParameter()
                self.mns_parameter.append(temp_model.from_map(k))
        return self


class PutEventTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        contact_parameters: PutEventTargetsResponseBodyContactParameters = None,
        failed_contact_parameters: PutEventTargetsResponseBodyFailedContactParameters = None,
        failed_fc_parameters: PutEventTargetsResponseBodyFailedFcParameters = None,
        failed_mns_parameters: PutEventTargetsResponseBodyFailedMnsParameters = None,
        failed_parameter_count: str = None,
        failed_sls_parameters: PutEventTargetsResponseBodyFailedSlsParameters = None,
        fc_parameters: PutEventTargetsResponseBodyFcParameters = None,
        message: str = None,
        mns_parameters: PutEventTargetsResponseBodyMnsParameters = None,
        parameter_count: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.contact_parameters = contact_parameters
        self.failed_contact_parameters = failed_contact_parameters
        self.failed_fc_parameters = failed_fc_parameters
        self.failed_mns_parameters = failed_mns_parameters
        self.failed_parameter_count = failed_parameter_count
        self.failed_sls_parameters = failed_sls_parameters
        self.fc_parameters = fc_parameters
        self.message = message
        self.mns_parameters = mns_parameters
        self.parameter_count = parameter_count
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.contact_parameters:
            self.contact_parameters.validate()
        if self.failed_contact_parameters:
            self.failed_contact_parameters.validate()
        if self.failed_fc_parameters:
            self.failed_fc_parameters.validate()
        if self.failed_mns_parameters:
            self.failed_mns_parameters.validate()
        if self.failed_sls_parameters:
            self.failed_sls_parameters.validate()
        if self.fc_parameters:
            self.fc_parameters.validate()
        if self.mns_parameters:
            self.mns_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.contact_parameters is not None:
            result['ContactParameters'] = self.contact_parameters.to_map()
        if self.failed_contact_parameters is not None:
            result['FailedContactParameters'] = self.failed_contact_parameters.to_map()
        if self.failed_fc_parameters is not None:
            result['FailedFcParameters'] = self.failed_fc_parameters.to_map()
        if self.failed_mns_parameters is not None:
            result['FailedMnsParameters'] = self.failed_mns_parameters.to_map()
        if self.failed_parameter_count is not None:
            result['FailedParameterCount'] = self.failed_parameter_count
        if self.failed_sls_parameters is not None:
            result['FailedSlsParameters'] = self.failed_sls_parameters.to_map()
        if self.fc_parameters is not None:
            result['FcParameters'] = self.fc_parameters.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.mns_parameters is not None:
            result['MnsParameters'] = self.mns_parameters.to_map()
        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContactParameters') is not None:
            temp_model = PutEventTargetsResponseBodyContactParameters()
            self.contact_parameters = temp_model.from_map(m['ContactParameters'])
        if m.get('FailedContactParameters') is not None:
            temp_model = PutEventTargetsResponseBodyFailedContactParameters()
            self.failed_contact_parameters = temp_model.from_map(m['FailedContactParameters'])
        if m.get('FailedFcParameters') is not None:
            temp_model = PutEventTargetsResponseBodyFailedFcParameters()
            self.failed_fc_parameters = temp_model.from_map(m['FailedFcParameters'])
        if m.get('FailedMnsParameters') is not None:
            temp_model = PutEventTargetsResponseBodyFailedMnsParameters()
            self.failed_mns_parameters = temp_model.from_map(m['FailedMnsParameters'])
        if m.get('FailedParameterCount') is not None:
            self.failed_parameter_count = m.get('FailedParameterCount')
        if m.get('FailedSlsParameters') is not None:
            temp_model = PutEventTargetsResponseBodyFailedSlsParameters()
            self.failed_sls_parameters = temp_model.from_map(m['FailedSlsParameters'])
        if m.get('FcParameters') is not None:
            temp_model = PutEventTargetsResponseBodyFcParameters()
            self.fc_parameters = temp_model.from_map(m['FcParameters'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MnsParameters') is not None:
            temp_model = PutEventTargetsResponseBodyMnsParameters()
            self.mns_parameters = temp_model.from_map(m['MnsParameters'])
        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PutEventTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutEventTargetsResponseBody = None,
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
            temp_model = PutEventTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutMetricRuleTargetsRequestTargets(TeaModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        level: str = None,
    ):
        self.arn = arn
        self.id = id
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.id is not None:
            result['Id'] = self.id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class PutMetricRuleTargetsRequest(TeaModel):
    def __init__(
        self,
        actions: str = None,
        region_id: str = None,
        rule_name: str = None,
        targets: List[PutMetricRuleTargetsRequestTargets] = None,
    ):
        self.actions = actions
        self.region_id = region_id
        # This parameter is required.
        self.rule_name = rule_name
        # This parameter is required.
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['Actions'] = self.actions
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = PutMetricRuleTargetsRequestTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class PutMetricRuleTargetsResponseBodyFailDataTargetsTarget(TeaModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        level: str = None,
    ):
        self.arn = arn
        self.id = id
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.id is not None:
            result['Id'] = self.id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class PutMetricRuleTargetsResponseBodyFailDataTargets(TeaModel):
    def __init__(
        self,
        target: List[PutMetricRuleTargetsResponseBodyFailDataTargetsTarget] = None,
    ):
        self.target = target

    def validate(self):
        if self.target:
            for k in self.target:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Target'] = []
        if self.target is not None:
            for k in self.target:
                result['Target'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target = []
        if m.get('Target') is not None:
            for k in m.get('Target'):
                temp_model = PutMetricRuleTargetsResponseBodyFailDataTargetsTarget()
                self.target.append(temp_model.from_map(k))
        return self


class PutMetricRuleTargetsResponseBodyFailData(TeaModel):
    def __init__(
        self,
        targets: PutMetricRuleTargetsResponseBodyFailDataTargets = None,
    ):
        self.targets = targets

    def validate(self):
        if self.targets:
            self.targets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.targets is not None:
            result['Targets'] = self.targets.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Targets') is not None:
            temp_model = PutMetricRuleTargetsResponseBodyFailDataTargets()
            self.targets = temp_model.from_map(m['Targets'])
        return self


class PutMetricRuleTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        fail_data: PutMetricRuleTargetsResponseBodyFailData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.fail_data = fail_data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.fail_data:
            self.fail_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.fail_data is not None:
            result['FailData'] = self.fail_data.to_map()
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
        if m.get('FailData') is not None:
            temp_model = PutMetricRuleTargetsResponseBodyFailData()
            self.fail_data = temp_model.from_map(m['FailData'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PutMetricRuleTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutMetricRuleTargetsResponseBody = None,
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
            temp_model = PutMetricRuleTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutResourceMetricRuleRequestEscalationsCritical(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class PutResourceMetricRuleRequestEscalationsInfo(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class PutResourceMetricRuleRequestEscalationsWarn(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class PutResourceMetricRuleRequestEscalations(TeaModel):
    def __init__(
        self,
        critical: PutResourceMetricRuleRequestEscalationsCritical = None,
        info: PutResourceMetricRuleRequestEscalationsInfo = None,
        warn: PutResourceMetricRuleRequestEscalationsWarn = None,
    ):
        self.critical = critical
        self.info = info
        self.warn = warn

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.info:
            self.info.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()
        if self.info is not None:
            result['Info'] = self.info.to_map()
        if self.warn is not None:
            result['Warn'] = self.warn.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = PutResourceMetricRuleRequestEscalationsCritical()
            self.critical = temp_model.from_map(m['Critical'])
        if m.get('Info') is not None:
            temp_model = PutResourceMetricRuleRequestEscalationsInfo()
            self.info = temp_model.from_map(m['Info'])
        if m.get('Warn') is not None:
            temp_model = PutResourceMetricRuleRequestEscalationsWarn()
            self.warn = temp_model.from_map(m['Warn'])
        return self


class PutResourceMetricRuleRequest(TeaModel):
    def __init__(
        self,
        escalations: PutResourceMetricRuleRequestEscalations = None,
        contact_groups: str = None,
        effective_interval: str = None,
        email_subject: str = None,
        interval: str = None,
        metric_name: str = None,
        namespace: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: int = None,
        webhook: str = None,
    ):
        self.escalations = escalations
        self.contact_groups = contact_groups
        self.effective_interval = effective_interval
        self.email_subject = email_subject
        self.interval = interval
        # This parameter is required.
        self.metric_name = metric_name
        # This parameter is required.
        self.namespace = namespace
        self.no_effective_interval = no_effective_interval
        self.period = period
        # This parameter is required.
        self.resources = resources
        # This parameter is required.
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.silence_time = silence_time
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval
        if self.email_subject is not None:
            result['EmailSubject'] = self.email_subject
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval
        if self.period is not None:
            result['Period'] = self.period
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Escalations') is not None:
            temp_model = PutResourceMetricRuleRequestEscalations()
            self.escalations = temp_model.from_map(m['Escalations'])
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')
        if m.get('EmailSubject') is not None:
            self.email_subject = m.get('EmailSubject')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class PutResourceMetricRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class PutResourceMetricRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutResourceMetricRuleResponseBody = None,
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
            temp_model = PutResourceMetricRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustomMetricListRequest(TeaModel):
    def __init__(
        self,
        dimension: str = None,
        group_id: str = None,
        md_5: str = None,
        metric_name: str = None,
        page: str = None,
        size: str = None,
    ):
        self.dimension = dimension
        # This parameter is required.
        self.group_id = group_id
        self.md_5 = md_5
        self.metric_name = metric_name
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class QueryCustomMetricListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class QueryCustomMetricListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCustomMetricListResponseBody = None,
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
            temp_model = QueryCustomMetricListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricDataRequest(TeaModel):
    def __init__(
        self,
        dimensions: str = None,
        end_time: str = None,
        express: str = None,
        length: str = None,
        metric: str = None,
        period: str = None,
        project: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.dimensions = dimensions
        self.end_time = end_time
        self.express = express
        self.length = length
        # This parameter is required.
        self.metric = metric
        self.period = period
        # This parameter is required.
        self.project = project
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.express is not None:
            result['Express'] = self.express
        if self.length is not None:
            result['Length'] = self.length
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.period is not None:
            result['Period'] = self.period
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Express') is not None:
            self.express = m.get('Express')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        datapoints: str = None,
        message: str = None,
        period: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.datapoints = datapoints
        self.message = message
        self.period = period
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
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints
        if self.message is not None:
            result['Message'] = self.message
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMetricDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMetricDataResponseBody = None,
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
            temp_model = QueryMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricLastRequest(TeaModel):
    def __init__(
        self,
        cursor: str = None,
        dimensions: str = None,
        end_time: str = None,
        express: str = None,
        length: str = None,
        metric: str = None,
        page: str = None,
        period: str = None,
        project: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.cursor = cursor
        self.dimensions = dimensions
        self.end_time = end_time
        self.express = express
        self.length = length
        # This parameter is required.
        self.metric = metric
        self.page = page
        self.period = period
        # This parameter is required.
        self.project = project
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.express is not None:
            result['Express'] = self.express
        if self.length is not None:
            result['Length'] = self.length
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.page is not None:
            result['Page'] = self.page
        if self.period is not None:
            result['Period'] = self.period
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Express') is not None:
            self.express = m.get('Express')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricLastResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        cursor: str = None,
        datapoints: str = None,
        message: str = None,
        period: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.cursor = cursor
        self.datapoints = datapoints
        self.message = message
        self.period = period
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
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints
        if self.message is not None:
            result['Message'] = self.message
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMetricLastResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMetricLastResponseBody = None,
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
            temp_model = QueryMetricLastResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricListRequest(TeaModel):
    def __init__(
        self,
        cursor: str = None,
        dimensions: str = None,
        end_time: str = None,
        express: str = None,
        length: str = None,
        metric: str = None,
        period: str = None,
        project: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.cursor = cursor
        self.dimensions = dimensions
        self.end_time = end_time
        self.express = express
        self.length = length
        # This parameter is required.
        self.metric = metric
        self.period = period
        # This parameter is required.
        self.project = project
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.express is not None:
            result['Express'] = self.express
        if self.length is not None:
            result['Length'] = self.length
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.period is not None:
            result['Period'] = self.period
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Express') is not None:
            self.express = m.get('Express')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        cursor: str = None,
        datapoints: str = None,
        message: str = None,
        period: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.cursor = cursor
        self.datapoints = datapoints
        self.message = message
        self.period = period
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
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints
        if self.message is not None:
            result['Message'] = self.message
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMetricListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMetricListResponseBody = None,
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
            temp_model = QueryMetricListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricMetaRequest(TeaModel):
    def __init__(
        self,
        labels: str = None,
        metric: str = None,
        page_number: int = None,
        page_size: int = None,
        project: str = None,
    ):
        self.labels = labels
        self.metric = metric
        self.page_number = page_number
        self.page_size = page_size
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class QueryMetricMetaResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        description: str = None,
        dimensions: str = None,
        labels: str = None,
        metric: str = None,
        periods: str = None,
        project: str = None,
        statistics: str = None,
        unit: str = None,
    ):
        self.description = description
        self.dimensions = dimensions
        self.labels = labels
        self.metric = metric
        self.periods = periods
        self.project = project
        self.statistics = statistics
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.periods is not None:
            result['Periods'] = self.periods
        if self.project is not None:
            result['Project'] = self.project
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Periods') is not None:
            self.periods = m.get('Periods')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class QueryMetricMetaResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[QueryMetricMetaResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = QueryMetricMetaResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class QueryMetricMetaResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        resources: QueryMetricMetaResponseBodyResources = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.resources = resources
        self.success = success

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = QueryMetricMetaResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMetricMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMetricMetaResponseBody = None,
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
            temp_model = QueryMetricMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricTopRequest(TeaModel):
    def __init__(
        self,
        dimensions: str = None,
        end_time: str = None,
        express: str = None,
        length: str = None,
        metric: str = None,
        order_desc: str = None,
        orderby: str = None,
        period: str = None,
        project: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.dimensions = dimensions
        self.end_time = end_time
        self.express = express
        self.length = length
        # This parameter is required.
        self.metric = metric
        self.order_desc = order_desc
        self.orderby = orderby
        self.period = period
        # This parameter is required.
        self.project = project
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.express is not None:
            result['Express'] = self.express
        if self.length is not None:
            result['Length'] = self.length
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order_desc is not None:
            result['OrderDesc'] = self.order_desc
        if self.orderby is not None:
            result['Orderby'] = self.orderby
        if self.period is not None:
            result['Period'] = self.period
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Express') is not None:
            self.express = m.get('Express')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('OrderDesc') is not None:
            self.order_desc = m.get('OrderDesc')
        if m.get('Orderby') is not None:
            self.orderby = m.get('Orderby')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricTopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        datapoints: str = None,
        message: str = None,
        period: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.datapoints = datapoints
        self.message = message
        self.period = period
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
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints
        if self.message is not None:
            result['Message'] = self.message
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMetricTopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMetricTopResponseBody = None,
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
            temp_model = QueryMetricTopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectMetaRequest(TeaModel):
    def __init__(
        self,
        labels: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.labels = labels
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryProjectMetaResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        description: str = None,
        labels: str = None,
        project: str = None,
    ):
        self.description = description
        self.labels = labels
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class QueryProjectMetaResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[QueryProjectMetaResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = QueryProjectMetaResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class QueryProjectMetaResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        resources: QueryProjectMetaResponseBodyResources = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.resources = resources
        self.success = success

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = QueryProjectMetaResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryProjectMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProjectMetaResponseBody = None,
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
            temp_model = QueryProjectMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStaticsAvailabilityRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
        time_range: str = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.task_id = task_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class QueryStaticsAvailabilityResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class QueryStaticsAvailabilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStaticsAvailabilityResponseBody = None,
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
            temp_model = QueryStaticsAvailabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStaticsResponseTimeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
        time_range: str = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.task_id = task_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class QueryStaticsResponseTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class QueryStaticsResponseTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStaticsResponseTimeResponseBody = None,
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
            temp_model = QueryStaticsResponseTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySystemEventCountRequest(TeaModel):
    def __init__(
        self,
        query_json: str = None,
        region_id: str = None,
    ):
        self.query_json = query_json
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_json is not None:
            result['QueryJson'] = self.query_json
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryJson') is not None:
            self.query_json = m.get('QueryJson')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QuerySystemEventCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class QuerySystemEventCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySystemEventCountResponseBody = None,
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
            temp_model = QuerySystemEventCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySystemEventDemoRequest(TeaModel):
    def __init__(
        self,
        event_name: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.event_name = event_name
        # This parameter is required.
        self.product = product
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QuerySystemEventDemoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class QuerySystemEventDemoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySystemEventDemoResponseBody = None,
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
            temp_model = QuerySystemEventDemoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskConfigRequest(TeaModel):
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
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryTaskConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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


class QueryTaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskConfigResponseBody = None,
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
            temp_model = QueryTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskMonitorDataRequest(TeaModel):
    def __init__(
        self,
        cursor: str = None,
        end_time: str = None,
        length: int = None,
        period: str = None,
        region_id: str = None,
        start_time: str = None,
        task_id: str = None,
        type: str = None,
        metric_name: str = None,
    ):
        self.cursor = cursor
        self.end_time = end_time
        self.length = length
        self.period = period
        self.region_id = region_id
        self.start_time = start_time
        # This parameter is required.
        self.task_id = task_id
        self.type = type
        # This parameter is required.
        self.metric_name = metric_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.length is not None:
            result['Length'] = self.length
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        return self


class QueryTaskMonitorDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        cursor: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.cursor = cursor
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class QueryTaskMonitorDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskMonitorDataResponseBody = None,
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
            temp_model = QueryTaskMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaskConfigListRequest(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        task_name: str = None,
    ):
        self.group_id = group_id
        self.id = id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class TaskConfigListResponseBodyTaskListNodeTaskConfigInstanceList(TeaModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class TaskConfigListResponseBodyTaskListNodeTaskConfig(TeaModel):
    def __init__(
        self,
        alert_config: str = None,
        disabled: bool = None,
        group_id: int = None,
        group_name: str = None,
        id: int = None,
        instance_list: TaskConfigListResponseBodyTaskListNodeTaskConfigInstanceList = None,
        json_data: str = None,
        task_name: str = None,
        task_scope: str = None,
        task_type: str = None,
    ):
        self.alert_config = alert_config
        self.disabled = disabled
        self.group_id = group_id
        self.group_name = group_name
        self.id = id
        self.instance_list = instance_list
        self.json_data = json_data
        self.task_name = task_name
        self.task_scope = task_scope
        self.task_type = task_type

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_config is not None:
            result['AlertConfig'] = self.alert_config
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()
        if self.json_data is not None:
            result['JsonData'] = self.json_data
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_scope is not None:
            result['TaskScope'] = self.task_scope
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConfig') is not None:
            self.alert_config = m.get('AlertConfig')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceList') is not None:
            temp_model = TaskConfigListResponseBodyTaskListNodeTaskConfigInstanceList()
            self.instance_list = temp_model.from_map(m['InstanceList'])
        if m.get('JsonData') is not None:
            self.json_data = m.get('JsonData')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskScope') is not None:
            self.task_scope = m.get('TaskScope')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class TaskConfigListResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        node_task_config: List[TaskConfigListResponseBodyTaskListNodeTaskConfig] = None,
    ):
        self.node_task_config = node_task_config

    def validate(self):
        if self.node_task_config:
            for k in self.node_task_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeTaskConfig'] = []
        if self.node_task_config is not None:
            for k in self.node_task_config:
                result['NodeTaskConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_task_config = []
        if m.get('NodeTaskConfig') is not None:
            for k in m.get('NodeTaskConfig'):
                temp_model = TaskConfigListResponseBodyTaskListNodeTaskConfig()
                self.node_task_config.append(temp_model.from_map(k))
        return self


class TaskConfigListResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        page_number: int = None,
        page_size: int = None,
        page_total: int = None,
        request_id: str = None,
        success: bool = None,
        task_list: TaskConfigListResponseBodyTaskList = None,
        total: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.page_number = page_number
        self.page_size = page_size
        self.page_total = page_total
        self.request_id = request_id
        self.success = success
        self.task_list = task_list
        self.total = total

    def validate(self):
        if self.task_list:
            self.task_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_list is not None:
            result['TaskList'] = self.task_list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskList') is not None:
            temp_model = TaskConfigListResponseBodyTaskList()
            self.task_list = temp_model.from_map(m['TaskList'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class TaskConfigListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TaskConfigListResponseBody = None,
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
            temp_model = TaskConfigListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlarmRequest(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        contact_groups: str = None,
        dry_run: bool = None,
        end_time: int = None,
        evaluation_count: int = None,
        id: str = None,
        name: str = None,
        notify_type: int = None,
        period: int = None,
        region_id: str = None,
        silence_time: int = None,
        start_time: int = None,
        statistics: str = None,
        threshold: str = None,
        webhook: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.contact_groups = contact_groups
        self.dry_run = dry_run
        self.end_time = end_time
        self.evaluation_count = evaluation_count
        # This parameter is required.
        self.id = id
        self.name = name
        self.notify_type = notify_type
        self.period = period
        self.region_id = region_id
        self.silence_time = silence_time
        self.start_time = start_time
        self.statistics = statistics
        # This parameter is required.
        self.threshold = threshold
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class UpdateAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class UpdateAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAlarmResponseBody = None,
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
            temp_model = UpdateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMonitoringTemplateRequest(TeaModel):
    def __init__(
        self,
        alert_templates_json: str = None,
        description: str = None,
        host_availability_template: str = None,
        id: int = None,
        name: str = None,
        process_monitor_templates: str = None,
        region_id: str = None,
        rest_version: int = None,
        system_event_templates: str = None,
    ):
        # This parameter is required.
        self.alert_templates_json = alert_templates_json
        self.description = description
        self.host_availability_template = host_availability_template
        # This parameter is required.
        self.id = id
        self.name = name
        self.process_monitor_templates = process_monitor_templates
        self.region_id = region_id
        # This parameter is required.
        self.rest_version = rest_version
        self.system_event_templates = system_event_templates

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_templates_json is not None:
            result['AlertTemplatesJson'] = self.alert_templates_json
        if self.description is not None:
            result['Description'] = self.description
        if self.host_availability_template is not None:
            result['HostAvailabilityTemplate'] = self.host_availability_template
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.process_monitor_templates is not None:
            result['ProcessMonitorTemplates'] = self.process_monitor_templates
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rest_version is not None:
            result['RestVersion'] = self.rest_version
        if self.system_event_templates is not None:
            result['SystemEventTemplates'] = self.system_event_templates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTemplatesJson') is not None:
            self.alert_templates_json = m.get('AlertTemplatesJson')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostAvailabilityTemplate') is not None:
            self.host_availability_template = m.get('HostAvailabilityTemplate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProcessMonitorTemplates') is not None:
            self.process_monitor_templates = m.get('ProcessMonitorTemplates')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RestVersion') is not None:
            self.rest_version = m.get('RestVersion')
        if m.get('SystemEventTemplates') is not None:
            self.system_event_templates = m.get('SystemEventTemplates')
        return self


class UpdateMonitoringTemplateResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMonitoringTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMonitoringTemplateResponseBody = None,
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
            temp_model = UpdateMonitoringTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


