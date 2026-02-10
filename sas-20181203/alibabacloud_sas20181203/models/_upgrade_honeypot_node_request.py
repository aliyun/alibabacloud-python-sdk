# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeHoneypotNodeRequest(DaraModel):
    def __init__(
        self,
        allow_honeypot_access_internet: bool = None,
        lang: str = None,
        node_id: str = None,
    ):
        # Specifies whether to allow the honeypot to access the Internet. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.allow_honeypot_access_internet = allow_honeypot_access_internet
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the management node that you want to upgrade.
        # 
        # >  You can call the [ListHoneypotNode](~~ListHoneypotNode~~) operation to obtain the ID.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_honeypot_access_internet is not None:
            result['AllowHoneypotAccessInternet'] = self.allow_honeypot_access_internet

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowHoneypotAccessInternet') is not None:
            self.allow_honeypot_access_internet = m.get('AllowHoneypotAccessInternet')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

