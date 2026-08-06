# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListPromptsResponseBody(DaraModel):
    def __init__(
        self,
        prompts: List[main_models.Prompt] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of prompts.
        self.prompts = prompts
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned under the current request conditions. This parameter is optional and may not be returned by default.
        self.total_count = total_count

    def validate(self):
        if self.prompts:
            for v1 in self.prompts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Prompts'] = []
        if self.prompts is not None:
            for k1 in self.prompts:
                result['Prompts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prompts = []
        if m.get('Prompts') is not None:
            for k1 in m.get('Prompts'):
                temp_model = main_models.Prompt()
                self.prompts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

