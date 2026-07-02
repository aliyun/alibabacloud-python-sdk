# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClientKeysRequest(DaraModel):
    def __init__(
        self,
        aap_name: str = None,
    ):
        # The name of the application access point (AAP).
        self.aap_name = aap_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aap_name is not None:
            result['AapName'] = self.aap_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AapName') is not None:
            self.aap_name = m.get('AapName')

        return self

