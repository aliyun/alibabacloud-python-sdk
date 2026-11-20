# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySecretTransferDetailsRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        record_id: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        # 迁移记录的id
        # 
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        return self

