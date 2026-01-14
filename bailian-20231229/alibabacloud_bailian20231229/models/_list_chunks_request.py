# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListChunksRequest(DaraModel):
    def __init__(
        self,
        fields: List[str] = None,
        file_id: str = None,
        filed: str = None,
        index_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # An array of field names. This parameter is used to filter non-private fields (prefixed with_underscores) in the Metadata parameter returned by this operation. By default, this parameter is left empty, which means all non-private fields in the Metadata parameter are returned. If you only want specified non-private fields, such as title, set this parameter to title.
        self.fields = fields
        self.file_id = file_id
        # The primary key ID of the document. This parameter is not required for structured knowledge base, but is required for unstructured knowledge base. To view the ID, you can click the ID icon next to the file name on the [Data Management](https://bailian.console.aliyun.com/#/data-center) page. You can filter returned chunks by the document ID. This parameter is left empty by default.
        self.filed = filed
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The number of the pages to return. Pages start from page 1. Default value: 1.
        self.page_num = page_num
        # The number of chunks to display on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['Fields'] = self.fields

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.filed is not None:
            result['Filed'] = self.filed

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Filed') is not None:
            self.filed = m.get('Filed')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

