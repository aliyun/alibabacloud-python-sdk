# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class PermissionCondition(DaraModel):
    def __init__(
        self,
        bool_equals: main_models.PermissionConditionBoolEquals = None,
        bool_not_equals: main_models.PermissionConditionBoolNotEquals = None,
        ip_equals: main_models.PermissionConditionIpEquals = None,
        ip_not_equals: main_models.PermissionConditionIpNotEquals = None,
        string_like: main_models.PermissionConditionStringLike = None,
        string_not_like: main_models.PermissionConditionStringNotLike = None,
    ):
        self.bool_equals = bool_equals
        self.bool_not_equals = bool_not_equals
        # The IP address condition, which is true when the IP address is equal to one of the following lists.
        self.ip_equals = ip_equals
        # The IP address condition. This condition is true when the IP address is not equal to any of the following list.
        self.ip_not_equals = ip_not_equals
        # The string match condition, which is true when the string is equal to one of the following lists.
        self.string_like = string_like
        # The string match condition. This condition is true when the input string is not equal to any one of the following lists.
        self.string_not_like = string_not_like

    def validate(self):
        if self.bool_equals:
            self.bool_equals.validate()
        if self.bool_not_equals:
            self.bool_not_equals.validate()
        if self.ip_equals:
            self.ip_equals.validate()
        if self.ip_not_equals:
            self.ip_not_equals.validate()
        if self.string_like:
            self.string_like.validate()
        if self.string_not_like:
            self.string_not_like.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bool_equals is not None:
            result['bool_equals'] = self.bool_equals.to_map()

        if self.bool_not_equals is not None:
            result['bool_not_equals'] = self.bool_not_equals.to_map()

        if self.ip_equals is not None:
            result['ip_equals'] = self.ip_equals.to_map()

        if self.ip_not_equals is not None:
            result['ip_not_equals'] = self.ip_not_equals.to_map()

        if self.string_like is not None:
            result['string_like'] = self.string_like.to_map()

        if self.string_not_like is not None:
            result['string_not_like'] = self.string_not_like.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bool_equals') is not None:
            temp_model = main_models.PermissionConditionBoolEquals()
            self.bool_equals = temp_model.from_map(m.get('bool_equals'))

        if m.get('bool_not_equals') is not None:
            temp_model = main_models.PermissionConditionBoolNotEquals()
            self.bool_not_equals = temp_model.from_map(m.get('bool_not_equals'))

        if m.get('ip_equals') is not None:
            temp_model = main_models.PermissionConditionIpEquals()
            self.ip_equals = temp_model.from_map(m.get('ip_equals'))

        if m.get('ip_not_equals') is not None:
            temp_model = main_models.PermissionConditionIpNotEquals()
            self.ip_not_equals = temp_model.from_map(m.get('ip_not_equals'))

        if m.get('string_like') is not None:
            temp_model = main_models.PermissionConditionStringLike()
            self.string_like = temp_model.from_map(m.get('string_like'))

        if m.get('string_not_like') is not None:
            temp_model = main_models.PermissionConditionStringNotLike()
            self.string_not_like = temp_model.from_map(m.get('string_not_like'))

        return self

class PermissionConditionStringNotLike(DaraModel):
    def __init__(
        self,
        vpc_id: List[str] = None,
    ):
        # The vpcID of the client as a string match condition.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')

        return self

class PermissionConditionStringLike(DaraModel):
    def __init__(
        self,
        vpc_id: List[str] = None,
    ):
        # The vpcID of the client as a string match condition.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')

        return self

class PermissionConditionIpNotEquals(DaraModel):
    def __init__(
        self,
        client_ip: List[str] = None,
    ):
        # The IP address of the client.
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['client_ip'] = self.client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_ip') is not None:
            self.client_ip = m.get('client_ip')

        return self

class PermissionConditionIpEquals(DaraModel):
    def __init__(
        self,
        client_ip: List[str] = None,
    ):
        # The IP address of the client.
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['client_ip'] = self.client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_ip') is not None:
            self.client_ip = m.get('client_ip')

        return self

class PermissionConditionBoolNotEquals(DaraModel):
    def __init__(
        self,
        is_share_link: bool = None,
    ):
        self.is_share_link = is_share_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_share_link is not None:
            result['is_share_link'] = self.is_share_link

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_share_link') is not None:
            self.is_share_link = m.get('is_share_link')

        return self

class PermissionConditionBoolEquals(DaraModel):
    def __init__(
        self,
        is_share_link: bool = None,
    ):
        self.is_share_link = is_share_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_share_link is not None:
            result['is_share_link'] = self.is_share_link

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_share_link') is not None:
            self.is_share_link = m.get('is_share_link')

        return self

