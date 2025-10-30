# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListDocumentsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        items: main_models.ListDocumentsResponseBodyItems = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The queried documents.
        self.items = items
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Items') is not None:
            temp_model = main_models.ListDocumentsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListDocumentsResponseBodyItems(DaraModel):
    def __init__(
        self,
        document_list: List[main_models.ListDocumentsResponseBodyItemsDocumentList] = None,
    ):
        self.document_list = document_list

    def validate(self):
        if self.document_list:
            for v1 in self.document_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DocumentList'] = []
        if self.document_list is not None:
            for k1 in self.document_list:
                result['DocumentList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.document_list = []
        if m.get('DocumentList') is not None:
            for k1 in m.get('DocumentList'):
                temp_model = main_models.ListDocumentsResponseBodyItemsDocumentList()
                self.document_list.append(temp_model.from_map(k1))

        return self

class ListDocumentsResponseBodyItemsDocumentList(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        source: str = None,
    ):
        # The name of the document.
        self.file_name = file_name
        # The source of the document.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

