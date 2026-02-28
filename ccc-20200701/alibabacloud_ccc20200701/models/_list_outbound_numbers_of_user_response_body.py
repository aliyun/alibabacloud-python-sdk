# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListOutboundNumbersOfUserResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListOutboundNumbersOfUserResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListOutboundNumbersOfUserResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOutboundNumbersOfUserResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListOutboundNumbersOfUserResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListOutboundNumbersOfUserResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOutboundNumbersOfUserResponseBodyDataList(DaraModel):
    def __init__(
        self,
        city: str = None,
        number: str = None,
        provider: str = None,
        provider_code: str = None,
        provider_display_name: str = None,
        provider_short_name: str = None,
        provider_type: str = None,
        province: str = None,
    ):
        self.city = city
        self.number = number
        self.provider = provider
        self.provider_code = provider_code
        self.provider_display_name = provider_display_name
        self.provider_short_name = provider_short_name
        self.provider_type = provider_type
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.number is not None:
            result['Number'] = self.number

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.provider_code is not None:
            result['ProviderCode'] = self.provider_code

        if self.provider_display_name is not None:
            result['ProviderDisplayName'] = self.provider_display_name

        if self.provider_short_name is not None:
            result['ProviderShortName'] = self.provider_short_name

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ProviderCode') is not None:
            self.provider_code = m.get('ProviderCode')

        if m.get('ProviderDisplayName') is not None:
            self.provider_display_name = m.get('ProviderDisplayName')

        if m.get('ProviderShortName') is not None:
            self.provider_short_name = m.get('ProviderShortName')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

