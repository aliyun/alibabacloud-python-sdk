# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EventMatchRule(DaraModel):
    def __init__(
        self,
        match_state: bool = None,
        name: str = None,
        prefix: str = None,
        suffix: str = None,
    ):
        # Specifies whether to match.
        self.match_state = match_state
        # The full name to match.
        self.name = name
        # The prefix to match.
        self.prefix = prefix
        # The suffix to match.
        self.suffix = suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_state is not None:
            result['MatchState'] = self.match_state

        if self.name is not None:
            result['Name'] = self.name

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.suffix is not None:
            result['Suffix'] = self.suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchState') is not None:
            self.match_state = m.get('MatchState')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        return self

