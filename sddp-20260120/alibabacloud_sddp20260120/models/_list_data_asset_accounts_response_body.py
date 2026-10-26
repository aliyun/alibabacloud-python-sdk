# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListDataAssetAccountsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListDataAssetAccountsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned data.
        self.current_page = current_page
        # The list of records returned in the current query.
        self.items = items
        # The number of entries returned per page in the current query.
        self.page_size = page_size
        # The request ID, which can be used to trace the current API call.
        self.request_id = request_id
        # The total number of entries that meet the current statistics or query conditions.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListDataAssetAccountsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataAssetAccountsResponseBodyItems(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        ali_uid: int = None,
        auth_db: str = None,
        auth_role: str = None,
        encryption_key_mode: str = None,
        engine_type: str = None,
        expire_time: int = None,
        id: int = None,
        instance_id: str = None,
        product_code: str = None,
        product_id: int = None,
        region_id: str = None,
        region_name: str = None,
    ):
        # The database account name.
        self.account_name = account_name
        # The ID of the Alibaba Cloud account to which the asset belongs.
        self.ali_uid = ali_uid
        # The authentication database of the MongoDB account. This parameter must be passed together with AccountName when modifying permissions.
        self.auth_db = auth_db
        # The column encryption access permissions. Valid values:
        # - fullAccess: plaintext access
        # - restrictedAccess: restricted access
        # - noneAccess: decryption prohibited. This value applies only to ApsaraDB RDS for MySQL instances whose current effective key mode is client_key.
        self.auth_role = auth_role
        # The current effective column encryption key mode. Valid values:
        # - client_key: local key
        # - kms_key: KMS key
        # This parameter is not returned if no effective configuration exists.
        self.encryption_key_mode = encryption_key_mode
        # The database engine type.
        self.engine_type = engine_type
        # The expiration time of the plaintext access permissions. The value is a UNIX timestamp that represents the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. This parameter is not returned if no validity period is set.
        self.expire_time = expire_time
        # The database account ID. This ID is used as AccountId when configuring permissions.
        self.id = id
        # The database instance ID.
        self.instance_id = instance_id
        # The cloud service code.
        self.product_code = product_code
        # The cloud service type ID. Valid values: 5 (RDS), 8 (POLARDB), and 27 (PolarDBX2).
        self.product_id = product_id
        # The region ID of the asset.
        self.region_id = region_id
        # The region name of the asset.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.auth_db is not None:
            result['AuthDb'] = self.auth_db

        if self.auth_role is not None:
            result['AuthRole'] = self.auth_role

        if self.encryption_key_mode is not None:
            result['EncryptionKeyMode'] = self.encryption_key_mode

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AuthDb') is not None:
            self.auth_db = m.get('AuthDb')

        if m.get('AuthRole') is not None:
            self.auth_role = m.get('AuthRole')

        if m.get('EncryptionKeyMode') is not None:
            self.encryption_key_mode = m.get('EncryptionKeyMode')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        return self

