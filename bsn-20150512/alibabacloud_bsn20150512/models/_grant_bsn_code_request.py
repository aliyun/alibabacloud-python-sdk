# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantBsnCodeRequest(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        grant_to_aliuid: int = None,
        notes: str = None,
        sn: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.grant_to_aliuid = grant_to_aliuid
        self.notes = notes
        # This parameter is required.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.grant_to_aliuid is not None:
            result['GrantToAliuid'] = self.grant_to_aliuid

        if self.notes is not None:
            result['Notes'] = self.notes

        if self.sn is not None:
            result['Sn'] = self.sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('GrantToAliuid') is not None:
            self.grant_to_aliuid = m.get('GrantToAliuid')

        if m.get('Notes') is not None:
            self.notes = m.get('Notes')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        return self

