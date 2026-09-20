# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServerlessClusterResponseBody(DaraModel):
    def __init__(
        self,
        auto_renew: str = None,
        cluster_type: str = None,
        create_time: str = None,
        cu_size: str = None,
        disk_size: str = None,
        expire_time: str = None,
        ha_type: str = None,
        has_user: str = None,
        inner_endpoint: str = None,
        instance_id: str = None,
        instance_name: str = None,
        is_deletion_protection: str = None,
        lock_mode: str = None,
        main_version: str = None,
        outer_endpoint: str = None,
        pay_type: str = None,
        region_id: str = None,
        request_id: str = None,
        reserver_max_qps_num: str = None,
        reserver_min_qps_num: str = None,
        resource_group_id: str = None,
        status: str = None,
        update_status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled. Valid values:
        # - **true**: Auto-renewal is enabled.
        # - **false**: Auto-renewal is not enabled.
        self.auto_renew = auto_renew
        # The cluster type. Valid values:
        # - **Cluster**: Cluster Edition.
        # - **Single**: single-node.
        self.cluster_type = cluster_type
        # The time when the cluster was created.
        self.create_time = create_time
        # The compute unit (CU) size.
        self.cu_size = cu_size
        # The disk size of the node. Unit: GB.
        self.disk_size = disk_size
        # The expiration time.
        self.expire_time = expire_time
        # Indicates whether high availability (HA) is enabled. Valid values:
        # - **true**: HA is enabled.
        # - **false**: HA is not enabled.
        self.ha_type = ha_type
        # Indicates whether the cluster has users. Valid values:
        # - **true**: The cluster has users.
        # - **false**: The cluster does not have users.
        self.has_user = has_user
        # The internal endpoint.
        self.inner_endpoint = inner_endpoint
        # The cluster ID.
        self.instance_id = instance_id
        # The cluster name.
        self.instance_name = instance_name
        # Indicates whether deletion protection is enabled.
        self.is_deletion_protection = is_deletion_protection
        # The lock type of the cluster.
        # > This parameter does not return a value.
        self.lock_mode = lock_mode
        # The major version.
        self.main_version = main_version
        # The public endpoint.
        self.outer_endpoint = outer_endpoint
        # The billing method. Valid values:
        # - **Prepaid**: subscription.
        # - **Postpaid**: pay-as-you-go.
        self.pay_type = pay_type
        # The region ID of the instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The maximum reserved QPS.
        self.reserver_max_qps_num = reserver_max_qps_num
        # The minimum reserved QPS.
        self.reserver_min_qps_num = reserver_min_qps_num
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The current status. Valid values:
        # - **CREATING**: being created.
        # - **ACTIVATION**: running.
        # - **DELETING**: being deleted.
        # - **RESTARTING**: being restarted.
        self.status = status
        # The minor version upgrade status. Valid values:
        # - **YES**: An upgrade is available.
        # - **NO**: No upgrade is available.
        # - **PENDING**: An upgrade is in progress.
        self.update_status = update_status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) to which the instance belongs.
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cu_size is not None:
            result['CuSize'] = self.cu_size

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.ha_type is not None:
            result['HaType'] = self.ha_type

        if self.has_user is not None:
            result['HasUser'] = self.has_user

        if self.inner_endpoint is not None:
            result['InnerEndpoint'] = self.inner_endpoint

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.main_version is not None:
            result['MainVersion'] = self.main_version

        if self.outer_endpoint is not None:
            result['OuterEndpoint'] = self.outer_endpoint

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reserver_max_qps_num is not None:
            result['ReserverMaxQpsNum'] = self.reserver_max_qps_num

        if self.reserver_min_qps_num is not None:
            result['ReserverMinQpsNum'] = self.reserver_min_qps_num

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_status is not None:
            result['UpdateStatus'] = self.update_status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CuSize') is not None:
            self.cu_size = m.get('CuSize')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HaType') is not None:
            self.ha_type = m.get('HaType')

        if m.get('HasUser') is not None:
            self.has_user = m.get('HasUser')

        if m.get('InnerEndpoint') is not None:
            self.inner_endpoint = m.get('InnerEndpoint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MainVersion') is not None:
            self.main_version = m.get('MainVersion')

        if m.get('OuterEndpoint') is not None:
            self.outer_endpoint = m.get('OuterEndpoint')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReserverMaxQpsNum') is not None:
            self.reserver_max_qps_num = m.get('ReserverMaxQpsNum')

        if m.get('ReserverMinQpsNum') is not None:
            self.reserver_min_qps_num = m.get('ReserverMinQpsNum')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateStatus') is not None:
            self.update_status = m.get('UpdateStatus')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

