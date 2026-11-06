# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDataProcessJobsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDataProcessJobsResponseBodyItems] = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # The list of data processing jobs.
        self.items = items
        # The current page number.
        self.page_number = page_number
        # The number of jobs returned on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of jobs that match the query conditions.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDataProcessJobsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDataProcessJobsResponseBodyItems(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        destination_id: str = None,
        destination_path: str = None,
        destination_type: str = None,
        job_id: str = None,
        processing_mode: str = None,
        region_id: str = None,
        source_id: str = None,
        source_path: str = None,
        source_type: str = None,
        status: str = None,
        template_id: str = None,
    ):
        # The time when the job was created, in RFC 3339 format.
        self.creation_time = creation_time
        # The description of the data processing job.
        self.description = description
        # The ID of the destination PolarDB cluster.
        self.destination_id = destination_id
        # The name of the destination database.
        self.destination_path = destination_path
        # The type of the destination. Currently, only PolarDB is supported.
        self.destination_type = destination_type
        # The ID of the data processing job.
        self.job_id = job_id
        # The data processing mode. Valid values: Full, Incremental, and Both.
        self.processing_mode = processing_mode
        # The ID of the region where the data processing job resides.
        self.region_id = region_id
        # The ID of the source PolarFS instance.
        self.source_id = source_id
        # The source data path in PolarFS.
        self.source_path = source_path
        # The type of the data source. Currently, only PolarFS is supported.
        self.source_type = source_type
        # The status of the data processing job.
        self.status = status
        # The ID of the template used by the job.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.destination_path is not None:
            result['DestinationPath'] = self.destination_path

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.processing_mode is not None:
            result['ProcessingMode'] = self.processing_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_path is not None:
            result['SourcePath'] = self.source_path

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('DestinationPath') is not None:
            self.destination_path = m.get('DestinationPath')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ProcessingMode') is not None:
            self.processing_mode = m.get('ProcessingMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourcePath') is not None:
            self.source_path = m.get('SourcePath')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

