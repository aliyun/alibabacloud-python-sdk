# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class GetJobResultResponseBody(DaraModel):
    def __init__(
        self,
        import_job_result: main_models.GetJobResultResp = None,
    ):
        # The details for obtaining the retries of the migration task.
        self.import_job_result = import_job_result

    def validate(self):
        if self.import_job_result:
            self.import_job_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_job_result is not None:
            result['ImportJobResult'] = self.import_job_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportJobResult') is not None:
            temp_model = main_models.GetJobResultResp()
            self.import_job_result = temp_model.from_map(m.get('ImportJobResult'))

        return self

