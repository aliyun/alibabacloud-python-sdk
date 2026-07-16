# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class QuestionOption(DaraModel):
    def __init__(
        self,
        children: List[main_models.QuestionOption] = None,
        color: str = None,
        key: str = None,
        label: str = None,
        remark: str = None,
        shortcut: str = None,
    ):
        # List of child options.
        self.children = children
        # Color.
        self.color = color
        # Tag Name.
        # 
        # This parameter is required.
        self.key = key
        # Label display name.
        # 
        # This parameter is required.
        self.label = label
        # Remark.
        self.remark = remark
        # Keyboard shortcut.
        self.shortcut = shortcut

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.color is not None:
            result['Color'] = self.color

        if self.key is not None:
            result['Key'] = self.key

        if self.label is not None:
            result['Label'] = self.label

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.shortcut is not None:
            result['Shortcut'] = self.shortcut

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.QuestionOption()
                self.children.append(temp_model.from_map(k1))

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Shortcut') is not None:
            self.shortcut = m.get('Shortcut')

        return self

