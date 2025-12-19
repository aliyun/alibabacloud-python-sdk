# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompleteResourceTokenAuthShrinkRequest(DaraModel):
    def __init__(
        self,
        session_uri: str = None,
        user_identifier_shrink: str = None,
    ):
        self.session_uri = session_uri
        self.user_identifier_shrink = user_identifier_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_uri is not None:
            result['SessionURI'] = self.session_uri

        if self.user_identifier_shrink is not None:
            result['UserIdentifier'] = self.user_identifier_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionURI') is not None:
            self.session_uri = m.get('SessionURI')

        if m.get('UserIdentifier') is not None:
            self.user_identifier_shrink = m.get('UserIdentifier')

        return self

