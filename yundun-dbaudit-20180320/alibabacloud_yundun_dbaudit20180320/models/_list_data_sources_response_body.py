# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class ListDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        db_list: List[main_models.ListDataSourcesResponseBodyDbList] = None,
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
                temp_model = main_models.ListDataSourcesResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataSourcesResponseBodyDbList(DaraModel):
    def __init__(
        self,
        asset_type: int = None,
        audit_switch: int = None,
        create_time: str = None,
        db_addresses: List[str] = None,
        db_certificate: str = None,
        db_id: int = None,
        db_instance_id: str = None,
        db_name: str = None,
        db_type: int = None,
        db_type_name: str = None,
        db_username: str = None,
        db_version: int = None,
        db_version_name: str = None,
    ):
        self.asset_type = asset_type
        self.audit_switch = audit_switch
        self.create_time = create_time
        self.db_addresses = db_addresses
        self.db_certificate = db_certificate
        self.db_id = db_id
        self.db_instance_id = db_instance_id
        self.db_name = db_name
        self.db_type = db_type
        self.db_type_name = db_type_name
        self.db_username = db_username
        self.db_version = db_version
        self.db_version_name = db_version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.audit_switch is not None:
            result['AuditSwitch'] = self.audit_switch

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses

        if self.db_certificate is not None:
            result['DbCertificate'] = self.db_certificate

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name

        if self.db_username is not None:
            result['DbUsername'] = self.db_username

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.db_version_name is not None:
            result['DbVersionName'] = self.db_version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AuditSwitch') is not None:
            self.audit_switch = m.get('AuditSwitch')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')

        if m.get('DbCertificate') is not None:
            self.db_certificate = m.get('DbCertificate')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')

        if m.get('DbUsername') is not None:
            self.db_username = m.get('DbUsername')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('DbVersionName') is not None:
            self.db_version_name = m.get('DbVersionName')

        return self

