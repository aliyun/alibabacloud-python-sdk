# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ModifyDBNodesClassRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        client_token: str = None,
        cloud_provider: str = None,
        dbcluster_id: str = None,
        dbnode: List[main_models.ModifyDBNodesClassRequestDBNode] = None,
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
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can generate the value of this parameter on the client side. The value must be unique across different requests and is case-sensitive. It can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The cloud provider of the instance.
        self.cloud_provider = cloud_provider
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The list of cluster nodes. If the cluster contains a node with HotReplicaMode set to ON, you must include all DBNodes (writer and reader nodes) in the same request, and the TargetClass of each node must be identical. Usage notes: HotReplicaMode scenario constraints: If the cluster contains a node with HotReplicaMode set to ON, you must include all DBNodes (writer and reader nodes) in the same request, and their TargetClass values must be identical.
        # 
        # This parameter is required.
        self.dbnode = dbnode
        # The modification type. Valid values:
        # 
        # - **Upgrade**: Upgrades the specifications.
        # 
        # - **Downgrade**: Downgrades the specifications.
        # 
        # This parameter is required.
        self.modify_type = modify_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest time to start the scheduled task. The format is `YYYY-MM-DDThh:mm:ssZ` (UTC).
        # > * The latest time must be at least 30 minutes later than the start time.
        # > * If `PlannedStartTime` is specified but this parameter is not, the latest time to start the task defaults to the start time plus 30 minutes. For example, if `PlannedStartTime` is set to `2021-01-14T09:00:00Z` and this parameter is left empty, the task will start at `2021-01-14T09:30:00Z` at the latest.
        self.planned_end_time = planned_end_time
        # The planned transient disconnection time.
        # 
        # The time follows the ISO 8601 standard in the UTC time zone. The format is YYYY-MM-DDTHH:mm:ssZ.
        self.planned_flashing_off_time = planned_flashing_off_time
        # The earliest time to start the scheduled configuration upgrade task. The format is `YYYY-MM-DDThh:mm:ssZ` (UTC).
        # > * This parameter takes effect only when `ModifyType` is set to `Upgrade`.
        # > * The start time can be any time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, the allowed start time ranges from `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # > * If this parameter is left empty, the configuration upgrade task is executed immediately by default.
        self.planned_start_time = planned_start_time
        # The coupon code. If this parameter is left empty, the default coupon is used.
        self.promotion_code = promotion_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The sub-edition of the cluster. Valid values:
        # 
        # - **normal_exclusive**: Dedicated
        # 
        # - **normal_general**: General-purpose
        self.sub_category = sub_category

    def validate(self):
        if self.dbnode:
            for v1 in self.dbnode:
                 if v1:
                    v1.validate()

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

        result['DBNode'] = []
        if self.dbnode is not None:
            for k1 in self.dbnode:
                result['DBNode'].append(k1.to_map() if k1 else None)

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

        self.dbnode = []
        if m.get('DBNode') is not None:
            for k1 in m.get('DBNode'):
                temp_model = main_models.ModifyDBNodesClassRequestDBNode()
                self.dbnode.append(temp_model.from_map(k1))

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

class ModifyDBNodesClassRequestDBNode(DaraModel):
    def __init__(
        self,
        dbnode_id: str = None,
        target_class: str = None,
    ):
        # The ID of the cluster node.
        # > If this parameter is specified, DBNode.N.TargetClass is required. N is an integer starting from 1, and the maximum value is 16 minus the current number of nodes.
        self.dbnode_id = dbnode_id
        # The specifications of the node to be modified. For more information about node specifications, see [Compute node specifications](https://help.aliyun.com/document_detail/102542.html). 
        # 
        # > If this parameter is specified, DBNode.N.DBNodeId is required. N is an integer starting from 1, and the maximum value is 16 minus the current number of nodes.
        self.target_class = target_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.target_class is not None:
            result['TargetClass'] = self.target_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('TargetClass') is not None:
            self.target_class = m.get('TargetClass')

        return self

