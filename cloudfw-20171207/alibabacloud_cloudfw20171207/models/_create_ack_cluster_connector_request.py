# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAckClusterConnectorRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connector_name: str = None,
        member_uid: str = None,
        primary_vswitch_id: str = None,
        primary_vswitch_ip: str = None,
        region_no: str = None,
        standby_vswitch_id: str = None,
        standby_vswitch_ip: str = None,
        ttl: str = None,
    ):
        # The ACK cluster ID. You can call the following operation to obtain the value:
        # - [DescribeAckClusters](~~DescribeAckClusters~~): Lists ACK clusters.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the ACK cluster connector. The name must be 1 to 64 characters in length and can contain letters, digits, Chinese characters, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.connector_name = connector_name
        # The Alibaba Cloud UID of the account to which the ACK cluster resource belongs.
        self.member_uid = member_uid
        # The primary vSwitch of the ACK cluster connector. You can call the following operation to obtain the value:
        # - [DescribeAccessInstanceVSwitchList](~~DescribeAccessInstanceVSwitchList~~): Lists the vSwitches of synchronization nodes.
        # 
        # This parameter is required.
        self.primary_vswitch_id = primary_vswitch_id
        # The IP address of the primary vSwitch of the ACK cluster connector.
        self.primary_vswitch_ip = primary_vswitch_ip
        # The region ID of the ACK cluster connector. You can call the following operation to obtain the value:
        # - [DescribeAccessInstanceRegionList](~~DescribeAccessInstanceRegionList~~): Lists the regions of synchronization nodes.
        # 
        # > For more information about the regions supported by ACK cluster connectors in Cloud Firewall, see [ACK cluster synchronization nodes](https://help.aliyun.com/document_detail/2865120.html).
        # 
        # This parameter is required.
        self.region_no = region_no
        # The standby vSwitch of the ACK cluster connector. You can call the following operation to obtain the value:
        # - [DescribeAccessInstanceVSwitchList](~~DescribeAccessInstanceVSwitchList~~): Lists the vSwitches of synchronization nodes.
        self.standby_vswitch_id = standby_vswitch_id
        # The IP address of the standby vSwitch of the ACK cluster connector.
        self.standby_vswitch_ip = standby_vswitch_ip
        # The synchronization interval of the ACK cluster connector. Valid values: 2 to 60. Unit: seconds.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connector_name is not None:
            result['ConnectorName'] = self.connector_name

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.primary_vswitch_id is not None:
            result['PrimaryVswitchId'] = self.primary_vswitch_id

        if self.primary_vswitch_ip is not None:
            result['PrimaryVswitchIp'] = self.primary_vswitch_ip

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.standby_vswitch_id is not None:
            result['StandbyVswitchId'] = self.standby_vswitch_id

        if self.standby_vswitch_ip is not None:
            result['StandbyVswitchIp'] = self.standby_vswitch_ip

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PrimaryVswitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVswitchId')

        if m.get('PrimaryVswitchIp') is not None:
            self.primary_vswitch_ip = m.get('PrimaryVswitchIp')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('StandbyVswitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVswitchId')

        if m.get('StandbyVswitchIp') is not None:
            self.standby_vswitch_ip = m.get('StandbyVswitchIp')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

