# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListExperimentsResponseBody(DaraModel):
    def __init__(
        self,
        experiments: List[main_models.ListExperimentsResponseBodyExperiments] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.experiments = experiments
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.experiments:
            for v1 in self.experiments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Experiments'] = []
        if self.experiments is not None:
            for k1 in self.experiments:
                result['Experiments'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiments = []
        if m.get('Experiments') is not None:
            for k1 in m.get('Experiments'):
                temp_model = main_models.ListExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListExperimentsResponseBodyExperiments(DaraModel):
    def __init__(
        self,
        alias_experiment_id: str = None,
        buckets: str = None,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        experiment_group_id: str = None,
        experiment_id: str = None,
        flow_percent: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.alias_experiment_id = alias_experiment_id
        self.buckets = buckets
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.experiment_group_id = experiment_group_id
        self.experiment_id = experiment_id
        self.flow_percent = flow_percent
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_experiment_id is not None:
            result['AliasExperimentId'] = self.alias_experiment_id

        if self.buckets is not None:
            result['Buckets'] = self.buckets

        if self.config is not None:
            result['Config'] = self.config

        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id

        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users

        if self.description is not None:
            result['Description'] = self.description

        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id

        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id

        if self.layer_id is not None:
            result['LayerId'] = self.layer_id

        if self.name is not None:
            result['Name'] = self.name

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasExperimentId') is not None:
            self.alias_experiment_id = m.get('AliasExperimentId')

        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')

        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')

        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')

        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

