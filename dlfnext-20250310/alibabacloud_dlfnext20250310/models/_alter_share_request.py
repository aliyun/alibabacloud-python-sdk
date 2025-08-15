# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlterShareRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        share_name: str = None,
    ):
        self.comment = comment
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

        if self.share_name is not None:
            result['shareName'] = self.share_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('shareName') is not None:
            self.share_name = m.get('shareName')

        return self

