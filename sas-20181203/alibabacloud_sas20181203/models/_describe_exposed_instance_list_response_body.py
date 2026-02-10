# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeExposedInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        exposed_instances: List[main_models.DescribeExposedInstanceListResponseBodyExposedInstances] = None,
        page_info: main_models.DescribeExposedInstanceListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The details of the exposures.
        self.exposed_instances = exposed_instances
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.exposed_instances:
            for v1 in self.exposed_instances:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExposedInstances'] = []
        if self.exposed_instances is not None:
            for k1 in self.exposed_instances:
                result['ExposedInstances'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exposed_instances = []
        if m.get('ExposedInstances') is not None:
            for k1 in m.get('ExposedInstances'):
                temp_model = main_models.DescribeExposedInstanceListResponseBodyExposedInstances()
                self.exposed_instances.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeExposedInstanceListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeExposedInstanceListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeExposedInstanceListResponseBodyExposedInstances(DaraModel):
    def __init__(
        self,
        asap_vul_count: int = None,
        asset_type: int = None,
        cloud_asset_info: str = None,
        cspm_alarm_count: int = None,
        exploit_health_count: int = None,
        exposure_component: str = None,
        exposure_component_list: List[main_models.DescribeExposedInstanceListResponseBodyExposedInstancesExposureComponentList] = None,
        exposure_ip: str = None,
        exposure_port: str = None,
        exposure_type: str = None,
        exposure_type_id: str = None,
        group_id: int = None,
        group_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        later_vul_count: int = None,
        nntf_vul_count: int = None,
        region_id: str = None,
        total_vul_count: int = None,
        uuid: str = None,
    ):
        # The number of high-severity vulnerabilities that are exposed on the Internet and can be exploited by attackers.
        self.asap_vul_count = asap_vul_count
        # The type of the asset. Valid values:
        # 
        # *   **0**: an ECS instance.
        # *   **1**: a SLB instance.
        # *   **2**: a NAT gateway.
        # *   **3**: an ApsaraDB RDS instance.
        # *   **4**: an ApsaraDB for MongoDB instance.
        # *   **5**: an ApsaraDB for Redis instance.
        # *   **6**: a container image.
        # *   **7**: a container.
        self.asset_type = asset_type
        # The JSON string that specifies the information about a database asset, which contains the following fields.
        # 
        # *   assetSubType: the asset subtype.
        # *   assetSubTypeName: the name of the asset subtype.
        # *   assetType: the type of the asset.
        # *   assetTypeName: the name of the asset type.
        # *   vendor: the service provider of the asset.
        self.cloud_asset_info = cloud_asset_info
        # The number of CSPM risks.
        self.cspm_alarm_count = cspm_alarm_count
        # The number of weak password risks.
        self.exploit_health_count = exploit_health_count
        # The server component that is exposed on the Internet.
        self.exposure_component = exposure_component
        # Expose component information list.
        self.exposure_component_list = exposure_component_list
        # The public IP address that is exposed on the Internet.
        self.exposure_ip = exposure_ip
        # The port that is exposed on the Internet.
        self.exposure_port = exposure_port
        # The resource from which the asset is exposed. Valid values:
        # 
        # *   **INTERNET_IP**: the public IP address of an ECS instance.
        # *   **SLB**: the public IP address of a Server Load Balancer (SLB) instance.
        # *   **EIP**: an elastic IP address (EIP).
        # *   **DNAT**: the NAT gateway that connects to the Internet by using the Destination Network Address Translation (DNAT) feature.
        # *   **DB_CONNECTION**: the public endpoint of a database.
        self.exposure_type = exposure_type
        # The ID of the instance to which the resource belongs. The valid values of this parameter vary based on the value of the ExposureType parameter.
        # 
        # *   If the value of the ExposureType parameter is **INTERNET_IP**, this parameter is empty.
        # *   If the value of the ExposureType parameter is **SLB**, the value of this parameter is the ID of the SLB instance.
        # *   If the value of the ExposureType parameter is **EIP**, the value of this parameter is the ID of the EIP.
        # *   If the value of the ExposureType parameter is **DNAT**, the value of this parameter is the ID of the NAT gateway.
        # *   If the value of the ExposureType parameter is **DB_CONNECTION**, the value of this parameter is the ID of the database.
        self.exposure_type_id = exposure_type_id
        # The ID of the server group.
        self.group_id = group_id
        # The name of the server group.
        self.group_name = group_name
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The name of the asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The number of medium-severity vulnerabilities that are exposed on the Internet and can be exploited by attackers.
        self.later_vul_count = later_vul_count
        # The number of low-severity vulnerabilities that are exposed on the Internet and can be exploited by attackers.
        self.nntf_vul_count = nntf_vul_count
        # The ID of the region in which the asset resides.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The total number of vulnerabilities that are exposed on the Internet and can be exploited by attackers.
        self.total_vul_count = total_vul_count
        # The UUID of the server or the instance ID of the cloud service.
        self.uuid = uuid

    def validate(self):
        if self.exposure_component_list:
            for v1 in self.exposure_component_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asap_vul_count is not None:
            result['AsapVulCount'] = self.asap_vul_count

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.cloud_asset_info is not None:
            result['CloudAssetInfo'] = self.cloud_asset_info

        if self.cspm_alarm_count is not None:
            result['CspmAlarmCount'] = self.cspm_alarm_count

        if self.exploit_health_count is not None:
            result['ExploitHealthCount'] = self.exploit_health_count

        if self.exposure_component is not None:
            result['ExposureComponent'] = self.exposure_component

        result['ExposureComponentList'] = []
        if self.exposure_component_list is not None:
            for k1 in self.exposure_component_list:
                result['ExposureComponentList'].append(k1.to_map() if k1 else None)

        if self.exposure_ip is not None:
            result['ExposureIp'] = self.exposure_ip

        if self.exposure_port is not None:
            result['ExposurePort'] = self.exposure_port

        if self.exposure_type is not None:
            result['ExposureType'] = self.exposure_type

        if self.exposure_type_id is not None:
            result['ExposureTypeId'] = self.exposure_type_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.later_vul_count is not None:
            result['LaterVulCount'] = self.later_vul_count

        if self.nntf_vul_count is not None:
            result['NntfVulCount'] = self.nntf_vul_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.total_vul_count is not None:
            result['TotalVulCount'] = self.total_vul_count

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsapVulCount') is not None:
            self.asap_vul_count = m.get('AsapVulCount')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('CloudAssetInfo') is not None:
            self.cloud_asset_info = m.get('CloudAssetInfo')

        if m.get('CspmAlarmCount') is not None:
            self.cspm_alarm_count = m.get('CspmAlarmCount')

        if m.get('ExploitHealthCount') is not None:
            self.exploit_health_count = m.get('ExploitHealthCount')

        if m.get('ExposureComponent') is not None:
            self.exposure_component = m.get('ExposureComponent')

        self.exposure_component_list = []
        if m.get('ExposureComponentList') is not None:
            for k1 in m.get('ExposureComponentList'):
                temp_model = main_models.DescribeExposedInstanceListResponseBodyExposedInstancesExposureComponentList()
                self.exposure_component_list.append(temp_model.from_map(k1))

        if m.get('ExposureIp') is not None:
            self.exposure_ip = m.get('ExposureIp')

        if m.get('ExposurePort') is not None:
            self.exposure_port = m.get('ExposurePort')

        if m.get('ExposureType') is not None:
            self.exposure_type = m.get('ExposureType')

        if m.get('ExposureTypeId') is not None:
            self.exposure_type_id = m.get('ExposureTypeId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LaterVulCount') is not None:
            self.later_vul_count = m.get('LaterVulCount')

        if m.get('NntfVulCount') is not None:
            self.nntf_vul_count = m.get('NntfVulCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TotalVulCount') is not None:
            self.total_vul_count = m.get('TotalVulCount')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeExposedInstanceListResponseBodyExposedInstancesExposureComponentList(DaraModel):
    def __init__(
        self,
        component_biz_type: str = None,
        component_name: str = None,
        component_version: str = None,
        listen_port: str = None,
    ):
        # Expose component type.
        self.component_biz_type = component_biz_type
        # Expose components.
        self.component_name = component_name
        # Expose component version.
        self.component_version = component_version
        # Exposed port.
        self.listen_port = listen_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_biz_type is not None:
            result['ComponentBizType'] = self.component_biz_type

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.component_version is not None:
            result['ComponentVersion'] = self.component_version

        if self.listen_port is not None:
            result['ListenPort'] = self.listen_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentBizType') is not None:
            self.component_biz_type = m.get('ComponentBizType')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('ComponentVersion') is not None:
            self.component_version = m.get('ComponentVersion')

        if m.get('ListenPort') is not None:
            self.listen_port = m.get('ListenPort')

        return self

