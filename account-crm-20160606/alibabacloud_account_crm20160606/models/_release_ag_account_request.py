# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseAgAccountRequest(DaraModel):
    def __init__(
        self,
        mpk: str = None,
        pk: str = None,
        release_reason: str = None,
    ):
        # This parameter is required.
        self.mpk = mpk
        # This parameter is required.
        self.pk = pk
        self.release_reason = release_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.release_reason is not None:
            result['ReleaseReason'] = self.release_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('ReleaseReason') is not None:
            self.release_reason = m.get('ReleaseReason')

        return self

