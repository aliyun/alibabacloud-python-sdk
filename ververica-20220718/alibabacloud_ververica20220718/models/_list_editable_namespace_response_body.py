# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ListEditableNamespaceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListEditableNamespaceResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        reason: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.http_code = http_code
        self.message = message
        self.reason = reason
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.message is not None:
            result['message'] = self.message

        if self.reason is not None:
            result['reason'] = self.reason

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListEditableNamespaceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListEditableNamespaceResponseBodyData(DaraModel):
    def __init__(
        self,
        editable_namespaces: List[main_models.EditableNamespace] = None,
        page_index: str = None,
        page_size: str = None,
        total: str = None,
    ):
        self.editable_namespaces = editable_namespaces
        self.page_index = page_index
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.editable_namespaces:
            for v1 in self.editable_namespaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['editableNamespaces'] = []
        if self.editable_namespaces is not None:
            for k1 in self.editable_namespaces:
                result['editableNamespaces'].append(k1.to_map() if k1 else None)

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.editable_namespaces = []
        if m.get('editableNamespaces') is not None:
            for k1 in m.get('editableNamespaces'):
                temp_model = main_models.EditableNamespace()
                self.editable_namespaces.append(temp_model.from_map(k1))

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

