# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterGetMemberBalanceLogsRequest(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        page: int = None,
        size: int = None,
        skip_total: bool = None,
    ):
        # The change type filter.
        self.change_type = change_type
        # The page number.
        self.page = page
        # The number of entries per page.
        self.size = size
        # Specifies whether to skip the total count calculation.
        self.skip_total = skip_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['changeType'] = self.change_type

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        if self.skip_total is not None:
            result['skipTotal'] = self.skip_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changeType') is not None:
            self.change_type = m.get('changeType')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('skipTotal') is not None:
            self.skip_total = m.get('skipTotal')

        return self

