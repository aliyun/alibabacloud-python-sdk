# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAccelerationLogByCubeIdRequest(DaraModel):
    def __init__(
        self,
        cube_id: str = None,
        end_date: str = None,
        page_no: int = None,
        page_size: int = None,
        start_date: str = None,
    ):
        # This parameter is required.
        self.cube_id = cube_id
        # This parameter is required.
        self.end_date = end_date
        self.page_no = page_no
        self.page_size = page_size
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

