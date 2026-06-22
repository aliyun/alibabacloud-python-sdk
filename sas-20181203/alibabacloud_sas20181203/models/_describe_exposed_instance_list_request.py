# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExposedInstanceListRequest(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        cspm_status: bool = None,
        current_page: int = None,
        exposure_component: str = None,
        exposure_component_biz_type: str = None,
        exposure_ip: str = None,
        exposure_port: str = None,
        group_id: int = None,
        health_status: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        page_size: int = None,
        resource_directory_account_id: int = None,
        vul_status: bool = None,
    ):
        # The asset type. Valid values:
        # 
        # - **0**: ECS
        # 
        # - **3**: RDS
        # 
        # - **4**: MONGODB
        # 
        # - **5**: RDS-Redis.
        self.asset_type = asset_type
        # Specifies whether the asset that you want to query has Cloud Security Posture Management (CSPM) risks. Valid values:
        # 
        # - **true**: The asset has CSPM risks.
        # - **false**: The asset does not have CSPM risks.
        self.cspm_status = cspm_status
        # The page number of the current page in a paged query.
        self.current_page = current_page
        # The name of the system component exposed on the Internet that you want to query.
        self.exposure_component = exposure_component
        # The type of the exposed component.
        self.exposure_component_biz_type = exposure_component_biz_type
        # The public IP address of the server type or the public network connection address of the database type that you want to query.
        self.exposure_ip = exposure_ip
        # The exposed port that you want to query.
        self.exposure_port = exposure_port
        # The ID of the server group that you want to query.
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query server group IDs.
        self.group_id = group_id
        # Specifies whether the asset that you want to query has baseline weak password risks. Valid values:
        # 
        # - **true**: The asset has baseline weak password risks.
        # - **false**: The asset does not have baseline weak password risks.
        self.health_status = health_status
        # The instance ID of the asset that you want to query.
        self.instance_id = instance_id
        # The name of the asset that you want to query.
        self.instance_name = instance_name
        # The number of entries per page in a paged query. Default value: 20. If you leave this parameter empty, 20 entries are returned per page.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # > You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether the asset that you want to query has vulnerabilities. Valid values:
        # - **true**: The asset has vulnerabilities.
        # - **false**: The asset does not have vulnerabilities.
        self.vul_status = vul_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.cspm_status is not None:
            result['CspmStatus'] = self.cspm_status

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.exposure_component is not None:
            result['ExposureComponent'] = self.exposure_component

        if self.exposure_component_biz_type is not None:
            result['ExposureComponentBizType'] = self.exposure_component_biz_type

        if self.exposure_ip is not None:
            result['ExposureIp'] = self.exposure_ip

        if self.exposure_port is not None:
            result['ExposurePort'] = self.exposure_port

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.vul_status is not None:
            result['VulStatus'] = self.vul_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('CspmStatus') is not None:
            self.cspm_status = m.get('CspmStatus')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ExposureComponent') is not None:
            self.exposure_component = m.get('ExposureComponent')

        if m.get('ExposureComponentBizType') is not None:
            self.exposure_component_biz_type = m.get('ExposureComponentBizType')

        if m.get('ExposureIp') is not None:
            self.exposure_ip = m.get('ExposureIp')

        if m.get('ExposurePort') is not None:
            self.exposure_port = m.get('ExposurePort')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('VulStatus') is not None:
            self.vul_status = m.get('VulStatus')

        return self

