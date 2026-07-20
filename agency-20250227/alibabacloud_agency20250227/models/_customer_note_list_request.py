# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CustomerNoteListRequest(DaraModel):
    def __init__(
        self,
        customer_uid: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.customer_uid = customer_uid
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

