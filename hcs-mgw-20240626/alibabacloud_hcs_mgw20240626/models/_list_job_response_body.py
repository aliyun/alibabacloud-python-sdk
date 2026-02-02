# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class ListJobResponseBody(DaraModel):
    def __init__(
        self,
        import_job_list: main_models.ListJobResp = None,
    ):
        # The queried migration tasks.
        self.import_job_list = import_job_list

    def validate(self):
        if self.import_job_list:
            self.import_job_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_job_list is not None:
            result['ImportJobList'] = self.import_job_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportJobList') is not None:
            temp_model = main_models.ListJobResp()
            self.import_job_list = temp_model.from_map(m.get('ImportJobList'))

        return self

