# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDIJobsRequest(DaraModel):
    def __init__(
        self,
        destination_data_source_type: str = None,
        job_name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        source_data_source_type: str = None,
    ):
        # The destination type. If you do not configure this parameter, no limits are imposed on the tasks.
        self.destination_data_source_type = destination_data_source_type
        # The name of the task. Fuzzy match is supported. If you do not configure this parameter, no limits are imposed on the tasks.
        self.job_name = job_name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The source type. If you do not configure this parameter, no limits are imposed on the tasks.
        self.source_data_source_type = source_data_source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')

        return self

