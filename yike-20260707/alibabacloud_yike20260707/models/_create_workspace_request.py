# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        title: str = None,
        user_count_limit: int = None,
    ):
        # The name of the studio. The name can be up to 50 characters in length and cannot contain single quotation marks, semicolons, less than signs, greater than signs, equal signs, vertical lines, or parentheses.
        # 
        # This parameter is required.
        self.title = title
        # The maximum number of users allowed in the studio team. Valid values: 2 to 1000.
        # 
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

