# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListApiPathFieldTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListApiPathFieldTemplatesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListApiPathFieldTemplatesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListApiPathFieldTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListApiPathFieldTemplatesResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The list of field templates. Each element in the items list is a field template record that contains the templateId, path, and protocol.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of records.
        self.total_size = total_size

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
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListApiPathFieldTemplatesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListApiPathFieldTemplatesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        path: str = None,
        protocol: str = None,
        template_id: str = None,
    ):
        # The request path corresponding to the field template.
        self.path = path
        # The API protocol applicable to the field template.
        self.protocol = protocol
        # The ID of the field template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['path'] = self.path

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

