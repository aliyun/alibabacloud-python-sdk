# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class CreateComputeTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        data_set_ids: str = None,
        morse_info_list: List[main_models.CreateComputeTaskRequestMorseInfoList] = None,
        name: str = None,
        remarks: str = None,
        type: str = None,
    ):
        self.app_id = app_id
        self.data_set_ids = data_set_ids
        self.morse_info_list = morse_info_list
        self.name = name
        self.remarks = remarks
        self.type = type

    def validate(self):
        if self.morse_info_list:
            for v1 in self.morse_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.data_set_ids is not None:
            result['dataSetIds'] = self.data_set_ids

        result['morseInfoList'] = []
        if self.morse_info_list is not None:
            for k1 in self.morse_info_list:
                result['morseInfoList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.remarks is not None:
            result['remarks'] = self.remarks

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('dataSetIds') is not None:
            self.data_set_ids = m.get('dataSetIds')

        self.morse_info_list = []
        if m.get('morseInfoList') is not None:
            for k1 in m.get('morseInfoList'):
                temp_model = main_models.CreateComputeTaskRequestMorseInfoList()
                self.morse_info_list.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateComputeTaskRequestMorseInfoList(DaraModel):
    def __init__(
        self,
        cu_id: str = None,
        cu_version: str = None,
    ):
        self.cu_id = cu_id
        self.cu_version = cu_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_id is not None:
            result['cuId'] = self.cu_id

        if self.cu_version is not None:
            result['cuVersion'] = self.cu_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuId') is not None:
            self.cu_id = m.get('cuId')

        if m.get('cuVersion') is not None:
            self.cu_version = m.get('cuVersion')

        return self

