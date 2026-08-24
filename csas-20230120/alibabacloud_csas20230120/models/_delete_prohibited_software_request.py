# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteProhibitedSoftwareRequest(DaraModel):
    def __init__(
        self,
        software_ids: List[str] = None,
    ):
        # The IDs of the prohibited software to delete. Duplicate IDs are not allowed. You can specify up to 100 IDs.
        # 
        # This parameter is required.
        self.software_ids = software_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.software_ids is not None:
            result['SoftwareIds'] = self.software_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SoftwareIds') is not None:
            self.software_ids = m.get('SoftwareIds')

        return self

