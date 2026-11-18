# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMediaFoldersRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        production_id: str = None,
    ):
        # The page number. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20. Maximum value: 50. If the value exceeds 50, it is truncated to 50.
        self.page_size = page_size
        # The project ID. If this parameter is not specified, the default project of the current account is used. The value is in the `pd_{uid}` format.
        self.production_id = production_id

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

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        return self

