# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListSaseUserTagsResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.ListSaseUserTagsResponseBodyDataList] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The list of user labels returned.
        self.data_list = data_list
        # The request ID.
        self.request_id = request_id
        # The total number of user labels.
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.ListSaseUserTagsResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListSaseUserTagsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        aliuid: str = None,
        count: int = None,
        description: str = None,
        name: str = None,
        tag_id: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.aliuid = aliuid
        # The number of users associated with the user label.
        self.count = count
        # The description of the user label.
        self.description = description
        # The name of the user label.
        self.name = name
        # The user label ID.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.count is not None:
            result['Count'] = self.count

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

