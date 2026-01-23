# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExportTasksRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        language: str = None,
        page_no: int = None,
        page_size: int = None,
        scene_code: str = None,
    ):
        self.id = id
        self.language = language
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.scene_code = scene_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.language is not None:
            result['Language'] = self.language

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

