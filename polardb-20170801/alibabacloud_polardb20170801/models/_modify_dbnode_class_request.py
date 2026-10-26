# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBNodeClassRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        client_token: str = None,
        cloud_provider: str = None,
        dbcluster_id: str = None,
        dbnode_target_class: str = None,
        dbnode_type: str = None,
        modify_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        planned_end_time: str = None,
        planned_flashing_off_time: str = None,
        planned_start_time: str = None,
        promotion_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sub_category: str = None,
    ):
        # Specifies whether to automatically use a coupon. Valid values:
        # * true (default): Uses the coupon.
        # * false: Does not use the coupon.
        self.auto_use_coupon = auto_use_coupon
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can generate the value of this parameter on the client side. The value must be unique across different requests and is case-sensitive. The value can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The cloud service provider of the instance.
        self.cloud_provider = cloud_provider
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The target specifications for all nodes. For more information, see [Compute node specifications](https://help.aliyun.com/document_detail/102542.html).
        # 
        # This parameter is required.
        self.dbnode_target_class = dbnode_target_class
        # The node type. Set the value to DLNode only when you modify the node specifications of an AI node.
        self.dbnode_type = dbnode_type
        # The modification type. Valid values: 
        # * **Upgrade**: Upgrades the specifications.
        # * **Downgrade**: Downgrades the specifications.
        # 
        # This parameter is required.
        self.modify_type = modify_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest time to start the scheduled task. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        # > * The latest time must be at least 30 minutes later than the start time.
        # > * If `PlannedStartTime` is specified but this parameter is left empty, the latest time to start the task defaults to 30 minutes after the start time. For example, if `PlannedStartTime` is set to `2021-01-14T09:00:00Z` and this parameter is left empty, the task starts at `2021-01-14T09:30:00Z` at the latest.
        self.planned_end_time = planned_end_time
        # The planned transient disconnection time.
        # 
        # The time follows the ISO 8601 standard in the `YYYY-MM-DDTHH:mm:ssZ` format. The time is displayed in UTC.
        self.planned_flashing_off_time = planned_flashing_off_time
        # The earliest time to start the scheduled upgrade or downgrade task within the specified time window. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        # > * This parameter takes effect only when `ModifyType` is set to `Upgrade` or `Downgrade`.
        # >* The start time must be within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, the allowed start time ranges from `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # >* If this parameter is left empty, the upgrade task is executed immediately by default.
        self.planned_start_time = planned_start_time
        # The coupon code. If this parameter is left empty, the default coupon is used.
        self.promotion_code = promotion_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The sub-edition of the cluster. Valid values:
        # 
        # - **normal_exclusive**: Dedicated.
        # 
        # - **normal_general**: General-purpose.
        # 
        # This parameter is required when you change the specifications between Dedicated and General-purpose.
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

        if self.dbnode_target_class is not None:
            result['DBNodeTargetClass'] = self.dbnode_target_class

        if self.dbnode_type is not None:
            result['DBNodeType'] = self.dbnode_type

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_flashing_off_time is not None:
            result['PlannedFlashingOffTime'] = self.planned_flashing_off_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('DBNodeTargetClass') is not None:
            self.dbnode_target_class = m.get('DBNodeTargetClass')

        if m.get('DBNodeType') is not None:
            self.dbnode_type = m.get('DBNodeType')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedFlashingOffTime') is not None:
            self.planned_flashing_off_time = m.get('PlannedFlashingOffTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SubCategory') is not None:
            self.sub_category = m.get('SubCategory')

        return self

