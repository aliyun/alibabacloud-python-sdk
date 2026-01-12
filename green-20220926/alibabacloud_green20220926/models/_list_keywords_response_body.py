# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListKeywordsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListKeywordsResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # Returned data.
        self.data = data
        # Further description of the error code.
        self.msg = msg
        # ID assigned by the backend to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Success flag.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListKeywordsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListKeywordsResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListKeywordsResponseBodyDataItems] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Data of the current page.
        self.items = items
        # Page size.
        self.page_size = page_size
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListKeywordsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListKeywordsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        keyword_lib_id: str = None,
        keyword_md_5id: int = None,
        word: str = None,
    ):
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Primary key ID.
        self.id = id
        # Keyword library ID.
        self.keyword_lib_id = keyword_lib_id
        # Keyword data ID.
        self.keyword_md_5id = keyword_md_5id
        # Keyword.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id

        if self.keyword_md_5id is not None:
            result['KeywordMd5Id'] = self.keyword_md_5id

        if self.word is not None:
            result['Word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')

        if m.get('KeywordMd5Id') is not None:
            self.keyword_md_5id = m.get('KeywordMd5Id')

        if m.get('Word') is not None:
            self.word = m.get('Word')

        return self

