# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListViberServiceMessageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListViberServiceMessageResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListViberServiceMessageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListViberServiceMessageResponseBodyData(DaraModel):
    def __init__(
        self,
        business_account_name: str = None,
        destination_country_id: List[str] = None,
        destination_international_country_id: List[str] = None,
        industry_involved: str = None,
        message_destination_country: List[str] = None,
        message_destination_international_country: List[str] = None,
        service_id: str = None,
        state: str = None,
    ):
        self.business_account_name = business_account_name
        self.destination_country_id = destination_country_id
        self.destination_international_country_id = destination_international_country_id
        self.industry_involved = industry_involved
        self.message_destination_country = message_destination_country
        self.message_destination_international_country = message_destination_international_country
        self.service_id = service_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_account_name is not None:
            result['BusinessAccountName'] = self.business_account_name

        if self.destination_country_id is not None:
            result['DestinationCountryId'] = self.destination_country_id

        if self.destination_international_country_id is not None:
            result['DestinationInternationalCountryId'] = self.destination_international_country_id

        if self.industry_involved is not None:
            result['IndustryInvolved'] = self.industry_involved

        if self.message_destination_country is not None:
            result['MessageDestinationCountry'] = self.message_destination_country

        if self.message_destination_international_country is not None:
            result['MessageDestinationInternationalCountry'] = self.message_destination_international_country

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessAccountName') is not None:
            self.business_account_name = m.get('BusinessAccountName')

        if m.get('DestinationCountryId') is not None:
            self.destination_country_id = m.get('DestinationCountryId')

        if m.get('DestinationInternationalCountryId') is not None:
            self.destination_international_country_id = m.get('DestinationInternationalCountryId')

        if m.get('IndustryInvolved') is not None:
            self.industry_involved = m.get('IndustryInvolved')

        if m.get('MessageDestinationCountry') is not None:
            self.message_destination_country = m.get('MessageDestinationCountry')

        if m.get('MessageDestinationInternationalCountry') is not None:
            self.message_destination_international_country = m.get('MessageDestinationInternationalCountry')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

