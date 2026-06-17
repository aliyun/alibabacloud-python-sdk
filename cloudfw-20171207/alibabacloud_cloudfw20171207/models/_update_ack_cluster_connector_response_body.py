# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class UpdateAckClusterConnectorResponseBody(DaraModel):
    def __init__(
        self,
        ack_cluster_connector: main_models.UpdateAckClusterConnectorResponseBodyAckClusterConnector = None,
        request_id: str = None,
    ):
        # The ACK cluster connector.
        self.ack_cluster_connector = ack_cluster_connector
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ack_cluster_connector:
            self.ack_cluster_connector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_cluster_connector is not None:
            result['AckClusterConnector'] = self.ack_cluster_connector.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckClusterConnector') is not None:
            temp_model = main_models.UpdateAckClusterConnectorResponseBodyAckClusterConnector()
            self.ack_cluster_connector = temp_model.from_map(m.get('AckClusterConnector'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateAckClusterConnectorResponseBodyAckClusterConnector(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        connector_health_check_status: str = None,
        connector_id: str = None,
        connector_name: str = None,
        connector_status: str = None,
        create_time: str = None,
        member_uid: str = None,
        primary_vswitch_id: str = None,
        primary_vswitch_ip: str = None,
        primary_vswitch_zone_id: str = None,
        region_no: str = None,
        standby_vswitch_id: str = None,
        standby_vswitch_ip: str = None,
        standby_vswitch_zone_id: str = None,
        ttl: int = None,
        vpc_id: str = None,
    ):
        # The ID of the ACK cluster. You can call the [DescribeAckClusters](~~DescribeAckClusters~~) operation to query the list of ACK clusters.
        # 
        # - [DescribeAckClusters](~~DescribeAckClusters~~): Queries a list of ACK clusters.
        self.cluster_id = cluster_id
        # The name of the ACK cluster.
        self.cluster_name = cluster_name
        # The health check status of the ACK cluster connector.
        self.connector_health_check_status = connector_health_check_status
        # The ID of the ACK cluster connector. You can call the [DescribeAckClusterConnectors](~~DescribeAckClusterConnectors~~) operation to query the list of ACK cluster connectors.
        # 
        # - [DescribeAckClusterConnectors](~~DescribeAckClusterConnectors~~): Queries a list of ACK cluster connectors.
        self.connector_id = connector_id
        # The name of the ACK cluster connector. The name must be 1 to 64 characters in length and can contain Chinese characters, letters, digits, periods (.), underscores (_), and hyphens (-).
        self.connector_name = connector_name
        # The instance status of the ACK cluster connector.
        self.connector_status = connector_status
        # The UNIX timestamp when the ACK cluster connector was created. Unit: seconds.
        self.create_time = create_time
        # The Alibaba Cloud account ID (UID) of the account to which the ACK cluster resources belong.
        self.member_uid = member_uid
        # The primary vSwitch of the ACK cluster connector. You can call the [DescribeAccessInstanceVSwitchList](~~DescribeAccessInstanceVSwitchList~~) operation to query the list of vSwitches for synchronization nodes.
        # 
        # - [DescribeAccessInstanceVSwitchList](~~DescribeAccessInstanceVSwitchList~~): Queries a list of vSwitches for synchronization nodes.
        self.primary_vswitch_id = primary_vswitch_id
        # The IP address of the primary vSwitch for the ACK cluster connector.
        self.primary_vswitch_ip = primary_vswitch_ip
        # The zone of the primary vSwitch for the ACK cluster connector. You can call the [DescribeAccessInstanceZoneList](~~DescribeAccessInstanceZoneList~~) operation to query the list of zones for synchronization nodes.
        # 
        # - [DescribeAccessInstanceZoneList](~~DescribeAccessInstanceZoneList~~): Queries in batches the list of zones for the vSwitches of sync nodes.
        self.primary_vswitch_zone_id = primary_vswitch_zone_id
        # The region ID of the ACK cluster connector. You can call the [DescribeAccessInstanceRegionList](~~DescribeAccessInstanceRegionList~~) operation to query the list of regions for synchronization nodes.
        # 
        # - [DescribeAccessInstanceRegionList](~~DescribeAccessInstanceRegionList~~): Queries the list of sync node regions.
        # 
        # > For more information about the regions that Cloud Firewall supports for ACK cluster connectors, see [ACK cluster synchronization nodes](https://help.aliyun.com/document_detail/2865120.html).
        self.region_no = region_no
        # The standby vSwitch of the ACK cluster connector. You can call the [DescribeAccessInstanceVSwitchList](~~DescribeAccessInstanceVSwitchList~~) operation to query the list of vSwitches for synchronization nodes.
        # 
        # - [DescribeAccessInstanceVSwitchList](~~DescribeAccessInstanceVSwitchList~~): Batch queries the list of vSwitches for synchronization nodes.
        self.standby_vswitch_id = standby_vswitch_id
        # The IP address of the standby vSwitch for the ACK cluster connector.
        self.standby_vswitch_ip = standby_vswitch_ip
        # The zone of the standby vSwitch for the ACK cluster connector. You can call the [DescribeAccessInstanceZoneList](~~DescribeAccessInstanceZoneList~~) operation to query the list of zones for synchronization nodes.
        # 
        # - [DescribeAccessInstanceZoneList](~~DescribeAccessInstanceZoneList~~): Batch queries the list of zones for the vSwitches of synchronization nodes.
        self.standby_vswitch_zone_id = standby_vswitch_zone_id
        # The synchronization interval for the ACK cluster connector. Valid values: 2 to 60. Unit: seconds.
        self.ttl = ttl
        # The ID of the VPC to which the ACK cluster belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.connector_health_check_status is not None:
            result['ConnectorHealthCheckStatus'] = self.connector_health_check_status

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.connector_name is not None:
            result['ConnectorName'] = self.connector_name

        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.primary_vswitch_id is not None:
            result['PrimaryVswitchId'] = self.primary_vswitch_id

        if self.primary_vswitch_ip is not None:
            result['PrimaryVswitchIp'] = self.primary_vswitch_ip

        if self.primary_vswitch_zone_id is not None:
            result['PrimaryVswitchZoneId'] = self.primary_vswitch_zone_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.standby_vswitch_id is not None:
            result['StandbyVswitchId'] = self.standby_vswitch_id

        if self.standby_vswitch_ip is not None:
            result['StandbyVswitchIp'] = self.standby_vswitch_ip

        if self.standby_vswitch_zone_id is not None:
            result['StandbyVswitchZoneId'] = self.standby_vswitch_zone_id

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ConnectorHealthCheckStatus') is not None:
            self.connector_health_check_status = m.get('ConnectorHealthCheckStatus')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')

        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PrimaryVswitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVswitchId')

        if m.get('PrimaryVswitchIp') is not None:
            self.primary_vswitch_ip = m.get('PrimaryVswitchIp')

        if m.get('PrimaryVswitchZoneId') is not None:
            self.primary_vswitch_zone_id = m.get('PrimaryVswitchZoneId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('StandbyVswitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVswitchId')

        if m.get('StandbyVswitchIp') is not None:
            self.standby_vswitch_ip = m.get('StandbyVswitchIp')

        if m.get('StandbyVswitchZoneId') is not None:
            self.standby_vswitch_zone_id = m.get('StandbyVswitchZoneId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

