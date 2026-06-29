# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveOrganizationMemberRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        locale: str = None,
    ):
        # The list of member account IDs to be removed.
        self.account_ids = account_ids
        # The language. Valid values: zh-CN and en-US.
        self.locale = locale

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.locale is not None:
            result['Locale'] = self.locale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        return self

