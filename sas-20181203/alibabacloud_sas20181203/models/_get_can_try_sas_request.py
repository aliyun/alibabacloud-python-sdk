# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCanTrySasRequest(DaraModel):
    def __init__(
        self,
        from_ecs: bool = None,
        lang: str = None,
    ):
        # Specifies whether the request is redirected from the Elastic Compute Service (ECS) console. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.from_ecs = from_ecs
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
        if self.from_ecs is not None:
            result['FromEcs'] = self.from_ecs

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromEcs') is not None:
            self.from_ecs = m.get('FromEcs')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

