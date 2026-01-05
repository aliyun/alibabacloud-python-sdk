# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAppsRequest(DaraModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
    ):
        # The IDs of the applications.
        self.app_id_list = app_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')

        return self

