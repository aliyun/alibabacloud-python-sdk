# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWarningMachinesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        warning_machines: List[main_models.DescribeWarningMachinesResponseBodyWarningMachines] = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **10**.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the servers.
        self.warning_machines = warning_machines

    def validate(self):
        if self.warning_machines:
            for v1 in self.warning_machines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WarningMachines'] = []
        if self.warning_machines is not None:
            for k1 in self.warning_machines:
                result['WarningMachines'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.warning_machines = []
        if m.get('WarningMachines') is not None:
            for k1 in m.get('WarningMachines'):
                temp_model = main_models.DescribeWarningMachinesResponseBodyWarningMachines()
                self.warning_machines.append(temp_model.from_map(k1))

        return self

class DescribeWarningMachinesResponseBodyWarningMachines(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        auth_version: int = None,
        bind: bool = None,
        container_id: str = None,
        container_name: str = None,
        high_warning_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        low_warning_count: int = None,
        medium_warning_count: int = None,
        online: bool = None,
        pass_count: int = None,
        port_open: bool = None,
        region_id: str = None,
        status: int = None,
        uuid: str = None,
    ):
        # The type of cloud product assets.
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the types of cloud product assets.
        self.asset_type = asset_type
        # The edition of Security Center that is authorized to protect the asset. Valid values:
        # 
        # *   **1**: Basic edition
        # *   **6**: Anti-virus edition
        # *   **5**: Advanced edition
        # *   **3**: Enterprise edition
        # *   **7**: Ultimate edition
        # *   **10**: Value-added Plan edition
        self.auth_version = auth_version
        # Indicates whether Security Center is authorized to protect the asset. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.bind = bind
        # The container ID.
        self.container_id = container_id
        # The name of the container.
        self.container_name = container_name
        # The number of **high-risk** items on the server.
        self.high_warning_count = high_warning_count
        # The server ID.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The number of **low-risk** items on the server.
        self.low_warning_count = low_warning_count
        # The number of **medium-risk** items on the server.
        self.medium_warning_count = medium_warning_count
        # Indicates whether the agent is online. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.online = online
        # The number of the check items that passed the baseline check on the server.
        self.pass_count = pass_count
        # Indicates whether a port on the server is accessible over the Internet. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.port_open = port_open
        # The ID of the region in which the server is deployed.
        self.region_id = region_id
        # The verification status of the risk item after the risk item is fixed. Valid values:
        # 
        # *   **1**: complete
        # *   **2**: verifying
        self.status = status
        # The UUID of the server on which the baseline check is performed.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.bind is not None:
            result['Bind'] = self.bind

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.high_warning_count is not None:
            result['HighWarningCount'] = self.high_warning_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.low_warning_count is not None:
            result['LowWarningCount'] = self.low_warning_count

        if self.medium_warning_count is not None:
            result['MediumWarningCount'] = self.medium_warning_count

        if self.online is not None:
            result['Online'] = self.online

        if self.pass_count is not None:
            result['PassCount'] = self.pass_count

        if self.port_open is not None:
            result['PortOpen'] = self.port_open

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('HighWarningCount') is not None:
            self.high_warning_count = m.get('HighWarningCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LowWarningCount') is not None:
            self.low_warning_count = m.get('LowWarningCount')

        if m.get('MediumWarningCount') is not None:
            self.medium_warning_count = m.get('MediumWarningCount')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')

        if m.get('PortOpen') is not None:
            self.port_open = m.get('PortOpen')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

