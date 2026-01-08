# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ModifyCfwInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        update_list: List[main_models.ModifyCfwInstanceRequestUpdateList] = None,
    ):
        self.instance_id = instance_id
        self.update_list = update_list

    def validate(self):
        if self.update_list:
            for v1 in self.update_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['UpdateList'] = []
        if self.update_list is not None:
            for k1 in self.update_list:
                result['UpdateList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.update_list = []
        if m.get('UpdateList') is not None:
            for k1 in m.get('UpdateList'):
                temp_model = main_models.ModifyCfwInstanceRequestUpdateList()
                self.update_list.append(temp_model.from_map(k1))

        return self

class ModifyCfwInstanceRequestUpdateList(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

