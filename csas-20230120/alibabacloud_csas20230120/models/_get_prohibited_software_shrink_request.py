# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProhibitedSoftwareShrinkRequest(DaraModel):
    def __init__(
        self,
        software_id_shrink: str = None,
    ):
        # The prohibited software ID.
        self.software_id_shrink = software_id_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.software_id_shrink is not None:
            result['SoftwareId'] = self.software_id_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SoftwareId') is not None:
            self.software_id_shrink = m.get('SoftwareId')

        return self

