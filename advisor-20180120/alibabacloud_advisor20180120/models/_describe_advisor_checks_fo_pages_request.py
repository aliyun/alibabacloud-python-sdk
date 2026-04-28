# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAdvisorChecksFoPagesRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id: int = None,
        biz_category: str = None,
        category: str = None,
        check_types: List[int] = None,
        language: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        product: str = None,
        source: str = None,
        status: str = None,
        token: str = None,
    ):
        self.assume_aliyun_id = assume_aliyun_id
        self.biz_category = biz_category
        self.category = category
        self.check_types = check_types
        self.language = language
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.product = product
        self.source = source
        self.status = status
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_aliyun_id is not None:
            result['AssumeAliyunId'] = self.assume_aliyun_id

        if self.biz_category is not None:
            result['BizCategory'] = self.biz_category

        if self.category is not None:
            result['Category'] = self.category

        if self.check_types is not None:
            result['CheckTypes'] = self.check_types

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product is not None:
            result['Product'] = self.product

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunId') is not None:
            self.assume_aliyun_id = m.get('AssumeAliyunId')

        if m.get('BizCategory') is not None:
            self.biz_category = m.get('BizCategory')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CheckTypes') is not None:
            self.check_types = m.get('CheckTypes')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

