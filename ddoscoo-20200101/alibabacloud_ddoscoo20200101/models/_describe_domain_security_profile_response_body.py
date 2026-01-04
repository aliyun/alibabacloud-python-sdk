# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainSecurityProfileResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.DescribeDomainSecurityProfileResponseBodyResult] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeDomainSecurityProfileResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DescribeDomainSecurityProfileResponseBodyResult(DaraModel):
    def __init__(
        self,
        global_enable: bool = None,
        global_mode: str = None,
    ):
        # Indicates whether the global mitigation policy is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.global_enable = global_enable
        # The mode of the global mitigation policy. Valid values:
        # 
        # *   **weak**: the Low mode
        # *   **default**: the Normal mode
        # *   **hard**: the Strict mode
        self.global_mode = global_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_enable is not None:
            result['GlobalEnable'] = self.global_enable

        if self.global_mode is not None:
            result['GlobalMode'] = self.global_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalEnable') is not None:
            self.global_enable = m.get('GlobalEnable')

        if m.get('GlobalMode') is not None:
            self.global_mode = m.get('GlobalMode')

        return self

