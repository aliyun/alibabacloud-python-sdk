# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUnknownThreatDetectStrategyRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        id: str = None,
        name: str = None,
        page_size: str = None,
        study_mode: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.id = id
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        self.study_mode = study_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.study_mode is not None:
            result['StudyMode'] = self.study_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StudyMode') is not None:
            self.study_mode = m.get('StudyMode')

        return self

