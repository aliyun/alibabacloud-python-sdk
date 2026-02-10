# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopHoneypotRequest(DaraModel):
    def __init__(
        self,
        honeypot_id: str = None,
        lang: str = None,
    ):
        # The honeypot ID.
        # 
        # >  You can call the [ListHoneypot](~~ListHoneypot~~) operation to obtain IDs of honeypots.
        # 
        # This parameter is required.
        self.honeypot_id = honeypot_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

