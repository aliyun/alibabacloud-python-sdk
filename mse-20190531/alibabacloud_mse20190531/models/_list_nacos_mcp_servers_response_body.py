# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListNacosMcpServersResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListNacosMcpServersResponseBodyData = None,
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
            temp_model = main_models.ListNacosMcpServersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNacosMcpServersResponseBodyData(DaraModel):
    def __init__(
        self,
        page_items: List[main_models.ListNacosMcpServersResponseBodyDataPageItems] = None,
        page_number: int = None,
        pages_available: int = None,
        total_count: int = None,
    ):
        self.page_items = page_items
        # pageNumber.
        self.page_number = page_number
        # pagesAvailable.
        self.pages_available = pages_available
        self.total_count = total_count

    def validate(self):
        if self.page_items:
            for v1 in self.page_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PageItems'] = []
        if self.page_items is not None:
            for k1 in self.page_items:
                result['PageItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.pages_available is not None:
            result['PagesAvailable'] = self.pages_available

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('PageItems') is not None:
            for k1 in m.get('PageItems'):
                temp_model = main_models.ListNacosMcpServersResponseBodyDataPageItems()
                self.page_items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PagesAvailable') is not None:
            self.pages_available = m.get('PagesAvailable')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNacosMcpServersResponseBodyDataPageItems(DaraModel):
    def __init__(
        self,
        capabilities: List[str] = None,
        description: str = None,
        front_protocol: str = None,
        id: str = None,
        name: str = None,
        protocol: str = None,
        version: str = None,
        version_detail: main_models.ListNacosMcpServersResponseBodyDataPageItemsVersionDetail = None,
    ):
        self.capabilities = capabilities
        self.description = description
        self.front_protocol = front_protocol
        # ID。
        self.id = id
        self.name = name
        self.protocol = protocol
        self.version = version
        self.version_detail = version_detail

    def validate(self):
        if self.version_detail:
            self.version_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities

        if self.description is not None:
            result['Description'] = self.description

        if self.front_protocol is not None:
            result['FrontProtocol'] = self.front_protocol

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.version is not None:
            result['Version'] = self.version

        if self.version_detail is not None:
            result['VersionDetail'] = self.version_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FrontProtocol') is not None:
            self.front_protocol = m.get('FrontProtocol')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionDetail') is not None:
            temp_model = main_models.ListNacosMcpServersResponseBodyDataPageItemsVersionDetail()
            self.version_detail = temp_model.from_map(m.get('VersionDetail'))

        return self

class ListNacosMcpServersResponseBodyDataPageItemsVersionDetail(DaraModel):
    def __init__(
        self,
        is_latest: bool = None,
        release_date: str = None,
        version: str = None,
    ):
        self.is_latest = is_latest
        self.release_date = release_date
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_latest is not None:
            result['Is_latest'] = self.is_latest

        if self.release_date is not None:
            result['Release_date'] = self.release_date

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Is_latest') is not None:
            self.is_latest = m.get('Is_latest')

        if m.get('Release_date') is not None:
            self.release_date = m.get('Release_date')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

