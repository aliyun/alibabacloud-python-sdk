# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTranslationTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        base_task_id: str = None,
        config_shrink: str = None,
        custom_terms_shrink: str = None,
        task_id: str = None,
    ):
        self.apikey = apikey
        self.base_task_id = base_task_id
        # This parameter is required.
        self.config_shrink = config_shrink
        self.custom_terms_shrink = custom_terms_shrink
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['APIKey'] = self.apikey

        if self.base_task_id is not None:
            result['BaseTaskId'] = self.base_task_id

        if self.config_shrink is not None:
            result['Config'] = self.config_shrink

        if self.custom_terms_shrink is not None:
            result['CustomTerms'] = self.custom_terms_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKey') is not None:
            self.apikey = m.get('APIKey')

        if m.get('BaseTaskId') is not None:
            self.base_task_id = m.get('BaseTaskId')

        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')

        if m.get('CustomTerms') is not None:
            self.custom_terms_shrink = m.get('CustomTerms')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

