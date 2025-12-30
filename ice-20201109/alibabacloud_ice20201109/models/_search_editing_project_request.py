# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchEditingProjectRequest(DaraModel):
    def __init__(
        self,
        create_source: str = None,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        project_type: str = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        template_type: str = None,
    ):
        # The source of the project.
        # 
        # \\-OpenAPI
        # 
        # \\-AliyunConsole
        # 
        # \\-WebSDK
        # 
        # Valid values:
        # 
        # *   AliyunConsole: The project is created in the Alibaba Cloud console.
        # *   WebSDK: The project is created by using the SDK for Web.
        # *   OpenAPI: The project is created by calling API operations.
        self.create_source = create_source
        # The end of the time range to query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Valid values: 1 to 100.
        self.page_size = page_size
        # The type of the editing project. Default value: EditingProject. Valid values:
        # 
        # *   EditingProject: a regular editing project.
        # *   LiveEditingProject: a live stream editing project.
        self.project_type = project_type
        # The sorting rule of results. Valid values:
        # 
        # \\- CreationTime:Desc (default): The results are sorted in reverse chronological order based on the creation time.
        # 
        # \\- CreationTime:Asc: The results are sorted in chronological order based on the creation time.
        self.sort_by = sort_by
        # The beginning of the time range to query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The status of the online editing project. Separate multiple values with commas (,). By default, all online editing projects are queried.
        # 
        # Valid values:
        # 
        # \\-Draft
        # 
        # \\-Producing
        # 
        # \\-Produced
        # 
        # \\-ProduceFailed
        self.status = status
        # The template type. Valid values:
        # 
        # \\-Timeline
        # 
        # \\-VETemplate
        # 
        # Valid values:
        # 
        # *   Timeline: regular template.
        # *   VETemplate: advanced template.
        # *   None: No template is used.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_source is not None:
            result['CreateSource'] = self.create_source

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_type is not None:
            result['ProjectType'] = self.project_type

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

