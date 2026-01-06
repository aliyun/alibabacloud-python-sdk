# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class Run(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[main_models.RunLabel] = None,
        metrics: List[main_models.RunMetric] = None,
        name: str = None,
        owner_id: str = None,
        params: List[main_models.RunParam] = None,
        request_id: str = None,
        run_id: str = None,
        source_id: str = None,
        source_type: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.labels = labels
        self.metrics = metrics
        self.name = name
        self.owner_id = owner_id
        self.params = params
        self.request_id = request_id
        self.run_id = run_id
        self.source_id = source_id
        self.source_type = source_type
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.RunLabel()
                self.labels.append(temp_model.from_map(k1))

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.RunMetric()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.RunParam()
                self.params.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

