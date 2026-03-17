# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSmartAccessGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        smart_access_gateways: main_models.DescribeSmartAccessGatewaysResponseBodySmartAccessGateways = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.smart_access_gateways = smart_access_gateways
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.smart_access_gateways:
            self.smart_access_gateways.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.smart_access_gateways is not None:
            result['SmartAccessGateways'] = self.smart_access_gateways.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmartAccessGateways') is not None:
            temp_model = main_models.DescribeSmartAccessGatewaysResponseBodySmartAccessGateways()
            self.smart_access_gateways = temp_model.from_map(m.get('SmartAccessGateways'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSmartAccessGatewaysResponseBodySmartAccessGateways(DaraModel):
    def __init__(
        self,
        smart_access_gateway: List[main_models.DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGateway] = None,
    ):
        self.smart_access_gateway = smart_access_gateway

    def validate(self):
        if self.smart_access_gateway:
            for v1 in self.smart_access_gateway:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SmartAccessGateway'] = []
        if self.smart_access_gateway is not None:
            for k1 in self.smart_access_gateway:
                result['SmartAccessGateway'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.smart_access_gateway = []
        if m.get('SmartAccessGateway') is not None:
            for k1 in m.get('SmartAccessGateway'):
                temp_model = main_models.DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGateway()
                self.smart_access_gateway.append(temp_model.from_map(k1))

        return self

class DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGateway(DaraModel):
    def __init__(
        self,
        accelerate_bandwidth: int = None,
        access_point_id: str = None,
        acl_ids: str = None,
        application_bandwidth_package_id: str = None,
        associated_ccn_id: str = None,
        associated_ccn_name: str = None,
        backup_software_version: str = None,
        backup_status: str = None,
        cidr_block: str = None,
        city: str = None,
        create_time: int = None,
        data_plan: int = None,
        description: str = None,
        dpi_monitor_status: str = None,
        dpi_status: str = None,
        enable_advanced_monitor: bool = None,
        enable_software_connection_audit: bool = None,
        end_time: int = None,
        enterprise_code: str = None,
        hardware_version: str = None,
        irids: str = None,
        idaas_application_id: str = None,
        idaas_id: str = None,
        ipsec_status: str = None,
        isp: str = None,
        links: main_models.DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGatewayLinks = None,
        max_bandwidth: str = None,
        name: str = None,
        position: str = None,
        qos_ids: str = None,
        reseller_instance_id: str = None,
        reseller_uid: str = None,
        resource_group_id: str = None,
        routing_strategy: str = None,
        security_lock_threshold: int = None,
        serial_number: str = None,
        smart_agid: str = None,
        smart_aguid: int = None,
        software_version: str = None,
        status: str = None,
        up_bandwidth_4g: int = None,
        up_bandwidth_wan: int = None,
        user_count: int = None,
        vpn_status: str = None,
    ):
        self.accelerate_bandwidth = accelerate_bandwidth
        self.access_point_id = access_point_id
        self.acl_ids = acl_ids
        self.application_bandwidth_package_id = application_bandwidth_package_id
        self.associated_ccn_id = associated_ccn_id
        self.associated_ccn_name = associated_ccn_name
        self.backup_software_version = backup_software_version
        self.backup_status = backup_status
        self.cidr_block = cidr_block
        self.city = city
        self.create_time = create_time
        self.data_plan = data_plan
        self.description = description
        self.dpi_monitor_status = dpi_monitor_status
        self.dpi_status = dpi_status
        self.enable_advanced_monitor = enable_advanced_monitor
        self.enable_software_connection_audit = enable_software_connection_audit
        self.end_time = end_time
        self.enterprise_code = enterprise_code
        self.hardware_version = hardware_version
        self.irids = irids
        self.idaas_application_id = idaas_application_id
        self.idaas_id = idaas_id
        self.ipsec_status = ipsec_status
        self.isp = isp
        self.links = links
        self.max_bandwidth = max_bandwidth
        self.name = name
        self.position = position
        self.qos_ids = qos_ids
        self.reseller_instance_id = reseller_instance_id
        self.reseller_uid = reseller_uid
        self.resource_group_id = resource_group_id
        self.routing_strategy = routing_strategy
        self.security_lock_threshold = security_lock_threshold
        self.serial_number = serial_number
        self.smart_agid = smart_agid
        self.smart_aguid = smart_aguid
        self.software_version = software_version
        self.status = status
        self.up_bandwidth_4g = up_bandwidth_4g
        self.up_bandwidth_wan = up_bandwidth_wan
        self.user_count = user_count
        self.vpn_status = vpn_status

    def validate(self):
        if self.links:
            self.links.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_bandwidth is not None:
            result['AccelerateBandwidth'] = self.accelerate_bandwidth

        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids

        if self.application_bandwidth_package_id is not None:
            result['ApplicationBandwidthPackageId'] = self.application_bandwidth_package_id

        if self.associated_ccn_id is not None:
            result['AssociatedCcnId'] = self.associated_ccn_id

        if self.associated_ccn_name is not None:
            result['AssociatedCcnName'] = self.associated_ccn_name

        if self.backup_software_version is not None:
            result['BackupSoftwareVersion'] = self.backup_software_version

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.city is not None:
            result['City'] = self.city

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_plan is not None:
            result['DataPlan'] = self.data_plan

        if self.description is not None:
            result['Description'] = self.description

        if self.dpi_monitor_status is not None:
            result['DpiMonitorStatus'] = self.dpi_monitor_status

        if self.dpi_status is not None:
            result['DpiStatus'] = self.dpi_status

        if self.enable_advanced_monitor is not None:
            result['EnableAdvancedMonitor'] = self.enable_advanced_monitor

        if self.enable_software_connection_audit is not None:
            result['EnableSoftwareConnectionAudit'] = self.enable_software_connection_audit

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.enterprise_code is not None:
            result['EnterpriseCode'] = self.enterprise_code

        if self.hardware_version is not None:
            result['HardwareVersion'] = self.hardware_version

        if self.irids is not None:
            result['IRIds'] = self.irids

        if self.idaas_application_id is not None:
            result['IdaasApplicationId'] = self.idaas_application_id

        if self.idaas_id is not None:
            result['IdaasId'] = self.idaas_id

        if self.ipsec_status is not None:
            result['IpsecStatus'] = self.ipsec_status

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.links is not None:
            result['Links'] = self.links.to_map()

        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth

        if self.name is not None:
            result['Name'] = self.name

        if self.position is not None:
            result['Position'] = self.position

        if self.qos_ids is not None:
            result['QosIds'] = self.qos_ids

        if self.reseller_instance_id is not None:
            result['ResellerInstanceId'] = self.reseller_instance_id

        if self.reseller_uid is not None:
            result['ResellerUid'] = self.reseller_uid

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy

        if self.security_lock_threshold is not None:
            result['SecurityLockThreshold'] = self.security_lock_threshold

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_aguid is not None:
            result['SmartAGUid'] = self.smart_aguid

        if self.software_version is not None:
            result['SoftwareVersion'] = self.software_version

        if self.status is not None:
            result['Status'] = self.status

        if self.up_bandwidth_4g is not None:
            result['UpBandwidth4G'] = self.up_bandwidth_4g

        if self.up_bandwidth_wan is not None:
            result['UpBandwidthWan'] = self.up_bandwidth_wan

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        if self.vpn_status is not None:
            result['VpnStatus'] = self.vpn_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateBandwidth') is not None:
            self.accelerate_bandwidth = m.get('AccelerateBandwidth')

        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')

        if m.get('ApplicationBandwidthPackageId') is not None:
            self.application_bandwidth_package_id = m.get('ApplicationBandwidthPackageId')

        if m.get('AssociatedCcnId') is not None:
            self.associated_ccn_id = m.get('AssociatedCcnId')

        if m.get('AssociatedCcnName') is not None:
            self.associated_ccn_name = m.get('AssociatedCcnName')

        if m.get('BackupSoftwareVersion') is not None:
            self.backup_software_version = m.get('BackupSoftwareVersion')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataPlan') is not None:
            self.data_plan = m.get('DataPlan')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DpiMonitorStatus') is not None:
            self.dpi_monitor_status = m.get('DpiMonitorStatus')

        if m.get('DpiStatus') is not None:
            self.dpi_status = m.get('DpiStatus')

        if m.get('EnableAdvancedMonitor') is not None:
            self.enable_advanced_monitor = m.get('EnableAdvancedMonitor')

        if m.get('EnableSoftwareConnectionAudit') is not None:
            self.enable_software_connection_audit = m.get('EnableSoftwareConnectionAudit')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnterpriseCode') is not None:
            self.enterprise_code = m.get('EnterpriseCode')

        if m.get('HardwareVersion') is not None:
            self.hardware_version = m.get('HardwareVersion')

        if m.get('IRIds') is not None:
            self.irids = m.get('IRIds')

        if m.get('IdaasApplicationId') is not None:
            self.idaas_application_id = m.get('IdaasApplicationId')

        if m.get('IdaasId') is not None:
            self.idaas_id = m.get('IdaasId')

        if m.get('IpsecStatus') is not None:
            self.ipsec_status = m.get('IpsecStatus')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Links') is not None:
            temp_model = main_models.DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGatewayLinks()
            self.links = temp_model.from_map(m.get('Links'))

        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('QosIds') is not None:
            self.qos_ids = m.get('QosIds')

        if m.get('ResellerInstanceId') is not None:
            self.reseller_instance_id = m.get('ResellerInstanceId')

        if m.get('ResellerUid') is not None:
            self.reseller_uid = m.get('ResellerUid')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')

        if m.get('SecurityLockThreshold') is not None:
            self.security_lock_threshold = m.get('SecurityLockThreshold')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGUid') is not None:
            self.smart_aguid = m.get('SmartAGUid')

        if m.get('SoftwareVersion') is not None:
            self.software_version = m.get('SoftwareVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpBandwidth4G') is not None:
            self.up_bandwidth_4g = m.get('UpBandwidth4G')

        if m.get('UpBandwidthWan') is not None:
            self.up_bandwidth_wan = m.get('UpBandwidthWan')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        if m.get('VpnStatus') is not None:
            self.vpn_status = m.get('VpnStatus')

        return self

class DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGatewayLinks(DaraModel):
    def __init__(
        self,
        link: List[main_models.DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGatewayLinksLink] = None,
    ):
        self.link = link

    def validate(self):
        if self.link:
            for v1 in self.link:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Link'] = []
        if self.link is not None:
            for k1 in self.link:
                result['Link'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.link = []
        if m.get('Link') is not None:
            for k1 in m.get('Link'):
                temp_model = main_models.DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGatewayLinksLink()
                self.link.append(temp_model.from_map(k1))

        return self

class DescribeSmartAccessGatewaysResponseBodySmartAccessGatewaysSmartAccessGatewayLinksLink(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        commodity_type: str = None,
        end_time: int = None,
        instance_id: str = None,
        relate_instance_id: str = None,
        relate_instance_region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.bandwidth = bandwidth
        self.commodity_type = commodity_type
        self.end_time = end_time
        self.instance_id = instance_id
        self.relate_instance_id = relate_instance_id
        self.relate_instance_region_id = relate_instance_region_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.relate_instance_id is not None:
            result['RelateInstanceId'] = self.relate_instance_id

        if self.relate_instance_region_id is not None:
            result['RelateInstanceRegionId'] = self.relate_instance_region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RelateInstanceId') is not None:
            self.relate_instance_id = m.get('RelateInstanceId')

        if m.get('RelateInstanceRegionId') is not None:
            self.relate_instance_region_id = m.get('RelateInstanceRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

