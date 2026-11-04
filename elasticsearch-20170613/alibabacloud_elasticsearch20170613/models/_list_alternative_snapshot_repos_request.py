# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlternativeSnapshotReposRequest(DaraModel):
    def __init__(
        self,
        already_set_items: bool = None,
    ):
        # Specifies whether to return the added OSS reference repositories. Default value: true. Valid values: true: Returns the added OSS reference repositories. false: Does not return the added OSS reference repositories.
        self.already_set_items = already_set_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_set_items is not None:
            result['alreadySetItems'] = self.already_set_items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alreadySetItems') is not None:
            self.already_set_items = m.get('alreadySetItems')

        return self

