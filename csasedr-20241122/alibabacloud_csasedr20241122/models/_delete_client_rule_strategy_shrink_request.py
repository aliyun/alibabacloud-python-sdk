# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteClientRuleStrategyShrinkRequest(DaraModel):
    def __init__(
        self,
        id_list_shrink: str = None,
    ):
        # The list of IDs of the policies to delete. Use the policy IDs returned by the create operation or obtained from the policy list or details operations.
        self.id_list_shrink = id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id_list_shrink is not None:
            result['IdList'] = self.id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdList') is not None:
            self.id_list_shrink = m.get('IdList')

        return self

