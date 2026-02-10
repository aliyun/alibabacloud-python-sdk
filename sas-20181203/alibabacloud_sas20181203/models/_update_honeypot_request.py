# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHoneypotRequest(DaraModel):
    def __init__(
        self,
        honeypot_id: str = None,
        honeypot_name: str = None,
        lang: str = None,
        meta: str = None,
    ):
        # The ID of the honeypot.
        # 
        # >  You can call the [ListHoneypot](~~ListHoneypot~~) operation to query the IDs of honeypots.
        # 
        # This parameter is required.
        self.honeypot_id = honeypot_id
        # The custom name of the honeypot.
        self.honeypot_name = honeypot_name
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The custom configuration of the honeypot.
        # 
        # > You can call the [ListAvailableHoneypot](~~ListAvailableHoneypot~~) operation to query the configurations of honeypots from the **Template** response parameter.
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        if self.honeypot_name is not None:
            result['HoneypotName'] = self.honeypot_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.meta is not None:
            result['Meta'] = self.meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        if m.get('HoneypotName') is not None:
            self.honeypot_name = m.get('HoneypotName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        return self

