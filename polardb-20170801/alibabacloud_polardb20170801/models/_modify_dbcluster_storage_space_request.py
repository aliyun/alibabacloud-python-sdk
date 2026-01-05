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
        self.auto_use_coupon = auto_use_coupon
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. The token is case-sensitive.
        self.client_token = client_token
        self.cloud_provider = cloud_provider
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest time to upgrade the specifications within the scheduled time period. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # >- The value of this parameter must be at least 30 minutes later than PlannedStartTime.
        # >- By default, if you specify `PlannedStartTime` but do not specify PlannedEndTime, the latest start time of the task is set to `PlannedEndTime + 30 minutes`. For example, if you set `PlannedStartTime` to `2021-01-14T09:00:00Z` and you do not specify PlannedEndTime, the latest start time of the task is `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The earliest time to upgrade the specifications within the scheduled time period. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # >- This parameter takes effect only when `ModifyType` is set to `Upgrade`.
        # >- The earliest start time of the task can be a point in time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can specify a point in the time that ranges from `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # >- If this parameter is left empty, the upgrade task is immediately performed.
        self.planned_start_time = planned_start_time
        self.promotion_code = promotion_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The storage capacity that you can select when you change the cluster. Unit: GB.
        # 
        # >  You can set this parameter for PolarDB for MySQL clusters of Standard Edition to a value that ranges from 20 to 32000.
        # 
        # This parameter is required.
        self.storage_space = storage_space
        # The category of the cluster. Default value: ON. Valid values:
        # 
        # *   **normal_exclusive**: dedicated
        # *   **normal_general**: general-purpose
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

