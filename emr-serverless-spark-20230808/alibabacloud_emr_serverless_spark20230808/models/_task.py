# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class Task(DaraModel):
    def __init__(
        self,
        archives: List[str] = None,
        artifact_url: str = None,
        biz_id: str = None,
        category_biz_id: str = None,
        content: str = None,
        creator: int = None,
        credential: main_models.TaskCredential = None,
        default_catalog_id: str = None,
        default_database: str = None,
        default_resource_queue_id: str = None,
        default_sql_compute_id: str = None,
        deployment_id: str = None,
        environment_id: str = None,
        extra_artifact_ids: List[str] = None,
        extra_spark_submit_params: str = None,
        files: List[str] = None,
        fusion: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        has_changed: bool = None,
        has_commited: bool = None,
        is_streaming: bool = None,
        jars: List[str] = None,
        kernel_id: str = None,
        last_run_resource_queue_id: str = None,
        modifier: int = None,
        name: str = None,
        params: Dict[str, str] = None,
        py_files: List[str] = None,
        session_cluster_id: str = None,
        spark_args: str = None,
        spark_conf: List[main_models.SparkConf] = None,
        spark_driver_cores: int = None,
        spark_driver_memory: int = None,
        spark_entrypoint: str = None,
        spark_executor_cores: int = None,
        spark_executor_memory: int = None,
        spark_log_level: str = None,
        spark_log_path: str = None,
        spark_submit_clause: str = None,
        spark_version: str = None,
        tags: Dict[str, str] = None,
        timeout: int = None,
        type: str = None,
    ):
        self.archives = archives
        self.artifact_url = artifact_url
        # This parameter is required.
        self.biz_id = biz_id
        self.category_biz_id = category_biz_id
        self.content = content
        # This parameter is required.
        self.creator = creator
        self.credential = credential
        self.default_catalog_id = default_catalog_id
        self.default_database = default_database
        self.default_resource_queue_id = default_resource_queue_id
        self.default_sql_compute_id = default_sql_compute_id
        self.deployment_id = deployment_id
        self.environment_id = environment_id
        self.extra_artifact_ids = extra_artifact_ids
        self.extra_spark_submit_params = extra_spark_submit_params
        self.files = files
        self.fusion = fusion
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        self.has_changed = has_changed
        # This parameter is required.
        self.has_commited = has_commited
        self.is_streaming = is_streaming
        self.jars = jars
        self.kernel_id = kernel_id
        self.last_run_resource_queue_id = last_run_resource_queue_id
        # This parameter is required.
        self.modifier = modifier
        # This parameter is required.
        self.name = name
        self.params = params
        self.py_files = py_files
        self.session_cluster_id = session_cluster_id
        self.spark_args = spark_args
        self.spark_conf = spark_conf
        # This parameter is required.
        self.spark_driver_cores = spark_driver_cores
        # This parameter is required.
        self.spark_driver_memory = spark_driver_memory
        self.spark_entrypoint = spark_entrypoint
        # This parameter is required.
        self.spark_executor_cores = spark_executor_cores
        # This parameter is required.
        self.spark_executor_memory = spark_executor_memory
        # This parameter is required.
        self.spark_log_level = spark_log_level
        # This parameter is required.
        self.spark_log_path = spark_log_path
        self.spark_submit_clause = spark_submit_clause
        # This parameter is required.
        self.spark_version = spark_version
        self.tags = tags
        self.timeout = timeout
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.credential:
            self.credential.validate()
        if self.spark_conf:
            for v1 in self.spark_conf:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archives is not None:
            result['archives'] = self.archives

        if self.artifact_url is not None:
            result['artifactUrl'] = self.artifact_url

        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.category_biz_id is not None:
            result['categoryBizId'] = self.category_biz_id

        if self.content is not None:
            result['content'] = self.content

        if self.creator is not None:
            result['creator'] = self.creator

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.default_catalog_id is not None:
            result['defaultCatalogId'] = self.default_catalog_id

        if self.default_database is not None:
            result['defaultDatabase'] = self.default_database

        if self.default_resource_queue_id is not None:
            result['defaultResourceQueueId'] = self.default_resource_queue_id

        if self.default_sql_compute_id is not None:
            result['defaultSqlComputeId'] = self.default_sql_compute_id

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.extra_artifact_ids is not None:
            result['extraArtifactIds'] = self.extra_artifact_ids

        if self.extra_spark_submit_params is not None:
            result['extraSparkSubmitParams'] = self.extra_spark_submit_params

        if self.files is not None:
            result['files'] = self.files

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.has_changed is not None:
            result['hasChanged'] = self.has_changed

        if self.has_commited is not None:
            result['hasCommited'] = self.has_commited

        if self.is_streaming is not None:
            result['isStreaming'] = self.is_streaming

        if self.jars is not None:
            result['jars'] = self.jars

        if self.kernel_id is not None:
            result['kernelId'] = self.kernel_id

        if self.last_run_resource_queue_id is not None:
            result['lastRunResourceQueueId'] = self.last_run_resource_queue_id

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.name is not None:
            result['name'] = self.name

        if self.params is not None:
            result['params'] = self.params

        if self.py_files is not None:
            result['pyFiles'] = self.py_files

        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id

        if self.spark_args is not None:
            result['sparkArgs'] = self.spark_args

        result['sparkConf'] = []
        if self.spark_conf is not None:
            for k1 in self.spark_conf:
                result['sparkConf'].append(k1.to_map() if k1 else None)

        if self.spark_driver_cores is not None:
            result['sparkDriverCores'] = self.spark_driver_cores

        if self.spark_driver_memory is not None:
            result['sparkDriverMemory'] = self.spark_driver_memory

        if self.spark_entrypoint is not None:
            result['sparkEntrypoint'] = self.spark_entrypoint

        if self.spark_executor_cores is not None:
            result['sparkExecutorCores'] = self.spark_executor_cores

        if self.spark_executor_memory is not None:
            result['sparkExecutorMemory'] = self.spark_executor_memory

        if self.spark_log_level is not None:
            result['sparkLogLevel'] = self.spark_log_level

        if self.spark_log_path is not None:
            result['sparkLogPath'] = self.spark_log_path

        if self.spark_submit_clause is not None:
            result['sparkSubmitClause'] = self.spark_submit_clause

        if self.spark_version is not None:
            result['sparkVersion'] = self.spark_version

        if self.tags is not None:
            result['tags'] = self.tags

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('archives') is not None:
            self.archives = m.get('archives')

        if m.get('artifactUrl') is not None:
            self.artifact_url = m.get('artifactUrl')

        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('categoryBizId') is not None:
            self.category_biz_id = m.get('categoryBizId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('credential') is not None:
            temp_model = main_models.TaskCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('defaultCatalogId') is not None:
            self.default_catalog_id = m.get('defaultCatalogId')

        if m.get('defaultDatabase') is not None:
            self.default_database = m.get('defaultDatabase')

        if m.get('defaultResourceQueueId') is not None:
            self.default_resource_queue_id = m.get('defaultResourceQueueId')

        if m.get('defaultSqlComputeId') is not None:
            self.default_sql_compute_id = m.get('defaultSqlComputeId')

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('extraArtifactIds') is not None:
            self.extra_artifact_ids = m.get('extraArtifactIds')

        if m.get('extraSparkSubmitParams') is not None:
            self.extra_spark_submit_params = m.get('extraSparkSubmitParams')

        if m.get('files') is not None:
            self.files = m.get('files')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('hasChanged') is not None:
            self.has_changed = m.get('hasChanged')

        if m.get('hasCommited') is not None:
            self.has_commited = m.get('hasCommited')

        if m.get('isStreaming') is not None:
            self.is_streaming = m.get('isStreaming')

        if m.get('jars') is not None:
            self.jars = m.get('jars')

        if m.get('kernelId') is not None:
            self.kernel_id = m.get('kernelId')

        if m.get('lastRunResourceQueueId') is not None:
            self.last_run_resource_queue_id = m.get('lastRunResourceQueueId')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('pyFiles') is not None:
            self.py_files = m.get('pyFiles')

        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')

        if m.get('sparkArgs') is not None:
            self.spark_args = m.get('sparkArgs')

        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k1 in m.get('sparkConf'):
                temp_model = main_models.SparkConf()
                self.spark_conf.append(temp_model.from_map(k1))

        if m.get('sparkDriverCores') is not None:
            self.spark_driver_cores = m.get('sparkDriverCores')

        if m.get('sparkDriverMemory') is not None:
            self.spark_driver_memory = m.get('sparkDriverMemory')

        if m.get('sparkEntrypoint') is not None:
            self.spark_entrypoint = m.get('sparkEntrypoint')

        if m.get('sparkExecutorCores') is not None:
            self.spark_executor_cores = m.get('sparkExecutorCores')

        if m.get('sparkExecutorMemory') is not None:
            self.spark_executor_memory = m.get('sparkExecutorMemory')

        if m.get('sparkLogLevel') is not None:
            self.spark_log_level = m.get('sparkLogLevel')

        if m.get('sparkLogPath') is not None:
            self.spark_log_path = m.get('sparkLogPath')

        if m.get('sparkSubmitClause') is not None:
            self.spark_submit_clause = m.get('sparkSubmitClause')

        if m.get('sparkVersion') is not None:
            self.spark_version = m.get('sparkVersion')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class TaskCredential(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        access_url: str = None,
        expire: int = None,
        host: str = None,
        path: str = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.access_url = access_url
        self.expire = expire
        self.host = host
        self.path = path
        self.policy = policy
        self.security_token = security_token
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['accessId'] = self.access_id

        if self.access_url is not None:
            result['accessUrl'] = self.access_url

        if self.expire is not None:
            result['expire'] = self.expire

        if self.host is not None:
            result['host'] = self.host

        if self.path is not None:
            result['path'] = self.path

        if self.policy is not None:
            result['policy'] = self.policy

        if self.security_token is not None:
            result['securityToken'] = self.security_token

        if self.signature is not None:
            result['signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')

        if m.get('accessUrl') is not None:
            self.access_url = m.get('accessUrl')

        if m.get('expire') is not None:
            self.expire = m.get('expire')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        return self

