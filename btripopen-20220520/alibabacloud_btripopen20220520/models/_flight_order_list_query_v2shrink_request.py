# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightOrderListQueryV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        approve_id_shrink: str = None,
        booker_id_shrink: str = None,
        depart_id_shrink: str = None,
        end_date: str = None,
        page_size: int = None,
        scroll_id: str = None,
        start_date: str = None,
        supplier_shrink: str = None,
        thirdpart_approve_id_shrink: str = None,
        update_end_date: str = None,
        update_start_date: str = None,
    ):
        self.approve_id_shrink = approve_id_shrink
        self.booker_id_shrink = booker_id_shrink
        self.depart_id_shrink = depart_id_shrink
        self.end_date = end_date
        self.page_size = page_size
        self.scroll_id = scroll_id
        self.start_date = start_date
        self.supplier_shrink = supplier_shrink
        self.thirdpart_approve_id_shrink = thirdpart_approve_id_shrink
        self.update_end_date = update_end_date
        self.update_start_date = update_start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve_id_shrink is not None:
            result['approve_id'] = self.approve_id_shrink

        if self.booker_id_shrink is not None:
            result['booker_id'] = self.booker_id_shrink

        if self.depart_id_shrink is not None:
            result['depart_id'] = self.depart_id_shrink

        if self.end_date is not None:
            result['end_date'] = self.end_date

        if self.page_size is not None:
            result['page_Size'] = self.page_size

        if self.scroll_id is not None:
            result['scroll_id'] = self.scroll_id

        if self.start_date is not None:
            result['start_date'] = self.start_date

        if self.supplier_shrink is not None:
            result['supplier'] = self.supplier_shrink

        if self.thirdpart_approve_id_shrink is not None:
            result['thirdpart_approve_id'] = self.thirdpart_approve_id_shrink

        if self.update_end_date is not None:
            result['update_end_date'] = self.update_end_date

        if self.update_start_date is not None:
            result['update_start_date'] = self.update_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approve_id') is not None:
            self.approve_id_shrink = m.get('approve_id')

        if m.get('booker_id') is not None:
            self.booker_id_shrink = m.get('booker_id')

        if m.get('depart_id') is not None:
            self.depart_id_shrink = m.get('depart_id')

        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')

        if m.get('page_Size') is not None:
            self.page_size = m.get('page_Size')

        if m.get('scroll_id') is not None:
            self.scroll_id = m.get('scroll_id')

        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')

        if m.get('supplier') is not None:
            self.supplier_shrink = m.get('supplier')

        if m.get('thirdpart_approve_id') is not None:
            self.thirdpart_approve_id_shrink = m.get('thirdpart_approve_id')

        if m.get('update_end_date') is not None:
            self.update_end_date = m.get('update_end_date')

        if m.get('update_start_date') is not None:
            self.update_start_date = m.get('update_start_date')

        return self

