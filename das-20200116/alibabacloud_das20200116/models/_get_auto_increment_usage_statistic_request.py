# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAutoIncrementUsageStatisticRequest(DaraModel):
    def __init__(
        self,
        db_names: str = None,
        instance_id: str = None,
        ratio_filter: float = None,
        real_time: bool = None,
    ):
        # The database name. If you specify a database, the operation queries the usage of auto-increment table IDs in the specified database. Otherwise, the operation queries the usage of auto-increment table IDs in all databases on the instance.
        # 
        # >  Specify the parameter value as a JSON array, such as [\\"db1\\",\\"db2\\"]. Separate multiple database names with commas (,).
        self.db_names = db_names
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The usage threshold of auto-increment IDs. Only usage that exceeds the threshold can be returned. Valid values are decimals that range from 0 to 1.
        # 
        # This parameter is required.
        self.ratio_filter = ratio_filter
        # Specifies whether to query real-time data. Valid values:
        # 
        # *   **true**: queries data in real time except for data generated in the last 10 minutes.****
        # *   **false**: queries data generated in the last 2 hours. If no such data exists, queries the latest data.
        # 
        # This parameter is required.
        self.real_time = real_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_names is not None:
            result['DbNames'] = self.db_names

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ratio_filter is not None:
            result['RatioFilter'] = self.ratio_filter

        if self.real_time is not None:
            result['RealTime'] = self.real_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RatioFilter') is not None:
            self.ratio_filter = m.get('RatioFilter')

        if m.get('RealTime') is not None:
            self.real_time = m.get('RealTime')

        return self

