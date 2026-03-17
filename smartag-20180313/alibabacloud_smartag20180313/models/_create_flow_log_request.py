# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFlowLogRequest(DaraModel):
    def __init__(
        self,
        active_aging: int = None,
        description: str = None,
        inactive_aging: int = None,
        logstore_name: str = None,
        name: str = None,
        netflow_server_ip: str = None,
        netflow_server_port: int = None,
        netflow_version: str = None,
        output_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        project_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sls_region_id: str = None,
    ):
        # The output interval under active connections. Valid values: **60 to 6000**. Unit: seconds. Default value: **300**.
        self.active_aging = active_aging
        # The description of the flow log.
        self.description = description
        # The output interval under inactive connections. Valid values: **10 to 600**. Unit: seconds. Default value: **15**.
        self.inactive_aging = inactive_aging
        # The Logstore in Log Service.
        # 
        # If OutputType is set to **sls** or **all**, this parameter is required.
        self.logstore_name = logstore_name
        # The name of the flow log.
        self.name = name
        # The IP address of the NetFlow collector where the flow log is stored.
        # 
        # If OutputType is set to **netflow** or **all**, this parameter is required.
        self.netflow_server_ip = netflow_server_ip
        # The port number of the NetFlow collector where the flow log is stored. Default value: **9995**.
        # 
        # If OutputType is set to **netflow** or **all**, this parameter is required.
        self.netflow_server_port = netflow_server_port
        # The version of the NetFlow collector where the flow log is stored. Valid values: **V5**, **V9**, and **V10**. Default value: **V9**.
        # 
        # If OutputType is set to **netflow** or **all**, this parameter is required.
        self.netflow_version = netflow_version
        # The type of the flow log. Valid values:
        # 
        # *   **sls**: The flow log is stored in Log Service.
        # *   **netflow**: The flow log is stored on a NetFlow collector.
        # *   **all**: The flow log is stored both in Log Service and on a NetFlow collector.
        self.output_type = output_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The project in Log Service.
        # 
        # If OutputType is set to **sls** or **all**, this parameter is required.
        self.project_name = project_name
        # The ID of the region to which the flow log belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the region where Log Service is deployed.
        # 
        # If OutputType is set to **sls** or **all**, this parameter is required.
        self.sls_region_id = sls_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_aging is not None:
            result['ActiveAging'] = self.active_aging

        if self.description is not None:
            result['Description'] = self.description

        if self.inactive_aging is not None:
            result['InactiveAging'] = self.inactive_aging

        if self.logstore_name is not None:
            result['LogstoreName'] = self.logstore_name

        if self.name is not None:
            result['Name'] = self.name

        if self.netflow_server_ip is not None:
            result['NetflowServerIp'] = self.netflow_server_ip

        if self.netflow_server_port is not None:
            result['NetflowServerPort'] = self.netflow_server_port

        if self.netflow_version is not None:
            result['NetflowVersion'] = self.netflow_version

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAging') is not None:
            self.active_aging = m.get('ActiveAging')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InactiveAging') is not None:
            self.inactive_aging = m.get('InactiveAging')

        if m.get('LogstoreName') is not None:
            self.logstore_name = m.get('LogstoreName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetflowServerIp') is not None:
            self.netflow_server_ip = m.get('NetflowServerIp')

        if m.get('NetflowServerPort') is not None:
            self.netflow_server_port = m.get('NetflowServerPort')

        if m.get('NetflowVersion') is not None:
            self.netflow_version = m.get('NetflowVersion')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        return self

