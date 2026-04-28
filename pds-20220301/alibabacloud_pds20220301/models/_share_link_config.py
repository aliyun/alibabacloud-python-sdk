# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ShareLinkConfig(DaraModel):
    def __init__(
        self,
        enable_share_link_office_edit: bool = None,
    ):
        self.enable_share_link_office_edit = enable_share_link_office_edit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_share_link_office_edit is not None:
            result['enable_share_link_office_edit'] = self.enable_share_link_office_edit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable_share_link_office_edit') is not None:
            self.enable_share_link_office_edit = m.get('enable_share_link_office_edit')

        return self

