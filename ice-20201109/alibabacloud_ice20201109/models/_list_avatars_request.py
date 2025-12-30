# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAvatarsRequest(DaraModel):
    def __init__(
        self,
        avatar_type: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # *   The type of the digital human.
        # *   2DAvatar
        self.avatar_type = avatar_type
        # *   The page number.
        # *   Default value: 1.
        self.page_no = page_no
        # *   The number of entries per page.
        # *   Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_type is not None:
            result['AvatarType'] = self.avatar_type

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarType') is not None:
            self.avatar_type = m.get('AvatarType')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

