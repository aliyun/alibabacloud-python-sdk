# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCollectorsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        page: int = None,
        res_id: str = None,
        size: int = None,
        source_type: str = None,
    ):
        # The instance ID associated with the collector.
        self.instance_id = instance_id
        # The collector name.
        self.name = name
        # The page number of the returned results. Default value: 1. Minimum value: 1. Maximum value: 200.
        self.page = page
        # The collector ID.
        self.res_id = res_id
        # The number of results per page. Default value: 20. Minimum value: 1. Maximum value: 500.
        self.size = size
        # The type of machine on which the collector is deployed. If this parameter is not specified, all types are returned. Valid values:
        # 
        # - ECS: ECS instance
        # 
        # - ACK: Container Kubernetes cluster.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.name is not None:
            result['name'] = self.name

        if self.page is not None:
            result['page'] = self.page

        if self.res_id is not None:
            result['resId'] = self.res_id

        if self.size is not None:
            result['size'] = self.size

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('resId') is not None:
            self.res_id = m.get('resId')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

