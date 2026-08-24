# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class ConfigSetDetailResponseBody(DaraModel):
    def __init__(
        self,
        detail: main_models.ConfigSetDetailResponseBodyDetail = None,
        request_id: str = None,
    ):
        # The configuration set information.
        self.detail = detail
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = main_models.ConfigSetDetailResponseBodyDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ConfigSetDetailResponseBodyDetail(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        ip_pool: main_models.ConfigSetDetailResponseBodyDetailIpPool = None,
        is_public_channel_backoff: bool = None,
        name: str = None,
        validation_option: main_models.ConfigSetDetailResponseBodyDetailValidationOption = None,
    ):
        # The description.
        self.description = description
        # The configuration set ID.
        self.id = id
        # The associated IP pool.
        self.ip_pool = ip_pool
        self.is_public_channel_backoff = is_public_channel_backoff
        # The configuration set name.
        self.name = name
        self.validation_option = validation_option

    def validate(self):
        if self.ip_pool:
            self.ip_pool.validate()
        if self.validation_option:
            self.validation_option.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_pool is not None:
            result['IpPool'] = self.ip_pool.to_map()

        if self.is_public_channel_backoff is not None:
            result['IsPublicChannelBackoff'] = self.is_public_channel_backoff

        if self.name is not None:
            result['Name'] = self.name

        if self.validation_option is not None:
            result['ValidationOption'] = self.validation_option.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpPool') is not None:
            temp_model = main_models.ConfigSetDetailResponseBodyDetailIpPool()
            self.ip_pool = temp_model.from_map(m.get('IpPool'))

        if m.get('IsPublicChannelBackoff') is not None:
            self.is_public_channel_backoff = m.get('IsPublicChannelBackoff')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ValidationOption') is not None:
            temp_model = main_models.ConfigSetDetailResponseBodyDetailValidationOption()
            self.validation_option = temp_model.from_map(m.get('ValidationOption'))

        return self

class ConfigSetDetailResponseBodyDetailValidationOption(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        forbidden_status_list: List[str] = None,
        forbidden_sub_status_list: List[str] = None,
    ):
        self.enabled = enabled
        self.forbidden_status_list = forbidden_status_list
        self.forbidden_sub_status_list = forbidden_sub_status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.forbidden_status_list is not None:
            result['ForbiddenStatusList'] = self.forbidden_status_list

        if self.forbidden_sub_status_list is not None:
            result['ForbiddenSubStatusList'] = self.forbidden_sub_status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ForbiddenStatusList') is not None:
            self.forbidden_status_list = m.get('ForbiddenStatusList')

        if m.get('ForbiddenSubStatusList') is not None:
            self.forbidden_sub_status_list = m.get('ForbiddenSubStatusList')

        return self

class ConfigSetDetailResponseBodyDetailIpPool(DaraModel):
    def __init__(
        self,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
    ):
        # The associated IP pool ID.
        self.ip_pool_id = ip_pool_id
        # The associated IP pool name.
        self.ip_pool_name = ip_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')

        return self

