# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ExpertResourceSetting(DaraModel):
    def __init__(
        self,
        jobmanager_resource_setting_spec: main_models.BasicResourceSettingSpec = None,
        resource_plan: str = None,
    ):
        # The basic resource configuration of the JobManager.
        self.jobmanager_resource_setting_spec = jobmanager_resource_setting_spec
        # The resource configuration plan of the deployment in expert mode.
        self.resource_plan = resource_plan

    def validate(self):
        if self.jobmanager_resource_setting_spec:
            self.jobmanager_resource_setting_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jobmanager_resource_setting_spec is not None:
            result['jobmanagerResourceSettingSpec'] = self.jobmanager_resource_setting_spec.to_map()

        if self.resource_plan is not None:
            result['resourcePlan'] = self.resource_plan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobmanagerResourceSettingSpec') is not None:
            temp_model = main_models.BasicResourceSettingSpec()
            self.jobmanager_resource_setting_spec = temp_model.from_map(m.get('jobmanagerResourceSettingSpec'))

        if m.get('resourcePlan') is not None:
            self.resource_plan = m.get('resourcePlan')

        return self

