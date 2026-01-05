# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class TempModifyDBNodeRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        client_token: str = None,
        dbcluster_id: str = None,
        dbnode: List[main_models.TempModifyDBNodeRequestDBNode] = None,
        modify_type: str = None,
        operation_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        promotion_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
    ):
        self.auto_use_coupon = auto_use_coupon
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value. Make sure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The information about the scaled/added node.
        # 
        # This parameter is required.
        self.dbnode = dbnode
        # The type of configuration change. Set the value to **TempUpgrade**.
        # 
        # This parameter is required.
        self.modify_type = modify_type
        # The operation type. Valid values:
        # 
        # *   **Modify**: temporarily upgrades the configuration of the cluster.
        # 
        # This parameter is required.
        self.operation_type = operation_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.promotion_code = promotion_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The rollback time of the configuration for the temporary upgrade. Specify the time in the ISO 8601 standard in the YYYY-MM-DD hh:mm:ss format.
        # 
        # >  The rollback time cannot be 1 hour earlier than the current time and cannot be later than one day before the time when the cluster expires.
        # 
        # This parameter is required.
        self.restore_time = restore_time

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

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DBNode'] = []
        if self.dbnode is not None:
            for k1 in self.dbnode:
                result['DBNode'].append(k1.to_map() if k1 else None)

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.dbnode = []
        if m.get('DBNode') is not None:
            for k1 in m.get('DBNode'):
                temp_model = main_models.TempModifyDBNodeRequestDBNode()
                self.dbnode.append(temp_model.from_map(k1))

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        return self

class TempModifyDBNodeRequestDBNode(DaraModel):
    def __init__(
        self,
        target_class: str = None,
        zone_id: str = None,
    ):
        # The specifications of the scaled/added node.
        # 
        # > 
        # 
        # *   The specification of the new node must be consistent with the specifications of the original nodes.
        # 
        # *   You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to view the specifications of the original nodes.
        self.target_class = target_class
        # The ID of the zone in which the added node is deployed. It must be the same zone as the original nodes.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_class is not None:
            result['TargetClass'] = self.target_class

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetClass') is not None:
            self.target_class = m.get('TargetClass')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

