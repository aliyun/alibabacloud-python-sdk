# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListIndexDocumentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListIndexDocumentsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error status code.
        self.code = code
        # The data field returned by the operation.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code returned by the operation.
        self.status = status
        # Indicates whether the operation was successful. Valid values:
        # - true: The operation was successful.
        # - false: The operation failed.
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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListIndexDocumentsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListIndexDocumentsResponseBodyData(DaraModel):
    def __init__(
        self,
        documents: List[main_models.ListIndexDocumentsResponseBodyDataDocuments] = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of files in the knowledge base, sorted by file import time in descending order (consistent with the console).
        self.documents = documents
        # The knowledge base ID.
        self.index_id = index_id
        # The returned page number.
        self.page_number = page_number
        # The returned number of entries per page.
        self.page_size = page_size
        # The total number of returned results.
        self.total_count = total_count

    def validate(self):
        if self.documents:
            for v1 in self.documents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['Documents'].append(k1.to_map() if k1 else None)

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.ListIndexDocumentsResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIndexDocumentsResponseBodyDataDocuments(DaraModel):
    def __init__(
        self,
        code: str = None,
        document_type: str = None,
        gmt_modified: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        size: int = None,
        source_id: str = None,
        status: str = None,
    ):
        # The error status code for the file import.
        self.code = code
        # The file format type. Valid values: pdf, docx, doc, txt, md, pptx, ppt, png, jpg, jpeg, bmp, gif, and EXCEL.
        self.document_type = document_type
        # The time when the file was imported to the knowledge base, in UNIX timestamp format.
        self.gmt_modified = gmt_modified
        # The file ID.
        self.id = id
        # The error message for the file import.
        self.message = message
        # The file name.
        self.name = name
        # The file size, in bytes.
        self.size = size
        # <props="china">
        # 
        # For document search or audio/video search knowledge bases, this parameter specifies the category ID, which is the `CategoryId` returned by the **AddCategory** operation. You can also obtain the category ID by clicking the ID icon next to the category name on the Files tab of the [Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center) page.
        # 
        # 
        # For data query or image Q&A knowledge bases, this parameter specifies the data table ID. You can obtain the data table ID by clicking the ID icon next to the data table name on the Tables tab of the [Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center) page.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # For document search knowledge bases, this parameter specifies the category ID, which is the `CategoryId` returned by the **AddCategory** operation. You can also obtain the category ID by clicking the ID icon next to the category name on the Files tab of the [Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center) page.
        # 
        # 
        # For data query or image Q&A knowledge bases, this parameter specifies the data table ID. You can obtain the data table ID by clicking the ID icon next to the data table name on the Tables tab of the [Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) page.
        # 
        # .
        self.source_id = source_id
        # The file import status. Valid values:
        # - INSERT_ERROR: The file failed to be imported.
        # - RUNNING: The file is being imported.
        # - DELETED: The file has been deleted.
        # - FINISH: The file was imported.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.document_type is not None:
            result['DocumentType'] = self.document_type

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

