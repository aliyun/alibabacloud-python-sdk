# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQueryOptimizeDataTopRequest(DaraModel):
    def __init__(
        self,
        engine: str = None,
        instance_ids: str = None,
        region: str = None,
        tag_names: str = None,
        time: str = None,
        type: str = None,
    ):
        # The database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **PolarDBMySQL**
        # *   **PostgreSQL**
        # 
        # This parameter is required.
        self.engine = engine
        # The instance IDs. Separate multiple IDs with commas (,).
        self.instance_ids = instance_ids
        # The region in which the instance resides. Valid values:
        # 
        # *   **cn-china**: Chinese mainland
        # *   **cn-hongkong**: China (Hong Kong)
        # *   **ap-southeast-1**: Singapore
        # 
        # This parameter takes effect only if **InstanceIds** is left empty. If you leave **InstanceIds** empty, the system obtains data from the region set by **Region**. By default, Region is set to **cn-china**. If you specify **InstanceIds**, **Region** does not take effect and the system obtains data from the region in which the first specified instance resides.****
        # 
        # >  Set this parameter to **cn-china** for all your instances that reside in the regions in the Chinese mainland.
        self.region = region
        # The reserved parameter.
        self.tag_names = tag_names
        # The time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.time = time
        # The type of instances that you want to query. Valid values:
        # 
        # *   **RED**: the best-performing instances
        # *   **BLACK**: the worst-performing instances
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region is not None:
            result['Region'] = self.region

        if self.tag_names is not None:
            result['TagNames'] = self.tag_names

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

