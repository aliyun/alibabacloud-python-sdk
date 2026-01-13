# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListParamsResponseBody(DaraModel):
    def __init__(
        self,
        params: List[main_models.ListParamsResponseBodyParams] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.params = params
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.ListParamsResponseBodyParams()
                self.params.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListParamsResponseBodyParams(DaraModel):
    def __init__(
        self,
        environment: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        param_id: str = None,
        value: str = None,
    ):
        self.environment = environment
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.param_id = param_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.param_id is not None:
            result['ParamId'] = self.param_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParamId') is not None:
            self.param_id = m.get('ParamId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

