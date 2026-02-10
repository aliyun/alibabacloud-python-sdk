# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateImageVulWhitelistTargetRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
        reason: str = None,
        source: str = None,
        target: str = None,
    ):
        # The whitelist ID.
        self.id = id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The reason why you add the vulnerability to the whitelist.
        self.reason = reason
        # The source of the whitelist. Valid values:
        # 
        # *   **image**
        # *   **agentless**
        self.source = source
        # The vulnerability that you want to add to the whitelist. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **type**: The type of the vulnerability. The value is fixed to repo.
        # *   **target**: The content of the vulnerability. The value is in the format of Namespace/Image repository.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.source is not None:
            result['Source'] = self.source

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

