# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class HotUpdateJobResult(DaraModel):
    def __init__(
        self,
        hot_update_params: main_models.HotUpdateJobParams = None,
        job_hot_update_id: str = None,
        job_id: str = None,
        status: main_models.HotUpdateJobStatus = None,
        target_resource_setting: main_models.BriefResourceSetting = None,
    ):
        self.hot_update_params = hot_update_params
        self.job_hot_update_id = job_hot_update_id
        self.job_id = job_id
        self.status = status
        self.target_resource_setting = target_resource_setting

    def validate(self):
        if self.hot_update_params:
            self.hot_update_params.validate()
        if self.status:
            self.status.validate()
        if self.target_resource_setting:
            self.target_resource_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hot_update_params is not None:
            result['hotUpdateParams'] = self.hot_update_params.to_map()

        if self.job_hot_update_id is not None:
            result['jobHotUpdateId'] = self.job_hot_update_id

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.target_resource_setting is not None:
            result['targetResourceSetting'] = self.target_resource_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotUpdateParams') is not None:
            temp_model = main_models.HotUpdateJobParams()
            self.hot_update_params = temp_model.from_map(m.get('hotUpdateParams'))

        if m.get('jobHotUpdateId') is not None:
            self.job_hot_update_id = m.get('jobHotUpdateId')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('status') is not None:
            temp_model = main_models.HotUpdateJobStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('targetResourceSetting') is not None:
            temp_model = main_models.BriefResourceSetting()
            self.target_resource_setting = temp_model.from_map(m.get('targetResourceSetting'))

        return self

