# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class ListCallCenterProvidersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCallCenterProvidersResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
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

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListCallCenterProvidersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCallCenterProvidersResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        providers: List[main_models.ListCallCenterProvidersResponseBodyDataProviders] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.providers = providers
        self.total_count = total_count

    def validate(self):
        if self.providers:
            for v1 in self.providers:
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

        result['Providers'] = []
        if self.providers is not None:
            for k1 in self.providers:
                result['Providers'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.providers = []
        if m.get('Providers') is not None:
            for k1 in m.get('Providers'):
                temp_model = main_models.ListCallCenterProvidersResponseBodyDataProviders()
                self.providers.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCallCenterProvidersResponseBodyDataProviders(DaraModel):
    def __init__(
        self,
        destination: str = None,
        display_name: str = None,
        extras: str = None,
        instance_id: str = None,
        name: str = None,
        originator: str = None,
        provider_id: str = None,
        provider_type: str = None,
        refer_to: str = None,
        trunk_id: str = None,
    ):
        self.destination = destination
        self.display_name = display_name
        self.extras = extras
        self.instance_id = instance_id
        self.name = name
        self.originator = originator
        self.provider_id = provider_id
        self.provider_type = provider_type
        self.refer_to = refer_to
        self.trunk_id = trunk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination is not None:
            result['Destination'] = self.destination

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.extras is not None:
            result['Extras'] = self.extras

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.originator is not None:
            result['Originator'] = self.originator

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        if self.refer_to is not None:
            result['ReferTo'] = self.refer_to

        if self.trunk_id is not None:
            result['TrunkId'] = self.trunk_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Extras') is not None:
            self.extras = m.get('Extras')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Originator') is not None:
            self.originator = m.get('Originator')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('ReferTo') is not None:
            self.refer_to = m.get('ReferTo')

        if m.get('TrunkId') is not None:
            self.trunk_id = m.get('TrunkId')

        return self

