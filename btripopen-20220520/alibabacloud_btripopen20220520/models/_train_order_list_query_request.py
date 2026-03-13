# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainOrderListQueryRequest(DaraModel):
    def __init__(
        self,
        all_apply: bool = None,
        apply_id: int = None,
        depart_id: str = None,
        end_time: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        thirdpart_apply_id: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
        user_id: str = None,
    ):
        self.all_apply = all_apply
        self.apply_id = apply_id
        self.depart_id = depart_id
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.start_time = start_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.update_end_time = update_end_time
        self.update_start_time = update_start_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_apply is not None:
            result['all_apply'] = self.all_apply

        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.update_end_time is not None:
            result['update_end_time'] = self.update_end_time

        if self.update_start_time is not None:
            result['update_start_time'] = self.update_start_time

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_apply') is not None:
            self.all_apply = m.get('all_apply')

        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('update_end_time') is not None:
            self.update_end_time = m.get('update_end_time')

        if m.get('update_start_time') is not None:
            self.update_start_time = m.get('update_start_time')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

