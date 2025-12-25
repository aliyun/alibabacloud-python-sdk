# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListIndexesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        index_list: main_models.ListIndexesResponseBodyIndexList = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The details of indexes.
        self.index_list = index_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.index_list:
            self.index_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.index_list is not None:
            result['IndexList'] = self.index_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('IndexList') is not None:
            temp_model = main_models.ListIndexesResponseBodyIndexList()
            self.index_list = temp_model.from_map(m.get('IndexList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListIndexesResponseBodyIndexList(DaraModel):
    def __init__(
        self,
        index: List[main_models.ListIndexesResponseBodyIndexListIndex] = None,
    ):
        self.index = index

    def validate(self):
        if self.index:
            for v1 in self.index:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Index'] = []
        if self.index is not None:
            for k1 in self.index:
                result['Index'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index = []
        if m.get('Index') is not None:
            for k1 in m.get('Index'):
                temp_model = main_models.ListIndexesResponseBodyIndexListIndex()
                self.index.append(temp_model.from_map(k1))

        return self

class ListIndexesResponseBodyIndexListIndex(DaraModel):
    def __init__(
        self,
        index_comment: str = None,
        index_id: str = None,
        index_name: str = None,
        index_type: str = None,
        table_id: str = None,
    ):
        # The description of the index.
        self.index_comment = index_comment
        # The ID of the index.
        self.index_id = index_id
        # The name of the index.
        self.index_name = index_name
        # The type of the index. Valid values:
        # 
        # *   Primary
        # *   Unique
        # *   Normal
        # *   FullText
        # *   Spatial
        self.index_type = index_type
        # The ID of the table.
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_comment is not None:
            result['IndexComment'] = self.index_comment

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.index_name is not None:
            result['IndexName'] = self.index_name

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        if self.table_id is not None:
            result['TableId'] = self.table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexComment') is not None:
            self.index_comment = m.get('IndexComment')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        return self

