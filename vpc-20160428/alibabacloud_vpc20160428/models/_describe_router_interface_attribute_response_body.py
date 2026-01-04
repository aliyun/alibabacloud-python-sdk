# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeRouterInterfaceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        bandwidth: int = None,
        business_status: str = None,
        charge_type: str = None,
        code: str = None,
        connected_time: str = None,
        creation_time: str = None,
        cross_border: bool = None,
        description: str = None,
        end_time: str = None,
        fast_link_mode: str = None,
        gmt_modified: str = None,
        has_reservation_data: str = None,
        hc_rate: int = None,
        hc_threshold: int = None,
        health_check_source_ip: str = None,
        health_check_status: str = None,
        health_check_target_ip: str = None,
        message: str = None,
        name: str = None,
        opposite_access_point_id: str = None,
        opposite_bandwidth: int = None,
        opposite_interface_business_status: str = None,
        opposite_interface_id: str = None,
        opposite_interface_owner_id: str = None,
        opposite_interface_spec: str = None,
        opposite_interface_status: str = None,
        opposite_region_id: str = None,
        opposite_router_id: str = None,
        opposite_router_type: str = None,
        opposite_vpc_instance_id: str = None,
        request_id: str = None,
        reservation_active_time: str = None,
        reservation_bandwidth: str = None,
        reservation_internet_charge_type: str = None,
        reservation_order_type: str = None,
        resource_group_id: str = None,
        role: str = None,
        router_id: str = None,
        router_interface_id: str = None,
        router_type: str = None,
        spec: str = None,
        status: str = None,
        success: bool = None,
        tags: main_models.DescribeRouterInterfaceAttributeResponseBodyTags = None,
        vpc_instance_id: str = None,
    ):
        # The ID of the access point.
        self.access_point_id = access_point_id
        # The bandwidth of the router interface. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The status of the router interface. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        # *   **SecurityLocked**
        self.business_status = business_status
        # The billing method. Valid values:
        # 
        # *   **AfterPay**: pay-as-you-go
        # *   **PrePaid**: subscription
        self.charge_type = charge_type
        # The HTTP status code.
        self.code = code
        # The time when the connection was established.
        self.connected_time = connected_time
        # The time when the router interface was created.
        self.creation_time = creation_time
        # Indicates whether the connection is a cross-border connection. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.cross_border = cross_border
        # The description of the router interface.
        self.description = description
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # Indicates whether the VBR that is created in the Fast Link mode is uplinked to the router interface. The Fast Link mode helps automatically connect router interfaces that are created for the VBR and its peer VPC. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > 
        # 
        # *   This parameter takes effect only when **RouterType** is set to **VBR** and **OppositeRouterType** is set to **VRouter**.
        # 
        # *   When **FastLinkMode** is set to **true**, **Role** must be set to **InitiatingSide**. **AccessPointId**, **OppositeRouterType**, **OpppsiteRouterId**, and **OppositeInterfaceOwnerId** are required.
        self.fast_link_mode = fast_link_mode
        # The time when the router interface was modified.
        self.gmt_modified = gmt_modified
        # Indicates whether renewal data is included. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.has_reservation_data = has_reservation_data
        # The rate of health checks. Unit: seconds. The value indicates the interval at which probe packets are sent during a health check.
        self.hc_rate = hc_rate
        # The healthy threshold. This value indicates the number of probe packets that are sent during a health check. Unit: packets.
        self.hc_threshold = hc_threshold
        # The source IP address that is used for the health check.
        self.health_check_source_ip = health_check_source_ip
        # The status of the health check. Valid values:
        # 
        # *   **Abnormal**
        # *   **Normal**
        # *   **NoRedundantRoute**
        # *   **NoHealthCheckConfig**
        self.health_check_status = health_check_status
        # The destination IP address that is used for the health check.
        self.health_check_target_ip = health_check_target_ip
        # The response parameters.
        self.message = message
        # The name of the router interface.
        self.name = name
        # The ID of the peer access point.
        self.opposite_access_point_id = opposite_access_point_id
        # The maximum bandwidth of the peer router interface. Unit: Mbit/s.
        self.opposite_bandwidth = opposite_bandwidth
        # The service status of the peer router interface. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        # *   **SecurityLocked**
        self.opposite_interface_business_status = opposite_interface_business_status
        # The ID of the peer router interface.
        self.opposite_interface_id = opposite_interface_id
        # The ID of the Alibaba Cloud account to which the peer router interface belongs.
        self.opposite_interface_owner_id = opposite_interface_owner_id
        # The specification of the peer router interface. Valid values:
        # 
        # *   **Mini.2**: 2 Mbit/s
        # *   **Mini.5**: 5 Mbit/s
        # *   **Small.1**: 10 Mbit/s
        # *   **Small.2**: 20 Mbit/s
        # *   **Small.5**: 50 Mbit/s
        # *   **Middle.1**: 100 Mbit/s
        # *   **Middle.2**: 200 Mbit/s
        # *   **Middle.5**: 500 Mbit/s
        # *   **Large.1**: 1,000 Mbit/s
        # *   **Large.2**: 2,000 Mbit/s
        # *   **Large.5**: 5,000 Mbit/s
        # *   **Xlarge.1**: 10,000 Mbit/s
        # *   **Negative**: not applicable
        self.opposite_interface_spec = opposite_interface_spec
        # The status of the peer router interface. Valid values:
        # 
        # *   **Idle**
        # *   **AcceptingConnecting**
        # *   **Connecting**
        # *   **Activating**
        # *   **Active**
        # *   **Modifying**
        # *   **Deactivating**
        # *   **Inactive**
        # *   **Deleting**
        # *   **Deleted**
        self.opposite_interface_status = opposite_interface_status
        # The region ID of the peer router interface.
        self.opposite_region_id = opposite_region_id
        # The ID of the router to which the peer router interface belongs.
        self.opposite_router_id = opposite_router_id
        # The type of the router to which the peer router interface belongs. Valid values:
        # 
        # *   **VRouter**
        # *   **VBR**
        self.opposite_router_type = opposite_router_type
        # The ID of the peer VPC.
        self.opposite_vpc_instance_id = opposite_vpc_instance_id
        # The request ID.
        self.request_id = request_id
        # The time when the renewal takes effect.
        self.reservation_active_time = reservation_active_time
        # The maximum bandwidth after the renewal takes effect. Unit: Mbit/s.
        self.reservation_bandwidth = reservation_bandwidth
        # The metering method that is used after the renewal takes effect. Valid values: If **PayByBandwidth** is returned, it indicates that the Express Connect circuit is billed on a pay-by-bandwidth basis.
        self.reservation_internet_charge_type = reservation_internet_charge_type
        # The type of the renewal order. Only **RENEW** may be returned, which indicates that the order is placed for service renewal.
        self.reservation_order_type = reservation_order_type
        # The resource group ID.
        # 
        # For more information about resource groups, see [What is a resource group?](https://help.aliyun.com/document_detail/94475.html)
        self.resource_group_id = resource_group_id
        # The role of the router interface in the peering connection.
        self.role = role
        # The ID of the router to which the router interface belongs.
        self.router_id = router_id
        # The ID of the router interface.
        self.router_interface_id = router_interface_id
        # The type of the router to which the route table belongs. Valid values:
        # 
        # *   **VRouter**
        # *   **VBR**
        self.router_type = router_type
        # The specification of the router interface. Valid values:
        # 
        # *   **Mini.2**: 2 Mbit/s
        # *   **Mini.5**: 5 Mbit/s
        # *   **Small.1**: 10 Mbit/s
        # *   **Small.2**: 20 Mbit/s
        # *   **Small.5**: 50 Mbit/s
        # *   **Middle.1**: 100 Mbit/s
        # *   **Middle.2**: 200 Mbit/s
        # *   **Middle.5**: 500 Mbit/s
        # *   **Large.1**: 1,000 Mbit/s
        # *   **Large.2**: 2,000 Mbit/s
        # *   **Large.5**: 5,000 Mbit/s
        # *   **Xlarge.1**: 10,000 Mbit/s
        self.spec = spec
        # The status of the router interface. Valid values:
        # 
        # *   **Idle**
        # *   **AcceptingConnecting**
        # *   **Connecting**
        # *   **Activating**
        # *   **Active**
        # *   **Modifying**
        # *   **Deactivating**
        # *   **Inactive**
        # *   **Deleting**
        self.status = status
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success
        # The tag of the resource.
        self.tags = tags
        # The ID of the virtual private cloud (VPC) to which the router interface belongs.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.code is not None:
            result['Code'] = self.code

        if self.connected_time is not None:
            result['ConnectedTime'] = self.connected_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.cross_border is not None:
            result['CrossBorder'] = self.cross_border

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fast_link_mode is not None:
            result['FastLinkMode'] = self.fast_link_mode

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data

        if self.hc_rate is not None:
            result['HcRate'] = self.hc_rate

        if self.hc_threshold is not None:
            result['HcThreshold'] = self.hc_threshold

        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip

        if self.health_check_status is not None:
            result['HealthCheckStatus'] = self.health_check_status

        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.opposite_access_point_id is not None:
            result['OppositeAccessPointId'] = self.opposite_access_point_id

        if self.opposite_bandwidth is not None:
            result['OppositeBandwidth'] = self.opposite_bandwidth

        if self.opposite_interface_business_status is not None:
            result['OppositeInterfaceBusinessStatus'] = self.opposite_interface_business_status

        if self.opposite_interface_id is not None:
            result['OppositeInterfaceId'] = self.opposite_interface_id

        if self.opposite_interface_owner_id is not None:
            result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id

        if self.opposite_interface_spec is not None:
            result['OppositeInterfaceSpec'] = self.opposite_interface_spec

        if self.opposite_interface_status is not None:
            result['OppositeInterfaceStatus'] = self.opposite_interface_status

        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id

        if self.opposite_router_id is not None:
            result['OppositeRouterId'] = self.opposite_router_id

        if self.opposite_router_type is not None:
            result['OppositeRouterType'] = self.opposite_router_type

        if self.opposite_vpc_instance_id is not None:
            result['OppositeVpcInstanceId'] = self.opposite_vpc_instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reservation_active_time is not None:
            result['ReservationActiveTime'] = self.reservation_active_time

        if self.reservation_bandwidth is not None:
            result['ReservationBandwidth'] = self.reservation_bandwidth

        if self.reservation_internet_charge_type is not None:
            result['ReservationInternetChargeType'] = self.reservation_internet_charge_type

        if self.reservation_order_type is not None:
            result['ReservationOrderType'] = self.reservation_order_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.role is not None:
            result['Role'] = self.role

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id

        if self.router_type is not None:
            result['RouterType'] = self.router_type

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConnectedTime') is not None:
            self.connected_time = m.get('ConnectedTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CrossBorder') is not None:
            self.cross_border = m.get('CrossBorder')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FastLinkMode') is not None:
            self.fast_link_mode = m.get('FastLinkMode')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')

        if m.get('HcRate') is not None:
            self.hc_rate = m.get('HcRate')

        if m.get('HcThreshold') is not None:
            self.hc_threshold = m.get('HcThreshold')

        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')

        if m.get('HealthCheckStatus') is not None:
            self.health_check_status = m.get('HealthCheckStatus')

        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OppositeAccessPointId') is not None:
            self.opposite_access_point_id = m.get('OppositeAccessPointId')

        if m.get('OppositeBandwidth') is not None:
            self.opposite_bandwidth = m.get('OppositeBandwidth')

        if m.get('OppositeInterfaceBusinessStatus') is not None:
            self.opposite_interface_business_status = m.get('OppositeInterfaceBusinessStatus')

        if m.get('OppositeInterfaceId') is not None:
            self.opposite_interface_id = m.get('OppositeInterfaceId')

        if m.get('OppositeInterfaceOwnerId') is not None:
            self.opposite_interface_owner_id = m.get('OppositeInterfaceOwnerId')

        if m.get('OppositeInterfaceSpec') is not None:
            self.opposite_interface_spec = m.get('OppositeInterfaceSpec')

        if m.get('OppositeInterfaceStatus') is not None:
            self.opposite_interface_status = m.get('OppositeInterfaceStatus')

        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')

        if m.get('OppositeRouterId') is not None:
            self.opposite_router_id = m.get('OppositeRouterId')

        if m.get('OppositeRouterType') is not None:
            self.opposite_router_type = m.get('OppositeRouterType')

        if m.get('OppositeVpcInstanceId') is not None:
            self.opposite_vpc_instance_id = m.get('OppositeVpcInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReservationActiveTime') is not None:
            self.reservation_active_time = m.get('ReservationActiveTime')

        if m.get('ReservationBandwidth') is not None:
            self.reservation_bandwidth = m.get('ReservationBandwidth')

        if m.get('ReservationInternetChargeType') is not None:
            self.reservation_internet_charge_type = m.get('ReservationInternetChargeType')

        if m.get('ReservationOrderType') is not None:
            self.reservation_order_type = m.get('ReservationOrderType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')

        if m.get('RouterType') is not None:
            self.router_type = m.get('RouterType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeRouterInterfaceAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

class DescribeRouterInterfaceAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tags: List[main_models.DescribeRouterInterfaceAttributeResponseBodyTagsTags] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeRouterInterfaceAttributeResponseBodyTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeRouterInterfaceAttributeResponseBodyTagsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the resource. You must enter at least one tag key and at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N added to the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # It can be up to 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

