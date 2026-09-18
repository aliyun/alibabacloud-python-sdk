# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paimodelgallery20250630 import models as main_models
from darabonba.model import DaraModel

class UpdateJobPlanRequest(DaraModel):
    def __init__(
        self,
        job_plan_current_step: str = None,
        tag: List[main_models.UpdateJobPlanRequestTag] = None,
    ):
        # The current step of the task plan. Set this parameter to `DatasetSynthesisAndModelTrain` for the full process or `DatasetSynthesisModelTrain` for step-by-step execution.
        self.job_plan_current_step = job_plan_current_step
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_plan_current_step is not None:
            result['JobPlanCurrentStep'] = self.job_plan_current_step

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobPlanCurrentStep') is not None:
            self.job_plan_current_step = m.get('JobPlanCurrentStep')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.UpdateJobPlanRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class UpdateJobPlanRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. If the tag key already exists, the tag is updated. Otherwise, a new tag is added.
        self.key = key
        # The tag key. If the tag key already exists, the tag is updated. Otherwise, a new tag is added.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

