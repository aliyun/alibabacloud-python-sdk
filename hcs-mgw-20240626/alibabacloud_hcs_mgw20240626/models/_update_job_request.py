# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class UpdateJobRequest(DaraModel):
    def __init__(
        self,
        import_job: main_models.UpdateJobInfo = None,
    ):
        # The details for updating the task.
        self.import_job = import_job

    def validate(self):
        if self.import_job:
            self.import_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_job is not None:
            result['ImportJob'] = self.import_job.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportJob') is not None:
            temp_model = main_models.UpdateJobInfo()
            self.import_job = temp_model.from_map(m.get('ImportJob'))

        return self

