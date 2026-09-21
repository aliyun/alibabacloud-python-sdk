# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRoutineEnvironmentVariablesRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        key_word: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The environment name.
        # 
        # Valid values:
        # - `production`: production environment
        # - `staging`: staging environment
        # 
        # This parameter is required.
        self.env = env
        # The keyword used to perform a case-insensitive fuzzy search on environment variable keys.
        self.key_word = key_word
        # The function name.
        # 
        # This parameter is required.
        self.name = name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

