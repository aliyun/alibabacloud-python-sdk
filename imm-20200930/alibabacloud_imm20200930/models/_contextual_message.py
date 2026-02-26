# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ContextualMessage(DaraModel):
    def __init__(
        self,
        content: str = None,
        files: List[main_models.ContextualFile] = None,
        role: str = None,
    ):
        # The message content.
        self.content = content
        # The files involved in the dialogue.
        self.files = files
        # The role in the dialogue.
        self.role = role

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ContextualFile()
                self.files.append(temp_model.from_map(k1))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

