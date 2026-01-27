# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskReplicaPairsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        replica_pairs: List[main_models.DescribeDiskReplicaPairsResponseBodyReplicaPairs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # Details of the replication pairs.
        self.replica_pairs = replica_pairs
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.replica_pairs:
            for v1 in self.replica_pairs:
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

        result['ReplicaPairs'] = []
        if self.replica_pairs is not None:
            for k1 in self.replica_pairs:
                result['ReplicaPairs'].append(k1.to_map() if k1 else None)

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

        self.replica_pairs = []
        if m.get('ReplicaPairs') is not None:
            for k1 in m.get('ReplicaPairs'):
                temp_model = main_models.DescribeDiskReplicaPairsResponseBodyReplicaPairs()
                self.replica_pairs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiskReplicaPairsResponseBodyReplicaPairs(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        charge_type: str = None,
        create_time: int = None,
        description: str = None,
        destination_disk_id: str = None,
        destination_region: str = None,
        destination_zone_id: str = None,
        enable_rtc: bool = None,
        expired_time: int = None,
        last_recover_point: int = None,
        pair_name: str = None,
        primary_region: str = None,
        primary_zone: str = None,
        rpo: int = None,
        replica_group_id: str = None,
        replica_group_name: str = None,
        replica_pair_id: str = None,
        resource_group_id: str = None,
        site: str = None,
        source_disk_id: str = None,
        source_region: str = None,
        source_zone_id: str = None,
        standby_region: str = None,
        standby_zone: str = None,
        status: str = None,
        status_message: str = None,
        tags: List[main_models.DescribeDiskReplicaPairsResponseBodyReplicaPairsTags] = None,
    ):
        # The bandwidth used to asynchronously replicate data from the primary disk to the secondary disk. Unit: Kbit/s.
        self.bandwidth = bandwidth
        # The billing method of the replication pair. Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        self.charge_type = charge_type
        # The time when the replication pair was created. The value of this parameter is a timestamp. Unit: seconds.
        self.create_time = create_time
        # The description of the replication pair.
        self.description = description
        # The ID of the secondary disk.
        self.destination_disk_id = destination_disk_id
        # The region ID of the secondary disk.
        self.destination_region = destination_region
        # The zone ID of the secondary disk.
        self.destination_zone_id = destination_zone_id
        # Whether the replication time control is enabled. If the replication pair has been added to a replication group, it is consistent with the attributes of the replication group.
        self.enable_rtc = enable_rtc
        # The time when the replication pair expires. The value of this parameter is a timestamp. Unit: seconds.
        self.expired_time = expired_time
        # The time when data was last replicated from the primary disk to the secondary disk in the replication pair. The value of this parameter is a timestamp. Unit: seconds. 86,400 seconds is equivalent to 24 hours.
        self.last_recover_point = last_recover_point
        # The name of the replication pair.
        self.pair_name = pair_name
        # The initial source region (primary region) of the replication pair.
        self.primary_region = primary_region
        # The initial source zone (primary zone) of the replication pair.
        self.primary_zone = primary_zone
        # The recovery point objective (RPO) of the replication pair. Unit: seconds.
        self.rpo = rpo
        # The ID of the replication pair-consistent group to which the replication pair belongs.
        self.replica_group_id = replica_group_id
        # The name of the replication pair-consistent group to which the replication pair belongs.
        self.replica_group_name = replica_group_name
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id
        # The ID of the resource group to which the replication pair belongs.
        self.resource_group_id = resource_group_id
        # The type of the site from which the information about the replication pairs and replication pair-consistent group was obtained. Valid values:
        # 
        # *   production: primary site
        # *   backup: secondary site
        self.site = site
        # The ID of the primary disk.
        self.source_disk_id = source_disk_id
        # The region ID of the primary disk.
        self.source_region = source_region
        # The zone ID of the primary disk.
        self.source_zone_id = source_zone_id
        # The initial destination region (secondary region) of the replication pair.
        self.standby_region = standby_region
        # The initial destination zone (secondary zone) of the replication pair.
        self.standby_zone = standby_zone
        # The status of the replication pair. Valid values:
        # 
        # *   invalid: The replication pair was invalid. When a replication pair becomes abnormal, it enters this state.
        # *   creating: The replication pair was being created.
        # *   created: The replication pair was created.
        # *   create_failed: The replication pair failed to be created.
        # *   initial_syncing: Data was synchronized from the primary disk to the secondary disk for the first time. After a replication pair is created and activated, the replication pair is in this state the first time data is synchronized from the primary disk to the secondary disk.
        # *   manual_syncing: Data was being manually synchronized from the primary disk to the secondary disk. After data is manually synchronized from the primary disk to the secondary disk, the replication pair returns to the stopped state. The first time data is manually synchronized from the primary disk to the secondary disk, the replication pair is in the manual_syncing state during the synchronization.
        # *   syncing: Data was being synchronized from the primary disk to the secondary disk. When data is being asynchronously replicated from the primary disk to the secondary disk again in subsequent operations, the replication pair is in this state.
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
        # The message that describes the state of the replication pair. This parameter has a value when `Status` has a value of invalid or `create_failed`. Valid values:
        # 
        # *   PrePayOrderExpired: The replication pair has expired.
        # *   PostPayOrderCeaseService: The pay-as-you-go replication pair has been stopped due to an overdue payment.
        # *   DeviceRemoved: The primary or secondary disk has been deleted.
        # *   DeviceKeyChanged: The `DeviceKey` mapping of the primary or secondary disk has changed.
        # *   DeviceSizeChanged: The `DeviceSize` value of the primary or secondary disk has changed.
        # *   OperationDenied.QuotaExceed: The maximum number of replication pairs that can be created has been reached.
        self.status_message = status_message
        # The tags of the replication pair.
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

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_disk_id is not None:
            result['DestinationDiskId'] = self.destination_disk_id

        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region

        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id

        if self.enable_rtc is not None:
            result['EnableRtc'] = self.enable_rtc

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.last_recover_point is not None:
            result['LastRecoverPoint'] = self.last_recover_point

        if self.pair_name is not None:
            result['PairName'] = self.pair_name

        if self.primary_region is not None:
            result['PrimaryRegion'] = self.primary_region

        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone

        if self.rpo is not None:
            result['RPO'] = self.rpo

        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id

        if self.replica_group_name is not None:
            result['ReplicaGroupName'] = self.replica_group_name

        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site is not None:
            result['Site'] = self.site

        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id

        if self.standby_region is not None:
            result['StandbyRegion'] = self.standby_region

        if self.standby_zone is not None:
            result['StandbyZone'] = self.standby_zone

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationDiskId') is not None:
            self.destination_disk_id = m.get('DestinationDiskId')

        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')

        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')

        if m.get('EnableRtc') is not None:
            self.enable_rtc = m.get('EnableRtc')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('LastRecoverPoint') is not None:
            self.last_recover_point = m.get('LastRecoverPoint')

        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')

        if m.get('PrimaryRegion') is not None:
            self.primary_region = m.get('PrimaryRegion')

        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')

        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')

        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')

        if m.get('ReplicaGroupName') is not None:
            self.replica_group_name = m.get('ReplicaGroupName')

        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')

        if m.get('StandbyRegion') is not None:
            self.standby_region = m.get('StandbyRegion')

        if m.get('StandbyZone') is not None:
            self.standby_zone = m.get('StandbyZone')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDiskReplicaPairsResponseBodyReplicaPairsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeDiskReplicaPairsResponseBodyReplicaPairsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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

