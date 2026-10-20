# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateOptimizeTaskRequest(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        status: str = None,
        client_token: str = None,
    ):
        # The type-related configurations. Optional prompts for ExperienceMining or SkillOptimize support only inline Markdown, and the body is saved to inputs.prompt.content (non-empty UTF-8, up to 16 KiB).
        self.config = config
        # The status of the task. Valid values: Enabled and Disabled.
        self.status = status
        # The idempotency token.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.status is not None:
            result['status'] = self.status

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

