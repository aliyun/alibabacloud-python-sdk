# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class InstanceDetail(DaraModel):
    def __init__(
        self,
        auto_backup: bool = None,
        components: List[main_models.InstanceDetailComponents] = None,
        configuration: str = None,
        create_time: str = None,
        db_version: str = None,
        encrypted: bool = None,
        expire_time: str = None,
        ha: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        kms_key_id: str = None,
        multi_zone_mode: str = None,
        order_id: str = None,
        payment_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        running_time: int = None,
        security_group_ids: List[str] = None,
        status: str = None,
        tags: List[main_models.InstanceDetailTags] = None,
        v_switch_ids: List[main_models.InstanceDetailVSwitchIds] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The automatic backup configuration.
        self.auto_backup = auto_backup
        # The component information.
        self.components = components
        # The configuration.
        self.configuration = configuration
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        # The instance version.
        self.db_version = db_version
        # Indicates whether data encryption is enabled.
        self.encrypted = encrypted
        # The expiration time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.expire_time = expire_time
        # Indicates whether high availability is enabled.
        self.ha = ha
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # kms key Id。
        self.kms_key_id = kms_key_id
        # The multi-zone deployment mode.
        self.multi_zone_mode = multi_zone_mode
        # The order ID.
        self.order_id = order_id
        # The billing method. Valid values: PayAsYouGo: pay-as-you-go billing method. Subscription: subscription.
        self.payment_type = payment_type
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The running time.
        self.running_time = running_time
        # The security group IDs.
        self.security_group_ids = security_group_ids
        # The instance status. Valid values:
        # 
        # - creating: Being created.
        # - running: Running.
        # - updating: Being upgraded. This includes specification changes, configuration changes, and public network access changes.
        # - disable: Unavailable. The cluster has expired and requires renewal to reactivate.
        # - deleting: Being deleted.
        # - deleted: Deleted.
        self.status = status
        # The tags.
        self.tags = tags
        # The vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switch_ids:
            for v1 in self.v_switch_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_backup is not None:
            result['autoBackup'] = self.auto_backup

        result['components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['components'].append(k1.to_map() if k1 else None)

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.db_version is not None:
            result['dbVersion'] = self.db_version

        if self.encrypted is not None:
            result['encrypted'] = self.encrypted

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.ha is not None:
            result['ha'] = self.ha

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.kms_key_id is not None:
            result['kmsKeyId'] = self.kms_key_id

        if self.multi_zone_mode is not None:
            result['multiZoneMode'] = self.multi_zone_mode

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.running_time is not None:
            result['runningTime'] = self.running_time

        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        result['vSwitchIds'] = []
        if self.v_switch_ids is not None:
            for k1 in self.v_switch_ids:
                result['vSwitchIds'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBackup') is not None:
            self.auto_backup = m.get('autoBackup')

        self.components = []
        if m.get('components') is not None:
            for k1 in m.get('components'):
                temp_model = main_models.InstanceDetailComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dbVersion') is not None:
            self.db_version = m.get('dbVersion')

        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('ha') is not None:
            self.ha = m.get('ha')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('kmsKeyId') is not None:
            self.kms_key_id = m.get('kmsKeyId')

        if m.get('multiZoneMode') is not None:
            self.multi_zone_mode = m.get('multiZoneMode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('runningTime') is not None:
            self.running_time = m.get('runningTime')

        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.InstanceDetailTags()
                self.tags.append(temp_model.from_map(k1))

        self.v_switch_ids = []
        if m.get('vSwitchIds') is not None:
            for k1 in m.get('vSwitchIds'):
                temp_model = main_models.InstanceDetailVSwitchIds()
                self.v_switch_ids.append(temp_model.from_map(k1))

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class InstanceDetailVSwitchIds(DaraModel):
    def __init__(
        self,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        # The vSwitch IDs.
        self.vsw_id = vsw_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsw_id is not None:
            result['vswId'] = self.vsw_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vswId') is not None:
            self.vsw_id = m.get('vswId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class InstanceDetailTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class InstanceDetailComponents(DaraModel):
    def __init__(
        self,
        cu_num: int = None,
        cu_type: str = None,
        data_disk: main_models.InstanceDetailComponentsDataDisk = None,
        disk_size_type: str = None,
        pay_type: str = None,
        pods_list: List[main_models.InstanceDetailComponentsPodsList] = None,
        replica: int = None,
        type: str = None,
    ):
        # The number of CUs.
        self.cu_num = cu_num
        # The CU type.
        self.cu_type = cu_type
        self.data_disk = data_disk
        # The disk size type for the Query Node. Set this parameter to Large for storage-optimized configurations, and to Normal for other configurations.
        self.disk_size_type = disk_size_type
        self.pay_type = pay_type
        self.pods_list = pods_list
        # The number of replicas.
        self.replica = replica
        # The component type.
        self.type = type

    def validate(self):
        if self.data_disk:
            self.data_disk.validate()
        if self.pods_list:
            for v1 in self.pods_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_num is not None:
            result['cuNum'] = self.cu_num

        if self.cu_type is not None:
            result['cuType'] = self.cu_type

        if self.data_disk is not None:
            result['dataDisk'] = self.data_disk.to_map()

        if self.disk_size_type is not None:
            result['diskSizeType'] = self.disk_size_type

        if self.pay_type is not None:
            result['payType'] = self.pay_type

        result['podsList'] = []
        if self.pods_list is not None:
            for k1 in self.pods_list:
                result['podsList'].append(k1.to_map() if k1 else None)

        if self.replica is not None:
            result['replica'] = self.replica

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuNum') is not None:
            self.cu_num = m.get('cuNum')

        if m.get('cuType') is not None:
            self.cu_type = m.get('cuType')

        if m.get('dataDisk') is not None:
            temp_model = main_models.InstanceDetailComponentsDataDisk()
            self.data_disk = temp_model.from_map(m.get('dataDisk'))

        if m.get('diskSizeType') is not None:
            self.disk_size_type = m.get('diskSizeType')

        if m.get('payType') is not None:
            self.pay_type = m.get('payType')

        self.pods_list = []
        if m.get('podsList') is not None:
            for k1 in m.get('podsList'):
                temp_model = main_models.InstanceDetailComponentsPodsList()
                self.pods_list.append(temp_model.from_map(k1))

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class InstanceDetailComponentsPodsList(DaraModel):
    def __init__(
        self,
        pod_id: str = None,
        pod_name: str = None,
    ):
        self.pod_id = pod_id
        self.pod_name = pod_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pod_id is not None:
            result['podId'] = self.pod_id

        if self.pod_name is not None:
            result['podName'] = self.pod_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('podId') is not None:
            self.pod_id = m.get('podId')

        if m.get('podName') is not None:
            self.pod_name = m.get('podName')

        return self

class InstanceDetailComponentsDataDisk(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        performance_level: str = None,
        size: int = None,
        storage_class: str = None,
    ):
        self.enabled = enabled
        self.performance_level = performance_level
        self.size = size
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level

        if self.size is not None:
            result['size'] = self.size

        if self.storage_class is not None:
            result['storageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('storageClass') is not None:
            self.storage_class = m.get('storageClass')

        return self

