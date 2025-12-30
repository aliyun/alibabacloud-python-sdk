# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResolverEndpointsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        vpc_region_id: str = None,
    ):
        # The keyword of the endpoint name, which is used for fuzzy searches.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The state of the endpoint that you want to query. Valid values:
        # 
        # *   SUCCESS: The endpoint works as expected.
        # *   INIT: The endpoint is being created.
        # *   FAILED: The endpoint failed to be created.
        # *   CHANGE_INIT: The endpoint is being modified.
        # *   CHANGE_FAILED: The endpoint failed to be modified.
        # *   EXCEPTION: The endpoint encountered an exception.
        # 
        # >  If you do not specify this parameter, endpoints in all states are returned.
        self.status = status
        # The region ID of the outbound virtual private cloud (VPC).
        self.vpc_region_id = vpc_region_id

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        return self

