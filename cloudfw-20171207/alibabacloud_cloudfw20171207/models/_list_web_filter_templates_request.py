# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListWebFilterTemplatesRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        status: str = None,
        web_filter_template_ids: List[str] = None,
    ):
        # The description of the web filtering template. Fuzzy match is supported.
        self.description = description
        # The name of the web filtering template. Fuzzy match is supported.
        self.name = name
        # The page number. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The status of the web filtering template. Exact match is supported. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        self.status = status
        # The IDs of the web filtering templates for batch exact matching. You can specify up to 100 template IDs.
        self.web_filter_template_ids = web_filter_template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.web_filter_template_ids is not None:
            result['WebFilterTemplateIds'] = self.web_filter_template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WebFilterTemplateIds') is not None:
            self.web_filter_template_ids = m.get('WebFilterTemplateIds')

        return self

