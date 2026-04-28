# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ShareLinkDetail(DaraModel):
    def __init__(
        self,
        enable_office_editable: bool = None,
    ):
        self.enable_office_editable = enable_office_editable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_office_editable is not None:
            result['enable_office_editable'] = self.enable_office_editable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable_office_editable') is not None:
            self.enable_office_editable = m.get('enable_office_editable')

        return self

