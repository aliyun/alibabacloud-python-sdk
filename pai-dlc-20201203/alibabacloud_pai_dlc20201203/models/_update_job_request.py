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
        description: str = None,
        job_specs: List[main_models.JobSpec] = None,
        priority: int = None,
        user_command: str = None,
    ):
        # The visibility of the job. The visibility can only be expanded, not reduced. Valid values:
        # - PUBLIC: visible to all users in the workspace.
        self.accessibility = accessibility
        self.description = description
        # The job specification definition.
        self.job_specs = job_specs
        # The priority of the job. Valid values: 1 to 9.
        # - 1: the lowest priority.
        # - 9: the highest priority.
        self.priority = priority
        # The user command.
        self.user_command = user_command

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

        if self.description is not None:
            result['Description'] = self.description

        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k1 in self.job_specs:
                result['JobSpecs'].append(k1.to_map() if k1 else None)

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.user_command is not None:
            result['UserCommand'] = self.user_command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k1 in m.get('JobSpecs'):
                temp_model = main_models.JobSpec()
                self.job_specs.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')

        return self

