# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeApsJobDetailResponseBody(DaraModel):
    def __init__(
        self,
        apsjob_detail: main_models.DescribeApsJobDetailResponseBodyAPSJobDetail = None,
        request_id: str = None,
    ):
        # The queried job.
        self.apsjob_detail = apsjob_detail
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.apsjob_detail:
            self.apsjob_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apsjob_detail is not None:
            result['APSJobDetail'] = self.apsjob_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APSJobDetail') is not None:
            temp_model = main_models.DescribeApsJobDetailResponseBodyAPSJobDetail()
            self.apsjob_detail = temp_model.from_map(m.get('APSJobDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApsJobDetailResponseBodyAPSJobDetail(DaraModel):
    def __init__(
        self,
        db_list: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_region: str = None,
        partition_list: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_region: str = None,
        status: str = None,
        target_table_mode: str = None,
    ):
        # The objects that are synchronized.
        self.db_list = db_list
        # The ID of the destination cluster.
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        # The region of the destination cluster.
        self.destination_endpoint_region = destination_endpoint_region
        # The partitions.
        self.partition_list = partition_list
        # The ID of the source instance.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The region of the source instance.
        self.source_endpoint_region = source_endpoint_region
        # The status of the job.
        self.status = status
        # The mode of the destination table.
        self.target_table_mode = target_table_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_list is not None:
            result['DbList'] = self.db_list

        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id

        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region

        if self.partition_list is not None:
            result['PartitionList'] = self.partition_list

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        if self.status is not None:
            result['Status'] = self.status

        if self.target_table_mode is not None:
            result['TargetTableMode'] = self.target_table_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')

        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')

        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')

        if m.get('PartitionList') is not None:
            self.partition_list = m.get('PartitionList')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetTableMode') is not None:
            self.target_table_mode = m.get('TargetTableMode')

        return self

