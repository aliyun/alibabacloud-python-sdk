# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class WafBatchRuleShared(DaraModel):
    def __init__(
        self,
        action: str = None,
        actions: main_models.WafBatchRuleSharedActions = None,
        cross_site_id: int = None,
        expression: str = None,
        match: main_models.WafRuleMatch2 = None,
        mode: str = None,
        name: str = None,
        target: str = None,
    ):
        self.action = action
        self.actions = actions
        self.cross_site_id = cross_site_id
        self.expression = expression
        self.match = match
        self.mode = mode
        self.name = name
        self.target = target

    def validate(self):
        if self.actions:
            self.actions.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.actions is not None:
            result['Actions'] = self.actions.to_map()

        if self.cross_site_id is not None:
            result['CrossSiteId'] = self.cross_site_id

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.match is not None:
            result['Match'] = self.match.to_map()

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Actions') is not None:
            temp_model = main_models.WafBatchRuleSharedActions()
            self.actions = temp_model.from_map(m.get('Actions'))

        if m.get('CrossSiteId') is not None:
            self.cross_site_id = m.get('CrossSiteId')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Match') is not None:
            temp_model = main_models.WafRuleMatch2()
            self.match = temp_model.from_map(m.get('Match'))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

class WafBatchRuleSharedActions(DaraModel):
    def __init__(
        self,
        response: main_models.WafBatchRuleSharedActionsResponse = None,
    ):
        self.response = response

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.response is not None:
            result['Response'] = self.response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Response') is not None:
            temp_model = main_models.WafBatchRuleSharedActionsResponse()
            self.response = temp_model.from_map(m.get('Response'))

        return self



class WafBatchRuleSharedActionsResponse(DaraModel):
    def __init__(
        self,
        code: int = None,
        id: int = None,
    ):
        self.code = code
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

