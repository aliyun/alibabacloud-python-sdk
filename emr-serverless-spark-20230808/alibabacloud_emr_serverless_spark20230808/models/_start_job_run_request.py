# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class StartJobRunRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        code_type: str = None,
        configuration_overrides: main_models.StartJobRunRequestConfigurationOverrides = None,
        display_release_version: str = None,
        execution_timeout_seconds: int = None,
        fusion: bool = None,
        job_driver: main_models.JobDriver = None,
        job_id: str = None,
        name: str = None,
        release_version: str = None,
        resource_queue_id: str = None,
        tags: List[main_models.Tag] = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The code type of the job. Valid values:
        # 
        # *   SQL
        # *   JAR
        # *   PYTHON
        self.code_type = code_type
        # The advanced configurations of Spark.
        self.configuration_overrides = configuration_overrides
        # The version of the Spark engine.
        self.display_release_version = display_release_version
        # The timeout period of the job.
        self.execution_timeout_seconds = execution_timeout_seconds
        # Specifies whether to enable Fusion engine for acceleration.
        self.fusion = fusion
        # The information about Spark Driver.
        self.job_driver = job_driver
        # The job ID.
        self.job_id = job_id
        # The name of the job.
        self.name = name
        # The version number of Spark.
        self.release_version = release_version
        # The name of the resource queue on which the Spark job runs.
        self.resource_queue_id = resource_queue_id
        # The tags of the job.
        self.tags = tags
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.configuration_overrides:
            self.configuration_overrides.validate()
        if self.job_driver:
            self.job_driver.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.code_type is not None:
            result['codeType'] = self.code_type

        if self.configuration_overrides is not None:
            result['configurationOverrides'] = self.configuration_overrides.to_map()

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.name is not None:
            result['name'] = self.name

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')

        if m.get('configurationOverrides') is not None:
            temp_model = main_models.StartJobRunRequestConfigurationOverrides()
            self.configuration_overrides = temp_model.from_map(m.get('configurationOverrides'))

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('jobDriver') is not None:
            temp_model = main_models.JobDriver()
            self.job_driver = temp_model.from_map(m.get('jobDriver'))

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class StartJobRunRequestConfigurationOverrides(DaraModel):
    def __init__(
        self,
        configurations: List[main_models.StartJobRunRequestConfigurationOverridesConfigurations] = None,
    ):
        # The SparkConf objects.
        self.configurations = configurations

    def validate(self):
        if self.configurations:
            for v1 in self.configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['configurations'] = []
        if self.configurations is not None:
            for k1 in self.configurations:
                result['configurations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k1 in m.get('configurations'):
                temp_model = main_models.StartJobRunRequestConfigurationOverridesConfigurations()
                self.configurations.append(temp_model.from_map(k1))

        return self

class StartJobRunRequestConfigurationOverridesConfigurations(DaraModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # The configuration file of SparkConf.
        self.config_file_name = config_file_name
        # The key of SparkConf.
        self.config_item_key = config_item_key
        # The value of SparkConf.
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')

        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')

        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')

        return self

