# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class TextTaskResult(DaraModel):
    def __init__(
        self,
        text_task: main_models.TextTask = None,
    ):
        self.text_task = text_task

    def validate(self):
        if self.text_task:
            self.text_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text_task is not None:
            result['textTask'] = self.text_task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('textTask') is not None:
            temp_model = main_models.TextTask()
            self.text_task = temp_model.from_map(m.get('textTask'))

        return self

