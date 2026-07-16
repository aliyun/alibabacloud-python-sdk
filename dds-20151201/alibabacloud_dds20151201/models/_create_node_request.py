# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNodeRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        auto_pay: bool = None,
        business_info: str = None,
        client_token: str = None,
        coupon_no: str = None,
        dbinstance_id: str = None,
        node_class: str = None,
        node_storage: int = None,
        node_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        readonly_replicas: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        search_dbinstance_class: str = None,
        search_node_count: int = None,
        search_storage: int = None,
        shard_direct: bool = None,
    ):
        # The account name. The name must meet the following requirements:
        # 
        # - Starts with a lowercase letter.
        # 
        # - Consists of lowercase letters, digits, and underscores (_).
        # 
        # - Is 4 to 16 characters in length.
        # 
        # > * Keywords of ApsaraDB for MongoDB cannot be used as the account name.
        # >
        # > * The account has read-only permissions.
        # >
        # > * You must set the account name and password only when you enable a public endpoint for a shard node for the first time. These parameters are not required on subsequent requests.
        self.account_name = account_name
        # The password for the account. The password must meet the following requirements:
        # 
        # - Must contain characters from at least three of the following categories: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # - Special characters include `!@#$%^&*()_+-=`.
        # 
        # - Is 8 to 32 characters in length.
        # 
        # > ApsaraDB for MongoDB does not support resetting the account password for shard nodes.
        self.account_password = account_password
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true**: (Default) Enables automatic payment. Ensure that your account has a sufficient balance.
        # 
        # <props="china">
        # 
        # - **false**: Disables automatic payment. In this case, you must manually pay for the node. To do so, log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Billing** > **Billing Management**. In the left-side navigation pane, choose **Subscription Orders** > **My Orders**. On the **Product Orders** tab, find the order and complete the payment.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # - **false**: Disables automatic payment. In this case, you must manually pay for the node. To do so, log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Billing** > **Billing Management**. In the left-side navigation pane, click **Order Management**. On the **Product Orders** page, find the order and complete the payment.
        # 
        # 
        # 
        # 
        # > This parameter is required for subscription instances.
        self.auto_pay = auto_pay
        # Additional business information.
        self.business_info = business_info
        # A client-generated token to ensure request idempotence. The token must be unique across requests, contain only ASCII characters, and not exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to use a coupon. Valid values:
        # 
        # - **default** or **null**: (Default) An available coupon is automatically applied.
        # 
        # - **youhuiquan_promotion_option_id_for_blank**: No coupon is used.
        self.coupon_no = coupon_no
        # The ID of the sharded cluster instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The instance type of the shard or mongos node. For more information, see [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html).
        # 
        # This parameter is required.
        self.node_class = node_class
        # The storage space of the node. Unit: GB.
        # 
        # The valid values of this parameter vary based on the storage type of the instance. For more information, see [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html).
        # 
        # > This parameter is required when the node type is **shard**.
        self.node_storage = node_storage
        # The node type. Valid values:
        # 
        # - **shard**: A shard node.
        # 
        # - **mongos**: A mongos node.
        # 
        # This parameter is required.
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes in a shard node.
        # 
        # Valid values: **0** to **5**. The default value is **0**.
        # 
        # > This parameter is available only on the China site (aliyun.com).
        self.readonly_replicas = readonly_replicas
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.search_dbinstance_class = search_dbinstance_class
        self.search_node_count = search_node_count
        self.search_storage = search_storage
        # Specifies whether to enable a public endpoint for the shard node. Valid values:
        # 
        # - **true**: Enables a public endpoint for the shard node.
        # 
        # - **false**: (Default) Does not enable a public endpoint for the shard node.
        self.shard_direct = shard_direct

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

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

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage

        if self.node_type is not None:
            result['NodeType'] = self.node_type

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

        if self.search_dbinstance_class is not None:
            result['SearchDBInstanceClass'] = self.search_dbinstance_class

        if self.search_node_count is not None:
            result['SearchNodeCount'] = self.search_node_count

        if self.search_storage is not None:
            result['SearchStorage'] = self.search_storage

        if self.shard_direct is not None:
            result['ShardDirect'] = self.shard_direct

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

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

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

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

        if m.get('SearchDBInstanceClass') is not None:
            self.search_dbinstance_class = m.get('SearchDBInstanceClass')

        if m.get('SearchNodeCount') is not None:
            self.search_node_count = m.get('SearchNodeCount')

        if m.get('SearchStorage') is not None:
            self.search_storage = m.get('SearchStorage')

        if m.get('ShardDirect') is not None:
            self.shard_direct = m.get('ShardDirect')

        return self

