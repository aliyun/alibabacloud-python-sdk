# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyScaItemRequest(DaraModel):
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
        # The type of the asset fingerprint that you want to query. Default value: **sca**. Valid values:
        # 
        # *   **sca**: middleware
        # *   **sca_database**: database
        # *   **sca_web**: web service
        # 
        # > If you do not specify this parameter, the default value **sca** is used, which indicates that middleware fingerprints are queried.
        self.biz = biz
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether to forcefully refresh the data that you want to query. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.force_flush = force_flush
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The search keyword. You must specify this parameter based on the value of the **SearchItem** parameter.
        # 
        # *   If the **SearchItem** parameter is set to **name**, you must enter the name of an asset fingerprint.
        # 
        # *   If the **SearchItem** parameter is set to **type**, you must enter the type of an asset fingerprint. Valid values:
        # 
        #     *   **system_service**: system service
        #     *   **software_library**: software library
        #     *   **docker_component**: container component
        #     *   **database**: database
        #     *   **web_container**: web container
        #     *   **jar**: JAR package
        #     *   **web_framework**: web framework
        # 
        # > You must specify both the **SearchItem** and **SearchInfo** parameters before you can query the asset fingerprints based on the specified name or type.
        self.search_info = search_info
        # The type of the search condition. Valid values:
        # 
        # *   **name**: the name of a database, middleware, or web service
        # *   **type**: the type of a database, middleware, or web service
        # 
        # > You must specify both the **SearchItem** and **SearchInfo** parameters before you can query the asset fingerprints based on the specified name or type.
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

