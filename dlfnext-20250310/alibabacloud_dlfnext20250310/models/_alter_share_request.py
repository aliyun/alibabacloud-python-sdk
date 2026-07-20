# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlterShareRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        enable_write: bool = None,
        share_name: str = None,
    ):
        self.comment = comment
        self.enable_write = enable_write
        self.share_name = share_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.enable_write is not None:
            result['enableWrite'] = self.enable_write

        if self.share_name is not None:
            result['shareName'] = self.share_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('enableWrite') is not None:
            self.enable_write = m.get('enableWrite')

        if m.get('shareName') is not None:
            self.share_name = m.get('shareName')

        return self

