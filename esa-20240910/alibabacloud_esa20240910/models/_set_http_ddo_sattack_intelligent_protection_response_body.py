# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetHttpDDoSAttackIntelligentProtectionResponseBody(DaraModel):
    def __init__(
        self,
        ai_mode: str = None,
        ai_template: str = None,
        request_id: str = None,
        site_id: int = None,
    ):
        self.ai_mode = ai_mode
        self.ai_template = ai_template
        self.request_id = request_id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode

        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')

        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

