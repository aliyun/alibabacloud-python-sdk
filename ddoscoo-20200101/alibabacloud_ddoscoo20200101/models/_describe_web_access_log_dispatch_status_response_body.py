# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebAccessLogDispatchStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sls_config_status: List[main_models.DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the log analysis feature is enabled for domain names.
        self.sls_config_status = sls_config_status
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.sls_config_status:
            for v1 in self.sls_config_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SlsConfigStatus'] = []
        if self.sls_config_status is not None:
            for k1 in self.sls_config_status:
                result['SlsConfigStatus'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sls_config_status = []
        if m.get('SlsConfigStatus') is not None:
            for k1 in m.get('SlsConfigStatus'):
                temp_model = main_models.DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus()
                self.sls_config_status.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enable: bool = None,
    ):
        # The domain name.
        self.domain = domain
        # Indicates whether the log analysis feature is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
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

