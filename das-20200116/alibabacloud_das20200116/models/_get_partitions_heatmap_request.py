# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPartitionsHeatmapRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        time_range: str = None,
        type: str = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The instance ID.
        self.instance_id = instance_id
        # The time range to be queried. Valid values:
        # 
        # *   **LAST_ONE_HOURS**: the last hour.
        # *   **LAST_SIX_HOURS**: the last six hours.
        # *   **LAST_ONE_DAYS**: the last day.
        # *   **LAST_THREE_DAYS**: the last three days.
        # *   **LAST_SEVEN_DAYS**: the last seven days.
        self.time_range = time_range
        # The type of the data to be queried. Valid values:
        # 
        # *   **READ_ROWS**: the read rows.
        # *   **WRITTEN_ROWS**: the written rows.
        # *   **READ_WRITTEN_ROWS**: the read and written rows.
        # *   **UPDATE_ROWS**: the updated rows.
        # *   **INSERTED_ROWS**: the inserted rows.
        # *   **DELETED_ROWS**: the deleted rows.
        # *   **READ_ROWS_WITH_DN**: the read rows returned from a data node.
        # *   **WRITTEN_ROWS_WITH_DN**: the written rows returned from a data node.
        # *   **READ_WRITTEN_ROWS_WITH_DN**: the read and written rows returned from a data node.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

