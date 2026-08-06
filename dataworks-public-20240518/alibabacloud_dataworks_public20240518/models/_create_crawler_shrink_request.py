# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCrawlerShrinkRequest(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
        enable_ai_comment: bool = None,
        name: str = None,
        options_shrink: str = None,
        resource_group_id: str = None,
        schedule_config_shrink: str = None,
        scope_shrink: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.data_source_id = data_source_id
        self.enable_ai_comment = enable_ai_comment
        # This parameter is required.
        self.name = name
        self.options_shrink = options_shrink
        self.resource_group_id = resource_group_id
        self.schedule_config_shrink = schedule_config_shrink
        self.scope_shrink = scope_shrink
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.enable_ai_comment is not None:
            result['EnableAiComment'] = self.enable_ai_comment

        if self.name is not None:
            result['Name'] = self.name

        if self.options_shrink is not None:
            result['Options'] = self.options_shrink

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_config_shrink is not None:
            result['ScheduleConfig'] = self.schedule_config_shrink

        if self.scope_shrink is not None:
            result['Scope'] = self.scope_shrink

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('EnableAiComment') is not None:
            self.enable_ai_comment = m.get('EnableAiComment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Options') is not None:
            self.options_shrink = m.get('Options')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config_shrink = m.get('ScheduleConfig')

        if m.get('Scope') is not None:
            self.scope_shrink = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

