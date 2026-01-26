# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListCmsInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListCmsInstancesResponseBodyData = None,
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
            temp_model = main_models.ListCmsInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCmsInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_tag: bool = None,
        products: List[main_models.ListCmsInstancesResponseBodyDataProducts] = None,
    ):
        self.enable_tag = enable_tag
        self.products = products

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_tag is not None:
            result['EnableTag'] = self.enable_tag

        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTag') is not None:
            self.enable_tag = m.get('EnableTag')

        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.ListCmsInstancesResponseBodyDataProducts()
                self.products.append(temp_model.from_map(k1))

        return self

class ListCmsInstancesResponseBodyDataProducts(DaraModel):
    def __init__(
        self,
        descr: str = None,
        id: str = None,
        instance: str = None,
        name: str = None,
        prod: str = None,
        source: str = None,
        state: str = None,
        time: str = None,
        type: str = None,
        url: str = None,
    ):
        self.descr = descr
        self.id = id
        self.instance = instance
        self.name = name
        self.prod = prod
        self.source = source
        self.state = state
        self.time = time
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.descr is not None:
            result['Descr'] = self.descr

        if self.id is not None:
            result['Id'] = self.id

        if self.instance is not None:
            result['Instance'] = self.instance

        if self.name is not None:
            result['Name'] = self.name

        if self.prod is not None:
            result['Prod'] = self.prod

        if self.source is not None:
            result['Source'] = self.source

        if self.state is not None:
            result['State'] = self.state

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Descr') is not None:
            self.descr = m.get('Descr')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Instance') is not None:
            self.instance = m.get('Instance')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prod') is not None:
            self.prod = m.get('Prod')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

