# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeBatchSlsDispatchStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sls_config_status_list: List[main_models.DescribeBatchSlsDispatchStatusResponseBodySlsConfigStatusList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sls_config_status_list = sls_config_status_list
        self.total_count = total_count

    def validate(self):
        if self.sls_config_status_list:
            for v1 in self.sls_config_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SlsConfigStatusList'] = []
        if self.sls_config_status_list is not None:
            for k1 in self.sls_config_status_list:
                result['SlsConfigStatusList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sls_config_status_list = []
        if m.get('SlsConfigStatusList') is not None:
            for k1 in m.get('SlsConfigStatusList'):
                temp_model = main_models.DescribeBatchSlsDispatchStatusResponseBodySlsConfigStatusList()
                self.sls_config_status_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBatchSlsDispatchStatusResponseBodySlsConfigStatusList(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enable: bool = None,
    ):
        self.domain = domain
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

