# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class GetUserConfigResponseBody(DaraModel):
    def __init__(
        self,
        account_sufficient: bool = None,
        code: str = None,
        enable_eci_disk: bool = None,
        free_tier: main_models.GetUserConfigResponseBodyFreeTier = None,
        free_tier_spec_available: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.account_sufficient = account_sufficient
        self.code = code
        self.enable_eci_disk = enable_eci_disk
        self.free_tier = free_tier
        self.free_tier_spec_available = free_tier_spec_available
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.free_tier:
            self.free_tier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_sufficient is not None:
            result['AccountSufficient'] = self.account_sufficient

        if self.code is not None:
            result['Code'] = self.code

        if self.enable_eci_disk is not None:
            result['EnableEciDisk'] = self.enable_eci_disk

        if self.free_tier is not None:
            result['FreeTier'] = self.free_tier.to_map()

        if self.free_tier_spec_available is not None:
            result['FreeTierSpecAvailable'] = self.free_tier_spec_available

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSufficient') is not None:
            self.account_sufficient = m.get('AccountSufficient')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EnableEciDisk') is not None:
            self.enable_eci_disk = m.get('EnableEciDisk')

        if m.get('FreeTier') is not None:
            temp_model = main_models.GetUserConfigResponseBodyFreeTier()
            self.free_tier = temp_model.from_map(m.get('FreeTier'))

        if m.get('FreeTierSpecAvailable') is not None:
            self.free_tier_spec_available = m.get('FreeTierSpecAvailable')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetUserConfigResponseBodyFreeTier(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        init_base_unit: str = None,
        init_base_value: float = None,
        init_show_unit: str = None,
        init_show_value: str = None,
        is_free_tier_user: bool = None,
        period_base_unit: str = None,
        period_base_value: float = None,
        period_show_unit: str = None,
        period_show_value: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.init_base_unit = init_base_unit
        self.init_base_value = init_base_value
        self.init_show_unit = init_show_unit
        self.init_show_value = init_show_value
        self.is_free_tier_user = is_free_tier_user
        self.period_base_unit = period_base_unit
        self.period_base_value = period_base_value
        self.period_show_unit = period_show_unit
        self.period_show_value = period_show_value
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.init_base_unit is not None:
            result['InitBaseUnit'] = self.init_base_unit

        if self.init_base_value is not None:
            result['InitBaseValue'] = self.init_base_value

        if self.init_show_unit is not None:
            result['InitShowUnit'] = self.init_show_unit

        if self.init_show_value is not None:
            result['InitShowValue'] = self.init_show_value

        if self.is_free_tier_user is not None:
            result['IsFreeTierUser'] = self.is_free_tier_user

        if self.period_base_unit is not None:
            result['PeriodBaseUnit'] = self.period_base_unit

        if self.period_base_value is not None:
            result['PeriodBaseValue'] = self.period_base_value

        if self.period_show_unit is not None:
            result['PeriodShowUnit'] = self.period_show_unit

        if self.period_show_value is not None:
            result['PeriodShowValue'] = self.period_show_value

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InitBaseUnit') is not None:
            self.init_base_unit = m.get('InitBaseUnit')

        if m.get('InitBaseValue') is not None:
            self.init_base_value = m.get('InitBaseValue')

        if m.get('InitShowUnit') is not None:
            self.init_show_unit = m.get('InitShowUnit')

        if m.get('InitShowValue') is not None:
            self.init_show_value = m.get('InitShowValue')

        if m.get('IsFreeTierUser') is not None:
            self.is_free_tier_user = m.get('IsFreeTierUser')

        if m.get('PeriodBaseUnit') is not None:
            self.period_base_unit = m.get('PeriodBaseUnit')

        if m.get('PeriodBaseValue') is not None:
            self.period_base_value = m.get('PeriodBaseValue')

        if m.get('PeriodShowUnit') is not None:
            self.period_show_unit = m.get('PeriodShowUnit')

        if m.get('PeriodShowValue') is not None:
            self.period_show_value = m.get('PeriodShowValue')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

