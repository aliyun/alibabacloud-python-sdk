# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteClientsRequest(DaraModel):
    def __init__(
        self,
        caller_ali_uid: str = None,
        in_manage: bool = None,
        uuids: List[str] = None,
    ):
        # aliuid
        self.caller_ali_uid = caller_ali_uid
        # This parameter is required.
        self.in_manage = in_manage
        # This parameter is required.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_ali_uid is not None:
            result['CallerAliUid'] = self.caller_ali_uid

        if self.in_manage is not None:
            result['InManage'] = self.in_manage

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerAliUid') is not None:
            self.caller_ali_uid = m.get('CallerAliUid')

        if m.get('InManage') is not None:
            self.in_manage = m.get('InManage')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

