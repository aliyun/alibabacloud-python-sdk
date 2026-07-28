# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class TuningHistory(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        annotations: Dict[str, str] = None,
        deployment_name: str = None,
        is_hot_update: bool = None,
        job_id: str = None,
        new_resource_setting: main_models.TuningHistoryNewResourceSetting = None,
        old_resource_setting: main_models.TuningHistoryOldResourceSetting = None,
        trigger_time: int = None,
        tuning_id: str = None,
        tuning_message: str = None,
        tuning_state: str = None,
    ):
        self.action_type = action_type
        self.annotations = annotations
        self.deployment_name = deployment_name
        self.is_hot_update = is_hot_update
        self.job_id = job_id
        self.new_resource_setting = new_resource_setting
        self.old_resource_setting = old_resource_setting
        self.trigger_time = trigger_time
        self.tuning_id = tuning_id
        self.tuning_message = tuning_message
        self.tuning_state = tuning_state

    def validate(self):
        if self.new_resource_setting:
            self.new_resource_setting.validate()
        if self.old_resource_setting:
            self.old_resource_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['actionType'] = self.action_type

        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        if self.is_hot_update is not None:
            result['isHotUpdate'] = self.is_hot_update

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.new_resource_setting is not None:
            result['newResourceSetting'] = self.new_resource_setting.to_map()

        if self.old_resource_setting is not None:
            result['oldResourceSetting'] = self.old_resource_setting.to_map()

        if self.trigger_time is not None:
            result['triggerTime'] = self.trigger_time

        if self.tuning_id is not None:
            result['tuningId'] = self.tuning_id

        if self.tuning_message is not None:
            result['tuningMessage'] = self.tuning_message

        if self.tuning_state is not None:
            result['tuningState'] = self.tuning_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')

        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        if m.get('isHotUpdate') is not None:
            self.is_hot_update = m.get('isHotUpdate')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('newResourceSetting') is not None:
            temp_model = main_models.TuningHistoryNewResourceSetting()
            self.new_resource_setting = temp_model.from_map(m.get('newResourceSetting'))

        if m.get('oldResourceSetting') is not None:
            temp_model = main_models.TuningHistoryOldResourceSetting()
            self.old_resource_setting = temp_model.from_map(m.get('oldResourceSetting'))

        if m.get('triggerTime') is not None:
            self.trigger_time = m.get('triggerTime')

        if m.get('tuningId') is not None:
            self.tuning_id = m.get('tuningId')

        if m.get('tuningMessage') is not None:
            self.tuning_message = m.get('tuningMessage')

        if m.get('tuningState') is not None:
            self.tuning_state = m.get('tuningState')

        return self

class TuningHistoryOldResourceSetting(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        memory: str = None,
        parallelism: int = None,
    ):
        self.cpu = cpu
        self.memory = memory
        self.parallelism = parallelism

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.memory is not None:
            result['memory'] = self.memory

        if self.parallelism is not None:
            result['parallelism'] = self.parallelism

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')

        return self

class TuningHistoryNewResourceSetting(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        memory: str = None,
        parallelism: int = None,
    ):
        self.cpu = cpu
        self.memory = memory
        self.parallelism = parallelism

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.memory is not None:
            result['memory'] = self.memory

        if self.parallelism is not None:
            result['parallelism'] = self.parallelism

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')

        return self

