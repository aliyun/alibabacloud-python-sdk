# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyListQueryRequest(DaraModel):
    def __init__(
        self,
        all_apply: bool = None,
        depart_id: str = None,
        end_time: str = None,
        gmt_modified: str = None,
        only_shang_lv_apply: bool = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        sub_corp_id: str = None,
        type: int = None,
        union_no: str = None,
        user_id: str = None,
    ):
        self.all_apply = all_apply
        self.depart_id = depart_id
        self.end_time = end_time
        self.gmt_modified = gmt_modified
        self.only_shang_lv_apply = only_shang_lv_apply
        self.page = page
        self.page_size = page_size
        self.start_time = start_time
        self.sub_corp_id = sub_corp_id
        self.type = type
        self.union_no = union_no
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

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.only_shang_lv_apply is not None:
            result['only_shang_lv_apply'] = self.only_shang_lv_apply

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.sub_corp_id is not None:
            result['sub_corp_id'] = self.sub_corp_id

        if self.type is not None:
            result['type'] = self.type

        if self.union_no is not None:
            result['union_no'] = self.union_no

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_apply') is not None:
            self.all_apply = m.get('all_apply')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('only_shang_lv_apply') is not None:
            self.only_shang_lv_apply = m.get('only_shang_lv_apply')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('sub_corp_id') is not None:
            self.sub_corp_id = m.get('sub_corp_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('union_no') is not None:
            self.union_no = m.get('union_no')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

