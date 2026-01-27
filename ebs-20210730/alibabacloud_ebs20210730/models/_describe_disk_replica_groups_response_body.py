# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskReplicaGroupsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        replica_groups: List[main_models.DescribeDiskReplicaGroupsResponseBodyReplicaGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A pagination token.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The information about the replication pair-consistent groups.
        self.replica_groups = replica_groups
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.replica_groups:
            for v1 in self.replica_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ReplicaGroups'] = []
        if self.replica_groups is not None:
            for k1 in self.replica_groups:
                result['ReplicaGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.replica_groups = []
        if m.get('ReplicaGroups') is not None:
            for k1 in m.get('ReplicaGroups'):
                temp_model = main_models.DescribeDiskReplicaGroupsResponseBodyReplicaGroups()
                self.replica_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiskReplicaGroupsResponseBodyReplicaGroups(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        description: str = None,
        destination_region_id: str = None,
        destination_zone_id: str = None,
        enable_rtc: bool = None,
        group_name: str = None,
        last_recover_point: int = None,
        pair_ids: List[bytes] = None,
        pair_number: int = None,
        primary_region: str = None,
        primary_zone: str = None,
        rpo: int = None,
        replica_group_id: str = None,
        resource_group_id: str = None,
        site: str = None,
        source_region_id: str = None,
        source_zone_id: str = None,
        standby_region: str = None,
        standby_zone: str = None,
        status: str = None,
        tags: List[main_models.DescribeDiskReplicaGroupsResponseBodyReplicaGroupsTags] = None,
    ):
        # The bandwidth value. Unit: Kbit/s. This parameter is not publicly available and has a system-preset value.
        self.bandwidth = bandwidth
        # The description of the replication pair-consistent group.
        self.description = description
        # The ID of the region in which the secondary site is deployed.
        self.destination_region_id = destination_region_id
        # The ID of the zone in which the secondary site is deployed.
        self.destination_zone_id = destination_zone_id
        # Indicates whether to enable replication time control.
        self.enable_rtc = enable_rtc
        # The name of the replication pair-consistent group.
        self.group_name = group_name
        # The time when data was last replicated from the primary disks to the secondary disks in the replication pair-consistent group. The value of this parameter is a timestamp. Unit: seconds.
        self.last_recover_point = last_recover_point
        # The IDs of replication pairs that belong to the replication pair-consistent group.
        self.pair_ids = pair_ids
        # The number of replication pairs that belong to the replication pair-consistent group.
        self.pair_number = pair_number
        # The initial source region (primary region) of the replication pair-consistent group.
        self.primary_region = primary_region
        # The initial source zone (primary zone) of the replication pair-consistent group.
        self.primary_zone = primary_zone
        # The recovery point objective (RPO) of the replication pair-consistent group. Unit: seconds.
        self.rpo = rpo
        # The IDs of the replication pair-consistent groups.
        self.replica_group_id = replica_group_id
        # The ID of the resource group to which the replication pair-consistent group belongs.
        self.resource_group_id = resource_group_id
        # The type of the site from which the information about the replication pairs and replication pair-consistent group was obtained. Valid values:
        # 
        # *   production: primary site
        # *   backup: secondary site
        self.site = site
        # The ID of the region in which the primary site is deployed.
        self.source_region_id = source_region_id
        # The ID of the zone in which the primary site is deployed.
        self.source_zone_id = source_zone_id
        # The initial destination region (secondary region) of the replication pair-consistent group.
        self.standby_region = standby_region
        # The initial destination zone (secondary zone) of the replication pair-consistent group.
        self.standby_zone = standby_zone
        # The status of the replication pair-consistent group. Valid values:
        # 
        # *   invalid: The replication pair-consistent group is invalid, which indicates that abnormal replication pairs are present in the replication pair-consistent group.
        # *   creating: The replication pair-consistent group is being created.
        # *   created: The replication pair-consistent group was created.
        # *   create_failed: The replication pair-consistent group failed to be created.
        # *   manual_syncing: Data was being manually synchronized between the disks in the replication pair-consistent group. When data was being manually synchronized for the first time, the replication pair is in this state.
        # *   syncing: Data was being synchronized between the disks. When data is being asynchronously replicated from the primary disk to the secondary disk again in subsequent operations, the replication pair is in this state.
        # *   normal: The replication pair was working as expected. When the system finishes replicating data from the primary disk to the secondary disk within the current replication cycle, the replication pair enters this state.
        # *   stopping: The replication pair was being stopped.
        # *   stopped: The replication pair was stopped.
        # *   stop_failed: The replication pair failed to be stopped.
        # *   failovering: A failover was being performed.
        # *   failovered: A failover was performed.
        # *   failover_failed: A failover failed to be performed.
        # *   reprotecting: A reverse replication was being performed.
        # *   reprotect_failed: A reverse replication failed to be performed.
        # *   deleting: The replication pair was being deleted.
        # *   delete_failed: The replication pair failed to be deleted.
        # *   deleted: The replication pair was deleted.
        self.status = status
        # The tags of the replication pair-consistent group.
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
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id

        if self.enable_rtc is not None:
            result['EnableRtc'] = self.enable_rtc

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.last_recover_point is not None:
            result['LastRecoverPoint'] = self.last_recover_point

        if self.pair_ids is not None:
            result['PairIds'] = self.pair_ids

        if self.pair_number is not None:
            result['PairNumber'] = self.pair_number

        if self.primary_region is not None:
            result['PrimaryRegion'] = self.primary_region

        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone

        if self.rpo is not None:
            result['RPO'] = self.rpo

        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site is not None:
            result['Site'] = self.site

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id

        if self.standby_region is not None:
            result['StandbyRegion'] = self.standby_region

        if self.standby_zone is not None:
            result['StandbyZone'] = self.standby_zone

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')

        if m.get('EnableRtc') is not None:
            self.enable_rtc = m.get('EnableRtc')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LastRecoverPoint') is not None:
            self.last_recover_point = m.get('LastRecoverPoint')

        if m.get('PairIds') is not None:
            self.pair_ids = m.get('PairIds')

        if m.get('PairNumber') is not None:
            self.pair_number = m.get('PairNumber')

        if m.get('PrimaryRegion') is not None:
            self.primary_region = m.get('PrimaryRegion')

        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')

        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')

        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')

        if m.get('StandbyRegion') is not None:
            self.standby_region = m.get('StandbyRegion')

        if m.get('StandbyZone') is not None:
            self.standby_zone = m.get('StandbyZone')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDiskReplicaGroupsResponseBodyReplicaGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeDiskReplicaGroupsResponseBodyReplicaGroupsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the replication pair-consistent group.
        self.tag_key = tag_key
        # The tag value of the replication pair-consistent group.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

