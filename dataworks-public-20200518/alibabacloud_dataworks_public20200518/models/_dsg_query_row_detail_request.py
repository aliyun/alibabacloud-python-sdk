# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgQueryRowDetailRequest(DaraModel):
    def __init__(
        self,
        engine_name: str = None,
        inst_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The engine type. Valid values:
        # - ODPS.ODPS
        # - EMR
        # - HOLO.POSTGRES
        # 
        # This parameter is required.
        self.engine_name = engine_name
        # The instance ID.
        # 
        # This parameter is required.
        self.inst_id = inst_id
        # The page number. Minimum value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name

        if self.inst_id is not None:
            result['InstId'] = self.inst_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstId') is not None:
            self.inst_id = m.get('InstId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

