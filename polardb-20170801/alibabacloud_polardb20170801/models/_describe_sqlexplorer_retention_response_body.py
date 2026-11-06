# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQLExplorerRetentionResponseBody(DaraModel):
    def __init__(
        self,
        config_value: str = None,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        request_id: str = None,
    ):
        # The retention period of SQL Explorer logs. Valid values:
        # * **30**: 30 days
        # * **180**: 180 days
        # * **365**: 1 year
        # * **1095**: 3 years
        # * **1825**: 5 years
        self.config_value = config_value
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

