# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class HotUpdateJobParams(DaraModel):
    def __init__(
        self,
        rescale_job_param: main_models.RescaleJobParam = None,
        update_job_config_param: main_models.UpdateJobConfigParam = None,
    ):
        self.rescale_job_param = rescale_job_param
        self.update_job_config_param = update_job_config_param

    def validate(self):
        if self.rescale_job_param:
            self.rescale_job_param.validate()
        if self.update_job_config_param:
            self.update_job_config_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rescale_job_param is not None:
            result['rescaleJobParam'] = self.rescale_job_param.to_map()

        if self.update_job_config_param is not None:
            result['updateJobConfigParam'] = self.update_job_config_param.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rescaleJobParam') is not None:
            temp_model = main_models.RescaleJobParam()
            self.rescale_job_param = temp_model.from_map(m.get('rescaleJobParam'))

        if m.get('updateJobConfigParam') is not None:
            temp_model = main_models.UpdateJobConfigParam()
            self.update_job_config_param = temp_model.from_map(m.get('updateJobConfigParam'))

        return self

