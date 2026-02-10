# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSearchConditionRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        source_ip: str = None,
        type: str = None,
    ):
        # The name of the frequently used search condition.
        # 
        # >  You can call the [DescribeSearchCondition](~~DescribeSearchCondition~~) operation to query frequently used search conditions.
        # 
        # This parameter is required.
        self.name = name
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the asset. Default value: ecs. Valid values:
        # 
        # *   **ecs**: an Elastic Compute Service (ECS) instance.
        # *   **cloud_product**: an Alibaba Cloud service.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

