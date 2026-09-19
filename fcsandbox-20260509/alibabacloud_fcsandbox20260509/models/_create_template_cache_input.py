# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTemplateCacheInput(DaraModel):
    def __init__(
        self,
        team_id: str = None,
        template_id: str = None,
    ):
        # The team ID.
        self.team_id = team_id
        # The unique identifier of the template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

