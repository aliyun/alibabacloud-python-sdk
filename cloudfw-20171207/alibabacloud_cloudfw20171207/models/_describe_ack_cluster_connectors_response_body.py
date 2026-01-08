# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAckClusterConnectorsResponseBody(DaraModel):
    def __init__(
        self,
        ack_cluster_connectors: List[main_models.DescribeAckClusterConnectorsResponseBodyAckClusterConnectors] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ack_cluster_connectors = ack_cluster_connectors
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ack_cluster_connectors:
            for v1 in self.ack_cluster_connectors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AckClusterConnectors'] = []
        if self.ack_cluster_connectors is not None:
            for k1 in self.ack_cluster_connectors:
                result['AckClusterConnectors'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ack_cluster_connectors = []
        if m.get('AckClusterConnectors') is not None:
            for k1 in m.get('AckClusterConnectors'):
                temp_model = main_models.DescribeAckClusterConnectorsResponseBodyAckClusterConnectors()
                self.ack_cluster_connectors.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAckClusterConnectorsResponseBodyAckClusterConnectors(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        connector_health_check_status: str = None,
        connector_id: str = None,
        connector_name: str = None,
        connector_status: str = None,
        create_time: str = None,
        group_uuids: List[str] = None,
        member_uid: str = None,
        primary_vswitch_id: str = None,
        primary_vswitch_ip: str = None,
        primary_vswitch_zone_id: str = None,
        region_no: str = None,
        standby_vswitch_id: str = None,
        standby_vswitch_ip: str = None,
        standby_vswitch_zone_id: str = None,
        ttl: int = None,
        unhealthy_reason: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.connector_health_check_status = connector_health_check_status
        self.connector_id = connector_id
        self.connector_name = connector_name
        self.connector_status = connector_status
        self.create_time = create_time
        self.group_uuids = group_uuids
        self.member_uid = member_uid
        self.primary_vswitch_id = primary_vswitch_id
        self.primary_vswitch_ip = primary_vswitch_ip
        self.primary_vswitch_zone_id = primary_vswitch_zone_id
        self.region_no = region_no
        self.standby_vswitch_id = standby_vswitch_id
        self.standby_vswitch_ip = standby_vswitch_ip
        self.standby_vswitch_zone_id = standby_vswitch_zone_id
        self.ttl = ttl
        self.unhealthy_reason = unhealthy_reason
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

        if self.group_uuids is not None:
            result['GroupUuids'] = self.group_uuids

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

        if self.unhealthy_reason is not None:
            result['UnhealthyReason'] = self.unhealthy_reason

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

        if m.get('GroupUuids') is not None:
            self.group_uuids = m.get('GroupUuids')

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

        if m.get('UnhealthyReason') is not None:
            self.unhealthy_reason = m.get('UnhealthyReason')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

