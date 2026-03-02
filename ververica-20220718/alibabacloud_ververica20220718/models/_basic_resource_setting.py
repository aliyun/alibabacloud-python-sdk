# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class BasicResourceSetting(DaraModel):
    def __init__(
        self,
        jobmanager_resource_setting_spec: main_models.BasicResourceSettingSpec = None,
        parallelism: int = None,
        taskmanager_resource_setting_spec: main_models.BasicResourceSettingSpec = None,
    ):
        # The resource configuration of the JobManager.
        self.jobmanager_resource_setting_spec = jobmanager_resource_setting_spec
        # The parallelism for a deployment.
        self.parallelism = parallelism
        # The resource configuration of a TaskManager.
        self.taskmanager_resource_setting_spec = taskmanager_resource_setting_spec

    def validate(self):
        if self.jobmanager_resource_setting_spec:
            self.jobmanager_resource_setting_spec.validate()
        if self.taskmanager_resource_setting_spec:
            self.taskmanager_resource_setting_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jobmanager_resource_setting_spec is not None:
            result['jobmanagerResourceSettingSpec'] = self.jobmanager_resource_setting_spec.to_map()

        if self.parallelism is not None:
            result['parallelism'] = self.parallelism

        if self.taskmanager_resource_setting_spec is not None:
            result['taskmanagerResourceSettingSpec'] = self.taskmanager_resource_setting_spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobmanagerResourceSettingSpec') is not None:
            temp_model = main_models.BasicResourceSettingSpec()
            self.jobmanager_resource_setting_spec = temp_model.from_map(m.get('jobmanagerResourceSettingSpec'))

        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')

        if m.get('taskmanagerResourceSettingSpec') is not None:
            temp_model = main_models.BasicResourceSettingSpec()
            self.taskmanager_resource_setting_spec = temp_model.from_map(m.get('taskmanagerResourceSettingSpec'))

        return self

