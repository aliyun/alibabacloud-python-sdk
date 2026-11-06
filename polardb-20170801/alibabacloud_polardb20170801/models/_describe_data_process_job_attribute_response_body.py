# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataProcessJobAttributeResponseBody(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        destination_config: str = None,
        destination_id: str = None,
        destination_path: str = None,
        destination_type: str = None,
        job_id: str = None,
        model_name: str = None,
        processing_mode: str = None,
        region_id: str = None,
        request_id: str = None,
        source_id: str = None,
        source_path: str = None,
        source_type: str = None,
        status: str = None,
        template_id: str = None,
        template_type: str = None,
    ):
        # The time when the task was created, in RFC 3339 format.
        self.creation_time = creation_time
        # The JSON string of the destination database connection configuration.
        self.destination_config = destination_config
        # The ID of the destination PolarDB cluster.
        self.destination_id = destination_id
        # The name of the destination database.
        self.destination_path = destination_path
        # The type of the destination. Currently, only PolarDB is supported.
        self.destination_type = destination_type
        # The ID of the data processing task.
        self.job_id = job_id
        # The name of the model used for feature extraction.
        self.model_name = model_name
        # The data processing mode. Valid values: Full, Incremental, and Both.
        self.processing_mode = processing_mode
        # The region ID of the region where the data processing task is located.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the source PolarFS instance.
        self.source_id = source_id
        # The source data path in PolarFS.
        self.source_path = source_path
        # The type of the data source. Currently, only PolarFS is supported.
        self.source_type = source_type
        # The status of the data processing task.
        self.status = status
        # The ID of the template used by the task.
        self.template_id = template_id
        # The node templatetype. Currently, only image is supported.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.destination_config is not None:
            result['DestinationConfig'] = self.destination_config

        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.destination_path is not None:
            result['DestinationPath'] = self.destination_path

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.processing_mode is not None:
            result['ProcessingMode'] = self.processing_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DestinationConfig') is not None:
            self.destination_config = m.get('DestinationConfig')

        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('DestinationPath') is not None:
            self.destination_path = m.get('DestinationPath')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ProcessingMode') is not None:
            self.processing_mode = m.get('ProcessingMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

