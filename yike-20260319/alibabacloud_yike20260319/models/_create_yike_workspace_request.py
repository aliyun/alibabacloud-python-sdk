# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateYikeWorkspaceRequest(DaraModel):
    def __init__(
        self,
        title: str = None,
        user_count_limit: int = None,
    ):
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.user_count_limit = user_count_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['Title'] = self.title

        if self.user_count_limit is not None:
            result['UserCountLimit'] = self.user_count_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserCountLimit') is not None:
            self.user_count_limit = m.get('UserCountLimit')

        return self

