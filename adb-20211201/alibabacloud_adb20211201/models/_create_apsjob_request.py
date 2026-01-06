# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAPSJobRequest(DaraModel):
    def __init__(
        self,
        aps_job_name: str = None,
        db_list: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_password: str = None,
        destination_endpoint_user_name: str = None,
        partition_list: str = None,
        region_id: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_password: str = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
        target_table_mode: str = None,
    ):
        # The name of the synchronization job.
        # 
        # This parameter is required.
        self.aps_job_name = aps_job_name
        # The objects to be synchronized.
        # 
        # This parameter is required.
        self.db_list = db_list
        # The name of the database account of the destination cluster.
        # 
        # This parameter is required.
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        # The password of the database account of the destination cluster.
        self.destination_endpoint_password = destination_endpoint_password
        # The name of the database account of the destination cluster.
        self.destination_endpoint_user_name = destination_endpoint_user_name
        # The partitions.
        self.partition_list = partition_list
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the source instance or cluster.
        # 
        # This parameter is required.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The password of the database account of the source instance.
        self.source_endpoint_password = source_endpoint_password
        # The region ID of the source instance.
        self.source_endpoint_region = source_endpoint_region
        # The name of the database account of the source instance.
        self.source_endpoint_user_name = source_endpoint_user_name
        # The mode of the destination table.
        self.target_table_mode = target_table_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aps_job_name is not None:
            result['ApsJobName'] = self.aps_job_name

        if self.db_list is not None:
            result['DbList'] = self.db_list

        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id

        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password

        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name

        if self.partition_list is not None:
            result['PartitionList'] = self.partition_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name

        if self.target_table_mode is not None:
            result['TargetTableMode'] = self.target_table_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsJobName') is not None:
            self.aps_job_name = m.get('ApsJobName')

        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')

        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')

        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')

        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')

        if m.get('PartitionList') is not None:
            self.partition_list = m.get('PartitionList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')

        if m.get('TargetTableMode') is not None:
            self.target_table_mode = m.get('TargetTableMode')

        return self

