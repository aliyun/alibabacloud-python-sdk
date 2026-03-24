# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDigitalEmployeeSkillsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        skill_name: str = None,
    ):
        # The maximum number of entries to return for this request.
        self.max_results = max_results
        # The token for the next page. A null value indicates that there are no more pages.
        self.next_token = next_token
        # The name of the skill.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        return self

