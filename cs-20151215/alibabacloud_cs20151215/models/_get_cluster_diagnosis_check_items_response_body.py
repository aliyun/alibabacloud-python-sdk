# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class GetClusterDiagnosisCheckItemsResponseBody(DaraModel):
    def __init__(
        self,
        check_items: List[main_models.GetClusterDiagnosisCheckItemsResponseBodyCheckItems] = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The check item.
        self.check_items = check_items
        # The status code.
        self.code = code
        # Indicates whether the check is successful.
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.check_items:
            for v1 in self.check_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['check_items'] = []
        if self.check_items is not None:
            for k1 in self.check_items:
                result['check_items'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['code'] = self.code

        if self.is_success is not None:
            result['is_success'] = self.is_success

        if self.request_id is not None:
            result['request_id'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_items = []
        if m.get('check_items') is not None:
            for k1 in m.get('check_items'):
                temp_model = main_models.GetClusterDiagnosisCheckItemsResponseBodyCheckItems()
                self.check_items.append(temp_model.from_map(k1))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('is_success') is not None:
            self.is_success = m.get('is_success')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        return self

class GetClusterDiagnosisCheckItemsResponseBodyCheckItems(DaraModel):
    def __init__(
        self,
        desc: str = None,
        display: str = None,
        group: str = None,
        level: str = None,
        message: str = None,
        name: str = None,
        refer: str = None,
        value: str = None,
    ):
        # The description.
        self.desc = desc
        # The display name.
        self.display = display
        # The name of the group to which the check item belongs.
        self.group = group
        # The severity level of the check result.
        # 
        # Valid values:
        # 
        # *   normal
        # *   warning
        # *   error
        self.level = level
        # The check result.
        self.message = message
        # The name of the check item.
        self.name = name
        # The reference value.
        self.refer = refer
        # The value of the check item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.display is not None:
            result['display'] = self.display

        if self.group is not None:
            result['group'] = self.group

        if self.level is not None:
            result['level'] = self.level

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.refer is not None:
            result['refer'] = self.refer

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('display') is not None:
            self.display = m.get('display')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('refer') is not None:
            self.refer = m.get('refer')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

