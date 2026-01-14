# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDocTypesResponseBody(DaraModel):
    def __init__(
        self,
        doc_type_list: List[main_models.DescribeDocTypesResponseBodyDocTypeList] = None,
        request_id: str = None,
    ):
        # A list of OSS object types.
        self.doc_type_list = doc_type_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.doc_type_list:
            for v1 in self.doc_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DocTypeList'] = []
        if self.doc_type_list is not None:
            for k1 in self.doc_type_list:
                result['DocTypeList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_type_list = []
        if m.get('DocTypeList') is not None:
            for k1 in m.get('DocTypeList'):
                temp_model = main_models.DescribeDocTypesResponseBodyDocTypeList()
                self.doc_type_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDocTypesResponseBodyDocTypeList(DaraModel):
    def __init__(
        self,
        code: int = None,
        id: int = None,
        name: str = None,
    ):
        # The code of the object type.
        self.code = code
        # The ID of the object type.
        self.id = id
        # The name of the object type.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

