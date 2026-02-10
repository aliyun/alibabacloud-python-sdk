# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSoarStrategyTaskResultRequest(DaraModel):
    def __init__(
        self,
        condition: str = None,
        current_page: int = None,
        page_size: int = None,
        strategy_task_id: int = None,
    ):
        # Condition parameters for task scheduling.
        self.condition = condition
        # The current page number during paginated queries.
        self.current_page = current_page
        # The maximum number of entries to display per page during paginated queries.
        self.page_size = page_size
        # Strategy task ID.
        # > You can obtain this parameter by calling the [DescribeSoarStrategyTasks](~~DescribeSoarStrategyTasks~~) interface.
        self.strategy_task_id = strategy_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.strategy_task_id is not None:
            result['StrategyTaskId'] = self.strategy_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StrategyTaskId') is not None:
            self.strategy_task_id = m.get('StrategyTaskId')

        return self

