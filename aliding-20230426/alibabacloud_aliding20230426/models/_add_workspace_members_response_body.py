# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddWorkspaceMembersResponseBody(DaraModel):
    def __init__(
        self,
        not_in_org_list: List[str] = None,
        request_id: str = None,
    ):
        self.not_in_org_list = not_in_org_list
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_in_org_list is not None:
            result['NotInOrgList'] = self.not_in_org_list

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotInOrgList') is not None:
            self.not_in_org_list = m.get('NotInOrgList')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

