# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSoftwarelibSoftwareRequest(DaraModel):
    def __init__(
        self,
        classify_id: str = None,
        current_page: int = None,
        max_results: int = None,
        next_token: str = None,
        os: str = None,
        page_size: int = None,
        software_name: str = None,
        source_type: str = None,
    ):
        # The software classification ID. You can call [ListSoftwarelibClassify](~~ListSoftwarelibClassify~~) to obtain the value.
        self.classify_id = classify_id
        # The page number of the current page in a paging query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The maximum number of entries per page. This parameter is not supported by this operation. Use CurrentPage and PageSize for pagination.
        self.max_results = max_results
        # The pagination token. This parameter is not supported by this operation. Use CurrentPage and PageSize for pagination.
        self.next_token = next_token
        # The operating system to which the software package applies. Valid values:
        # - **Windows**: Windows.
        # - **Mac(Apple)**: macOS with Apple silicon.
        # - **Mac(Intel)**: macOS with Intel processors.
        self.os = os
        # The number of entries per page in a paging query. Valid values: 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The software name. Fuzzy match is supported.
        self.software_name = software_name
        # The software source. Valid values:
        # - **custom**: custom software.
        # - **builtin**: built-in software library.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify_id is not None:
            result['ClassifyId'] = self.classify_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.os is not None:
            result['Os'] = self.os

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.software_name is not None:
            result['SoftwareName'] = self.software_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassifyId') is not None:
            self.classify_id = m.get('ClassifyId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

