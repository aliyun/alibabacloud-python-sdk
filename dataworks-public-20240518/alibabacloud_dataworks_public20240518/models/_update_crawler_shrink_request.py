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
        # Specifies whether to enable AI metadata description. This parameter is supported only when SupportAiComment returned by GetCrawlerTypeCapabilities is set to true. If this parameter is not specified, the existing value remains unchanged.
        self.enable_ai_comment = enable_ai_comment
        # The ID of the metadata crawler. You can call ListCrawlers to query crawler IDs.
        # 
        # This parameter is required.
        self.id = id
        # The extension configurations for the crawler type. Only the specified configuration items are updated. Unspecified configuration items remain unchanged. The supported keys and values are determined by the SupportedOptionKeys returned by GetCrawlerTypeCapabilities.
        self.options_shrink = options_shrink
        # The ID of the Serverless 2.0 resource group used to run the collection task. Whether this parameter is supported and whether it is required depend on the capabilities returned by GetCrawlerTypeCapabilities. If this parameter is not specified, the existing value remains unchanged.
        self.resource_group_id = resource_group_id
        # The scheduling configuration. If this parameter is specified, the scheduling method is updated. If this parameter is not specified, the existing value remains unchanged.
        self.schedule_config_shrink = schedule_config_shrink
        # The collection scope configuration. If this parameter is specified, the collection scope is updated. If this parameter is not specified, the existing value remains unchanged.
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

