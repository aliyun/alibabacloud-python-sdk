# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class ListJobHistoryResponseBody(DaraModel):
    def __init__(
        self,
        job_history_list: main_models.ListJobHistoryResp = None,
    ):
        # The running history of the migration task.
        self.job_history_list = job_history_list

    def validate(self):
        if self.job_history_list:
            self.job_history_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_history_list is not None:
            result['JobHistoryList'] = self.job_history_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobHistoryList') is not None:
            temp_model = main_models.ListJobHistoryResp()
            self.job_history_list = temp_model.from_map(m.get('JobHistoryList'))

        return self

