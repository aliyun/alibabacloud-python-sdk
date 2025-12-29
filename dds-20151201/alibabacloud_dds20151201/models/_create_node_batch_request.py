# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNodeBatchRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        auto_pay: bool = None,
        business_info: str = None,
        client_token: str = None,
        coupon_no: str = None,
        dbinstance_id: str = None,
        from_app: str = None,
        nodes_info: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        shard_direct: bool = None,
    ):
        # The username of the account. The username must meet the following requirements:
        # - The username starts with a lowercase letter. 
        # - The username contains lowercase letters, digits, and underscores (_). 
        # - The username is 4 to 16 characters in length. 
        # 
        # > - Keywords cannot be used as account usernames. 
        # > - The permissions of this account are fixed at read-only. 
        # > - The username and password are required to be set only when you apply for an endpoint for the shard node for the first time.
        self.account_name = account_name
        # The password of the account. The password must meet the following requirements:
        # - The password contains at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. 
        # - These special characters include ! @ # $ % ^ & * ( ) _ + - = 
        # - The password is 8 to 32 characters in length. 
        # > The account password of the shard node cannot be reset.
        self.account_password = account_password
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # - **true**: enables automatic payment. Make sure that you have sufficient balance within your account. 
        # - **false**: disables automatic payment. In this case, you must manually pay for the instance. You can perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > **Orders**. On the Orders page, find the order and complete the payment.
        self.auto_pay = auto_pay
        # The business information.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to use coupons. Default value: null. Valid values:
        # 
        # *   **default** or **null**: uses coupons.
        # *   **youhuiquan_promotion_option_id_for_blank**: does not use coupons.
        self.coupon_no = coupon_no
        # The ID of the instance for which you want to add nodes.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The source of the request. Valid values:
        # - **OpenApi**: ApsaraDB for MongoDB API 
        # - **mongo_buy**: ApsaraDB for MongoDB console
        self.from_app = from_app
        # The specifications of the mongos or shard node that you want to add. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html). 
        # 
        # > Up to 32 mongos or shard nodes are supported for each sharded cluster instance.
        # 
        # This parameter is required.
        self.nodes_info = nodes_info
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to apply for an endpoint for the shard node. Default value: false. Valid values:
        # - **true**: applies for an endpoint for the shard node. 
        # - **false**: does not apply for an endpoint for the shard node.
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

        if self.from_app is not None:
            result['FromApp'] = self.from_app

        if self.nodes_info is not None:
            result['NodesInfo'] = self.nodes_info

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')

        if m.get('NodesInfo') is not None:
            self.nodes_info = m.get('NodesInfo')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ShardDirect') is not None:
            self.shard_direct = m.get('ShardDirect')

        return self

