# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class BatchDeleteJobsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id_list: List[int] = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.job_id_list = job_id_list
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchDeleteJobsResponseBody(TeaModel):
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


class BatchDeleteJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDeleteJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchDeleteJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDisableJobsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id_list: List[int] = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.job_id_list = job_id_list
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchDisableJobsResponseBody(TeaModel):
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


class BatchDisableJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDisableJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchDisableJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchEnableJobsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id_list: List[int] = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.job_id_list = job_id_list
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchEnableJobsResponseBody(TeaModel):
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


class BatchEnableJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchEnableJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchEnableJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppGroupRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_name: str = None,
        description: str = None,
        group_id: str = None,
        max_jobs: int = None,
        monitor_config_json: str = None,
        monitor_contacts_json: str = None,
        namespace: str = None,
        namespace_name: str = None,
        namespace_source: str = None,
        region_id: str = None,
        schedule_busy_workers: bool = None,
    ):
        self.app_key = app_key
        self.app_name = app_name
        self.description = description
        self.group_id = group_id
        self.max_jobs = max_jobs
        self.monitor_config_json = monitor_config_json
        self.monitor_contacts_json = monitor_contacts_json
        self.namespace = namespace
        self.namespace_name = namespace_name
        self.namespace_source = namespace_source
        self.region_id = region_id
        self.schedule_busy_workers = schedule_busy_workers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.max_jobs is not None:
            result['MaxJobs'] = self.max_jobs
        if self.monitor_config_json is not None:
            result['MonitorConfigJson'] = self.monitor_config_json
        if self.monitor_contacts_json is not None:
            result['MonitorContactsJson'] = self.monitor_contacts_json
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schedule_busy_workers is not None:
            result['ScheduleBusyWorkers'] = self.schedule_busy_workers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MaxJobs') is not None:
            self.max_jobs = m.get('MaxJobs')
        if m.get('MonitorConfigJson') is not None:
            self.monitor_config_json = m.get('MonitorConfigJson')
        if m.get('MonitorContactsJson') is not None:
            self.monitor_contacts_json = m.get('MonitorContactsJson')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScheduleBusyWorkers') is not None:
            self.schedule_busy_workers = m.get('ScheduleBusyWorkers')
        return self


class CreateAppGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        app_group_id: int = None,
        app_key: str = None,
    ):
        self.app_group_id = app_group_id
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class CreateAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateAppGroupResponseBodyData = None,
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
            temp_model = CreateAppGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequestContactInfo(TeaModel):
    def __init__(
        self,
        ding: str = None,
        user_mail: str = None,
        user_name: str = None,
        user_phone: str = None,
    ):
        self.ding = ding
        self.user_mail = user_mail
        self.user_name = user_name
        self.user_phone = user_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding is not None:
            result['Ding'] = self.ding
        if self.user_mail is not None:
            result['UserMail'] = self.user_mail
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')
        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        attempt_interval: int = None,
        calendar: str = None,
        class_name: str = None,
        consumer_size: int = None,
        contact_info: List[CreateJobRequestContactInfo] = None,
        content: str = None,
        data_offset: int = None,
        description: str = None,
        dispatcher_size: int = None,
        execute_mode: str = None,
        fail_enable: bool = None,
        group_id: str = None,
        jar_url: str = None,
        job_type: str = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        miss_worker_enable: bool = None,
        name: str = None,
        namespace: str = None,
        namespace_source: str = None,
        page_size: int = None,
        parameters: str = None,
        queue_size: int = None,
        region_id: str = None,
        send_channel: str = None,
        task_attempt_interval: int = None,
        task_max_attempt: int = None,
        time_expression: str = None,
        time_type: int = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.class_name = class_name
        self.consumer_size = consumer_size
        self.contact_info = contact_info
        self.content = content
        self.data_offset = data_offset
        self.description = description
        self.dispatcher_size = dispatcher_size
        self.execute_mode = execute_mode
        self.fail_enable = fail_enable
        self.group_id = group_id
        self.jar_url = jar_url
        self.job_type = job_type
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        self.miss_worker_enable = miss_worker_enable
        self.name = name
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.page_size = page_size
        self.parameters = parameters
        self.queue_size = queue_size
        self.region_id = region_id
        self.send_channel = send_channel
        self.task_attempt_interval = task_attempt_interval
        self.task_max_attempt = task_max_attempt
        self.time_expression = time_expression
        self.time_type = time_type
        self.timeout = timeout
        self.timeout_enable = timeout_enable
        self.timeout_kill_enable = timeout_kill_enable

    def validate(self):
        if self.contact_info:
            for k in self.contact_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k in self.contact_info:
                result['ContactInfo'].append(k.to_map() if k else None)
        if self.content is not None:
            result['Content'] = self.content
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.description is not None:
            result['Description'] = self.description
        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size
        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.jar_url is not None:
            result['JarUrl'] = self.jar_url
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval
        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable
        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k in m.get('ContactInfo'):
                temp_model = CreateJobRequestContactInfo()
                self.contact_info.append(temp_model.from_map(k))
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')
        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JarUrl') is not None:
            self.jar_url = m.get('JarUrl')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')
        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
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
        body: CreateJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        region_id: str = None,
        source: str = None,
        uid: str = None,
    ):
        self.description = description
        self.name = name
        self.region_id = region_id
        self.source = source
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class CreateNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        namespace_uid: str = None,
    ):
        self.namespace_uid = namespace_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_uid is not None:
            result['NamespaceUid'] = self.namespace_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceUid') is not None:
            self.namespace_uid = m.get('NamespaceUid')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateNamespaceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
            temp_model = CreateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.job_id = job_id
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteJobResponseBody(TeaModel):
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


class DeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkflowRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        workflow_id: int = None,
    ):
        self.group_id = group_id
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.region_id = region_id
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class DeleteWorkflowResponseBody(TeaModel):
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


class DeleteWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
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


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DesignateWorkersRequest(TeaModel):
    def __init__(
        self,
        designate_type: int = None,
        group_id: str = None,
        job_id: int = None,
        labels: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        transferable: bool = None,
        workers: str = None,
    ):
        # 指定机器的类型
        self.designate_type = designate_type
        # 应用分组ID
        self.group_id = group_id
        # 任务ID
        self.job_id = job_id
        # 指定label列表json格式
        self.labels = labels
        # 命名空间UID
        self.namespace = namespace
        # 命名空间来源
        self.namespace_source = namespace_source
        self.region_id = region_id
        # 是否故障转移
        self.transferable = transferable
        # 指定机器列表json格式
        self.workers = workers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.transferable is not None:
            result['Transferable'] = self.transferable
        if self.workers is not None:
            result['Workers'] = self.workers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Transferable') is not None:
            self.transferable = m.get('Transferable')
        if m.get('Workers') is not None:
            self.workers = m.get('Workers')
        return self


class DesignateWorkersResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 是否成功
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


class DesignateWorkersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DesignateWorkersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DesignateWorkersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableJobRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.job_id = job_id
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableJobResponseBody(TeaModel):
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


class DisableJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWorkflowRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        workflow_id: int = None,
    ):
        self.group_id = group_id
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.region_id = region_id
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class DisableWorkflowResponseBody(TeaModel):
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


class DisableWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableJobRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.job_id = job_id
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableJobResponseBody(TeaModel):
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


class EnableJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWorkflowRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        workflow_id: int = None,
    ):
        self.group_id = group_id
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.region_id = region_id
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class EnableWorkflowResponseBody(TeaModel):
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


class EnableWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteJobRequest(TeaModel):
    def __init__(
        self,
        check_job_status: bool = None,
        designate_type: int = None,
        group_id: str = None,
        instance_parameters: str = None,
        job_id: int = None,
        label: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        worker: str = None,
    ):
        self.check_job_status = check_job_status
        # 指定机器类型：1.workerAddr; 2. label
        self.designate_type = designate_type
        self.group_id = group_id
        self.instance_parameters = instance_parameters
        self.job_id = job_id
        # 指定机器的标签
        self.label = label
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.region_id = region_id
        # 指定机器的workerAddr
        self.worker = worker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_job_status is not None:
            result['CheckJobStatus'] = self.check_job_status
        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_parameters is not None:
            result['InstanceParameters'] = self.instance_parameters
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.label is not None:
            result['Label'] = self.label
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.worker is not None:
            result['Worker'] = self.worker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckJobStatus') is not None:
            self.check_job_status = m.get('CheckJobStatus')
        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceParameters') is not None:
            self.instance_parameters = m.get('InstanceParameters')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Worker') is not None:
            self.worker = m.get('Worker')
        return self


class ExecuteJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_instance_id: int = None,
    ):
        self.job_instance_id = job_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        return self


class ExecuteJobResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ExecuteJobResponseBodyData = None,
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
            temp_model = ExecuteJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExecuteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteWorkflowRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_parameters: str = None,
        namespace: str = None,
        namespace_source: str = None,
        workflow_id: int = None,
    ):
        self.group_id = group_id
        self.instance_parameters = instance_parameters
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_parameters is not None:
            result['InstanceParameters'] = self.instance_parameters
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceParameters') is not None:
            self.instance_parameters = m.get('InstanceParameters')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class ExecuteWorkflowResponseBodyData(TeaModel):
    def __init__(
        self,
        wf_instance_id: int = None,
    ):
        self.wf_instance_id = wf_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wf_instance_id is not None:
            result['WfInstanceId'] = self.wf_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WfInstanceId') is not None:
            self.wf_instance_id = m.get('WfInstanceId')
        return self


class ExecuteWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ExecuteWorkflowResponseBodyData = None,
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
            temp_model = ExecuteWorkflowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExecuteWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobInfoRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        job_name: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.job_id = job_id
        self.job_name = job_name
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo(TeaModel):
    def __init__(
        self,
        ding: str = None,
        user_mail: str = None,
        user_name: str = None,
        user_phone: str = None,
    ):
        self.ding = ding
        self.user_mail = user_mail
        self.user_name = user_name
        self.user_phone = user_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding is not None:
            result['Ding'] = self.ding
        if self.user_mail is not None:
            result['UserMail'] = self.user_mail
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')
        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')
        return self


class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig(TeaModel):
    def __init__(
        self,
        fail_enable: bool = None,
        miss_worker_enable: bool = None,
        send_channel: str = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        self.fail_enable = fail_enable
        self.miss_worker_enable = miss_worker_enable
        self.send_channel = send_channel
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
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
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
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
        return self


class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo(TeaModel):
    def __init__(
        self,
        contact_info: List[GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo] = None,
        monitor_config: GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig = None,
    ):
        self.contact_info = contact_info
        self.monitor_config = monitor_config

    def validate(self):
        if self.contact_info:
            for k in self.contact_info:
                if k:
                    k.validate()
        if self.monitor_config:
            self.monitor_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k in self.contact_info:
                result['ContactInfo'].append(k.to_map() if k else None)
        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k in m.get('ContactInfo'):
                temp_model = GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo()
                self.contact_info.append(temp_model.from_map(k))
        if m.get('MonitorConfig') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig()
            self.monitor_config = temp_model.from_map(m['MonitorConfig'])
        return self


class GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs(TeaModel):
    def __init__(
        self,
        consumer_size: int = None,
        dispatcher_size: int = None,
        page_size: int = None,
        queue_size: int = None,
        task_attempt_interval: int = None,
        task_max_attempt: int = None,
    ):
        self.consumer_size = consumer_size
        self.dispatcher_size = dispatcher_size
        self.page_size = page_size
        self.queue_size = queue_size
        self.task_attempt_interval = task_attempt_interval
        self.task_max_attempt = task_max_attempt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size
        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size
        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval
        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')
        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')
        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')
        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')
        return self


class GetJobInfoResponseBodyDataJobConfigInfoTimeConfig(TeaModel):
    def __init__(
        self,
        calendar: str = None,
        data_offset: int = None,
        time_expression: str = None,
        time_type: int = None,
    ):
        self.calendar = calendar
        self.data_offset = data_offset
        self.time_expression = time_expression
        self.time_type = time_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        return self


class GetJobInfoResponseBodyDataJobConfigInfo(TeaModel):
    def __init__(
        self,
        attempt_interval: int = None,
        class_name: str = None,
        content: str = None,
        description: str = None,
        execute_mode: str = None,
        jar_url: str = None,
        job_id: int = None,
        job_monitor_info: GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo = None,
        map_task_xattrs: GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs = None,
        max_attempt: int = None,
        max_concurrency: str = None,
        name: str = None,
        parameters: str = None,
        status: int = None,
        time_config: GetJobInfoResponseBodyDataJobConfigInfoTimeConfig = None,
    ):
        self.attempt_interval = attempt_interval
        self.class_name = class_name
        self.content = content
        self.description = description
        self.execute_mode = execute_mode
        self.jar_url = jar_url
        self.job_id = job_id
        self.job_monitor_info = job_monitor_info
        self.map_task_xattrs = map_task_xattrs
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        self.name = name
        self.parameters = parameters
        self.status = status
        self.time_config = time_config

    def validate(self):
        if self.job_monitor_info:
            self.job_monitor_info.validate()
        if self.map_task_xattrs:
            self.map_task_xattrs.validate()
        if self.time_config:
            self.time_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode
        if self.jar_url is not None:
            result['JarUrl'] = self.jar_url
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_monitor_info is not None:
            result['JobMonitorInfo'] = self.job_monitor_info.to_map()
        if self.map_task_xattrs is not None:
            result['MapTaskXAttrs'] = self.map_task_xattrs.to_map()
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.status is not None:
            result['Status'] = self.status
        if self.time_config is not None:
            result['TimeConfig'] = self.time_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')
        if m.get('JarUrl') is not None:
            self.jar_url = m.get('JarUrl')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobMonitorInfo') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo()
            self.job_monitor_info = temp_model.from_map(m['JobMonitorInfo'])
        if m.get('MapTaskXAttrs') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs()
            self.map_task_xattrs = temp_model.from_map(m['MapTaskXAttrs'])
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeConfig') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfoTimeConfig()
            self.time_config = temp_model.from_map(m['TimeConfig'])
        return self


class GetJobInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        job_config_info: GetJobInfoResponseBodyDataJobConfigInfo = None,
    ):
        self.job_config_info = job_config_info

    def validate(self):
        if self.job_config_info:
            self.job_config_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_config_info is not None:
            result['JobConfigInfo'] = self.job_config_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobConfigInfo') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfo()
            self.job_config_info = temp_model.from_map(m['JobConfigInfo'])
        return self


class GetJobInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetJobInfoResponseBodyData = None,
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
            temp_model = GetJobInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetJobInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobInstanceRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        job_instance_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
    ):
        self.group_id = group_id
        self.job_id = job_id
        self.job_instance_id = job_instance_id
        self.namespace = namespace
        self.namespace_source = namespace_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        return self


class GetJobInstanceResponseBodyDataJobInstanceDetail(TeaModel):
    def __init__(
        self,
        data_time: str = None,
        end_time: str = None,
        executor: str = None,
        instance_id: int = None,
        job_id: int = None,
        progress: str = None,
        result: str = None,
        schedule_time: str = None,
        start_time: str = None,
        status: int = None,
        time_type: int = None,
        trigger_type: int = None,
        work_addr: str = None,
    ):
        self.data_time = data_time
        self.end_time = end_time
        self.executor = executor
        self.instance_id = instance_id
        self.job_id = job_id
        self.progress = progress
        self.result = result
        self.schedule_time = schedule_time
        self.start_time = start_time
        self.status = status
        self.time_type = time_type
        self.trigger_type = trigger_type
        self.work_addr = work_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor is not None:
            result['Executor'] = self.executor
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result is not None:
            result['Result'] = self.result
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Executor') is not None:
            self.executor = m.get('Executor')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')
        return self


class GetJobInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        job_instance_detail: GetJobInstanceResponseBodyDataJobInstanceDetail = None,
    ):
        self.job_instance_detail = job_instance_detail

    def validate(self):
        if self.job_instance_detail:
            self.job_instance_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_instance_detail is not None:
            result['JobInstanceDetail'] = self.job_instance_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInstanceDetail') is not None:
            temp_model = GetJobInstanceResponseBodyDataJobInstanceDetail()
            self.job_instance_detail = temp_model.from_map(m['JobInstanceDetail'])
        return self


class GetJobInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetJobInstanceResponseBodyData = None,
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
            temp_model = GetJobInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetJobInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobInstanceListRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.job_id = job_id
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetJobInstanceListResponseBodyDataJobInstanceDetails(TeaModel):
    def __init__(
        self,
        data_time: str = None,
        end_time: str = None,
        executor: str = None,
        instance_id: int = None,
        job_id: int = None,
        progress: str = None,
        result: str = None,
        schedule_time: str = None,
        start_time: str = None,
        status: int = None,
        time_type: int = None,
        trigger_type: int = None,
        work_addr: str = None,
    ):
        self.data_time = data_time
        self.end_time = end_time
        self.executor = executor
        self.instance_id = instance_id
        self.job_id = job_id
        self.progress = progress
        self.result = result
        self.schedule_time = schedule_time
        self.start_time = start_time
        self.status = status
        self.time_type = time_type
        self.trigger_type = trigger_type
        self.work_addr = work_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor is not None:
            result['Executor'] = self.executor
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result is not None:
            result['Result'] = self.result
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Executor') is not None:
            self.executor = m.get('Executor')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')
        return self


class GetJobInstanceListResponseBodyData(TeaModel):
    def __init__(
        self,
        job_instance_details: List[GetJobInstanceListResponseBodyDataJobInstanceDetails] = None,
    ):
        self.job_instance_details = job_instance_details

    def validate(self):
        if self.job_instance_details:
            for k in self.job_instance_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobInstanceDetails'] = []
        if self.job_instance_details is not None:
            for k in self.job_instance_details:
                result['JobInstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_instance_details = []
        if m.get('JobInstanceDetails') is not None:
            for k in m.get('JobInstanceDetails'):
                temp_model = GetJobInstanceListResponseBodyDataJobInstanceDetails()
                self.job_instance_details.append(temp_model.from_map(k))
        return self


class GetJobInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetJobInstanceListResponseBodyData = None,
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
            temp_model = GetJobInstanceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobInstanceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetJobInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkFlowRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        workflow_id: int = None,
    ):
        # 应用分组ID
        self.group_id = group_id
        # 命名空间uid
        self.namespace = namespace
        # 命名空间来源
        self.namespace_source = namespace_source
        self.region_id = region_id
        # 工作流ID
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class GetWorkFlowResponseBodyDataWorkFlowInfo(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        status: str = None,
        time_expression: str = None,
        time_type: str = None,
        workflow_id: int = None,
    ):
        # 工作流描述
        self.description = description
        # 工作流名称
        self.name = name
        # 工作流状态
        self.status = status
        # 工作流时间表达式
        self.time_expression = time_expression
        # 工作流时间类型
        self.time_type = time_type
        # 工作流ID
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges(TeaModel):
    def __init__(
        self,
        source: int = None,
        target: int = None,
    ):
        # 起始任务ID
        self.source = source
        # 目的任务ID
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes(TeaModel):
    def __init__(
        self,
        id: int = None,
        label: str = None,
        status: int = None,
    ):
        # 任务ID
        self.id = id
        # 任务名称
        self.label = label
        # 任务状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetWorkFlowResponseBodyDataWorkFlowNodeInfo(TeaModel):
    def __init__(
        self,
        edges: List[GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges] = None,
        nodes: List[GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes] = None,
    ):
        # 工作流边列表
        self.edges = edges
        # 工作流节点列表
        self.nodes = nodes

    def validate(self):
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges()
                self.edges.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class GetWorkFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        work_flow_info: GetWorkFlowResponseBodyDataWorkFlowInfo = None,
        work_flow_node_info: GetWorkFlowResponseBodyDataWorkFlowNodeInfo = None,
    ):
        # 工作流基本信息
        self.work_flow_info = work_flow_info
        # 工作流节点信息
        self.work_flow_node_info = work_flow_node_info

    def validate(self):
        if self.work_flow_info:
            self.work_flow_info.validate()
        if self.work_flow_node_info:
            self.work_flow_node_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.work_flow_info is not None:
            result['WorkFlowInfo'] = self.work_flow_info.to_map()
        if self.work_flow_node_info is not None:
            result['WorkFlowNodeInfo'] = self.work_flow_node_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkFlowInfo') is not None:
            temp_model = GetWorkFlowResponseBodyDataWorkFlowInfo()
            self.work_flow_info = temp_model.from_map(m['WorkFlowInfo'])
        if m.get('WorkFlowNodeInfo') is not None:
            temp_model = GetWorkFlowResponseBodyDataWorkFlowNodeInfo()
            self.work_flow_node_info = temp_model.from_map(m['WorkFlowNodeInfo'])
        return self


class GetWorkFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetWorkFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 错误码
        self.code = code
        # 工作流的数据
        self.data = data
        # 错误信息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 会否成功
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
            temp_model = GetWorkFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWorkFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWorkFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetWorkFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkerListRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetWorkerListResponseBodyDataWorkerInfos(TeaModel):
    def __init__(
        self,
        ip: str = None,
        label: str = None,
        port: int = None,
        starter: str = None,
        version: str = None,
        worker_address: str = None,
    ):
        self.ip = ip
        self.label = label
        self.port = port
        self.starter = starter
        self.version = version
        self.worker_address = worker_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.label is not None:
            result['Label'] = self.label
        if self.port is not None:
            result['Port'] = self.port
        if self.starter is not None:
            result['Starter'] = self.starter
        if self.version is not None:
            result['Version'] = self.version
        if self.worker_address is not None:
            result['WorkerAddress'] = self.worker_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Starter') is not None:
            self.starter = m.get('Starter')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkerAddress') is not None:
            self.worker_address = m.get('WorkerAddress')
        return self


class GetWorkerListResponseBodyData(TeaModel):
    def __init__(
        self,
        worker_infos: List[GetWorkerListResponseBodyDataWorkerInfos] = None,
    ):
        self.worker_infos = worker_infos

    def validate(self):
        if self.worker_infos:
            for k in self.worker_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WorkerInfos'] = []
        if self.worker_infos is not None:
            for k in self.worker_infos:
                result['WorkerInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.worker_infos = []
        if m.get('WorkerInfos') is not None:
            for k in m.get('WorkerInfos'):
                temp_model = GetWorkerListResponseBodyDataWorkerInfos()
                self.worker_infos.append(temp_model.from_map(k))
        return self


class GetWorkerListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetWorkerListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
            temp_model = GetWorkerListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWorkerListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWorkerListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetWorkerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantPermissionRequest(TeaModel):
    def __init__(
        self,
        grant_option: bool = None,
        group_id: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.grant_option = grant_option
        self.group_id = group_id
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.region_id = region_id
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GrantPermissionResponseBody(TeaModel):
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


class GrantPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GrantPermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GrantPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListGroupsResponseBodyDataAppGroups(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_name: str = None,
        description: str = None,
        group_id: str = None,
    ):
        self.app_key = app_key
        self.app_name = app_name
        self.description = description
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ListGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_groups: List[ListGroupsResponseBodyDataAppGroups] = None,
    ):
        self.app_groups = app_groups

    def validate(self):
        if self.app_groups:
            for k in self.app_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppGroups'] = []
        if self.app_groups is not None:
            for k in self.app_groups:
                result['AppGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_groups = []
        if m.get('AppGroups') is not None:
            for k in m.get('AppGroups'):
                temp_model = ListGroupsResponseBodyDataAppGroups()
                self.app_groups.append(temp_model.from_map(k))
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListGroupsResponseBodyData = None,
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
            temp_model = ListGroupsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        job_name: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.group_id = group_id
        self.job_name = job_name
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo(TeaModel):
    def __init__(
        self,
        ding: str = None,
        user_mail: str = None,
        user_name: str = None,
        user_phone: str = None,
    ):
        self.ding = ding
        self.user_mail = user_mail
        self.user_name = user_name
        self.user_phone = user_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding is not None:
            result['Ding'] = self.ding
        if self.user_mail is not None:
            result['UserMail'] = self.user_mail
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')
        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')
        return self


class ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig(TeaModel):
    def __init__(
        self,
        fail_enable: bool = None,
        miss_worker_enable: bool = None,
        send_channel: str = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        self.fail_enable = fail_enable
        self.miss_worker_enable = miss_worker_enable
        self.send_channel = send_channel
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
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
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
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
        return self


class ListJobsResponseBodyDataJobsJobMonitorInfo(TeaModel):
    def __init__(
        self,
        contact_info: List[ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo] = None,
        monitor_config: ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig = None,
    ):
        self.contact_info = contact_info
        self.monitor_config = monitor_config

    def validate(self):
        if self.contact_info:
            for k in self.contact_info:
                if k:
                    k.validate()
        if self.monitor_config:
            self.monitor_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k in self.contact_info:
                result['ContactInfo'].append(k.to_map() if k else None)
        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k in m.get('ContactInfo'):
                temp_model = ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo()
                self.contact_info.append(temp_model.from_map(k))
        if m.get('MonitorConfig') is not None:
            temp_model = ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig()
            self.monitor_config = temp_model.from_map(m['MonitorConfig'])
        return self


class ListJobsResponseBodyDataJobsMapTaskXAttrs(TeaModel):
    def __init__(
        self,
        consumer_size: int = None,
        dispatcher_size: int = None,
        page_size: int = None,
        queue_size: int = None,
        task_attempt_interval: int = None,
        task_max_attempt: int = None,
    ):
        self.consumer_size = consumer_size
        self.dispatcher_size = dispatcher_size
        self.page_size = page_size
        self.queue_size = queue_size
        self.task_attempt_interval = task_attempt_interval
        self.task_max_attempt = task_max_attempt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size
        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size
        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval
        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')
        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')
        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')
        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')
        return self


class ListJobsResponseBodyDataJobsTimeConfig(TeaModel):
    def __init__(
        self,
        calendar: str = None,
        data_offset: int = None,
        time_expression: str = None,
        time_type: int = None,
    ):
        self.calendar = calendar
        self.data_offset = data_offset
        self.time_expression = time_expression
        self.time_type = time_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        return self


class ListJobsResponseBodyDataJobs(TeaModel):
    def __init__(
        self,
        attempt_interval: int = None,
        class_name: str = None,
        content: str = None,
        description: str = None,
        execute_mode: str = None,
        jar_url: str = None,
        job_id: int = None,
        job_monitor_info: ListJobsResponseBodyDataJobsJobMonitorInfo = None,
        map_task_xattrs: ListJobsResponseBodyDataJobsMapTaskXAttrs = None,
        max_attempt: int = None,
        max_concurrency: str = None,
        name: str = None,
        parameters: str = None,
        status: int = None,
        time_config: ListJobsResponseBodyDataJobsTimeConfig = None,
    ):
        self.attempt_interval = attempt_interval
        self.class_name = class_name
        self.content = content
        self.description = description
        self.execute_mode = execute_mode
        self.jar_url = jar_url
        self.job_id = job_id
        self.job_monitor_info = job_monitor_info
        self.map_task_xattrs = map_task_xattrs
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        self.name = name
        self.parameters = parameters
        self.status = status
        self.time_config = time_config

    def validate(self):
        if self.job_monitor_info:
            self.job_monitor_info.validate()
        if self.map_task_xattrs:
            self.map_task_xattrs.validate()
        if self.time_config:
            self.time_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode
        if self.jar_url is not None:
            result['JarUrl'] = self.jar_url
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_monitor_info is not None:
            result['JobMonitorInfo'] = self.job_monitor_info.to_map()
        if self.map_task_xattrs is not None:
            result['MapTaskXAttrs'] = self.map_task_xattrs.to_map()
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.status is not None:
            result['Status'] = self.status
        if self.time_config is not None:
            result['TimeConfig'] = self.time_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')
        if m.get('JarUrl') is not None:
            self.jar_url = m.get('JarUrl')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobMonitorInfo') is not None:
            temp_model = ListJobsResponseBodyDataJobsJobMonitorInfo()
            self.job_monitor_info = temp_model.from_map(m['JobMonitorInfo'])
        if m.get('MapTaskXAttrs') is not None:
            temp_model = ListJobsResponseBodyDataJobsMapTaskXAttrs()
            self.map_task_xattrs = temp_model.from_map(m['MapTaskXAttrs'])
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeConfig') is not None:
            temp_model = ListJobsResponseBodyDataJobsTimeConfig()
            self.time_config = temp_model.from_map(m['TimeConfig'])
        return self


class ListJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        jobs: List[ListJobsResponseBodyDataJobs] = None,
    ):
        self.jobs = jobs

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListJobsResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k))
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
        body: ListJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacesRequest(TeaModel):
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


class ListNamespacesResponseBodyDataNamespaces(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        uid: str = None,
    ):
        self.description = description
        self.name = name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.uid is not None:
            result['UId'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UId') is not None:
            self.uid = m.get('UId')
        return self


class ListNamespacesResponseBodyData(TeaModel):
    def __init__(
        self,
        namespaces: List[ListNamespacesResponseBodyDataNamespaces] = None,
    ):
        self.namespaces = namespaces

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListNamespacesResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        return self


class ListNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListNamespacesResponseBodyData = None,
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
            temp_model = ListNamespacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokePermissionRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        self.group_id = group_id
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RevokePermissionResponseBody(TeaModel):
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


class RevokePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokePermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RevokePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: int = None,
        job_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
        self.job_id = job_id
        self.namespace = namespace
        self.namespace_source = namespace_source
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopInstanceResponseBody(TeaModel):
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


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateJobRequestContactInfo(TeaModel):
    def __init__(
        self,
        ding: str = None,
        user_mail: str = None,
        user_name: str = None,
        user_phone: str = None,
    ):
        self.ding = ding
        self.user_mail = user_mail
        self.user_name = user_name
        self.user_phone = user_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding is not None:
            result['Ding'] = self.ding
        if self.user_mail is not None:
            result['UserMail'] = self.user_mail
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')
        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')
        return self


class UpdateJobRequest(TeaModel):
    def __init__(
        self,
        attempt_interval: int = None,
        calendar: str = None,
        class_name: str = None,
        consumer_size: int = None,
        contact_info: List[UpdateJobRequestContactInfo] = None,
        content: str = None,
        data_offset: int = None,
        description: str = None,
        dispatcher_size: int = None,
        execute_mode: str = None,
        fail_enable: bool = None,
        group_id: str = None,
        jar_url: str = None,
        job_id: int = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        miss_worker_enable: bool = None,
        name: str = None,
        namespace: str = None,
        namespace_source: str = None,
        page_size: int = None,
        parameters: str = None,
        queue_size: int = None,
        region_id: str = None,
        send_channel: str = None,
        task_attempt_interval: int = None,
        task_max_attempt: int = None,
        time_expression: str = None,
        time_type: int = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.class_name = class_name
        self.consumer_size = consumer_size
        self.contact_info = contact_info
        self.content = content
        self.data_offset = data_offset
        self.description = description
        self.dispatcher_size = dispatcher_size
        self.execute_mode = execute_mode
        self.fail_enable = fail_enable
        self.group_id = group_id
        self.jar_url = jar_url
        self.job_id = job_id
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        self.miss_worker_enable = miss_worker_enable
        self.name = name
        self.namespace = namespace
        self.namespace_source = namespace_source
        self.page_size = page_size
        self.parameters = parameters
        self.queue_size = queue_size
        self.region_id = region_id
        self.send_channel = send_channel
        self.task_attempt_interval = task_attempt_interval
        self.task_max_attempt = task_max_attempt
        self.time_expression = time_expression
        self.time_type = time_type
        self.timeout = timeout
        self.timeout_enable = timeout_enable
        self.timeout_kill_enable = timeout_kill_enable

    def validate(self):
        if self.contact_info:
            for k in self.contact_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k in self.contact_info:
                result['ContactInfo'].append(k.to_map() if k else None)
        if self.content is not None:
            result['Content'] = self.content
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.description is not None:
            result['Description'] = self.description
        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size
        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.jar_url is not None:
            result['JarUrl'] = self.jar_url
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval
        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable
        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k in m.get('ContactInfo'):
                temp_model = UpdateJobRequestContactInfo()
                self.contact_info.append(temp_model.from_map(k))
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')
        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JarUrl') is not None:
            self.jar_url = m.get('JarUrl')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')
        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
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
        body: UpdateJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


