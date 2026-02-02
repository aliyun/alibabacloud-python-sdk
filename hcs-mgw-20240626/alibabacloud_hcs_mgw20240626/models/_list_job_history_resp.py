# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class ListJobHistoryResp(DaraModel):
    def __init__(
        self,
        job_history: List[main_models.JobHistory] = None,
        next_marker: str = None,
        truncated: str = None,
    ):
        self.job_history = job_history
        self.next_marker = next_marker
        self.truncated = truncated

    def validate(self):
        if self.job_history:
            for v1 in self.job_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobHistory'] = []
        if self.job_history is not None:
            for k1 in self.job_history:
                result['JobHistory'].append(k1.to_map() if k1 else None)

        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker

        if self.truncated is not None:
            result['Truncated'] = self.truncated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_history = []
        if m.get('JobHistory') is not None:
            for k1 in m.get('JobHistory'):
                temp_model = main_models.JobHistory()
                self.job_history.append(temp_model.from_map(k1))

        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')

        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')

        return self

