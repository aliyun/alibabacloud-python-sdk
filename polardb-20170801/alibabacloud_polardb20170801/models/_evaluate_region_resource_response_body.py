# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluateRegionResourceResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_available: str = None,
        dbtype: str = None,
        dbversion: str = None,
        request_id: str = None,
    ):
        # Indicates whether the resources are sufficient.
        # 
        # - **true**: The resources are sufficient.
        # 
        # - **false**: The resources are insufficient.
        self.dbinstance_available = dbinstance_available
        # The database engine type. Valid values:
        # 
        # - **MySQL**
        # 
        # - **PostgreSQL**
        # 
        # - **Oracle**
        self.dbtype = dbtype
        # The version of the database engine.
        # 
        # - Valid values for MySQL:
        # 
        #   - **5.6**
        # 
        #   - **5.7**
        # 
        #   - **8.0**
        # 
        # - Valid values for PostgreSQL:
        # 
        #   - **11**
        # 
        #   - **14**
        # 
        # - Valid value for Oracle: **11**.
        self.dbversion = dbversion
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_available is not None:
            result['DBInstanceAvailable'] = self.dbinstance_available

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceAvailable') is not None:
            self.dbinstance_available = m.get('DBInstanceAvailable')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

