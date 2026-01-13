# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrivateRAGServiceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # Instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) Interface to query the details of all AnalyticDB PostgreSQL Instances in the target region, including Instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

