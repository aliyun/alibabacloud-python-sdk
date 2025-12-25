# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        region_id: str = None,
    ):
        # Database remark information.
        self.comment = comment
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database name. The name must meet the following requirements:
        # 
        # *   The name can contain lowercase letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a lowercase letter and end with a lowercase letter or digit.
        # *   The name can be up to 64 characters in length.
        # 
        # >  An underscore (_) is counted as two characters.
        # 
        # This parameter is required.
        self.dbname = dbname
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

