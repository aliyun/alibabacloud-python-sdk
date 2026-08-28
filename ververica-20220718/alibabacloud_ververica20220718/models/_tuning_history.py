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
        # The action type. Valid values:
        # - SCALE_UP_PARALLELISM: scales up parallelism.
        # - SCALE_DOWN_PARALLELISM: scales down parallelism.
        # - SCALE_UP_MEMORY: scales up memory.
        # - RESTART: restarts the job.
        self.action_type = action_type
        # The additional annotations.
        self.annotations = annotations
        # The full path name of the deployment.
        self.deployment_name = deployment_name
        # Indicates whether this is a hot update. A value of true indicates that the change takes effect without restarting the job. A value of false indicates that the job must be restarted.
        self.is_hot_update = is_hot_update
        # The ID of the associated job.
        self.job_id = job_id
        # The resource configuration after tuning. This value may be null if the tuning failed.
        self.new_resource_setting = new_resource_setting
        # The resource configuration before tuning.
        self.old_resource_setting = old_resource_setting
        # The trigger timestamp in milliseconds.
        self.trigger_time = trigger_time
        # The UUID of the tuning record.
        self.tuning_id = tuning_id
        # The tuning message. This is an internationalized, human-readable string that is not recommended for programmatic parsing.
        self.tuning_message = tuning_message
        # The tuning state. Valid values:
        # - SUCCESS: The tuning succeeded.
        # - FAILED: The tuning failed.
        # - EXECUTING: The tuning is in progress.
        # - TERMINATED: The tuning was terminated.
        # - FAILED_WITH_ROLLBACK_SUCCESS: The tuning failed but the rollback succeeded.
        # - FAILED_WITH_ROLLBACK_FAILED: The tuning failed and the rollback also failed.
        # - FAILED_WITH_RESOURCE_LACK: The tuning failed due to insufficient resources.
        # - FAILED_WITH_SAME_RESOURCE_SETTING: The tuning failed because the resource configuration did not change.
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
        # The number of CPU cores per TaskManager.
        self.cpu = cpu
        # The memory per TaskManager, in a format such as 4 Gi.
        self.memory = memory
        # The parallelism.
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
        # The number of CPU cores per TaskManager.
        self.cpu = cpu
        # The memory per TaskManager, in a format such as 4 Gi.
        self.memory = memory
        # The parallelism.
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

