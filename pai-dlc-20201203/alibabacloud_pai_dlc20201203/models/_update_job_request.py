# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class UpdateJobRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        job_specs: List[main_models.JobSpec] = None,
        priority: int = None,
    ):
        # The job visibility. Valid values:
        # 
        # *   PUBLIC: The job is visible to all members in the workspace.
        # *   PRIVATE: The job is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        self.job_specs = job_specs
        # The job priority. Valid values: 1 to 9.
        # 
        # *   1: the lowest priority.
        # *   9: the highest priority.
        self.priority = priority

    def validate(self):
        if self.job_specs:
            for v1 in self.job_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k1 in self.job_specs:
                result['JobSpecs'].append(k1.to_map() if k1 else None)

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k1 in m.get('JobSpecs'):
                temp_model = main_models.JobSpec()
                self.job_specs.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

