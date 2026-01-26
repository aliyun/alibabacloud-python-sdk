# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetCommercialStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_and_commodity_status: main_models.GetCommercialStatusResponseBodyUserAndCommodityStatus = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The commercialization status of the service.
        self.user_and_commodity_status = user_and_commodity_status

    def validate(self):
        if self.user_and_commodity_status:
            self.user_and_commodity_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_and_commodity_status is not None:
            result['UserAndCommodityStatus'] = self.user_and_commodity_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserAndCommodityStatus') is not None:
            temp_model = main_models.GetCommercialStatusResponseBodyUserAndCommodityStatus()
            self.user_and_commodity_status = temp_model.from_map(m.get('UserAndCommodityStatus'))

        return self

class GetCommercialStatusResponseBodyUserAndCommodityStatus(DaraModel):
    def __init__(
        self,
        basic: bool = None,
        charge_type: str = None,
        enable: bool = None,
        extra_info: Dict[str, Any] = None,
        free_days: int = None,
        lable: str = None,
        status: str = None,
    ):
        # Indicates whether you are using the Basic Edition.
        self.basic = basic
        # The billing method.
        self.charge_type = charge_type
        # Indicates whether the service is activated.
        self.enable = enable
        # The additional information.
        self.extra_info = extra_info
        # The number of days during which the service is free of charge.
        self.free_days = free_days
        # The tags.
        self.lable = lable
        # The commercialization status.
        # 
        # Valid values:
        # 
        # *   Normal: The service is activated.
        # *   Abnormal: An exception occurs during activation.
        # *   Free: The service is not activated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic is not None:
            result['Basic'] = self.basic

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.free_days is not None:
            result['FreeDays'] = self.free_days

        if self.lable is not None:
            result['Lable'] = self.lable

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Basic') is not None:
            self.basic = m.get('Basic')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('FreeDays') is not None:
            self.free_days = m.get('FreeDays')

        if m.get('Lable') is not None:
            self.lable = m.get('Lable')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

