# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WhiteIpListRequest(DaraModel):
    def __init__(
        self,
        dest_aliyun_uid: str = None,
        dest_primary_vsw_id: str = None,
        dest_role_name: str = None,
        dest_secondary_vsw_id: str = None,
        dest_vpc_id: str = None,
        destination_region: str = None,
        region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        src_aliyun_uid: str = None,
        src_primary_vsw_id: str = None,
        src_role_name: str = None,
        src_secondary_vsw_id: str = None,
        src_vpc_id: str = None,
        type: str = None,
        zero_etl_job: bool = None,
    ):
        # The UID of the destination Alibaba Cloud account.
        self.dest_aliyun_uid = dest_aliyun_uid
        # The primary vSwitch of the destination for VPC NAT.
        self.dest_primary_vsw_id = dest_primary_vsw_id
        # The name of the destination role.
        self.dest_role_name = dest_role_name
        # The secondary vSwitch of the destination for VPC NAT.
        self.dest_secondary_vsw_id = dest_secondary_vsw_id
        # The ID of the destination VPC.
        self.dest_vpc_id = dest_vpc_id
        # The region ID of the destination instance. For details, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # > -  If the destination instance is a self-managed database with a public IP address or a third-party ApsaraDB database, you can set this parameter to **ap-southeast-1** or the area ID that is geographically closest to the database.
        # -  This parameter is required when the DTS task is a data migration or data synchronization task.
        self.destination_region = destination_region
        # The region ID of the source instance. For details, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > If the source instance is a self-managed database with a public IP address or a third-party ApsaraDB database, you can set this parameter to **ap-southeast-1** or the area ID that is geographically closest to the database.
        # 
        # This parameter is required.
        self.region = region
        # The region to which the DTS instance belongs. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The UID of the source Alibaba Cloud account.
        self.src_aliyun_uid = src_aliyun_uid
        # The primary vSwitch of the source for VPC NAT.
        self.src_primary_vsw_id = src_primary_vsw_id
        # The name of the source role.
        self.src_role_name = src_role_name
        # The secondary vSwitch of the source for VPC NAT.
        self.src_secondary_vsw_id = src_secondary_vsw_id
        # The ID of the source VPC.
        self.src_vpc_id = src_vpc_id
        # The connection method of the self-managed database or third-party ApsaraDB database. Valid values:
        # - **internet**: connected over the Internet.
        # - **vpc**: connected over Express Connect, VPN Gateway, or Smart Access Gateway.
        # 
        # This parameter is required.
        self.type = type
        # Specifies whether the node is a seamless integration (Zero-ETL) node. Valid values:
        # - **true**: The node is a seamless integration (Zero-ETL) node.
        # - **false**: The node is not a seamless integration (Zero-ETL) node.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_aliyun_uid is not None:
            result['DestAliyunUid'] = self.dest_aliyun_uid

        if self.dest_primary_vsw_id is not None:
            result['DestPrimaryVswId'] = self.dest_primary_vsw_id

        if self.dest_role_name is not None:
            result['DestRoleName'] = self.dest_role_name

        if self.dest_secondary_vsw_id is not None:
            result['DestSecondaryVswId'] = self.dest_secondary_vsw_id

        if self.dest_vpc_id is not None:
            result['DestVpcId'] = self.dest_vpc_id

        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.src_aliyun_uid is not None:
            result['SrcAliyunUid'] = self.src_aliyun_uid

        if self.src_primary_vsw_id is not None:
            result['SrcPrimaryVswId'] = self.src_primary_vsw_id

        if self.src_role_name is not None:
            result['SrcRoleName'] = self.src_role_name

        if self.src_secondary_vsw_id is not None:
            result['SrcSecondaryVswId'] = self.src_secondary_vsw_id

        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id

        if self.type is not None:
            result['Type'] = self.type

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestAliyunUid') is not None:
            self.dest_aliyun_uid = m.get('DestAliyunUid')

        if m.get('DestPrimaryVswId') is not None:
            self.dest_primary_vsw_id = m.get('DestPrimaryVswId')

        if m.get('DestRoleName') is not None:
            self.dest_role_name = m.get('DestRoleName')

        if m.get('DestSecondaryVswId') is not None:
            self.dest_secondary_vsw_id = m.get('DestSecondaryVswId')

        if m.get('DestVpcId') is not None:
            self.dest_vpc_id = m.get('DestVpcId')

        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SrcAliyunUid') is not None:
            self.src_aliyun_uid = m.get('SrcAliyunUid')

        if m.get('SrcPrimaryVswId') is not None:
            self.src_primary_vsw_id = m.get('SrcPrimaryVswId')

        if m.get('SrcRoleName') is not None:
            self.src_role_name = m.get('SrcRoleName')

        if m.get('SrcSecondaryVswId') is not None:
            self.src_secondary_vsw_id = m.get('SrcSecondaryVswId')

        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

