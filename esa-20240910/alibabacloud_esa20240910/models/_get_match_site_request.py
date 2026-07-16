# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMatchSiteRequest(DaraModel):
    def __init__(
        self,
        record_name: str = None,
    ):
        # The record name.
        # 
        # This parameter is required.
        self.record_name = record_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_name is not None:
            result['RecordName'] = self.record_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        return self

