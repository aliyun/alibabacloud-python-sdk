# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterStorageSpaceRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        client_token: str = None,
        cloud_provider: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        promotion_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_space: int = None,
        sub_category: str = None,
    ):
        # Specifies whether to automatically use a coupon. Valid values:
        # 
        # - `true` (default): A coupon is automatically used.
        # 
        # - `false`: A coupon is not used.
        self.auto_use_coupon = auto_use_coupon
        # A client-generated token that ensures the idempotence of the request. The token must be unique for each request, case-sensitive, and a maximum of 64 ASCII characters in length.
        self.client_token = client_token
        # Specifies the cloud provider of the instance.
        self.cloud_provider = cloud_provider
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies the latest time to start the scheduled task. Specify the time in UTC in the `YYYY-MM-DDThh:mm:ssZ` format.
        # 
        # > - The latest start time must be at least 30 minutes later than the earliest start time.
        # >
        # > - If you specify `PlannedStartTime` but not this parameter, the latest start time is `PlannedStartTime + 30 minutes` by default. For example, if you set `PlannedStartTime` to `2021-01-14T09:00:00Z` and leave this parameter empty, the task starts no later than `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # Specifies the earliest time to start the scheduled task. Specify the time in UTC in the `YYYY-MM-DDThh:mm:ssZ` format.
        # 
        # > - This parameter takes effect only when `ModifyType` is set to `Upgrade`.
        # >
        # > - The start time can be a point in time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can set the start time to a value that is between `2021-01-14T09:00:00Z` and `2021-01-15T09:00:00Z`.
        # >
        # > - If you leave this parameter empty, the task runs immediately.
        self.planned_start_time = planned_start_time
        # Specifies the promotion code. If you do not specify this parameter, the system uses the default coupon.
        self.promotion_code = promotion_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies the new storage space. Unit: GB.
        # 
        # > For PolarDB for MySQL Standard Edition clusters, the storage space must be between 20 GB and 32,000 GB.
        # 
        # This parameter is required.
        self.storage_space = storage_space
        # Specifies the subcategory of the cluster. Valid values:
        # 
        # - **normal_exclusive**: dedicated
        # 
        # - **normal_general**: general-purpose
        self.sub_category = sub_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.sub_category is not None:
            result['SubCategory'] = self.sub_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('SubCategory') is not None:
            self.sub_category = m.get('SubCategory')

        return self

