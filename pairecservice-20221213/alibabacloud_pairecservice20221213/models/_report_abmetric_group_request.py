# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportABMetricGroupRequest(DaraModel):
    def __init__(
        self,
        base_experiment_id: str = None,
        dimension_fields: str = None,
        end_date: str = None,
        experiment_group_id: str = None,
        experiment_ids: str = None,
        instance_id: str = None,
        report_type: str = None,
        scene_id: str = None,
        start_date: str = None,
        time_statistics_method: str = None,
    ):
        # The ID of the base experiment.
        # 
        # This parameter is required.
        self.base_experiment_id = base_experiment_id
        # The dimension fields.
        self.dimension_fields = dimension_fields
        # The end date.
        self.end_date = end_date
        # The ID of the experiment group. You can call the [ListExperimentGroups](https://help.aliyun.com/document_detail/2402573.html) operation to obtain the ID of the experiment group. This parameter is required for offline and real-time reports.
        self.experiment_group_id = experiment_group_id
        # The IDs of the experiments. You can call the [ListExperiments](https://help.aliyun.com/document_detail/2402582.html) operation to obtain the IDs of the experiments.
        # 
        # This parameter is required.
        self.experiment_ids = experiment_ids
        # The instance ID. You can call the [ListInstances](https://help.aliyun.com/document_detail/2411819.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the report.
        # 
        # - Realtime: real-time report.
        # 
        # - Offline: offline report.
        # 
        # - Market: dashboard report.
        # 
        # This parameter is required.
        self.report_type = report_type
        # The ID of the scene. You can call the [ListScenes](https://help.aliyun.com/document_detail/2402581.html) operation to obtain the scene ID.
        self.scene_id = scene_id
        # The start date.
        self.start_date = start_date
        # The time statistics method. This parameter is required for real-time reports.
        # 
        # - Hour: The statistics are collected by hour.
        # 
        # - Day: The statistics are accumulated from 00:00 on the current day.
        self.time_statistics_method = time_statistics_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_experiment_id is not None:
            result['BaseExperimentId'] = self.base_experiment_id

        if self.dimension_fields is not None:
            result['DimensionFields'] = self.dimension_fields

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id

        if self.experiment_ids is not None:
            result['ExperimentIds'] = self.experiment_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.time_statistics_method is not None:
            result['TimeStatisticsMethod'] = self.time_statistics_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseExperimentId') is not None:
            self.base_experiment_id = m.get('BaseExperimentId')

        if m.get('DimensionFields') is not None:
            self.dimension_fields = m.get('DimensionFields')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')

        if m.get('ExperimentIds') is not None:
            self.experiment_ids = m.get('ExperimentIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TimeStatisticsMethod') is not None:
            self.time_statistics_method = m.get('TimeStatisticsMethod')

        return self

