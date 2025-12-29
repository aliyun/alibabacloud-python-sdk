# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNodeSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        business_info: str = None,
        client_token: str = None,
        coupon_no: str = None,
        dbinstance_id: str = None,
        effective_time: str = None,
        from_app: str = None,
        node_class: str = None,
        node_id: str = None,
        node_storage: int = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        readonly_replicas: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        target_hidden_zone_id: str = None,
        target_secondary_zone_id: str = None,
        target_vswitch_id: str = None,
        target_zone_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true** (default): enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. In this case, you must manually pay for the instance.
        self.auto_pay = auto_pay
        # The business information. This is an additional parameter.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The time when the changed configurations take effect. Valid values:
        # 
        # *   **Immediately** (default): The new configurations immediately take effect
        # *   **MaintainTime**: The new configurations take effect during the maintenance window of the instance.
        self.effective_time = effective_time
        # The source of the request. Valid values:
        # 
        # *   **OpenApi**: the ApsaraDB for MongoDB API
        # *   **mongo_buy**: the ApsaraDB for MongoDB console
        self.from_app = from_app
        # The specifications of the shard or mongos node. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        self.node_class = node_class
        # The ID of the shard or mongos node in the sharded cluster instance. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to query the node ID.
        # 
        # > If you set this parameter to the ID of the shard node, you must also specify the **NodeStorage** parameter.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The storage capacity of the shard node. Unit: GB.
        # 
        # *   Valid values are **10** to **2000** if the instance uses local SSDs.
        # *   Valid values are **20** to **16000** if the instance uses enhanced SSDs (ESSDs) at PL1.
        # 
        # > The value must be a multiple of 10.
        self.node_storage = node_storage
        # The order type. Valid values:
        # 
        # *   **UPGRADE**
        # *   **DOWNGRADE**
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes in the shard node.
        # 
        # Valid values: **0** to **5**. The value must be an integer. Default value: **0**.
        self.readonly_replicas = readonly_replicas
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The execution time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.switch_time = switch_time
        self.target_hidden_zone_id = target_hidden_zone_id
        self.target_secondary_zone_id = target_secondary_zone_id
        self.target_vswitch_id = target_vswitch_id
        self.target_zone_id = target_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.from_app is not None:
            result['FromApp'] = self.from_app

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.target_hidden_zone_id is not None:
            result['TargetHiddenZoneId'] = self.target_hidden_zone_id

        if self.target_secondary_zone_id is not None:
            result['TargetSecondaryZoneId'] = self.target_secondary_zone_id

        if self.target_vswitch_id is not None:
            result['TargetVswitchId'] = self.target_vswitch_id

        if self.target_zone_id is not None:
            result['TargetZoneId'] = self.target_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TargetHiddenZoneId') is not None:
            self.target_hidden_zone_id = m.get('TargetHiddenZoneId')

        if m.get('TargetSecondaryZoneId') is not None:
            self.target_secondary_zone_id = m.get('TargetSecondaryZoneId')

        if m.get('TargetVswitchId') is not None:
            self.target_vswitch_id = m.get('TargetVswitchId')

        if m.get('TargetZoneId') is not None:
            self.target_zone_id = m.get('TargetZoneId')

        return self

