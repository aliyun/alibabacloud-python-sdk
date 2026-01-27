# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApprovalSchemasForApprovalProcessesRequest(DaraModel):
    def __init__(
        self,
        process_ids: List[str] = None,
    ):
        # This parameter is required.
        self.process_ids = process_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_ids is not None:
            result['ProcessIds'] = self.process_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessIds') is not None:
            self.process_ids = m.get('ProcessIds')

        return self

