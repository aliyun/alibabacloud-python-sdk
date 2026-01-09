# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDashboardShrinkRequest(DaraModel):
    def __init__(
        self,
        dashboard_name: str = None,
        display_name: str = None,
        offset: int = None,
        size: int = None,
        tags_shrink: str = None,
    ):
        self.dashboard_name = dashboard_name
        self.display_name = display_name
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Maximum value: 500. Default value: 500.
        self.size = size
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        return self

