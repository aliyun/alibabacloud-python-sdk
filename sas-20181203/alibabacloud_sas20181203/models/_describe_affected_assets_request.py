# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAffectedAssetsRequest(DaraModel):
    def __init__(
        self,
        current: str = None,
        levels: str = None,
        page_size: str = None,
    ):
        # The current page number.
        self.current = current
        # The severity level. Separate multiple values with commas (,). Valid values:
        # - serious: urgent
        # - suspicious: suspicious
        # - remind: reminder.
        self.levels = levels
        # The maximum number of entries per page in a paginated query. Default value: 20. If this parameter is left empty, 20 entries are returned.
        # >Do not leave PageSize empty.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['Current'] = self.current

        if self.levels is not None:
            result['Levels'] = self.levels

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('Levels') is not None:
            self.levels = m.get('Levels')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

