# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGtmInstancesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        need_detail_attributes: bool = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The keyword that you use for query. Exact match is supported by instance ID or instance name.
        self.keyword = keyword
        # The language in which you want the values of some response parameters to be returned. These response parameters support multiple languages.
        self.lang = lang
        # Specifies whether additional information is required. Default value: **false**.
        self.need_detail_attributes = need_detail_attributes
        # The page number to return.
        self.page_number = page_number
        # The number of entries to return per page.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.need_detail_attributes is not None:
            result['NeedDetailAttributes'] = self.need_detail_attributes

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NeedDetailAttributes') is not None:
            self.need_detail_attributes = m.get('NeedDetailAttributes')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

