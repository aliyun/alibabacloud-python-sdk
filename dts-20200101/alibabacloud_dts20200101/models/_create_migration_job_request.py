# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMigrationJobRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        migration_job_class: str = None,
        owner_id: str = None,
        region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter. This parameter will be discontinued.
        self.account_id = account_id
        # The client token that is used to ensure the idempotence of the request. Generate a value from your client to ensure that the value is unique among different requests. The **ClientToken** parameter supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The specification of the data migration instance. Valid values: **small**, **medium**, **large**, **xlarge**, and **2xlarge**.
        # 
        # > - For the test performance of each specification, see [Data migration specifications](https://help.aliyun.com/document_detail/26606.html).
        # - For instance specifications and pricing, see [Pricing](https://help.aliyun.com/document_detail/117780.html).
        # 
        # This parameter is required.
        self.migration_job_class = migration_job_class
        self.owner_id = owner_id
        # The region of the data migration instance, which is the region of the destination database instance. For more information, see the supported [region list](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region = region
        # The region of the data migration instance. You do not need to specify this parameter. This parameter will be discontinued.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

