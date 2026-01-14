# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddFileRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        lease_id: str = None,
        original_file_url: str = None,
        parser: str = None,
        tags: List[str] = None,
    ):
        # The primary key ID of the category to which the document is uploaded. This parameter corresponds to the `CategoryId` returned by the [AddCategory](https://www.alibabacloud.com/help/eh/model-studio/developer-reference/api-bailian-2023-12-29-addcategory) operation. You can also click the ID icon next to the category name on the Unstructured Data tab of the [Application Data](https://modelstudio.console.alibabacloud.com/#/data-center) page to view the ID. You can set the parameter to default, which specifies the Default Category created by the system.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The type of the category. Valid values:
        # - UNSTRUCTURED
        # - SESSION_FILE
        self.category_type = category_type
        # The lease ID, which corresponds to the `FileUploadLeaseId` parameter returned by the [ApplyFileUploadLease](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-applyfileuploadlease) operation.
        # 
        # This parameter is required.
        self.lease_id = lease_id
        self.original_file_url = original_file_url
        # The parser. Valid value:
        # 
        # *   DASHSCOPE_DOCMIND: Intelligent document parsing by Alibaba Cloud.
        # 
        # This parameter is required.
        self.parser = parser
        # A list of tags associated with the document. The default value is null, which means no tags. You can specify up to 10 tags.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.lease_id is not None:
            result['LeaseId'] = self.lease_id

        if self.original_file_url is not None:
            result['OriginalFileUrl'] = self.original_file_url

        if self.parser is not None:
            result['Parser'] = self.parser

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('LeaseId') is not None:
            self.lease_id = m.get('LeaseId')

        if m.get('OriginalFileUrl') is not None:
            self.original_file_url = m.get('OriginalFileUrl')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

