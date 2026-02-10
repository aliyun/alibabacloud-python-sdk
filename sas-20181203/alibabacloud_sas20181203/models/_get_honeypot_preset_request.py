# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHoneypotPresetRequest(DaraModel):
    def __init__(
        self,
        honeypot_preset_id: str = None,
        lang: str = None,
    ):
        # The ID of the honeypot template.
        # 
        # > You can call the [ListHoneypotPreset](~~ListHoneypotPreset~~) operation to query the IDs of honeypot templates.
        # 
        # This parameter is required.
        self.honeypot_preset_id = honeypot_preset_id
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
        if self.honeypot_preset_id is not None:
            result['HoneypotPresetId'] = self.honeypot_preset_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoneypotPresetId') is not None:
            self.honeypot_preset_id = m.get('HoneypotPresetId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

