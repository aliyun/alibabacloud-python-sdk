# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class IllustrationTaskResult(DaraModel):
    def __init__(
        self,
        illustration_task: main_models.IllustrationTask = None,
        request_id: str = None,
    ):
        self.illustration_task = illustration_task
        self.request_id = request_id

    def validate(self):
        if self.illustration_task:
            self.illustration_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.illustration_task is not None:
            result['illustrationTask'] = self.illustration_task.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('illustrationTask') is not None:
            temp_model = main_models.IllustrationTask()
            self.illustration_task = temp_model.from_map(m.get('illustrationTask'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

