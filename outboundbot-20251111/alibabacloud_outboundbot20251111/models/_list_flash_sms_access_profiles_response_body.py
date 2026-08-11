# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class ListFlashSmsAccessProfilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListFlashSmsAccessProfilesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The list of variable values in the error message.
        self.params = params
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListFlashSmsAccessProfilesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListFlashSmsAccessProfilesResponseBodyData(DaraModel):
    def __init__(
        self,
        flash_sms_access_profiles: List[main_models.ListFlashSmsAccessProfilesResponseBodyDataFlashSmsAccessProfiles] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The data list.
        self.flash_sms_access_profiles = flash_sms_access_profiles
        # The page number, starting from 1.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The total number of records that match the conditions.
        self.total_count = total_count

    def validate(self):
        if self.flash_sms_access_profiles:
            for v1 in self.flash_sms_access_profiles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlashSmsAccessProfiles'] = []
        if self.flash_sms_access_profiles is not None:
            for k1 in self.flash_sms_access_profiles:
                result['FlashSmsAccessProfiles'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flash_sms_access_profiles = []
        if m.get('FlashSmsAccessProfiles') is not None:
            for k1 in m.get('FlashSmsAccessProfiles'):
                temp_model = main_models.ListFlashSmsAccessProfilesResponseBodyDataFlashSmsAccessProfiles()
                self.flash_sms_access_profiles.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFlashSmsAccessProfilesResponseBodyDataFlashSmsAccessProfiles(DaraModel):
    def __init__(
        self,
        access_profile: str = None,
        access_profile_id: str = None,
        created_time: int = None,
        provider_id: str = None,
        provider_name: str = None,
        updated_time: int = None,
    ):
        # The provider configuration information.
        self.access_profile = access_profile
        # The flash SMS configuration ID.
        self.access_profile_id = access_profile_id
        # The creation time, in millisecond-level timestamp.
        self.created_time = created_time
        # The provider ID. Valid values:\\
        # Uincall: Beijing Youyin Communication Co., Ltd.\\
        # ChuangLan: Beijing ChuangLan Cloud Intelligence Information Co., Ltd.\\
        # ChinaMobile: China Mobile.\\
        # ShangHaiTianNan: Shanghai Tiannan.\\
        # HeDao: Galexis.\\
        # DySms: Alibaba Communication.
        self.provider_id = provider_id
        # The provider name.
        self.provider_name = provider_name
        # The update time, in millisecond-level timestamp.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile is not None:
            result['AccessProfile'] = self.access_profile

        if self.access_profile_id is not None:
            result['AccessProfileId'] = self.access_profile_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfile') is not None:
            self.access_profile = m.get('AccessProfile')

        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

