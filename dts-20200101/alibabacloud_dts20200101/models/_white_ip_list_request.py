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
        # The Alibaba Cloud account ID of the destination.
        self.dest_aliyun_uid = dest_aliyun_uid
        # The ID of the primary vSwitch for the destination VPC NAT gateway.
        self.dest_primary_vsw_id = dest_primary_vsw_id
        # The name of the destination role.
        self.dest_role_name = dest_role_name
        # The ID of the secondary vSwitch for the destination VPC NAT gateway.
        self.dest_secondary_vsw_id = dest_secondary_vsw_id
        # The ID of the destination VPC.
        self.dest_vpc_id = dest_vpc_id
        # The region ID of the destination instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # > - If the destination instance is a self-managed database or a third-party cloud database that has a public IP address, you can specify **cn-hangzhou** or the ID of the region that is geographically closest to the database.
        # - This parameter is required when the DTS task is a data migration or data synchronization task.
        self.destination_region = destination_region
        # The region ID of the source instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > If the source instance is a self-managed database or a third-party cloud database that has a public IP address, you can specify **cn-hangzhou** or the ID of the region that is geographically closest to the database.
        # 
        # This parameter is required.
        self.region = region
        # The region ID of the DTS instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The Alibaba Cloud account ID of the source.
        self.src_aliyun_uid = src_aliyun_uid
        # The ID of the primary vSwitch for the source VPC NAT gateway.
        self.src_primary_vsw_id = src_primary_vsw_id
        # The name of the source role.
        self.src_role_name = src_role_name
        # The ID of the secondary vSwitch for the source VPC NAT gateway.
        self.src_secondary_vsw_id = src_secondary_vsw_id
        # The ID of the source VPC.
        self.src_vpc_id = src_vpc_id
        # The connection method of the self-managed database or third-party cloud database. Valid values:
        # - **internet**: connected over the Internet.
        # - **vpc**: connected over an Express Connect circuit, a VPN gateway, or a Smart Access Gateway (SAG).
        # 
        # This parameter is required.
        self.type = type
        # Specifies whether the task is a zero-ETL task. Valid values:
        # - **true**: yes.
        # - **false**: no.
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

