# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCorpTasksRequest(DaraModel):
    def __init__(
        self,
        app_types: str = None,
        corp_id: str = None,
        create_from_time_gmt: int = None,
        create_to_time_gmt: int = None,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        process_codes: str = None,
        token: str = None,
    ):
        # This parameter is required.
        self.app_types = app_types
        # This parameter is required.
        self.corp_id = corp_id
        self.create_from_time_gmt = create_from_time_gmt
        self.create_to_time_gmt = create_to_time_gmt
        self.keyword = keyword
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.process_codes = process_codes
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_types is not None:
            result['AppTypes'] = self.app_types

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.create_from_time_gmt is not None:
            result['CreateFromTimeGMT'] = self.create_from_time_gmt

        if self.create_to_time_gmt is not None:
            result['CreateToTimeGMT'] = self.create_to_time_gmt

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.language is not None:
            result['Language'] = self.language

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.process_codes is not None:
            result['ProcessCodes'] = self.process_codes

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTypes') is not None:
            self.app_types = m.get('AppTypes')

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('CreateFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('CreateFromTimeGMT')

        if m.get('CreateToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('CreateToTimeGMT')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcessCodes') is not None:
            self.process_codes = m.get('ProcessCodes')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

