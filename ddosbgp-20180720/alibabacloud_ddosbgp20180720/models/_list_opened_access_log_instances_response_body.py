# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class ListOpenedAccessLogInstancesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sls_config_status: List[main_models.ListOpenedAccessLogInstancesResponseBodySlsConfigStatus] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The configuration of log analysis for the Anti-DDoS Origin instances.
        self.sls_config_status = sls_config_status
        # The number of the Anti-DDoS Origin instances for which log analysis was enabled.
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
                temp_model = main_models.ListOpenedAccessLogInstancesResponseBodySlsConfigStatus()
                self.sls_config_status.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOpenedAccessLogInstancesResponseBodySlsConfigStatus(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        instance_id: str = None,
    ):
        # Indicates whether log analysis was enabled for the Anti-DDoS Origin instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable = enable
        # The ID of the Anti-DDoS Origin instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

