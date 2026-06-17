# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearLogStoreStorageRequest(DaraModel):
    def __init__(
        self,
        site: str = None,
    ):
        # The name of the site. If you have only one Logstore, you can leave this parameter empty. If you have two Logstores, set this parameter to cn or intl.
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site is not None:
            result['Site'] = self.site

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Site') is not None:
            self.site = m.get('Site')

        return self

