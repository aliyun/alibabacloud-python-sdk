# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeConnectionCountRecordsResponseBody(DaraModel):
    def __init__(
        self,
        access_ip_records: List[main_models.DescribeConnectionCountRecordsResponseBodyAccessIpRecords] = None,
        dbcluster_id: str = None,
        request_id: str = None,
        user_records: List[main_models.DescribeConnectionCountRecordsResponseBodyUserRecords] = None,
    ):
        # The queried client IP addresses.
        self.access_ip_records = access_ip_records
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The queried database accounts.
        self.user_records = user_records

    def validate(self):
        if self.access_ip_records:
            for v1 in self.access_ip_records:
                 if v1:
                    v1.validate()
        if self.user_records:
            for v1 in self.user_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessIpRecords'] = []
        if self.access_ip_records is not None:
            for k1 in self.access_ip_records:
                result['AccessIpRecords'].append(k1.to_map() if k1 else None)

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserRecords'] = []
        if self.user_records is not None:
            for k1 in self.user_records:
                result['UserRecords'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_ip_records = []
        if m.get('AccessIpRecords') is not None:
            for k1 in m.get('AccessIpRecords'):
                temp_model = main_models.DescribeConnectionCountRecordsResponseBodyAccessIpRecords()
                self.access_ip_records.append(temp_model.from_map(k1))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.user_records = []
        if m.get('UserRecords') is not None:
            for k1 in m.get('UserRecords'):
                temp_model = main_models.DescribeConnectionCountRecordsResponseBodyUserRecords()
                self.user_records.append(temp_model.from_map(k1))

        return self

class DescribeConnectionCountRecordsResponseBodyUserRecords(DaraModel):
    def __init__(
        self,
        count: int = None,
        user: str = None,
    ):
        # The number of connections.
        self.count = count
        # The username of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class DescribeConnectionCountRecordsResponseBodyAccessIpRecords(DaraModel):
    def __init__(
        self,
        access_ip: str = None,
        count: int = None,
    ):
        # The IP address of the client.
        self.access_ip = access_ip
        # The number of connections.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

