# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataProcessJobRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_config: str = None,
        destination_id: str = None,
        destination_path: str = None,
        destination_type: str = None,
        model_name: str = None,
        processing_mode: str = None,
        region_id: str = None,
        source_config: str = None,
        source_id: str = None,
        source_path: str = None,
        source_type: str = None,
        template_id: str = None,
    ):
        # The description of the data processing task.
        self.description = description
        # The JSON string for the destination database connection configuration, including Account and Password.
        self.destination_config = destination_config
        # The ID of the destination PolarDB cluster.
        # 
        # This parameter is required.
        self.destination_id = destination_id
        # The name of the destination database.
        # 
        # This parameter is required.
        self.destination_path = destination_path
        # The type of the destination. Only PolarDB is supported.
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The name of the model used for feature extraction.
        self.model_name = model_name
        # The processing mode. Valid values: Full, Incremental, and Both.
        # 
        # This parameter is required.
        self.processing_mode = processing_mode
        # The ID of the region where the task resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The additional configuration for the data source in JSON string format. This parameter can be left empty.
        self.source_config = source_config
        # The ID of the PolarFS instance that serves as the data source.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The source data path in PolarFS. An empty string indicates the default path.
        # 
        # This parameter is required.
        self.source_path = source_path
        # The type of the data source. Only PolarFS is supported.
        # 
        # This parameter is required.
        self.source_type = source_type
        # The ID of the task template used to process data.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_config is not None:
            result['DestinationConfig'] = self.destination_config

        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.destination_path is not None:
            result['DestinationPath'] = self.destination_path

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.processing_mode is not None:
            result['ProcessingMode'] = self.processing_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_config is not None:
            result['SourceConfig'] = self.source_config

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_path is not None:
            result['SourcePath'] = self.source_path

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationConfig') is not None:
            self.destination_config = m.get('DestinationConfig')

        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('DestinationPath') is not None:
            self.destination_path = m.get('DestinationPath')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ProcessingMode') is not None:
            self.processing_mode = m.get('ProcessingMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceConfig') is not None:
            self.source_config = m.get('SourceConfig')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourcePath') is not None:
            self.source_path = m.get('SourcePath')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

