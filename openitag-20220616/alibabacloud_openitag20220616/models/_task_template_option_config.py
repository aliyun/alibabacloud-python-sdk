# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class TaskTemplateOptionConfig(DaraModel):
    def __init__(
        self,
        default_result: str = None,
        options: List[main_models.QuestionOption] = None,
        pre_options: List[str] = None,
        rule: str = None,
    ):
        # The default value must be adapted according to the question type. For a Radio or text box question, directly enter the tag value. For a Multiple Choice question, configure it as ["{tag 1}", "{tag 2}"].
        self.default_result = default_result
        # Select the list of question options.
        self.options = options
        # List of preset options for text-type questions.
        self.pre_options = pre_options
        # Validation rule item; valid only for fill-in-the-blank text-type questions.
        self.rule = rule

    def validate(self):
        if self.options:
            for v1 in self.options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result

        result['Options'] = []
        if self.options is not None:
            for k1 in self.options:
                result['Options'].append(k1.to_map() if k1 else None)

        if self.pre_options is not None:
            result['PreOptions'] = self.pre_options

        if self.rule is not None:
            result['Rule'] = self.rule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')

        self.options = []
        if m.get('Options') is not None:
            for k1 in m.get('Options'):
                temp_model = main_models.QuestionOption()
                self.options.append(temp_model.from_map(k1))

        if m.get('PreOptions') is not None:
            self.pre_options = m.get('PreOptions')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        return self

