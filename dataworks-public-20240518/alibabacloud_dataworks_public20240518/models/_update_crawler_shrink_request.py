# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCrawlerShrinkRequest(DaraModel):
    def __init__(
        self,
        enable_ai_comment: bool = None,
        id: int = None,
        options_shrink: str = None,
        resource_group_id: str = None,
        schedule_config_shrink: str = None,
        scope_shrink: str = None,
    ):
        self.enable_ai_comment = enable_ai_comment
        # This parameter is required.
        self.id = id
        self.options_shrink = options_shrink
        self.resource_group_id = resource_group_id
        self.schedule_config_shrink = schedule_config_shrink
        self.scope_shrink = scope_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_ai_comment is not None:
            result['EnableAiComment'] = self.enable_ai_comment

        if self.id is not None:
            result['Id'] = self.id

        if self.options_shrink is not None:
            result['Options'] = self.options_shrink

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_config_shrink is not None:
            result['ScheduleConfig'] = self.schedule_config_shrink

        if self.scope_shrink is not None:
            result['Scope'] = self.scope_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAiComment') is not None:
            self.enable_ai_comment = m.get('EnableAiComment')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Options') is not None:
            self.options_shrink = m.get('Options')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config_shrink = m.get('ScheduleConfig')

        if m.get('Scope') is not None:
            self.scope_shrink = m.get('Scope')

        return self

