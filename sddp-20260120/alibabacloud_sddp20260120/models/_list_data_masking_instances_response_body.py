# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListDataMaskingInstancesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListDataMaskingInstancesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned data.
        self.current_page = current_page
        # The list of records returned by the current query.
        self.items = items
        # The number of entries returned per page in the current query.
        self.page_size = page_size
        # The request ID, which can be used to locate the current API call.
        self.request_id = request_id
        # The total number of entries that meet the current statistics or query scope.
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
                temp_model = main_models.ListDataMaskingInstancesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataMaskingInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        encryption_algorithm: str = None,
        encryption_key_id: str = None,
        engine_type: str = None,
        full_access_account_count: int = None,
        instance_id: str = None,
        product_code: str = None,
        product_id: int = None,
        region_id: str = None,
        region_name: str = None,
    ):
        # The current column encryption algorithm of the instance.
        self.encryption_algorithm = encryption_algorithm
        # The ID of the KMS key used by the instance. This parameter may not be returned in local key scenarios.
        self.encryption_key_id = encryption_key_id
        # The type of the database engine.
        self.engine_type = engine_type
        # The number of database accounts that have the fullAccess plaintext access permissions.
        self.full_access_account_count = full_access_account_count
        # The database instance identity.
        self.instance_id = instance_id
        # The code of the cloud service.
        self.product_code = product_code
        # The ID of the cloud service type. Valid values: 5: RDS. 8: POLARDB. 27: PolarDBX2.
        self.product_id = product_id
        # The ID of the region where the asset is located.
        self.region_id = region_id
        # The name of the region where the asset is located.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encryption_algorithm is not None:
            result['EncryptionAlgorithm'] = self.encryption_algorithm

        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.full_access_account_count is not None:
            result['FullAccessAccountCount'] = self.full_access_account_count

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
        if m.get('EncryptionAlgorithm') is not None:
            self.encryption_algorithm = m.get('EncryptionAlgorithm')

        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('FullAccessAccountCount') is not None:
            self.full_access_account_count = m.get('FullAccessAccountCount')

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

