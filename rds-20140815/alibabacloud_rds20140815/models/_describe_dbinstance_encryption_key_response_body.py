# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceEncryptionKeyResponseBody(DaraModel):
    def __init__(
        self,
        creator: str = None,
        delete_date: str = None,
        description: str = None,
        encryption_key: str = None,
        encryption_key_list: List[main_models.DescribeDBInstanceEncryptionKeyResponseBodyEncryptionKeyList] = None,
        encryption_key_status: str = None,
        key_usage: str = None,
        material_expire_time: str = None,
        origin: str = None,
        request_id: str = None,
    ):
        # The user who created the key.
        self.creator = creator
        # The scheduled time at which the key is deleted. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.delete_date = delete_date
        # The description of the key.
        self.description = description
        # The ID of the key.
        self.encryption_key = encryption_key
        # The details about the key.
        self.encryption_key_list = encryption_key_list
        # The status of the key. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.encryption_key_status = encryption_key_status
        # The purpose of the key.
        self.key_usage = key_usage
        # The time at which the key expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.material_expire_time = material_expire_time
        # The source of the key.
        self.origin = origin
        # The ID of the request.
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
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date

        if self.description is not None:
            result['Description'] = self.description

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        result['EncryptionKeyList'] = []
        if self.encryption_key_list is not None:
            for k1 in self.encryption_key_list:
                result['EncryptionKeyList'].append(k1.to_map() if k1 else None)

        if self.encryption_key_status is not None:
            result['EncryptionKeyStatus'] = self.encryption_key_status

        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage

        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        self.encryption_key_list = []
        if m.get('EncryptionKeyList') is not None:
            for k1 in m.get('EncryptionKeyList'):
                temp_model = main_models.DescribeDBInstanceEncryptionKeyResponseBodyEncryptionKeyList()
                self.encryption_key_list.append(temp_model.from_map(k1))

        if m.get('EncryptionKeyStatus') is not None:
            self.encryption_key_status = m.get('EncryptionKeyStatus')

        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')

        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceEncryptionKeyResponseBodyEncryptionKeyList(DaraModel):
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
        # The alias of the key.
        self.alias_name = alias_name
        # The user who created the key.
        self.creator = creator
        # The scheduled time at which the key is deleted. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.delete_date = delete_date
        # The description of the key.
        self.description = description
        # The ID of the key.
        self.encryption_key = encryption_key
        # The status of the key. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.encryption_key_status = encryption_key_status
        # The type of the key. Valid values:
        # 
        # *   **CMK**
        # *   **ServiceKey**
        self.key_type = key_type
        # The purpose of the key.
        self.key_usage = key_usage
        # The time at which the key expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.material_expire_time = material_expire_time
        # The source of the key.
        self.origin = origin
        # The role of the instance. Valid values:
        # 
        # *   **Master**: primary instance
        # *   **slave**: read-only instance
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

