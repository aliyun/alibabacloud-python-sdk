# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class UpdateProcessDefinitionWithScheduleRequest(DaraModel):
    def __init__(
        self,
        alert_email_address: str = None,
        description: str = None,
        execution_type: str = None,
        global_params: List[main_models.UpdateProcessDefinitionWithScheduleRequestGlobalParams] = None,
        name: str = None,
        product_namespace: str = None,
        publish: bool = None,
        region_id: str = None,
        release_state: str = None,
        resource_queue: str = None,
        retry_times: int = None,
        run_as: str = None,
        schedule: main_models.UpdateProcessDefinitionWithScheduleRequestSchedule = None,
        tags: Dict[str, str] = None,
        task_definition_json: List[main_models.UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJson] = None,
        task_parallelism: int = None,
        task_relation_json: List[main_models.UpdateProcessDefinitionWithScheduleRequestTaskRelationJson] = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The description of the workflow.
        self.description = description
        # The execution policy.
        # 
        # This parameter is required.
        self.execution_type = execution_type
        self.global_params = global_params
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The code of the service.
        # 
        # This parameter is required.
        self.product_namespace = product_namespace
        # Specifies whether to publish the workflow.
        self.publish = publish
        # The region ID.
        self.region_id = region_id
        # The status of the workflow.
        self.release_state = release_state
        # The resource queue.
        self.resource_queue = resource_queue
        # The number of retries.
        self.retry_times = retry_times
        # The execution user.
        self.run_as = run_as
        # The scheduling settings.
        self.schedule = schedule
        # The tags.
        self.tags = tags
        # The descriptions of all nodes in the workflow.
        # 
        # This parameter is required.
        self.task_definition_json = task_definition_json
        # The node parallelism.
        self.task_parallelism = task_parallelism
        # The dependencies of all nodes in the workflow. preTaskCode specifies the ID of an upstream node, and postTaskCode specifies the ID of a downstream node. The ID of each node is unique. If a node does not have an upstream node, set preTaskCode to 0.
        # 
        # This parameter is required.
        self.task_relation_json = task_relation_json
        # The default timeout period of the workflow.
        self.timeout = timeout

    def validate(self):
        if self.global_params:
            for v1 in self.global_params:
                 if v1:
                    v1.validate()
        if self.schedule:
            self.schedule.validate()
        if self.task_definition_json:
            for v1 in self.task_definition_json:
                 if v1:
                    v1.validate()
        if self.task_relation_json:
            for v1 in self.task_relation_json:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address

        if self.description is not None:
            result['description'] = self.description

        if self.execution_type is not None:
            result['executionType'] = self.execution_type

        result['globalParams'] = []
        if self.global_params is not None:
            for k1 in self.global_params:
                result['globalParams'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace

        if self.publish is not None:
            result['publish'] = self.publish

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.release_state is not None:
            result['releaseState'] = self.release_state

        if self.resource_queue is not None:
            result['resourceQueue'] = self.resource_queue

        if self.retry_times is not None:
            result['retryTimes'] = self.retry_times

        if self.run_as is not None:
            result['runAs'] = self.run_as

        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()

        if self.tags is not None:
            result['tags'] = self.tags

        result['taskDefinitionJson'] = []
        if self.task_definition_json is not None:
            for k1 in self.task_definition_json:
                result['taskDefinitionJson'].append(k1.to_map() if k1 else None)

        if self.task_parallelism is not None:
            result['taskParallelism'] = self.task_parallelism

        result['taskRelationJson'] = []
        if self.task_relation_json is not None:
            for k1 in self.task_relation_json:
                result['taskRelationJson'].append(k1.to_map() if k1 else None)

        if self.timeout is not None:
            result['timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')

        self.global_params = []
        if m.get('globalParams') is not None:
            for k1 in m.get('globalParams'):
                temp_model = main_models.UpdateProcessDefinitionWithScheduleRequestGlobalParams()
                self.global_params.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')

        if m.get('publish') is not None:
            self.publish = m.get('publish')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('releaseState') is not None:
            self.release_state = m.get('releaseState')

        if m.get('resourceQueue') is not None:
            self.resource_queue = m.get('resourceQueue')

        if m.get('retryTimes') is not None:
            self.retry_times = m.get('retryTimes')

        if m.get('runAs') is not None:
            self.run_as = m.get('runAs')

        if m.get('schedule') is not None:
            temp_model = main_models.UpdateProcessDefinitionWithScheduleRequestSchedule()
            self.schedule = temp_model.from_map(m.get('schedule'))

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        self.task_definition_json = []
        if m.get('taskDefinitionJson') is not None:
            for k1 in m.get('taskDefinitionJson'):
                temp_model = main_models.UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJson()
                self.task_definition_json.append(temp_model.from_map(k1))

        if m.get('taskParallelism') is not None:
            self.task_parallelism = m.get('taskParallelism')

        self.task_relation_json = []
        if m.get('taskRelationJson') is not None:
            for k1 in m.get('taskRelationJson'):
                temp_model = main_models.UpdateProcessDefinitionWithScheduleRequestTaskRelationJson()
                self.task_relation_json.append(temp_model.from_map(k1))

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        return self

class UpdateProcessDefinitionWithScheduleRequestTaskRelationJson(DaraModel):
    def __init__(
        self,
        name: str = None,
        post_task_code: int = None,
        post_task_version: int = None,
        pre_task_code: int = None,
        pre_task_version: int = None,
    ):
        # The name of the node topology. You can enter a workflow name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the downstream node.
        # 
        # This parameter is required.
        self.post_task_code = post_task_code
        # The version of the downstream node.
        # 
        # This parameter is required.
        self.post_task_version = post_task_version
        # The ID of the upstream node.
        # 
        # This parameter is required.
        self.pre_task_code = pre_task_code
        # The version of the upstream node.
        # 
        # This parameter is required.
        self.pre_task_version = pre_task_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.post_task_code is not None:
            result['postTaskCode'] = self.post_task_code

        if self.post_task_version is not None:
            result['postTaskVersion'] = self.post_task_version

        if self.pre_task_code is not None:
            result['preTaskCode'] = self.pre_task_code

        if self.pre_task_version is not None:
            result['preTaskVersion'] = self.pre_task_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('postTaskCode') is not None:
            self.post_task_code = m.get('postTaskCode')

        if m.get('postTaskVersion') is not None:
            self.post_task_version = m.get('postTaskVersion')

        if m.get('preTaskCode') is not None:
            self.pre_task_code = m.get('preTaskCode')

        if m.get('preTaskVersion') is not None:
            self.pre_task_version = m.get('preTaskVersion')

        return self

class UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJson(DaraModel):
    def __init__(
        self,
        alert_email_address: str = None,
        code: int = None,
        description: str = None,
        fail_alert_enable: bool = None,
        fail_retry_times: int = None,
        name: str = None,
        start_alert_enable: bool = None,
        tags: Dict[str, str] = None,
        task_params: main_models.UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams = None,
        task_type: str = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The node ID.
        # 
        # This parameter is required.
        self.code = code
        # The node description.
        self.description = description
        # Specifies whether to send alerts when the node fails.
        self.fail_alert_enable = fail_alert_enable
        # The number of retries when the node fails.
        self.fail_retry_times = fail_retry_times
        # The name of the job.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to send alerts when the node is started.
        self.start_alert_enable = start_alert_enable
        # The tags of the job.
        self.tags = tags
        # The job parameters.
        # 
        # This parameter is required.
        self.task_params = task_params
        # The type of the node.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The default timeout period of the node.
        self.timeout = timeout

    def validate(self):
        if self.task_params:
            self.task_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address

        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.fail_alert_enable is not None:
            result['failAlertEnable'] = self.fail_alert_enable

        if self.fail_retry_times is not None:
            result['failRetryTimes'] = self.fail_retry_times

        if self.name is not None:
            result['name'] = self.name

        if self.start_alert_enable is not None:
            result['startAlertEnable'] = self.start_alert_enable

        if self.tags is not None:
            result['tags'] = self.tags

        if self.task_params is not None:
            result['taskParams'] = self.task_params.to_map()

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.timeout is not None:
            result['timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('failAlertEnable') is not None:
            self.fail_alert_enable = m.get('failAlertEnable')

        if m.get('failRetryTimes') is not None:
            self.fail_retry_times = m.get('failRetryTimes')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('startAlertEnable') is not None:
            self.start_alert_enable = m.get('startAlertEnable')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('taskParams') is not None:
            temp_model = main_models.UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams()
            self.task_params = temp_model.from_map(m.get('taskParams'))

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        return self

class UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams(DaraModel):
    def __init__(
        self,
        display_spark_version: str = None,
        environment_id: str = None,
        fusion: bool = None,
        local_params: List[main_models.UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams] = None,
        resource_queue_id: str = None,
        spark_conf: List[main_models.UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf] = None,
        spark_driver_cores: int = None,
        spark_driver_memory: int = None,
        spark_executor_cores: int = None,
        spark_executor_memory: int = None,
        spark_log_level: str = None,
        spark_log_path: str = None,
        spark_version: str = None,
        task_biz_id: str = None,
        type: str = None,
        workspace_biz_id: str = None,
    ):
        # The displayed version of the Spark engine.
        self.display_spark_version = display_spark_version
        # The environment ID.
        self.environment_id = environment_id
        # Specifies whether to enable Fusion engine for acceleration.
        self.fusion = fusion
        self.local_params = local_params
        # The name of the queue on which the job runs.
        # 
        # This parameter is required.
        self.resource_queue_id = resource_queue_id
        # The configurations of the Spark jobs.
        self.spark_conf = spark_conf
        # The number of driver cores of the Spark job.
        self.spark_driver_cores = spark_driver_cores
        # The size of driver memory of the Spark job.
        self.spark_driver_memory = spark_driver_memory
        # The number of executor cores of the Spark job.
        self.spark_executor_cores = spark_executor_cores
        # The size of executor memory of the Spark job.
        self.spark_executor_memory = spark_executor_memory
        # The level of the Spark log.
        self.spark_log_level = spark_log_level
        # The path where the operational logs of the Spark job are stored.
        self.spark_log_path = spark_log_path
        # The version of the Spark engine.
        self.spark_version = spark_version
        # The ID of the data development job.
        # 
        # This parameter is required.
        self.task_biz_id = task_biz_id
        # The type of the Spark job.
        self.type = type
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_biz_id = workspace_biz_id

    def validate(self):
        if self.local_params:
            for v1 in self.local_params:
                 if v1:
                    v1.validate()
        if self.spark_conf:
            for v1 in self.spark_conf:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_spark_version is not None:
            result['displaySparkVersion'] = self.display_spark_version

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.fusion is not None:
            result['fusion'] = self.fusion

        result['localParams'] = []
        if self.local_params is not None:
            for k1 in self.local_params:
                result['localParams'].append(k1.to_map() if k1 else None)

        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id

        result['sparkConf'] = []
        if self.spark_conf is not None:
            for k1 in self.spark_conf:
                result['sparkConf'].append(k1.to_map() if k1 else None)

        if self.spark_driver_cores is not None:
            result['sparkDriverCores'] = self.spark_driver_cores

        if self.spark_driver_memory is not None:
            result['sparkDriverMemory'] = self.spark_driver_memory

        if self.spark_executor_cores is not None:
            result['sparkExecutorCores'] = self.spark_executor_cores

        if self.spark_executor_memory is not None:
            result['sparkExecutorMemory'] = self.spark_executor_memory

        if self.spark_log_level is not None:
            result['sparkLogLevel'] = self.spark_log_level

        if self.spark_log_path is not None:
            result['sparkLogPath'] = self.spark_log_path

        if self.spark_version is not None:
            result['sparkVersion'] = self.spark_version

        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id

        if self.type is not None:
            result['type'] = self.type

        if self.workspace_biz_id is not None:
            result['workspaceBizId'] = self.workspace_biz_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displaySparkVersion') is not None:
            self.display_spark_version = m.get('displaySparkVersion')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        self.local_params = []
        if m.get('localParams') is not None:
            for k1 in m.get('localParams'):
                temp_model = main_models.UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams()
                self.local_params.append(temp_model.from_map(k1))

        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')

        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k1 in m.get('sparkConf'):
                temp_model = main_models.UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf()
                self.spark_conf.append(temp_model.from_map(k1))

        if m.get('sparkDriverCores') is not None:
            self.spark_driver_cores = m.get('sparkDriverCores')

        if m.get('sparkDriverMemory') is not None:
            self.spark_driver_memory = m.get('sparkDriverMemory')

        if m.get('sparkExecutorCores') is not None:
            self.spark_executor_cores = m.get('sparkExecutorCores')

        if m.get('sparkExecutorMemory') is not None:
            self.spark_executor_memory = m.get('sparkExecutorMemory')

        if m.get('sparkLogLevel') is not None:
            self.spark_log_level = m.get('sparkLogLevel')

        if m.get('sparkLogPath') is not None:
            self.spark_log_path = m.get('sparkLogPath')

        if m.get('sparkVersion') is not None:
            self.spark_version = m.get('sparkVersion')

        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('workspaceBizId') is not None:
            self.workspace_biz_id = m.get('workspaceBizId')

        return self

class UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the SparkConf object.
        self.key = key
        # The value of the SparkConf object.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams(DaraModel):
    def __init__(
        self,
        direct: str = None,
        prop: str = None,
        type: str = None,
        value: str = None,
    ):
        self.direct = direct
        self.prop = prop
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direct is not None:
            result['direct'] = self.direct

        if self.prop is not None:
            result['prop'] = self.prop

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direct') is not None:
            self.direct = m.get('direct')

        if m.get('prop') is not None:
            self.prop = m.get('prop')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class UpdateProcessDefinitionWithScheduleRequestSchedule(DaraModel):
    def __init__(
        self,
        crontab: str = None,
        end_time: str = None,
        start_time: str = None,
        timezone_id: str = None,
    ):
        # The CRON expression that is used for scheduling.
        self.crontab = crontab
        # The end time of the scheduling.
        self.end_time = end_time
        # The start time of the scheduling.
        self.start_time = start_time
        # The ID of the time zone.
        self.timezone_id = timezone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crontab is not None:
            result['crontab'] = self.crontab

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.timezone_id is not None:
            result['timezoneId'] = self.timezone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crontab') is not None:
            self.crontab = m.get('crontab')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timezoneId') is not None:
            self.timezone_id = m.get('timezoneId')

        return self

class UpdateProcessDefinitionWithScheduleRequestGlobalParams(DaraModel):
    def __init__(
        self,
        direct: str = None,
        prop: str = None,
        type: str = None,
        value: str = None,
    ):
        self.direct = direct
        self.prop = prop
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direct is not None:
            result['direct'] = self.direct

        if self.prop is not None:
            result['prop'] = self.prop

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direct') is not None:
            self.direct = m.get('direct')

        if m.get('prop') is not None:
            self.prop = m.get('prop')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

