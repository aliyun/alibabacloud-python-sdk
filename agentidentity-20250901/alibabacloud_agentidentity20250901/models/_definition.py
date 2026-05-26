# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class Definition(DaraModel):
    def __init__(
        self,
        cedar: main_models.DefinitionCedar = None,
    ):
        self.cedar = cedar

    def validate(self):
        if self.cedar:
            self.cedar.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cedar is not None:
            result['Cedar'] = self.cedar.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cedar') is not None:
            temp_model = main_models.DefinitionCedar()
            self.cedar = temp_model.from_map(m.get('Cedar'))

        return self



class DefinitionCedar(DaraModel):
    def __init__(
        self,
        statement: str = None,
    ):
        self.statement = statement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.statement is not None:
            result['Statement'] = self.statement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Statement') is not None:
            self.statement = m.get('Statement')

        return self

