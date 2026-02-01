# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListInstancesEcsInfoListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListInstancesEcsInfoListResponseBodyData] = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message

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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListInstancesEcsInfoListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class ListInstancesEcsInfoListResponseBodyData(DaraModel):
    def __init__(
        self,
        ip: str = None,
        tag_key: str = None,
        tag_value: str = None,
        type: str = None,
    ):
        self.ip = ip
        self.tag_key = tag_key
        self.tag_value = tag_value
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['ip'] = self.ip

        if self.tag_key is not None:
            result['tag_key'] = self.tag_key

        if self.tag_value is not None:
            result['tag_value'] = self.tag_value

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('tag_key') is not None:
            self.tag_key = m.get('tag_key')

        if m.get('tag_value') is not None:
            self.tag_value = m.get('tag_value')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

