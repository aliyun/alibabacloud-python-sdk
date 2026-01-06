# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationRequest(DaraModel):
    def __init__(
        self,
        app_filter: str = None,
        app_name_search_keyword: str = None,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
        token: str = None,
    ):
        self.app_filter = app_filter
        self.app_name_search_keyword = app_name_search_keyword
        # This parameter is required.
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_filter is not None:
            result['AppFilter'] = self.app_filter

        if self.app_name_search_keyword is not None:
            result['AppNameSearchKeyword'] = self.app_name_search_keyword

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppFilter') is not None:
            self.app_filter = m.get('AppFilter')

        if m.get('AppNameSearchKeyword') is not None:
            self.app_name_search_keyword = m.get('AppNameSearchKeyword')

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

