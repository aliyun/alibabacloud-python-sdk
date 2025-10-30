# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeModelServiceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        model_service_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.model_service_id = model_service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        return self

