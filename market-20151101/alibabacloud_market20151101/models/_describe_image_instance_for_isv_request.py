# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageInstanceForIsvRequest(DaraModel):
    def __init__(
        self,
        customer_pk: int = None,
        ecs_instance_id: str = None,
    ):
        self.customer_pk = customer_pk
        self.ecs_instance_id = ecs_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_pk is not None:
            result['CustomerPk'] = self.customer_pk

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerPk') is not None:
            self.customer_pk = m.get('CustomerPk')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        return self

