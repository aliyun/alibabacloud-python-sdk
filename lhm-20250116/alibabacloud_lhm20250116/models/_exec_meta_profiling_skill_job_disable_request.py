# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecMetaProfilingSkillJobDisableRequest(DaraModel):
    def __init__(
        self,
        ds_id: int = None,
    ):
        self.ds_id = ds_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_id is not None:
            result['dsId'] = self.ds_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dsId') is not None:
            self.ds_id = m.get('dsId')

        return self

