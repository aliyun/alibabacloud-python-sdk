# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListVirusScanAdditionalListsResponseBody(DaraModel):
    def __init__(
        self,
        additional_lists: List[main_models.ListVirusScanAdditionalListsResponseBodyAdditionalLists] = None,
        request_id: str = None,
    ):
        self.additional_lists = additional_lists
        self.request_id = request_id

    def validate(self):
        if self.additional_lists:
            for v1 in self.additional_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdditionalLists'] = []
        if self.additional_lists is not None:
            for k1 in self.additional_lists:
                result['AdditionalLists'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_lists = []
        if m.get('AdditionalLists') is not None:
            for k1 in m.get('AdditionalLists'):
                temp_model = main_models.ListVirusScanAdditionalListsResponseBodyAdditionalLists()
                self.additional_lists.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVirusScanAdditionalListsResponseBodyAdditionalLists(DaraModel):
    def __init__(
        self,
        additional_type: str = None,
        lists: List[main_models.ListVirusScanAdditionalListsResponseBodyAdditionalListsLists] = None,
    ):
        self.additional_type = additional_type
        self.lists = lists

    def validate(self):
        if self.lists:
            for v1 in self.lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_type is not None:
            result['AdditionalType'] = self.additional_type

        result['Lists'] = []
        if self.lists is not None:
            for k1 in self.lists:
                result['Lists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalType') is not None:
            self.additional_type = m.get('AdditionalType')

        self.lists = []
        if m.get('Lists') is not None:
            for k1 in m.get('Lists'):
                temp_model = main_models.ListVirusScanAdditionalListsResponseBodyAdditionalListsLists()
                self.lists.append(temp_model.from_map(k1))

        return self

class ListVirusScanAdditionalListsResponseBodyAdditionalListsLists(DaraModel):
    def __init__(
        self,
        list_detail: List[main_models.ListVirusScanAdditionalListsResponseBodyAdditionalListsListsListDetail] = None,
        list_type: str = None,
    ):
        self.list_detail = list_detail
        self.list_type = list_type

    def validate(self):
        if self.list_detail:
            for v1 in self.list_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListDetail'] = []
        if self.list_detail is not None:
            for k1 in self.list_detail:
                result['ListDetail'].append(k1.to_map() if k1 else None)

        if self.list_type is not None:
            result['ListType'] = self.list_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_detail = []
        if m.get('ListDetail') is not None:
            for k1 in m.get('ListDetail'):
                temp_model = main_models.ListVirusScanAdditionalListsResponseBodyAdditionalListsListsListDetail()
                self.list_detail.append(temp_model.from_map(k1))

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        return self

class ListVirusScanAdditionalListsResponseBodyAdditionalListsListsListDetail(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        detail: str = None,
        list_id: str = None,
    ):
        self.create_time = create_time
        self.detail = detail
        self.list_id = list_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.list_id is not None:
            result['ListId'] = self.list_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('ListId') is not None:
            self.list_id = m.get('ListId')

        return self

