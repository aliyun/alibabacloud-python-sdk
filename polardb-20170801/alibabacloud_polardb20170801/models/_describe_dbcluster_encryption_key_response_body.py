# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterEncryptionKeyResponseBody(DaraModel):
    def __init__(
        self,
        encryption_key_list: List[main_models.DescribeDBClusterEncryptionKeyResponseBodyEncryptionKeyList] = None,
        request_id: str = None,
    ):
        self.encryption_key_list = encryption_key_list
        self.request_id = request_id

    def validate(self):
        if self.encryption_key_list:
            for v1 in self.encryption_key_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EncryptionKeyList'] = []
        if self.encryption_key_list is not None:
            for k1 in self.encryption_key_list:
                result['EncryptionKeyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.encryption_key_list = []
        if m.get('EncryptionKeyList') is not None:
            for k1 in m.get('EncryptionKeyList'):
                temp_model = main_models.DescribeDBClusterEncryptionKeyResponseBodyEncryptionKeyList()
                self.encryption_key_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterEncryptionKeyResponseBodyEncryptionKeyList(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        creator: str = None,
        delete_date: str = None,
        description: str = None,
        encryption_key: str = None,
        encryption_key_status: str = None,
        key_type: str = None,
        key_usage: str = None,
        material_expire_time: str = None,
        origin: str = None,
        used_by: str = None,
    ):
        self.alias_name = alias_name
        self.creator = creator
        self.delete_date = delete_date
        self.description = description
        self.encryption_key = encryption_key
        self.encryption_key_status = encryption_key_status
        self.key_type = key_type
        self.key_usage = key_usage
        self.material_expire_time = material_expire_time
        self.origin = origin
        self.used_by = used_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date

        if self.description is not None:
            result['Description'] = self.description

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_key_status is not None:
            result['EncryptionKeyStatus'] = self.encryption_key_status

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage

        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.used_by is not None:
            result['UsedBy'] = self.used_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionKeyStatus') is not None:
            self.encryption_key_status = m.get('EncryptionKeyStatus')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')

        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('UsedBy') is not None:
            self.used_by = m.get('UsedBy')

        return self

