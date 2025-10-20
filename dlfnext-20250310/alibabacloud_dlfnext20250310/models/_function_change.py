# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class FunctionChange(DaraModel):
    def __init__(
        self,
        action: str = None,
        comment: str = None,
        definition: main_models.FunctionDefinition = None,
        key: str = None,
        name: str = None,
        value: str = None,
    ):
        self.action = action
        # required in UpdateFunctionComment
        self.comment = comment
        # required in AddDefinition/UpdateDefinition
        self.definition = definition
        # required in SetFunctionOption/RemoveFunctionOption
        self.key = key
        # required in AddDefinition/UpdateDefinition/DropDefinition
        self.name = name
        # required in SetFunctionOption
        self.value = value

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.comment is not None:
            result['comment'] = self.comment

        if self.definition is not None:
            result['definition'] = self.definition.to_map()

        if self.key is not None:
            result['key'] = self.key

        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('definition') is not None:
            temp_model = main_models.FunctionDefinition()
            self.definition = temp_model.from_map(m.get('definition'))

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

