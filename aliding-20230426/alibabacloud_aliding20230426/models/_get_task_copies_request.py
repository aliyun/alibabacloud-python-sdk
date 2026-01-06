# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskCopiesRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        create_from_time_gmt: int = None,
        create_to_time_gmt: int = None,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        process_codes: str = None,
        system_token: str = None,
    ):
        self.app_type = app_type
        self.create_from_time_gmt = create_from_time_gmt
        self.create_to_time_gmt = create_to_time_gmt
        self.keyword = keyword
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.process_codes = process_codes
        # This parameter is required.
        self.system_token = system_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

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

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

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

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

