# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListNamespacesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListNamespacesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNamespacesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListNamespacesResponseBodyDataResult] = None,
        results: List[main_models.ListNamespacesResponseBodyDataResults] = None,
        total_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.results = results
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListNamespacesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.ListNamespacesResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListNamespacesResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        app_count: int = None,
        create_time: int = None,
        describe: str = None,
        instance_count: int = None,
        namespace: str = None,
        region: str = None,
        update_time: int = None,
        user_id: str = None,
        version: int = None,
    ):
        self.app_count = app_count
        self.create_time = create_time
        self.describe = describe
        self.instance_count = instance_count
        self.namespace = namespace
        self.region = region
        self.update_time = update_time
        self.user_id = user_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_count is not None:
            result['AppCount'] = self.app_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListNamespacesResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        app_count: int = None,
        create_time: int = None,
        describe: str = None,
        instance_count: int = None,
        namespace: str = None,
        region: str = None,
        tags: Dict[str, Any] = None,
        update_time: int = None,
        user_id: str = None,
        version: int = None,
    ):
        self.app_count = app_count
        self.create_time = create_time
        self.describe = describe
        self.instance_count = instance_count
        self.namespace = namespace
        self.region = region
        self.tags = tags
        self.update_time = update_time
        self.user_id = user_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_count is not None:
            result['AppCount'] = self.app_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

