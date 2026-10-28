# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableDasProRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        sql_retention: int = None,
        user_id: str = None,
    ):
        # The instance ID of the database.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The storage duration of SQL Explorer data. Unit: days. Default value: **30**. Valid values:
        # 
        # - **30**
        # - **180**
        # - **365**
        # - **1095**
        # - **1825**
        self.sql_retention = sql_retention
        # The instance ID, which is the ID of the Alibaba Cloud account that created the database instance.
        # 
        # > This parameter is optional. After you specify the ID of the target database instance, the system automatically obtains the instance ID when you call the API operation.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sql_retention is not None:
            result['SqlRetention'] = self.sql_retention

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SqlRetention') is not None:
            self.sql_retention = m.get('SqlRetention')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

