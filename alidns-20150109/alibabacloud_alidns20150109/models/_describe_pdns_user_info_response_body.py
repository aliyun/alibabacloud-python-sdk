# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_info: main_models.DescribePdnsUserInfoResponseBodyUserInfo = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the user.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserInfo') is not None:
            temp_model = main_models.DescribePdnsUserInfoResponseBodyUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class DescribePdnsUserInfoResponseBodyUserInfo(DaraModel):
    def __init__(
        self,
        available_access_security_type: str = None,
        available_service: str = None,
        pdns_id: int = None,
        secret_key: str = None,
        service_type: str = None,
        state: str = None,
        statistic_switch_status: str = None,
        stopped_service: str = None,
    ):
        # The enabled access security types.
        self.available_access_security_type = available_access_security_type
        # The enabled public recursive DNS service.
        self.available_service = available_service
        # The configuration ID of the users in public recursive DNS.
        self.pdns_id = pdns_id
        # The SecretKey configured for a UDP-based CIDR block.
        self.secret_key = secret_key
        # The type of the public recursive DNS service.
        self.service_type = service_type
        # The status of the public recursive DNS service.
        self.state = state
        # The status of the traffic analysis switch for the user in public recursive DNS service.
        self.statistic_switch_status = statistic_switch_status
        # The disabled public recursive DNS service.
        self.stopped_service = stopped_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_access_security_type is not None:
            result['AvailableAccessSecurityType'] = self.available_access_security_type

        if self.available_service is not None:
            result['AvailableService'] = self.available_service

        if self.pdns_id is not None:
            result['PdnsId'] = self.pdns_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.state is not None:
            result['State'] = self.state

        if self.statistic_switch_status is not None:
            result['StatisticSwitchStatus'] = self.statistic_switch_status

        if self.stopped_service is not None:
            result['StoppedService'] = self.stopped_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAccessSecurityType') is not None:
            self.available_access_security_type = m.get('AvailableAccessSecurityType')

        if m.get('AvailableService') is not None:
            self.available_service = m.get('AvailableService')

        if m.get('PdnsId') is not None:
            self.pdns_id = m.get('PdnsId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StatisticSwitchStatus') is not None:
            self.statistic_switch_status = m.get('StatisticSwitchStatus')

        if m.get('StoppedService') is not None:
            self.stopped_service = m.get('StoppedService')

        return self

