# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class RecommendNextActionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_actions: List[main_models.RecommendNextActionsResponseBodyNextActions] = None,
        request_id: str = None,
        title: str = None,
    ):
        # The business status code. A value of 200 indicates success. A failure returns a backend error code (ERR.* / InvalidParameter.*).
        self.code = code
        # The status code description.
        self.message = message
        # The next-step recommendations.
        self.next_actions = next_actions
        # The request ID.
        self.request_id = request_id
        # The meeting reservation title.
        self.title = title

    def validate(self):
        if self.next_actions:
            for v1 in self.next_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['nextActions'] = []
        if self.next_actions is not None:
            for k1 in self.next_actions:
                result['nextActions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.next_actions = []
        if m.get('nextActions') is not None:
            for k1 in m.get('nextActions'):
                temp_model = main_models.RecommendNextActionsResponseBodyNextActions()
                self.next_actions.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class RecommendNextActionsResponseBodyNextActions(DaraModel):
    def __init__(
        self,
        action_title: str = None,
        skill_code: str = None,
        skill_name: str = None,
        type: str = None,
    ):
        # The recommendation title.
        self.action_title = action_title
        # The skill code.
        self.skill_code = skill_code
        # The skill name.
        self.skill_name = skill_name
        # The recommendation type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_title is not None:
            result['actionTitle'] = self.action_title

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionTitle') is not None:
            self.action_title = m.get('actionTitle')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

