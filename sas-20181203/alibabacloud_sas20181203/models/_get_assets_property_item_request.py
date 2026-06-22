# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAssetsPropertyItemRequest(DaraModel):
    def __init__(
        self,
        biz: str = None,
        current_page: int = None,
        force_flush: bool = None,
        lang: str = None,
        page_size: int = None,
        search_info: str = None,
        search_item: str = None,
    ):
        # The type of Asset Fingerprints to query. Default value: **sca**. Valid values:
        # 
        # - **lkm**: kernel module
        # - **autorun**: startup item
        # - **web_server**: website.
        # 
        # This parameter is required.
        self.biz = biz
        # The page number of the page to return. Default value: **1**, which indicates the first page.
        self.current_page = current_page
        # Specifies whether to forcefully refresh the data to be queried. Valid values:
        # - **true**: Forcefully refresh.
        # - **false**: Do not forcefully refresh.
        self.force_flush = force_flush
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - zh: Chinese
        # - en: English.
        self.lang = lang
        # The maximum number of entries to return on each page when using paging. Default value: 20. If the PageSize parameter is left empty, 20 entries are returned by default.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The content to query. Specify different query content based on the value of **SearchItem**:
        # - If **SearchItem** is set to **domain**, enter the domain name of the Asset Fingerprints entry.
        # - If **SearchItem** is set to **module_name**, enter the module name of the Asset Fingerprints entry.
        # - If **SearchItem** is set to **path**, enter the startup item path of the Asset Fingerprints entry.
        # 
        # > The **SearchItem** and **SearchInfo** parameters must be used together. Both parameters must be set at the same time for the query to take effect. Setting only one parameter does not take effect. You can use these parameters to query all data of a specific Asset Fingerprints entry by name.
        self.search_info = search_info
        # The type of query condition. Set different aggregation search conditions based on the **Biz** parameter. Valid values:
        # - If **Biz** is set to **web_server**, the following search conditions are supported for **SearchItem**:
        #     - **domain**: domain name
        # - If **Biz** is set to **lkm**, the following search conditions are supported for **SearchItem**:
        #     - **module_name**: module name
        # - If **Biz** is set to **autorun**, the following search conditions are supported for **SearchItem**:
        #     - **path**: startup item path
        # > The **SearchItem** and **SearchInfo** parameters must be used together. Both parameters must be set at the same time for the query to take effect. Setting only one parameter does not take effect. You can use these parameters to query all data of a specific Asset Fingerprints entry by name.
        self.search_item = search_item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.force_flush is not None:
            result['ForceFlush'] = self.force_flush

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_info is not None:
            result['SearchInfo'] = self.search_info

        if self.search_item is not None:
            result['SearchItem'] = self.search_item

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ForceFlush') is not None:
            self.force_flush = m.get('ForceFlush')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchInfo') is not None:
            self.search_info = m.get('SearchInfo')

        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')

        return self

