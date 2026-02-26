# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LeavePictureList(DaraModel):
    def __init__(
        self,
        desc: str = None,
        picture: str = None,
    ):
        self.desc = desc
        self.picture = picture

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.picture is not None:
            result['picture'] = self.picture

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('picture') is not None:
            self.picture = m.get('picture')

        return self

