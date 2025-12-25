# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBNodeShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        client_token: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: str = None,
        dbinstance_storage_type: str = None,
        dbnode_shrink: str = None,
        dry_run: bool = None,
        effective_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        produce_async: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to automatically complete the payment. Valid values:
        # 
        # 1.  **true**: automatically completes the payment. Make sure that your account balance is sufficient.
        # 2.  **false**: does not automatically complete the payment. An unpaid order is generated.
        # 
        # >  The default value is true. If your account balance is insufficient, you can set the AutoPay parameter to false to generate an unpaid order. Then, you can log on to the ApsaraDB RDS console to pay for the order.
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The new storage capacity of the instance. Unit: GB For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd**: performance level 1 (PL1) enhanced SSD (ESSD)
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        self.dbinstance_storage_type = dbinstance_storage_type
        # The information about the node.
        # 
        # >  This parameter is used for ApsaraDB RDS for MySQL instances that run RDS Cluster Edition.
        self.dbnode_shrink = dbnode_shrink
        # Specifies whether to perform a dry run. Valid values: Valid values:
        # 
        # *   **true**: performs a dry run and does not perform the actual request. The system checks items such as the request parameters, request format, service limits, and available resources.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed.
        self.dry_run = dry_run
        # The time when you want the change to take effect. Valid values:
        # 
        # *   **Immediate** (default): The change immediately takes effect.
        # *   **MaintainTime**: The effective time is within the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        self.effective_time = effective_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to asynchronously perform the operation. Valid values:
        # 
        # *   **true** (default): sends only the order. The operation is asynchronously performed.
        # *   **false**: sends the request. After the request passes the check, the operation is directly performed.
        # 
        # >  The default value is true, which indicates that the change operation is asynchronously performed. If you set this parameter to false, the change operation is simultaneously performed. This prolongs the response time of the operation.
        self.produce_async = produce_async
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.dbnode_shrink is not None:
            result['DBNode'] = self.dbnode_shrink

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.produce_async is not None:
            result['ProduceAsync'] = self.produce_async

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DBNode') is not None:
            self.dbnode_shrink = m.get('DBNode')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProduceAsync') is not None:
            self.produce_async = m.get('ProduceAsync')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

