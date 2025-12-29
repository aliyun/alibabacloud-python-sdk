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
        shard_direct: bool = None,
    ):
        # The username of the account. The username must meet the following requirements:
        # 
        # *   The username starts with a lowercase letter.
        # *   The username can contain lowercase letters, digits, and underscores (_).
        # *   The username must be 4 to 16 characters in length.
        # 
        # > 
        # 
        # *   Keywords cannot be used as accounts.
        # 
        # *   This account is granted the read-only permissions.
        # *   The username and password need to be set if you apply for an endpoint for the shard node for the first time.
        self.account_name = account_name
        # The password of the account. The password must meet the following requirements:
        # 
        # *   The password contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   These special characters include ! @ # $ % ^ & \\* ( ) _ + - =
        # *   The password is 8 to 32 characters in length.
        # 
        # >  ApsaraDB for MongoDB does not allow you to reset the password of an account.
        self.account_password = account_password
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true** (default): enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. You can perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > Orders. On the **Orders** page, find the order that you want to pay for and complete the payment.
        # 
        # >  This parameter is required only when the billing method of the instance is subscription.
        self.auto_pay = auto_pay
        # The business information. This is an additional parameter.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the generated token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The coupon code. Default value: **youhuiquan_promotion_option_id_for_blank**.
        self.coupon_no = coupon_no
        # The ID of the sharded cluster instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The instance type of the shard or mongos node. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        # 
        # This parameter is required.
        self.node_class = node_class
        # The disk capacity of the node. Unit: GB.
        # 
        # Valid values: **10** to **2000**. The value must be a multiple of 10.
        # 
        # >  This parameter is required only when the NodeType parameter is set to **shard**.
        self.node_storage = node_storage
        # The type of the node. Valid values:
        # 
        # *   **shard**: shard node
        # *   **mongos**: mongos node
        # 
        # This parameter is required.
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes in the shard node.
        # 
        # Valid values: **0**, 1, 2, 3, 4, and **5**. Default value: **0**.
        # 
        # >  This parameter is available only for ApsaraDB for MongoDB instances that are purchased on the China site (aliyun.com).
        self.readonly_replicas = readonly_replicas
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to apply for an endpoint for the shard node. Valid values:
        # 
        # *   **true**: applies for an endpoint for the shard node.
        # *   **false** (default): does not apply for an endpoint for the shard node.
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

        if m.get('ShardDirect') is not None:
            self.shard_direct = m.get('ShardDirect')

        return self

