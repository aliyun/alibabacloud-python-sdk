# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        charge_type: str = None,
        edition_type: str = None,
        engine_version: str = None,
        expired: str = None,
        global_instance: bool = None,
        instance_class: str = None,
        instance_ids: str = None,
        instance_status: str = None,
        instance_type: str = None,
        network_type: str = None,
        node_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        private_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        search_key: str = None,
        security_token: str = None,
        tag: List[main_models.DescribeInstancesRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The architecture type. Valid values:
        # * **cluster**: cluster.
        # * **standard**: standard.
        # * **rwsplit**: read/write splitting.
        self.architecture_type = architecture_type
        # The billing method. Valid values:
        # * **PrePaid**: subscription.
        # * **PostPaid**: pay-as-you-go.
        self.charge_type = charge_type
        # The edition of the instance. Valid values:
        # * **Community**: ApsaraDB for Redis Community Edition.
        # * **Enterprise**: Tair Enhanced Edition.
        self.edition_type = edition_type
        # The Redis-compatible engine version of the instance. Valid values: **2.8**, **4.0**, **5.0**, **6.0**, and **7.0**.
        self.engine_version = engine_version
        # The expiration status of the instance. Valid values:
        # 
        # * **true**: expired.
        # * **false**: not expired.
        self.expired = expired
        # Specifies whether to filter child instances of distributed instances from the returned instance list. Valid values:
        # * **true**: returns only child instance information.
        # * **false**: does not return child instance information.
        self.global_instance = global_instance
        # The instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/107984.html).
        self.instance_class = instance_class
        # The IDs of the instances to query.
        # > To specify multiple instance IDs, separate them with commas (,). A maximum of 30 instance IDs can be specified in a single request.
        self.instance_ids = instance_ids
        # The status of the instance. Valid values:
        # * **Normal**: normal.
        # * **Creating**: being created.
        # * **Changing**: being changed.
        # * **Inactive**: disabled.
        # * **Flushing**: being flushed.
        # * **Released**: released.
        # * **Transforming**: being transformed.
        # * **Migrating**: being migrated.
        # * **BackupRecovering**: being restored from a backup.
        # * **MinorVersionUpgrading**: minor version being upgraded.
        # * **NetworkModifying**: network type being changed.
        # * **SSLModifying**: SSL being changed.
        # * **MajorVersionUpgrading**: major version being upgraded. The instance can be accessed normally.
        # 
        # > For more information about instance statuses, see [Instance statuses and impacts](https://help.aliyun.com/document_detail/200740.html).
        self.instance_status = instance_status
        # The category of the instance. Valid values:
        # * **Tair**: Tair (Enhanced Edition)
        # * **Redis**: ApsaraDB for Redis Community Edition
        # * **Memcache**
        self.instance_type = instance_type
        # The network type of the instance. Valid values:
        # * **CLASSIC**: classic network.
        # * **VPC**: virtual private cloud (VPC).
        self.network_type = network_type
        # The node type. Valid values:
        # * **MASTER_SLAVE**: high availability (dual-replica)
        # * **STAND_ALONE**: single replica
        # * **double**: dual-replica
        # * **single**: single replica
        # > For cloud-native instances, select **MASTER_SLAVE** or **STAND_ALONE**. For classic instances, select **double** or **single**.
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the instance list. Pages start from **1**. Default value: **1**.
        self.page_number = page_number
        # The maximum number of entries per page. Maximum value: **50**. Default value: **30**.
        self.page_size = page_size
        # The private IP address of the VPC.
        self.private_ip = private_ip
        # The region ID of the instance.
        # 
        # > When calling this API, if the **Tag** parameter is specified, this parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # > You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) API or use the console to obtain the list of resource group IDs. For more information, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The keyword used for fuzzy search by instance name or instance ID.
        self.search_key = search_key
        self.security_token = security_token
        # The tags of the instance.
        self.tag = tag
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.edition_type is not None:
            result['EditionType'] = self.edition_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.global_instance is not None:
            result['GlobalInstance'] = self.global_instance

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EditionType') is not None:
            self.edition_type = m.get('EditionType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('GlobalInstance') is not None:
            self.global_instance = m.get('GlobalInstance')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The tag key and value together form a key-value pair.
        # > A maximum of 5 tag key-value pairs can be specified at a time.
        self.key = key
        # The value of the tag. The tag value and key together form a key-value pair.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

