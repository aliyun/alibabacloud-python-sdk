# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class IFlightOrderListQueryRequest(DaraModel):
    def __init__(
        self,
        apply_id_list: List[str] = None,
        book_type_list: List[int] = None,
        booker_id: List[str] = None,
        end_date: str = None,
        page_size: int = None,
        scroll_id: str = None,
        start_date: str = None,
        third_part_apply_id_list: List[str] = None,
    ):
        self.apply_id_list = apply_id_list
        self.book_type_list = book_type_list
        self.booker_id = booker_id
        self.end_date = end_date
        self.page_size = page_size
        self.scroll_id = scroll_id
        self.start_date = start_date
        self.third_part_apply_id_list = third_part_apply_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id_list is not None:
            result['apply_id_list'] = self.apply_id_list

        if self.book_type_list is not None:
            result['book_type_list'] = self.book_type_list

        if self.booker_id is not None:
            result['booker_id'] = self.booker_id

        if self.end_date is not None:
            result['end_date'] = self.end_date

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.scroll_id is not None:
            result['scroll_id'] = self.scroll_id

        if self.start_date is not None:
            result['start_date'] = self.start_date

        if self.third_part_apply_id_list is not None:
            result['third_part_apply_id_list'] = self.third_part_apply_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id_list') is not None:
            self.apply_id_list = m.get('apply_id_list')

        if m.get('book_type_list') is not None:
            self.book_type_list = m.get('book_type_list')

        if m.get('booker_id') is not None:
            self.booker_id = m.get('booker_id')

        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('scroll_id') is not None:
            self.scroll_id = m.get('scroll_id')

        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')

        if m.get('third_part_apply_id_list') is not None:
            self.third_part_apply_id_list = m.get('third_part_apply_id_list')

        return self

