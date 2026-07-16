# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class ListPromptVersionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListPromptVersionsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListPromptVersionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPromptVersionsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_items: List[main_models.ListPromptVersionsResponseBodyDataPageItems] = None,
        page_number: int = None,
        pages_available: int = None,
        total_count: int = None,
    ):
        self.page_items = page_items
        self.page_number = page_number
        self.pages_available = pages_available
        self.total_count = total_count

    def validate(self):
        if self.page_items:
            for v1 in self.page_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PageItems'] = []
        if self.page_items is not None:
            for k1 in self.page_items:
                result['PageItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.pages_available is not None:
            result['PagesAvailable'] = self.pages_available

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('PageItems') is not None:
            for k1 in m.get('PageItems'):
                temp_model = main_models.ListPromptVersionsResponseBodyDataPageItems()
                self.page_items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PagesAvailable') is not None:
            self.pages_available = m.get('PagesAvailable')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPromptVersionsResponseBodyDataPageItems(DaraModel):
    def __init__(
        self,
        commit_msg: str = None,
        gmt_modified: int = None,
        prompt_key: str = None,
        src_user: str = None,
        status: str = None,
        version: str = None,
    ):
        self.commit_msg = commit_msg
        self.gmt_modified = gmt_modified
        self.prompt_key = prompt_key
        self.src_user = src_user
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit_msg is not None:
            result['CommitMsg'] = self.commit_msg

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        if self.src_user is not None:
            result['SrcUser'] = self.src_user

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitMsg') is not None:
            self.commit_msg = m.get('CommitMsg')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        if m.get('SrcUser') is not None:
            self.src_user = m.get('SrcUser')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

