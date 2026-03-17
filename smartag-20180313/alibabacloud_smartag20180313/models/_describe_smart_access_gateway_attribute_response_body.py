# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSmartAccessGatewayAttributeResponseBody(DaraModel):
    def __init__(
        self,
        accelerate_bandwidth: int = None,
        access_point_id: str = None,
        acl_ids: main_models.DescribeSmartAccessGatewayAttributeResponseBodyAclIds = None,
        application_bandwidth_package_bussiness_status: str = None,
        application_bandwidth_package_id: str = None,
        application_bandwidth_package_name: str = None,
        application_bandwidth_package_operation_locks: main_models.DescribeSmartAccessGatewayAttributeResponseBodyApplicationBandwidthPackageOperationLocks = None,
        associated_ccn_id: str = None,
        associated_ccn_name: str = None,
        backup_box_controller_ip: str = None,
        box_controller_ip: str = None,
        cidr_block: str = None,
        city: str = None,
        create_time: int = None,
        data_plan: int = None,
        description: str = None,
        devices: main_models.DescribeSmartAccessGatewayAttributeResponseBodyDevices = None,
        enable_optimization: bool = None,
        enable_software_connection_audit: bool = None,
        end_time: int = None,
        flow_log_ids: main_models.DescribeSmartAccessGatewayAttributeResponseBodyFlowLogIds = None,
        irids: main_models.DescribeSmartAccessGatewayAttributeResponseBodyIRIds = None,
        instance_type: str = None,
        ipsec_status: str = None,
        links: main_models.DescribeSmartAccessGatewayAttributeResponseBodyLinks = None,
        max_bandwidth: str = None,
        name: str = None,
        optimization_type: bool = None,
        position: str = None,
        qos_ids: main_models.DescribeSmartAccessGatewayAttributeResponseBodyQosIds = None,
        request_id: str = None,
        reseller_instance_id: str = None,
        reseller_uid: str = None,
        resource_group_id: str = None,
        routing_strategy: str = None,
        security_lock_threshold: int = None,
        serial_number: str = None,
        smart_agid: str = None,
        status: str = None,
        traffic_master_sn: str = None,
        up_bandwidth_4g: int = None,
        up_bandwidth_wan: int = None,
        user_count: int = None,
        vpn_status: str = None,
    ):
        # The maximum bandwidth value for application acceleration. Unit: Mbit/s.
        self.accelerate_bandwidth = accelerate_bandwidth
        # The ID of the access point for the SAG instance.
        self.access_point_id = access_point_id
        self.acl_ids = acl_ids
        # The status of the bandwidth plan for application acceleration. Valid value:
        # 
        # *   **Abnormal**: abnormal
        # *   **Normal**: normal
        self.application_bandwidth_package_bussiness_status = application_bandwidth_package_bussiness_status
        # The ID of the bandwidth plan for application acceleration that is associated with the SAG instance.
        self.application_bandwidth_package_id = application_bandwidth_package_id
        # The name of the bandwidth plan for application acceleration that is associated with the SAG instance.
        self.application_bandwidth_package_name = application_bandwidth_package_name
        # Indicates whether the bandwidth plan is locked.
        self.application_bandwidth_package_operation_locks = application_bandwidth_package_operation_locks
        # The ID of the Cloud Connect Network (CCN) instance with which the SAG instance is associated.
        self.associated_ccn_id = associated_ccn_id
        # The ID of the Cloud Connect Network (CCN) instance with which the SAG instance is associated.
        self.associated_ccn_name = associated_ccn_name
        # The public IP address of the standby SAG device.
        self.backup_box_controller_ip = backup_box_controller_ip
        # The public IP address of the active SAG device.
        self.box_controller_ip = box_controller_ip
        # The private CIDR block of the destination network with which the on-premises network or client needs to communicate.
        self.cidr_block = cidr_block
        # The ID of the city where the SAG device is deployed.
        self.city = city
        # The timestamp when the SAG instance was created.
        self.create_time = create_time
        # The data transfer plan of the SAG instance. Unit: GB.
        # 
        # >  Each client account has a data transfer plan free of charge for 5 GB each month.
        self.data_plan = data_plan
        # The description of the SAG instance.
        self.description = description
        self.devices = devices
        # Indicates whether the transmission optimization feature is enabled.
        # 
        # *   **true**: yes
        # *   **false**: no
        self.enable_optimization = enable_optimization
        # Indicates whether the audit log for connections to the SAG app instance is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.enable_software_connection_audit = enable_software_connection_audit
        # The timestamp when the SAG instance expires.
        self.end_time = end_time
        self.flow_log_ids = flow_log_ids
        self.irids = irids
        # The type of the SAG instance. Valid values:
        # 
        # *   **sag-1000**: indicates an SAG CPE instance and the instance is associated with an SAG-1000 device.
        # *   **sag-10wm**: indicates an SAG CPE instance and the instance is associated with an SAG-100WM device.
        # *   **sag-software**: indicates an SAG app instance.
        # *   **sag-vcpe**: an SAG vCPE instance.
        self.instance_type = instance_type
        # The status of the IPsec-VPN connection. Valid values:
        # 
        # *   **up**: normal
        # *   **down**: abnormal
        self.ipsec_status = ipsec_status
        self.links = links
        # The maximum bandwidth value of the SAG instance. Unit: Mbit/s.
        self.max_bandwidth = max_bandwidth
        # The name of the SAG instance.
        self.name = name
        # The transmission optimization type of the SAG instance. If transmission optimization is enabled, the default value is **fec**.
        self.optimization_type = optimization_type
        # The location of the SAG instance.
        self.position = position
        self.qos_ids = qos_ids
        # The ID of the request.
        self.request_id = request_id
        # The ID of the instance provided by the third-party reseller.
        self.reseller_instance_id = reseller_instance_id
        # The ID of the third-party reseller.
        self.reseller_uid = reseller_uid
        # The ID of the resource group to which the SAG instance belongs.
        self.resource_group_id = resource_group_id
        # The method that the SAG instance uses to advertise routes to Alibaba Cloud.
        # 
        # *   **static**: static routing
        # *   **dynamic**: dynamic routing
        self.routing_strategy = routing_strategy
        # The time threshold. If the SAG device remains disconnected for the specified period of time, the SAG device is locked.
        # 
        # Unit: seconds.
        self.security_lock_threshold = security_lock_threshold
        # The serial number of the SAG device.
        self.serial_number = serial_number
        # The ID of the SAG instance.
        self.smart_agid = smart_agid
        # The status of the SAG instance. Valid values:
        # 
        # *   **Ordered**: The order is to be shipped.
        # *   **Delivered**: The SAG instance is shipped.
        # *   **Received**: The SAG instance is activated.
        # *   **Unconfirmed**: The SAG instance is to be confirmed.
        # *   **Active**: The SAG instance is available.
        # *   **Offline**: The SAG instance is disconnected.
        # *   **Arrearage**: The SAG device is locked due to overdue payments.
        self.status = status
        # The serial number of the active SAG device.
        self.traffic_master_sn = traffic_master_sn
        # The maximum upstream bandwidth of 4G network connections established by the SAG device. Unit: Mbit/s.
        self.up_bandwidth_4g = up_bandwidth_4g
        # The maximum upstream bandwidth of network connections established on the WAN port of the SAG device. Unit: Mbit/s.
        self.up_bandwidth_wan = up_bandwidth_wan
        # The number of client accounts on the SAG instance.
        self.user_count = user_count
        # The status of the VPN connection. Valid values:
        # 
        # *   **up**: normal
        # *   **down**: abnormal
        self.vpn_status = vpn_status

    def validate(self):
        if self.acl_ids:
            self.acl_ids.validate()
        if self.application_bandwidth_package_operation_locks:
            self.application_bandwidth_package_operation_locks.validate()
        if self.devices:
            self.devices.validate()
        if self.flow_log_ids:
            self.flow_log_ids.validate()
        if self.irids:
            self.irids.validate()
        if self.links:
            self.links.validate()
        if self.qos_ids:
            self.qos_ids.validate()

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
            result['AclIds'] = self.acl_ids.to_map()

        if self.application_bandwidth_package_bussiness_status is not None:
            result['ApplicationBandwidthPackageBussinessStatus'] = self.application_bandwidth_package_bussiness_status

        if self.application_bandwidth_package_id is not None:
            result['ApplicationBandwidthPackageId'] = self.application_bandwidth_package_id

        if self.application_bandwidth_package_name is not None:
            result['ApplicationBandwidthPackageName'] = self.application_bandwidth_package_name

        if self.application_bandwidth_package_operation_locks is not None:
            result['ApplicationBandwidthPackageOperationLocks'] = self.application_bandwidth_package_operation_locks.to_map()

        if self.associated_ccn_id is not None:
            result['AssociatedCcnId'] = self.associated_ccn_id

        if self.associated_ccn_name is not None:
            result['AssociatedCcnName'] = self.associated_ccn_name

        if self.backup_box_controller_ip is not None:
            result['BackupBoxControllerIp'] = self.backup_box_controller_ip

        if self.box_controller_ip is not None:
            result['BoxControllerIp'] = self.box_controller_ip

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

        if self.devices is not None:
            result['Devices'] = self.devices.to_map()

        if self.enable_optimization is not None:
            result['EnableOptimization'] = self.enable_optimization

        if self.enable_software_connection_audit is not None:
            result['EnableSoftwareConnectionAudit'] = self.enable_software_connection_audit

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.flow_log_ids is not None:
            result['FlowLogIds'] = self.flow_log_ids.to_map()

        if self.irids is not None:
            result['IRIds'] = self.irids.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ipsec_status is not None:
            result['IpsecStatus'] = self.ipsec_status

        if self.links is not None:
            result['Links'] = self.links.to_map()

        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth

        if self.name is not None:
            result['Name'] = self.name

        if self.optimization_type is not None:
            result['OptimizationType'] = self.optimization_type

        if self.position is not None:
            result['Position'] = self.position

        if self.qos_ids is not None:
            result['QosIds'] = self.qos_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.status is not None:
            result['Status'] = self.status

        if self.traffic_master_sn is not None:
            result['TrafficMasterSn'] = self.traffic_master_sn

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
            temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyAclIds()
            self.acl_ids = temp_model.from_map(m.get('AclIds'))

        if m.get('ApplicationBandwidthPackageBussinessStatus') is not None:
            self.application_bandwidth_package_bussiness_status = m.get('ApplicationBandwidthPackageBussinessStatus')

        if m.get('ApplicationBandwidthPackageId') is not None:
            self.application_bandwidth_package_id = m.get('ApplicationBandwidthPackageId')

        if m.get('ApplicationBandwidthPackageName') is not None:
            self.application_bandwidth_package_name = m.get('ApplicationBandwidthPackageName')

        if m.get('ApplicationBandwidthPackageOperationLocks') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyApplicationBandwidthPackageOperationLocks()
            self.application_bandwidth_package_operation_locks = temp_model.from_map(m.get('ApplicationBandwidthPackageOperationLocks'))

        if m.get('AssociatedCcnId') is not None:
            self.associated_ccn_id = m.get('AssociatedCcnId')

        if m.get('AssociatedCcnName') is not None:
            self.associated_ccn_name = m.get('AssociatedCcnName')

        if m.get('BackupBoxControllerIp') is not None:
            self.backup_box_controller_ip = m.get('BackupBoxControllerIp')

        if m.get('BoxControllerIp') is not None:
            self.box_controller_ip = m.get('BoxControllerIp')

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

        if m.get('Devices') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyDevices()
            self.devices = temp_model.from_map(m.get('Devices'))

        if m.get('EnableOptimization') is not None:
            self.enable_optimization = m.get('EnableOptimization')

        if m.get('EnableSoftwareConnectionAudit') is not None:
            self.enable_software_connection_audit = m.get('EnableSoftwareConnectionAudit')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FlowLogIds') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyFlowLogIds()
            self.flow_log_ids = temp_model.from_map(m.get('FlowLogIds'))

        if m.get('IRIds') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyIRIds()
            self.irids = temp_model.from_map(m.get('IRIds'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IpsecStatus') is not None:
            self.ipsec_status = m.get('IpsecStatus')

        if m.get('Links') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyLinks()
            self.links = temp_model.from_map(m.get('Links'))

        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OptimizationType') is not None:
            self.optimization_type = m.get('OptimizationType')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('QosIds') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyQosIds()
            self.qos_ids = temp_model.from_map(m.get('QosIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrafficMasterSn') is not None:
            self.traffic_master_sn = m.get('TrafficMasterSn')

        if m.get('UpBandwidth4G') is not None:
            self.up_bandwidth_4g = m.get('UpBandwidth4G')

        if m.get('UpBandwidthWan') is not None:
            self.up_bandwidth_wan = m.get('UpBandwidthWan')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        if m.get('VpnStatus') is not None:
            self.vpn_status = m.get('VpnStatus')

        return self

class DescribeSmartAccessGatewayAttributeResponseBodyQosIds(DaraModel):
    def __init__(
        self,
        qos_id: List[str] = None,
    ):
        self.qos_id = qos_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        return self

class DescribeSmartAccessGatewayAttributeResponseBodyLinks(DaraModel):
    def __init__(
        self,
        link: List[main_models.DescribeSmartAccessGatewayAttributeResponseBodyLinksLink] = None,
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
                temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyLinksLink()
                self.link.append(temp_model.from_map(k1))

        return self

class DescribeSmartAccessGatewayAttributeResponseBodyLinksLink(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        commodity_type: str = None,
        end_time: int = None,
        health_check_target_ip: str = None,
        instance_id: str = None,
        relate_instance_id: str = None,
        relate_instance_region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.bandwidth = bandwidth
        self.commodity_type = commodity_type
        self.end_time = end_time
        self.health_check_target_ip = health_check_target_ip
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

        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip

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

        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')

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

class DescribeSmartAccessGatewayAttributeResponseBodyIRIds(DaraModel):
    def __init__(
        self,
        irid: List[str] = None,
    ):
        self.irid = irid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.irid is not None:
            result['IRId'] = self.irid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IRId') is not None:
            self.irid = m.get('IRId')

        return self

class DescribeSmartAccessGatewayAttributeResponseBodyFlowLogIds(DaraModel):
    def __init__(
        self,
        flow_log_id: List[str] = None,
    ):
        self.flow_log_id = flow_log_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        return self

class DescribeSmartAccessGatewayAttributeResponseBodyDevices(DaraModel):
    def __init__(
        self,
        device: List[main_models.DescribeSmartAccessGatewayAttributeResponseBodyDevicesDevice] = None,
    ):
        self.device = device

    def validate(self):
        if self.device:
            for v1 in self.device:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Device'] = []
        if self.device is not None:
            for k1 in self.device:
                result['Device'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device = []
        if m.get('Device') is not None:
            for k1 in m.get('Device'):
                temp_model = main_models.DescribeSmartAccessGatewayAttributeResponseBodyDevicesDevice()
                self.device.append(temp_model.from_map(k1))

        return self

class DescribeSmartAccessGatewayAttributeResponseBodyDevicesDevice(DaraModel):
    def __init__(
        self,
        distribute_sk_status: int = None,
        dpi_signature_db_version: str = None,
        ha_state: str = None,
        hc_state: str = None,
        monitor_version: str = None,
        secret_key: str = None,
        serial_number: str = None,
        software_version: str = None,
    ):
        self.distribute_sk_status = distribute_sk_status
        self.dpi_signature_db_version = dpi_signature_db_version
        self.ha_state = ha_state
        self.hc_state = hc_state
        self.monitor_version = monitor_version
        self.secret_key = secret_key
        self.serial_number = serial_number
        self.software_version = software_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribute_sk_status is not None:
            result['DistributeSkStatus'] = self.distribute_sk_status

        if self.dpi_signature_db_version is not None:
            result['DpiSignatureDbVersion'] = self.dpi_signature_db_version

        if self.ha_state is not None:
            result['HaState'] = self.ha_state

        if self.hc_state is not None:
            result['HcState'] = self.hc_state

        if self.monitor_version is not None:
            result['MonitorVersion'] = self.monitor_version

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.software_version is not None:
            result['SoftwareVersion'] = self.software_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeSkStatus') is not None:
            self.distribute_sk_status = m.get('DistributeSkStatus')

        if m.get('DpiSignatureDbVersion') is not None:
            self.dpi_signature_db_version = m.get('DpiSignatureDbVersion')

        if m.get('HaState') is not None:
            self.ha_state = m.get('HaState')

        if m.get('HcState') is not None:
            self.hc_state = m.get('HcState')

        if m.get('MonitorVersion') is not None:
            self.monitor_version = m.get('MonitorVersion')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SoftwareVersion') is not None:
            self.software_version = m.get('SoftwareVersion')

        return self

class DescribeSmartAccessGatewayAttributeResponseBodyApplicationBandwidthPackageOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        # The reason why the instance was locked.
        self.lock_reason = lock_reason
        # The lock mode of the instance. The value is set to **FinancialLocked**.
        self.lock_type = lock_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.lock_type is not None:
            result['LockType'] = self.lock_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')

        return self

class DescribeSmartAccessGatewayAttributeResponseBodyAclIds(DaraModel):
    def __init__(
        self,
        acl_id: List[str] = None,
    ):
        self.acl_id = acl_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        return self

