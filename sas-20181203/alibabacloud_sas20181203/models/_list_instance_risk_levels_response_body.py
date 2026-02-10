# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListInstanceRiskLevelsResponseBody(DaraModel):
    def __init__(
        self,
        instance_risk_levels: List[main_models.ListInstanceRiskLevelsResponseBodyInstanceRiskLevels] = None,
        request_id: str = None,
    ):
        # The risk levels of instances.
        self.instance_risk_levels = instance_risk_levels
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_risk_levels:
            for v1 in self.instance_risk_levels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceRiskLevels'] = []
        if self.instance_risk_levels is not None:
            for k1 in self.instance_risk_levels:
                result['InstanceRiskLevels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_risk_levels = []
        if m.get('InstanceRiskLevels') is not None:
            for k1 in m.get('InstanceRiskLevels'):
                temp_model = main_models.ListInstanceRiskLevelsResponseBodyInstanceRiskLevels()
                self.instance_risk_levels.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstanceRiskLevelsResponseBodyInstanceRiskLevels(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        level: str = None,
        uuid: str = None,
    ):
        # The ID of the server.
        self.instance_id = instance_id
        # The risk level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        # *   **none**
        self.level = level
        # The UUID of the server for which you want to modify the defense rule. You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to query the UUIDs of servers.
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

        if self.level is not None:
            result['Level'] = self.level

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

