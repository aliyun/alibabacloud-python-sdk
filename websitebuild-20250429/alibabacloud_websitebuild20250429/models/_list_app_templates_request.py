# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppTemplatesRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        color_scheme: str = None,
        industry: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        product_version: str = None,
        status: str = None,
    ):
        # Application Type
        self.app_type = app_type
        # Color scheme
        self.color_scheme = color_scheme
        # industry categorization
        self.industry = industry
        # Search keyword
        self.keyword = keyword
        # Number of results per query.  
        # 
        # Value range: 10–100. Default Value: 20.
        self.max_results = max_results
        # Token indicating the start of the next query. It is empty when there is no next query.
        self.next_token = next_token
        # Page number
        self.page_num = page_num
        # Page size
        self.page_size = page_size
        # Edition
        self.product_version = product_version
        # template Status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.color_scheme is not None:
            result['ColorScheme'] = self.color_scheme

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ColorScheme') is not None:
            self.color_scheme = m.get('ColorScheme')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

