# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSupabaseProjectResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dashboard_password: str = None,
        dashboard_user_name: str = None,
        disk_performance_level: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_version: str = None,
        pay_type: str = None,
        private_connect_url: str = None,
        project_id: str = None,
        project_name: str = None,
        project_spec: str = None,
        public_connect_url: str = None,
        region_id: str = None,
        request_id: str = None,
        security_ip_list: str = None,
        status: str = None,
        storage_size: int = None,
        storage_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The Supabase Dashboard password (Not Used)
        self.dashboard_password = dashboard_password
        # The Supabase Dashboard user name (Not Used)
        self.dashboard_user_name = dashboard_user_name
        # The Enterprise SSD (ESSD) performance level of the cluster. Valid values:
        # 
        # *   PL0
        # *   PL1
        self.disk_performance_level = disk_performance_level
        # The type of the database engine.
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        self.instance_version = instance_version
        self.pay_type = pay_type
        # The private (VPC) connection URL for the Supabase Dashboard.
        self.private_connect_url = private_connect_url
        # The Supabase instance ID.
        self.project_id = project_id
        # The name of the Supabase project.
        self.project_name = project_name
        # The performance level of the Supabase instance.
        self.project_spec = project_spec
        # The public connection URL for the Supabase Dashboard.
        self.public_connect_url = public_connect_url
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        self.region_id = region_id
        # The unique ID of the request.
        self.request_id = request_id
        # A comma-separated list of IP addresses and CIDR blocks allowed to connect.
        self.security_ip_list = security_ip_list
        # The status of the Supabase instance.
        self.status = status
        # The storage capacity of the instance. Unit: GB.
        self.storage_size = storage_size
        self.storage_type = storage_type
        # The vSwitch ID of the instance. This parameter must be specified when VPCId is specified.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # 
        # > 
        # 
        # *   You can call the [DescribeRdsVpcs](https://help.aliyun.com/document_detail/208327.html) operation to query the available VPC IDs.
        # 
        # *   This parameter is required.
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list and zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password

        if self.dashboard_user_name is not None:
            result['DashboardUserName'] = self.dashboard_user_name

        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_version is not None:
            result['InstanceVersion'] = self.instance_version

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.private_connect_url is not None:
            result['PrivateConnectUrl'] = self.private_connect_url

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.project_spec is not None:
            result['ProjectSpec'] = self.project_spec

        if self.public_connect_url is not None:
            result['PublicConnectUrl'] = self.public_connect_url

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')

        if m.get('DashboardUserName') is not None:
            self.dashboard_user_name = m.get('DashboardUserName')

        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceVersion') is not None:
            self.instance_version = m.get('InstanceVersion')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PrivateConnectUrl') is not None:
            self.private_connect_url = m.get('PrivateConnectUrl')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProjectSpec') is not None:
            self.project_spec = m.get('ProjectSpec')

        if m.get('PublicConnectUrl') is not None:
            self.public_connect_url = m.get('PublicConnectUrl')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

