# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListSupabaseProjectsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListSupabaseProjectsResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # A list of objects, where each object represents a Supabase instance.
        self.items = items
        # The maximum amount of data to read this time. Default value: 10.
        self.max_results = max_results
        # The pagination token to use in the next request to get the next page. If this field is empty, there are no more results.
        self.next_token = next_token
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The unique ID of the request.
        self.request_id = request_id
        # The total number of log entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListSupabaseProjectsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListSupabaseProjectsResponseBodyItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dashboard_password: str = None,
        dashboard_user_name: str = None,
        disk_performance_level: str = None,
        engine: str = None,
        engine_version: str = None,
        pay_type: str = None,
        private_connect_url: str = None,
        project_id: str = None,
        project_name: str = None,
        project_spec: str = None,
        public_connect_url: str = None,
        region_id: str = None,
        security_iplist: str = None,
        status: str = None,
        storage_size: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # Supabase Dashboard password (not used).
        self.dashboard_password = dashboard_password
        # Supabase Dashboard user name (not used).
        self.dashboard_user_name = dashboard_user_name
        # The ESSD performance level.
        self.disk_performance_level = disk_performance_level
        # The database engine type.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription.
        # *   **Free**: Free.
        self.pay_type = pay_type
        # The private (VPC) connection URL for the Supabase Dashboard.
        self.private_connect_url = private_connect_url
        # The Supabase project ID.
        self.project_id = project_id
        # The name of the Supabase project.
        self.project_name = project_name
        # The type of the Supabase instance.
        self.project_spec = project_spec
        # The public connection URL for the Supabase Dashboard.
        self.public_connect_url = public_connect_url
        # The region ID.
        self.region_id = region_id
        # A comma-separated list of IP addresses and CIDR blocks allowed to connect. Valid values:
        # 
        # *   0.0.0.0/0
        # *   10.23.12.24(IP)
        # *   10.23.12.24/24. This is a CIDR block. The value`/24`indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value in the range of`[1,32]`.
        self.security_iplist = security_iplist
        # The status of the Supabase instance.
        self.status = status
        # The storage capacity of the instance. Unit: GB.
        self.storage_size = storage_size
        # The vSwitch ID of the instance.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID.
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

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

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

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

