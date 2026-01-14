# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMailTaskListRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        paused: bool = None,
        user_nick: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.paused = paused
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.paused is not None:
            result['Paused'] = self.paused

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

