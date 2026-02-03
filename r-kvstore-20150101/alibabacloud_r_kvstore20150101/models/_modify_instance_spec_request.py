# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        business_info: str = None,
        client_token: str = None,
        coupon_no: str = None,
        effective_time: str = None,
        force_trans: bool = None,
        force_upgrade: bool = None,
        instance_class: str = None,
        instance_id: str = None,
        major_version: str = None,
        node_type: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        read_only_count: int = None,
        region_id: str = None,
        replica_count: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        shard_count: int = None,
        slave_read_only_count: int = None,
        slave_replica_count: int = None,
        source_biz: str = None,
        storage: int = None,
        storage_type: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true** (default): enables automatic payment.
        # *   **false**: disables automatic payment. If you set this parameter to **false**, the instance must be manually renewed before it expires. For more information, see [Renew an instance](https://help.aliyun.com/document_detail/26352.html).
        self.auto_pay = auto_pay
        # The ID of the promotional event or the business information.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The time when you want the configurations to be changed. Valid values:
        # 
        # *   **Immediately** (default): immediately changes the configurations.
        # *   **MaintainTime**: changes the configurations within the maintenance window. You can call the [ModifyInstanceMaintainTime](https://help.aliyun.com/document_detail/473775.html) operation to change the maintenance window.
        self.effective_time = effective_time
        # Specifies whether to enable forced transmission during a configuration change. Valid values:
        # 
        # *   **false** (default): Before the configuration change, the system checks the minor version of the instance. If the minor version of the instance is outdated, an error is reported. You must update the minor version of the instance and try again.
        # *   **true**: The system skips the version check and directly performs the configuration change.
        self.force_trans = force_trans
        # Specifies whether to forcibly change the configurations. Valid values:
        # 
        # *   **false**: The system does not forcefully change the configurations.
        # *   **true** (default): The system forcefully changes the configurations.
        self.force_upgrade = force_upgrade
        # The new instance type. You can call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/473765.html) operation to query the instance types available for configuration change within the zone to which the instance belongs.
        # 
        # >  For more information about the instance types, see [Overview](https://help.aliyun.com/document_detail/26350.html).
        self.instance_class = instance_class
        # The instance ID. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The major version of the classic instance that you want to upgrade. Valid values: **2.8**, **4.0**, and **5.0**.
        # 
        # >  The **InstanceClass** parameter is required when you upgrade the instance version. This parameter indicates that you can upgrade the instance version only when you update the instance specifications. If you only need to upgrade the instance version, call the [ModifyInstanceMajorVersion](https://help.aliyun.com/document_detail/473776.html) operation.
        self.major_version = major_version
        # The type of the node. Valid values:
        # 
        # *   **MASTER_SLAVE**: high availability (master-replica)
        # *   **STAND_ALONE**: standalone
        # *   **double**: master-replica
        # *   **single**: standalone
        # 
        # >  To create a cloud-native instance, set this parameter to **MASTER_SLAVE** or **STAND_ALONE**. To create a classic instance, set this parameter to **double** or **single**.
        self.node_type = node_type
        # The change type. This parameter is required when you change the configurations of a subscription instance. Valid values:
        # 
        # *   **UPGRADE** (default): upgrades the configurations of the subscription instance.
        # *   **DOWNGRADE**: downgrades the configurations of the subscription instance.
        # 
        # > 
        # 
        # *   To downgrade a subscription instance, you must set this parameter to **DOWNGRADE**.
        # 
        # *   If the price of an instance increases after its configurations are changed, the instance is upgraded. If the price decreases, the instance is downgraded. For example, the price of an 8 GB read/write splitting instance with five read replicas is higher than that of a 16 GB cluster instance. If you want to change a 16 GB cluster instance to an 8 GB read/write splitting instance with five read replicas, you must upgrade the instance.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read replicas in the primary zone. Valid values: 0 to 5. This parameter applies only to the following scenarios:
        # 
        # *   If the instance is a cloud-native standard instance, you can set this parameter to a value greater than 0 to enable the read/write splitting architecture.
        # *   If the instance is a cloud-native read/write splitting instance, you can use this parameter to customize the number of read replicas. You can also set this parameter to 0 to disable the read/write splitting architecture and switch the instance to the standard architecture.
        self.read_only_count = read_only_count
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent region list.
        self.region_id = region_id
        # The number of replica nodes in the primary zone. This parameter is applicable only to cloud-native multi-replica cluster instances. Valid values: 1 to 4.
        # 
        # > 
        # 
        # *   The sum of the values of this parameter and the SlaveReplicaCount parameter cannot be greater than 4.
        # 
        # *   You can specify either ReplicaCount or ReadOnlyCount.
        # 
        # *   A master-replica instance cannot contain multiple replica nodes.
        self.replica_count = replica_count
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The number of shards. This parameter is applicable only to cloud-native cluster instances.
        # 
        # > 
        # 
        # *   If you want to change a cloud-native cluster instance to a standard instance, you must explicitly set the ShardCount parameter to 1 and specify the specifications of the master-replica instance.
        # 
        # *   To change a cloud-native standard instance to a cluster instance, you must explicitly set the ShardCount parameter to a value greater than 1 and specify the specifications of the cluster instance.
        self.shard_count = shard_count
        # The number of read replicas in the secondary zone when you create a read/write splitting instance that is deployed across multiple zones. Valid values: 1 to 9. The sum of the values of this parameter and the ReadOnlyCount parameter cannot be greater than 9.
        self.slave_read_only_count = slave_read_only_count
        # The number of replica nodes in the secondary zone when you create a cloud-native multi-replica cluster instance that is deployed across multiple zones. The sum of the values of this parameter and the ReplicaCount parameter cannot be greater than 4.
        # 
        # >  When you create a cloud-native multi-replica cluster instance that is deployed across multiple zones, you must specify both SlaveReplicaCount and SecondaryZoneId.
        self.slave_replica_count = slave_replica_count
        # The source of the operation. This parameter is used only for internal maintenance. You do not need to specify this parameter.
        self.source_biz = source_biz
        # The storage capacity of the ESSD/SSD-based instance. The valid values vary based on the instance type. For more information, see [ESSD/SSD-based instances](https://help.aliyun.com/document_detail/2527111.html).
        # 
        # >  This parameter is required only when you set the **InstanceType** parameter to **tair_essd** to create an ESSD-based instance. If you create a Tair **SSD**-based instance, the Storage parameter is automatically specified based on predefined specifications. You do not need to specify this parameter.
        self.storage = storage
        # The storage type. Valid values: **essd_pl1**, **essd_pl2**, and **essd_pl3**.
        # 
        # >  This parameter is required only when you set the **InstanceType** parameter to **tair_essd** to create an ESSD-based instance.
        self.storage_type = storage_type

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

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.force_trans is not None:
            result['ForceTrans'] = self.force_trans

        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_count is not None:
            result['ReplicaCount'] = self.replica_count

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.slave_read_only_count is not None:
            result['SlaveReadOnlyCount'] = self.slave_read_only_count

        if self.slave_replica_count is not None:
            result['SlaveReplicaCount'] = self.slave_replica_count

        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

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

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ForceTrans') is not None:
            self.force_trans = m.get('ForceTrans')

        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaCount') is not None:
            self.replica_count = m.get('ReplicaCount')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('SlaveReadOnlyCount') is not None:
            self.slave_read_only_count = m.get('SlaveReadOnlyCount')

        if m.get('SlaveReplicaCount') is not None:
            self.slave_replica_count = m.get('SlaveReplicaCount')

        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

