# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeBatchSlsDispatchStatusResponseBody(DaraModel):
    def __init__(
        self,
        item_list: List[main_models.DescribeBatchSlsDispatchStatusResponseBodyItemList] = None,
        logstore_name: str = None,
        project_name: str = None,
        request_id: str = None,
    ):
        self.item_list = item_list
        self.logstore_name = logstore_name
        self.project_name = project_name
        self.request_id = request_id

    def validate(self):
        if self.item_list:
            for v1 in self.item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ItemList'] = []
        if self.item_list is not None:
            for k1 in self.item_list:
                result['ItemList'].append(k1.to_map() if k1 else None)

        if self.logstore_name is not None:
            result['LogstoreName'] = self.logstore_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k1 in m.get('ItemList'):
                temp_model = main_models.DescribeBatchSlsDispatchStatusResponseBodyItemList()
                self.item_list.append(temp_model.from_map(k1))

        if m.get('LogstoreName') is not None:
            self.logstore_name = m.get('LogstoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBatchSlsDispatchStatusResponseBodyItemList(DaraModel):
    def __init__(
        self,
        config_status: str = None,
        dispatch_name: str = None,
        dispatch_value: str = None,
        enable: bool = None,
        filter_keys: List[str] = None,
        search_name: str = None,
    ):
        self.config_status = config_status
        self.dispatch_name = dispatch_name
        self.dispatch_value = dispatch_value
        self.enable = enable
        self.filter_keys = filter_keys
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status

        if self.dispatch_name is not None:
            result['DispatchName'] = self.dispatch_name

        if self.dispatch_value is not None:
            result['DispatchValue'] = self.dispatch_value

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.filter_keys is not None:
            result['FilterKeys'] = self.filter_keys

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')

        if m.get('DispatchName') is not None:
            self.dispatch_name = m.get('DispatchName')

        if m.get('DispatchValue') is not None:
            self.dispatch_value = m.get('DispatchValue')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FilterKeys') is not None:
            self.filter_keys = m.get('FilterKeys')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

