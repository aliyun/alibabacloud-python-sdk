# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateDingtalkPersonalTodoTaskShrinkHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')

        return self

