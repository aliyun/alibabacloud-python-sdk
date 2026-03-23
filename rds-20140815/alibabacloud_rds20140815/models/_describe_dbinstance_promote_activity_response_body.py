# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancePromoteActivityResponseBody(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        bid: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        dbtype: str = None,
        is_activity: str = None,
        request_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.bid = bid
        self.dbinstance_id = dbinstance_id
        self.dbinstance_name = dbinstance_name
        self.dbtype = dbtype
        self.is_activity = is_activity
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bid is not None:
            result['Bid'] = self.bid

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.is_activity is not None:
            result['IsActivity'] = self.is_activity

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('IsActivity') is not None:
            self.is_activity = m.get('IsActivity')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

