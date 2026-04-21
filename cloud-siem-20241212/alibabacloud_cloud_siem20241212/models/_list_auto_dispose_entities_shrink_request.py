# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAutoDisposeEntitiesShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_dispose_record_ids_shrink: str = None,
        current_page: str = None,
        data_source_type: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: str = None,
        uuid: str = None,
    ):
        self.auto_dispose_record_ids_shrink = auto_dispose_record_ids_shrink
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.data_source_type = data_source_type
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.page_size = page_size
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_dispose_record_ids_shrink is not None:
            result['AutoDisposeRecordIds'] = self.auto_dispose_record_ids_shrink

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDisposeRecordIds') is not None:
            self.auto_dispose_record_ids_shrink = m.get('AutoDisposeRecordIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

