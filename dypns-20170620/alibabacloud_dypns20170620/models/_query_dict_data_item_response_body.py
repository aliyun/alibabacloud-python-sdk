# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class QueryDictDataItemResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryDictDataItemResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryDictDataItemResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDictDataItemResponseBodyData(DaraModel):
    def __init__(
        self,
        classify_item_code: str = None,
        classify_item_value: str = None,
        data_item_code: str = None,
        data_item_order: int = None,
        data_item_parent: str = None,
        data_item_value: str = None,
        item_type: int = None,
        sub_list_data: List[main_models.QueryDictDataItemResponseBodyDataSubListData] = None,
    ):
        self.classify_item_code = classify_item_code
        self.classify_item_value = classify_item_value
        self.data_item_code = data_item_code
        self.data_item_order = data_item_order
        self.data_item_parent = data_item_parent
        self.data_item_value = data_item_value
        self.item_type = item_type
        self.sub_list_data = sub_list_data

    def validate(self):
        if self.sub_list_data:
            for v1 in self.sub_list_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify_item_code is not None:
            result['ClassifyItemCode'] = self.classify_item_code

        if self.classify_item_value is not None:
            result['ClassifyItemValue'] = self.classify_item_value

        if self.data_item_code is not None:
            result['DataItemCode'] = self.data_item_code

        if self.data_item_order is not None:
            result['DataItemOrder'] = self.data_item_order

        if self.data_item_parent is not None:
            result['DataItemParent'] = self.data_item_parent

        if self.data_item_value is not None:
            result['DataItemValue'] = self.data_item_value

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        result['SubListData'] = []
        if self.sub_list_data is not None:
            for k1 in self.sub_list_data:
                result['SubListData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassifyItemCode') is not None:
            self.classify_item_code = m.get('ClassifyItemCode')

        if m.get('ClassifyItemValue') is not None:
            self.classify_item_value = m.get('ClassifyItemValue')

        if m.get('DataItemCode') is not None:
            self.data_item_code = m.get('DataItemCode')

        if m.get('DataItemOrder') is not None:
            self.data_item_order = m.get('DataItemOrder')

        if m.get('DataItemParent') is not None:
            self.data_item_parent = m.get('DataItemParent')

        if m.get('DataItemValue') is not None:
            self.data_item_value = m.get('DataItemValue')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        self.sub_list_data = []
        if m.get('SubListData') is not None:
            for k1 in m.get('SubListData'):
                temp_model = main_models.QueryDictDataItemResponseBodyDataSubListData()
                self.sub_list_data.append(temp_model.from_map(k1))

        return self

class QueryDictDataItemResponseBodyDataSubListData(DaraModel):
    def __init__(
        self,
        classify_item_code: str = None,
        classify_item_value: str = None,
        data_item_code: str = None,
        data_item_order: int = None,
        data_item_parent: str = None,
        data_item_value: str = None,
        item_type: int = None,
    ):
        self.classify_item_code = classify_item_code
        self.classify_item_value = classify_item_value
        self.data_item_code = data_item_code
        self.data_item_order = data_item_order
        self.data_item_parent = data_item_parent
        self.data_item_value = data_item_value
        self.item_type = item_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify_item_code is not None:
            result['ClassifyItemCode'] = self.classify_item_code

        if self.classify_item_value is not None:
            result['ClassifyItemValue'] = self.classify_item_value

        if self.data_item_code is not None:
            result['DataItemCode'] = self.data_item_code

        if self.data_item_order is not None:
            result['DataItemOrder'] = self.data_item_order

        if self.data_item_parent is not None:
            result['DataItemParent'] = self.data_item_parent

        if self.data_item_value is not None:
            result['DataItemValue'] = self.data_item_value

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassifyItemCode') is not None:
            self.classify_item_code = m.get('ClassifyItemCode')

        if m.get('ClassifyItemValue') is not None:
            self.classify_item_value = m.get('ClassifyItemValue')

        if m.get('DataItemCode') is not None:
            self.data_item_code = m.get('DataItemCode')

        if m.get('DataItemOrder') is not None:
            self.data_item_order = m.get('DataItemOrder')

        if m.get('DataItemParent') is not None:
            self.data_item_parent = m.get('DataItemParent')

        if m.get('DataItemValue') is not None:
            self.data_item_value = m.get('DataItemValue')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        return self

