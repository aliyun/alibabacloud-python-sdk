# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class GetDBAuditCountListResponseBody(DaraModel):
    def __init__(
        self,
        db_list: List[main_models.GetDBAuditCountListResponseBodyDbList] = None,
        request_id: str = None,
    ):
        self.db_list = db_list
        self.request_id = request_id

    def validate(self):
        if self.db_list:
            for v1 in self.db_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DbList'] = []
        if self.db_list is not None:
            for k1 in self.db_list:
                result['DbList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_list = []
        if m.get('DbList') is not None:
            for k1 in m.get('DbList'):
                temp_model = main_models.GetDBAuditCountListResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDBAuditCountListResponseBodyDbList(DaraModel):
    def __init__(
        self,
        asset_type: int = None,
        db_addresses: List[str] = None,
        db_id: int = None,
        db_name: str = None,
        db_type: int = None,
        db_type_name: str = None,
        db_version: int = None,
        db_version_name: str = None,
        risk_count: int = None,
        session_count: int = None,
        sql_count: int = None,
    ):
        self.asset_type = asset_type
        self.db_addresses = db_addresses
        self.db_id = db_id
        self.db_name = db_name
        self.db_type = db_type
        self.db_type_name = db_type_name
        self.db_version = db_version
        self.db_version_name = db_version_name
        self.risk_count = risk_count
        self.session_count = session_count
        self.sql_count = sql_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.db_version_name is not None:
            result['DbVersionName'] = self.db_version_name

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('DbVersionName') is not None:
            self.db_version_name = m.get('DbVersionName')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')

        return self

