# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeCdcClassListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeCdcClassListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeCdcClassListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdcClassListResponseBodyData(DaraModel):
    def __init__(
        self,
        class_code_list: List[main_models.DescribeCdcClassListResponseBodyDataClassCodeList] = None,
    ):
        # array
        self.class_code_list = class_code_list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.class_code_list = []
        if m.get('ClassCodeList') is not None:
            for k1 in m.get('ClassCodeList'):
                temp_model = main_models.DescribeCdcClassListResponseBodyDataClassCodeList()
                self.class_code_list.append(temp_model.from_map(k1))

        return self

class DescribeCdcClassListResponseBodyDataClassCodeList(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        cpu_core: str = None,
        mem: str = None,
    ):
        self.class_code = class_code
        self.cpu_core = cpu_core
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.cpu_core is not None:
            result['CpuCore'] = self.cpu_core

        if self.mem is not None:
            result['Mem'] = self.mem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('CpuCore') is not None:
            self.cpu_core = m.get('CpuCore')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        return self

