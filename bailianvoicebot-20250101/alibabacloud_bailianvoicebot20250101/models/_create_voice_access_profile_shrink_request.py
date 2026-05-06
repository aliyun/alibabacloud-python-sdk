# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVoiceAccessProfileShrinkRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        nls_engine: str = None,
        profile_shrink: str = None,
    ):
        self.business_unit_id = business_unit_id
        self.nls_engine = nls_engine
        self.profile_shrink = profile_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.profile_shrink is not None:
            result['Profile'] = self.profile_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('Profile') is not None:
            self.profile_shrink = m.get('Profile')

        return self

