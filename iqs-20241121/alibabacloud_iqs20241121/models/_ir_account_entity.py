# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IrAccountEntity(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        account_status: str = None,
        adjusted_normal_qps: int = None,
        configuration: str = None,
        create_time: str = None,
        id: int = None,
        is_deleted: int = None,
        modified_time: str = None,
        quark_key: str = None,
        quark_osr: str = None,
        quark_username: str = None,
        search_type: str = None,
        test_qps: int = None,
        test_query_per_day: int = None,
        test_start_time: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.account_status = account_status
        self.adjusted_normal_qps = adjusted_normal_qps
        self.configuration = configuration
        self.create_time = create_time
        self.id = id
        self.is_deleted = is_deleted
        self.modified_time = modified_time
        self.quark_key = quark_key
        self.quark_osr = quark_osr
        self.quark_username = quark_username
        self.search_type = search_type
        self.test_qps = test_qps
        self.test_query_per_day = test_query_per_day
        self.test_start_time = test_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.account_name is not None:
            result['accountName'] = self.account_name

        if self.account_status is not None:
            result['accountStatus'] = self.account_status

        if self.adjusted_normal_qps is not None:
            result['adjustedNormalQps'] = self.adjusted_normal_qps

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.is_deleted is not None:
            result['isDeleted'] = self.is_deleted

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.quark_key is not None:
            result['quarkKey'] = self.quark_key

        if self.quark_osr is not None:
            result['quarkOsr'] = self.quark_osr

        if self.quark_username is not None:
            result['quarkUsername'] = self.quark_username

        if self.search_type is not None:
            result['searchType'] = self.search_type

        if self.test_qps is not None:
            result['testQps'] = self.test_qps

        if self.test_query_per_day is not None:
            result['testQueryPerDay'] = self.test_query_per_day

        if self.test_start_time is not None:
            result['testStartTime'] = self.test_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')

        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')

        if m.get('adjustedNormalQps') is not None:
            self.adjusted_normal_qps = m.get('adjustedNormalQps')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isDeleted') is not None:
            self.is_deleted = m.get('isDeleted')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('quarkKey') is not None:
            self.quark_key = m.get('quarkKey')

        if m.get('quarkOsr') is not None:
            self.quark_osr = m.get('quarkOsr')

        if m.get('quarkUsername') is not None:
            self.quark_username = m.get('quarkUsername')

        if m.get('searchType') is not None:
            self.search_type = m.get('searchType')

        if m.get('testQps') is not None:
            self.test_qps = m.get('testQps')

        if m.get('testQueryPerDay') is not None:
            self.test_query_per_day = m.get('testQueryPerDay')

        if m.get('testStartTime') is not None:
            self.test_start_time = m.get('testStartTime')

        return self

