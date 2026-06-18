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
        # An array of field names used to filter non-private fields (those not prefixed with an underscore _) in the Metadata field returned by this operation. By default, Fields is empty, and all non-private fields in Metadata are returned. To return only specific non-private fields in Metadata, such as title, pass title in this parameter.
        # 
        # Default value: empty.
        self.fields = fields
        # <props="china">
        # 
        # The file ID, which is the `FileId` returned by the **AddFile** operation. This field is not required for data query or image Q&A knowledge bases. This field is required for document search or audio/video search knowledge bases. You can also obtain the file ID by clicking the ID icon next to the file name on the Files tab of [Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center). You can use the file ID to filter the returned chunks. Default value: empty.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # The file ID, which is the `FileId` returned by the **AddFile** operation. This field is not required for data query or image Q&A knowledge bases. This field is required for document search knowledge bases. You can also obtain the file ID by clicking the ID icon next to the file name on the Files tab of
        # [Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). You can use the file ID to filter the returned chunks. Default value: empty.
        # 
        # .
        self.file_id = file_id
        # The file ID field in the legacy Model Studio SDK. The usage and default value are identical to those of the `FileId` field. If you are using the following versions (or later) of the Model Studio SDK, use the `FileId` field instead. If you are using the SWIFT Model Studio SDK, continue to use this field.
        # 
        # - Java (async): 1.0.18
        # - Java: 1.10.2
        # - TypeScript: 1.10.2
        # - Go: 1.10.2
        # - PHP: 1.10.2
        # - Python: 1.10.2
        # - C#: 1.10.2
        # - C++: 1.10.17
        # 
        # > **How to check the Model Studio SDK version**: Visit the <props="china">[Model Studio SDK center](https://api.aliyun.com/api-tools/sdk/bailian?version=2023-12-29)<props="intl">[Model Studio SDK center](https://api.alibabacloud.com/api-tools/sdk/bailian?version=2023-12-29), click "**Install**" in the left-side navigation pane, set the API version to "**2023-12-29**", select your programming language, and then click "**History Versions**" to view the version.
        self.filed = filed
        # The knowledge base ID, which is the `Data.Id` returned by the **CreateIndex** operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The page number to query. Minimum value: 1. Default value: 1.
        self.page_num = page_num
        # The number of text chunks to display per page in a paged query. Maximum value: 100. Default value: 10.
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

