# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Answer(DaraModel):
    def __init__(
        self,
        content: str = None,
        references: List[main_models.ReferenceFile] = None,
    ):
        # The answer.
        self.content = content
        # The reference sources of the answer.
        self.references = references

    def validate(self):
        if self.references:
            for v1 in self.references:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        result['References'] = []
        if self.references is not None:
            for k1 in self.references:
                result['References'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.references = []
        if m.get('References') is not None:
            for k1 in m.get('References'):
                temp_model = main_models.ReferenceFile()
                self.references.append(temp_model.from_map(k1))

        return self

