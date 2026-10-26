# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyDBNodeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        client_token: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: str = None,
        dbinstance_storage_type: str = None,
        dbnode: List[main_models.ModifyDBNodeRequestDBNode] = None,
        dry_run: bool = None,
        effective_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        produce_async: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to automatically pay for the order.
        # Valid values:
        # 
        # 1. **true**: Automatic payment is enabled. Make sure that your account balance is sufficient.
        # 
        # 1. **false**: Only an order is generated and no payment is made.
        # 
        # 
        # 
        # 
        # > Default value: true. If your payment method has an insufficient balance, you can set this parameter to false. In this case, an unpaid order is generated, and you can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The new instance storage capacity. Unit: GB. For details, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance. Valid values:
        # * **cloud_essd**: PL1 ESSD.
        # * **cloud_essd2**: PL2 ESSD.
        # * **cloud_essd3**: PL3 ESSD.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The node information.
        # > This parameter applies to ApsaraDB RDS for MySQL Cluster Edition instances.
        self.dbnode = dbnode
        # Specifies whether to perform a precheck before the node modifications. Valid values:
        # * **true**: A precheck is performed, but the modifications are not applied. The precheck includes checks on request parameters, request format, service limits, and inventory.
        # * **false**: A normal request is sent, and the modifications are directly applied after the precheck is passed (default).
        self.dry_run = dry_run
        # The effective period. Valid values:
        # * **Immediate** (default): The modifications immediately take effect.
        # * **MaintainTime**: The modifications take effect within the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        self.effective_time = effective_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to asynchronously apply the modifications. Valid values:
        # * **true**: Only an order is generated, and the modifications are asynchronously applied (default).
        # * **false**: The modifications are synchronously applied after the precheck is passed.
        # 
        # > Default value: true. The modifications are asynchronously applied. If you set this parameter to false, the modifications are synchronously applied, and the API response time is relatively long.
        self.produce_async = produce_async
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

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

        result['DBNode'] = []
        if self.dbnode is not None:
            for k1 in self.dbnode:
                result['DBNode'].append(k1.to_map() if k1 else None)

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

        self.dbnode = []
        if m.get('DBNode') is not None:
            for k1 in m.get('DBNode'):
                temp_model = main_models.ModifyDBNodeRequestDBNode()
                self.dbnode.append(temp_model.from_map(k1))

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

class ModifyDBNodeRequestDBNode(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        node_id: str = None,
    ):
        # The node specifications.
        self.class_code = class_code
        # The node ID.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['classCode'] = self.class_code

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classCode') is not None:
            self.class_code = m.get('classCode')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        return self

