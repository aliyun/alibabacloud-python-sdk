# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudGtmMonitorNodesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        show_disabled_nodes: bool = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US** (default): English
        self.accept_language = accept_language
        self.show_disabled_nodes = show_disabled_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.show_disabled_nodes is not None:
            result['ShowDisabledNodes'] = self.show_disabled_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ShowDisabledNodes') is not None:
            self.show_disabled_nodes = m.get('ShowDisabledNodes')

        return self

