# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListInstanceRiskLevelsRequest(DaraModel):
    def __init__(
        self,
        instance_list: List[main_models.ListInstanceRiskLevelsRequestInstanceList] = None,
    ):
        # The instances.
        self.instance_list = instance_list

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.ListInstanceRiskLevelsRequestInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        return self

class ListInstanceRiskLevelsRequestInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        uuid: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The serial number of the instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

