# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class Experiment(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        artifact_uri: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[main_models.ExperimentLabel] = None,
        latest_run: main_models.Run = None,
        name: str = None,
        owner_id: str = None,
        request_id: str = None,
        tensorboard_log_uri: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.artifact_uri = artifact_uri
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.labels = labels
        self.latest_run = latest_run
        self.name = name
        self.owner_id = owner_id
        self.request_id = request_id
        self.tensorboard_log_uri = tensorboard_log_uri
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.latest_run:
            self.latest_run.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.artifact_uri is not None:
            result['ArtifactUri'] = self.artifact_uri

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

        if self.latest_run is not None:
            result['LatestRun'] = self.latest_run.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tensorboard_log_uri is not None:
            result['TensorboardLogUri'] = self.tensorboard_log_uri

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('ArtifactUri') is not None:
            self.artifact_uri = m.get('ArtifactUri')

        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ExperimentLabel()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatestRun') is not None:
            temp_model = main_models.Run()
            self.latest_run = temp_model.from_map(m.get('LatestRun'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TensorboardLogUri') is not None:
            self.tensorboard_log_uri = m.get('TensorboardLogUri')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

