# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecommendNextActionsRequest(DaraModel):
    def __init__(
        self,
        custom_prompt: str = None,
        output_type: str = None,
        recent_message_count: int = None,
        session_id: str = None,
        tenant_id: str = None,
    ):
        # The extraction instruction.
        self.custom_prompt = custom_prompt
        # The output type: `conversation/skill/task`.
        self.output_type = output_type
        # The number of recent messages used to assemble contextual information.
        self.recent_message_count = recent_message_count
        # The session ID to filter by. If specified, returns all Active/Expired status information associated with this session.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The tenant ID. This is a common parameter. In winnexo-cli, pass this explicitly with --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt

        if self.output_type is not None:
            result['outputType'] = self.output_type

        if self.recent_message_count is not None:
            result['recentMessageCount'] = self.recent_message_count

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')

        if m.get('outputType') is not None:
            self.output_type = m.get('outputType')

        if m.get('recentMessageCount') is not None:
            self.recent_message_count = m.get('recentMessageCount')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

