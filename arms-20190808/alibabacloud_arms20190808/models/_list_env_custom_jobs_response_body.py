# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEnvCustomJobsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListEnvCustomJobsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListEnvCustomJobsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEnvCustomJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_release_name: str = None,
        addon_version: str = None,
        config_yaml: str = None,
        creation_timestamp: str = None,
        custom_job_name: str = None,
        environment_id: str = None,
        region_id: str = None,
        scrape_configs: List[main_models.ListEnvCustomJobsResponseBodyDataScrapeConfigs] = None,
        status: str = None,
    ):
        # The name of the add-on to which the custom job belongs.
        self.addon_name = addon_name
        # The instance name of the add-on.
        self.addon_release_name = addon_release_name
        # The version of the add-on.
        self.addon_version = addon_version
        # If the request parameter EncryptYaml is set to true, a Base64-encoded YAML string is returned. Otherwise, a plaintext YAML string is returned.
        self.config_yaml = config_yaml
        # The time when the custom job was created. The value of this parameter is a timestamp.
        self.creation_timestamp = creation_timestamp
        # The name of the custom job.
        self.custom_job_name = custom_job_name
        # The ID of the environment instance.
        self.environment_id = environment_id
        # The region ID.
        self.region_id = region_id
        # The capture configurations.
        self.scrape_configs = scrape_configs
        # The status of the custom job.
        self.status = status

    def validate(self):
        if self.scrape_configs:
            for v1 in self.scrape_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name

        if self.addon_release_name is not None:
            result['AddonReleaseName'] = self.addon_release_name

        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version

        if self.config_yaml is not None:
            result['ConfigYaml'] = self.config_yaml

        if self.creation_timestamp is not None:
            result['CreationTimestamp'] = self.creation_timestamp

        if self.custom_job_name is not None:
            result['CustomJobName'] = self.custom_job_name

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ScrapeConfigs'] = []
        if self.scrape_configs is not None:
            for k1 in self.scrape_configs:
                result['ScrapeConfigs'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('AddonReleaseName') is not None:
            self.addon_release_name = m.get('AddonReleaseName')

        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')

        if m.get('ConfigYaml') is not None:
            self.config_yaml = m.get('ConfigYaml')

        if m.get('CreationTimestamp') is not None:
            self.creation_timestamp = m.get('CreationTimestamp')

        if m.get('CustomJobName') is not None:
            self.custom_job_name = m.get('CustomJobName')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.scrape_configs = []
        if m.get('ScrapeConfigs') is not None:
            for k1 in m.get('ScrapeConfigs'):
                temp_model = main_models.ListEnvCustomJobsResponseBodyDataScrapeConfigs()
                self.scrape_configs.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListEnvCustomJobsResponseBodyDataScrapeConfigs(DaraModel):
    def __init__(
        self,
        job_name: str = None,
        metrics_path: str = None,
        scrape_discoverys: List[str] = None,
        scrape_interval: str = None,
    ):
        # The name of the job.
        self.job_name = job_name
        # The path of the metric.
        self.metrics_path = metrics_path
        # The service discovery methods.
        self.scrape_discoverys = scrape_discoverys
        # The capture interval.
        self.scrape_interval = scrape_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.metrics_path is not None:
            result['MetricsPath'] = self.metrics_path

        if self.scrape_discoverys is not None:
            result['ScrapeDiscoverys'] = self.scrape_discoverys

        if self.scrape_interval is not None:
            result['ScrapeInterval'] = self.scrape_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('MetricsPath') is not None:
            self.metrics_path = m.get('MetricsPath')

        if m.get('ScrapeDiscoverys') is not None:
            self.scrape_discoverys = m.get('ScrapeDiscoverys')

        if m.get('ScrapeInterval') is not None:
            self.scrape_interval = m.get('ScrapeInterval')

        return self

