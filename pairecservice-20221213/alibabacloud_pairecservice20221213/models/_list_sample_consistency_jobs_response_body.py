# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListSampleConsistencyJobsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sample_consistency_jobs: List[main_models.ListSampleConsistencyJobsResponseBodySampleConsistencyJobs] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sample_consistency_jobs = sample_consistency_jobs
        self.total_count = total_count

    def validate(self):
        if self.sample_consistency_jobs:
            for v1 in self.sample_consistency_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SampleConsistencyJobs'] = []
        if self.sample_consistency_jobs is not None:
            for k1 in self.sample_consistency_jobs:
                result['SampleConsistencyJobs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sample_consistency_jobs = []
        if m.get('SampleConsistencyJobs') is not None:
            for k1 in m.get('SampleConsistencyJobs'):
                temp_model = main_models.ListSampleConsistencyJobsResponseBodySampleConsistencyJobs()
                self.sample_consistency_jobs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSampleConsistencyJobsResponseBodySampleConsistencyJobs(DaraModel):
    def __init__(
        self,
        config: str = None,
        duration: str = None,
        eas_model_service_name: str = None,
        end_time: int = None,
        feature_save_resource_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_id_field: str = None,
        logs: str = None,
        name: str = None,
        partition_field: str = None,
        partition_field_format: str = None,
        request_id_field: str = None,
        sample_consistency_job_id: str = None,
        sample_rate: str = None,
        sample_table_name: str = None,
        scene_id: str = None,
        scene_name: str = None,
        start_time: int = None,
        status: str = None,
        user_id_field: str = None,
    ):
        self.config = config
        self.duration = duration
        self.eas_model_service_name = eas_model_service_name
        self.end_time = end_time
        self.feature_save_resource_id = feature_save_resource_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_id_field = item_id_field
        self.logs = logs
        self.name = name
        self.partition_field = partition_field
        self.partition_field_format = partition_field_format
        self.request_id_field = request_id_field
        self.sample_consistency_job_id = sample_consistency_job_id
        self.sample_rate = sample_rate
        self.sample_table_name = sample_table_name
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.start_time = start_time
        self.status = status
        self.user_id_field = user_id_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.eas_model_service_name is not None:
            result['EasModelServiceName'] = self.eas_model_service_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.feature_save_resource_id is not None:
            result['FeatureSaveResourceId'] = self.feature_save_resource_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field

        if self.logs is not None:
            result['Logs'] = self.logs

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_field is not None:
            result['PartitionField'] = self.partition_field

        if self.partition_field_format is not None:
            result['PartitionFieldFormat'] = self.partition_field_format

        if self.request_id_field is not None:
            result['RequestIdField'] = self.request_id_field

        if self.sample_consistency_job_id is not None:
            result['SampleConsistencyJobId'] = self.sample_consistency_job_id

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.sample_table_name is not None:
            result['SampleTableName'] = self.sample_table_name

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EasModelServiceName') is not None:
            self.eas_model_service_name = m.get('EasModelServiceName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FeatureSaveResourceId') is not None:
            self.feature_save_resource_id = m.get('FeatureSaveResourceId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')

        if m.get('Logs') is not None:
            self.logs = m.get('Logs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionField') is not None:
            self.partition_field = m.get('PartitionField')

        if m.get('PartitionFieldFormat') is not None:
            self.partition_field_format = m.get('PartitionFieldFormat')

        if m.get('RequestIdField') is not None:
            self.request_id_field = m.get('RequestIdField')

        if m.get('SampleConsistencyJobId') is not None:
            self.sample_consistency_job_id = m.get('SampleConsistencyJobId')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('SampleTableName') is not None:
            self.sample_table_name = m.get('SampleTableName')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')

        return self

