# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUnknownThreatDetectEventRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        hash_key: str = None,
        page_size: int = None,
        parent_process_path: str = None,
        process_path: str = None,
        remark: str = None,
        status: int = None,
        uuid: str = None,
    ):
        self.current_page = current_page
        self.hash_key = hash_key
        self.page_size = page_size
        self.parent_process_path = parent_process_path
        self.process_path = process_path
        self.remark = remark
        self.status = status
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_process_path is not None:
            result['ParentProcessPath'] = self.parent_process_path

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentProcessPath') is not None:
            self.parent_process_path = m.get('ParentProcessPath')

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

