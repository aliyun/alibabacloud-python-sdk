# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateRunRequest(DaraModel):
    def __init__(
        self,
        experiment_id: str = None,
        labels: List[main_models.Label] = None,
        name: str = None,
        params: List[main_models.RunParam] = None,
        source_id: str = None,
        source_type: str = None,
    ):
        # The ID of the experiment associated with the run.
        # 
        # This parameter is required.
        self.experiment_id = experiment_id
        # The list of labels for the run.
        self.labels = labels
        # The name of the run. The naming convention is as follows:
        # 
        # - Starts with a lowercase or uppercase letter.
        # 
        # - Can contain lowercase letters, uppercase letters, digits, underscores (_), and hyphens (-).
        # 
        # - The length must be 1 to 63 characters.
        # 
        # If this parameter is left empty, the server-generated random ID (RunID) is used as the name.
        self.name = name
        # The list of parameters for the run.
        self.params = params
        # The ID of the PAI workload associated with the run.
        self.source_id = source_id
        # The source type of the PAI workload associated with the run. Options include TrainingService, DLC, or empty. This parameter is optional. The default value is empty.
        self.source_type = source_type

    def validate(self):
        if self.labels:
            for v1 in self.labels:
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
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.RunParam()
                self.params.append(temp_model.from_map(k1))

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

