# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeAllDBInstanceClassResponseBody(DaraModel):
    def __init__(
        self,
        class_code_list: List[main_models.DescribeAllDBInstanceClassResponseBodyClassCodeList] = None,
        request_id: str = None,
    ):
        # The instance specifications.
        self.class_code_list = class_code_list
        self.request_id = request_id

    def validate(self):
        if self.class_code_list:
            for v1 in self.class_code_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClassCodeList'] = []
        if self.class_code_list is not None:
            for k1 in self.class_code_list:
                result['ClassCodeList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.class_code_list = []
        if m.get('ClassCodeList') is not None:
            for k1 in m.get('ClassCodeList'):
                temp_model = main_models.DescribeAllDBInstanceClassResponseBodyClassCodeList()
                self.class_code_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAllDBInstanceClassResponseBodyClassCodeList(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        cpu_cores: int = None,
        default_storage_in_gb: int = None,
        max_storage_in_gb: int = None,
        memory_in_gb: int = None,
        min_storage_in_gb: int = None,
        step_storage_in_gb: int = None,
    ):
        self.class_code = class_code
        self.cpu_cores = cpu_cores
        self.default_storage_in_gb = default_storage_in_gb
        self.max_storage_in_gb = max_storage_in_gb
        # The memory size.
        self.memory_in_gb = memory_in_gb
        self.min_storage_in_gb = min_storage_in_gb
        self.step_storage_in_gb = step_storage_in_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores

        if self.default_storage_in_gb is not None:
            result['DefaultStorageInGB'] = self.default_storage_in_gb

        if self.max_storage_in_gb is not None:
            result['MaxStorageInGB'] = self.max_storage_in_gb

        if self.memory_in_gb is not None:
            result['MemoryInGB'] = self.memory_in_gb

        if self.min_storage_in_gb is not None:
            result['MinStorageInGB'] = self.min_storage_in_gb

        if self.step_storage_in_gb is not None:
            result['StepStorageInGB'] = self.step_storage_in_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')

        if m.get('DefaultStorageInGB') is not None:
            self.default_storage_in_gb = m.get('DefaultStorageInGB')

        if m.get('MaxStorageInGB') is not None:
            self.max_storage_in_gb = m.get('MaxStorageInGB')

        if m.get('MemoryInGB') is not None:
            self.memory_in_gb = m.get('MemoryInGB')

        if m.get('MinStorageInGB') is not None:
            self.min_storage_in_gb = m.get('MinStorageInGB')

        if m.get('StepStorageInGB') is not None:
            self.step_storage_in_gb = m.get('StepStorageInGB')

        return self

