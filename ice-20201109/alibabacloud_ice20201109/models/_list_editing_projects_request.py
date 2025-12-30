# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEditingProjectsRequest(DaraModel):
    def __init__(
        self,
        create_source: str = None,
        end_time: str = None,
        keyword: str = None,
        max_results: str = None,
        next_token: str = None,
        project_type: str = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        template_type: str = None,
    ):
        # The method for creating the online editing project. Valid values:
        # 
        # \\- OpenAPI
        # 
        # \\- AliyunConsole
        # 
        # \\- WebSDK
        self.create_source = create_source
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The search keyword. You can search by job ID.
        self.keyword = keyword
        # The number of entries per page. A maximum of 100 entries can be returned on each page.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The type of the editing project. Valid values:
        # 
        # *   EditingProject: a regular editing project.
        # *   LiveEditingProject: a live stream editing project.
        self.project_type = project_type
        # The order of sorting of the results. Valid values:
        # 
        # *   CreationTime:Desc (default): sorts the results in reverse chronological order.
        # *   CreationTime:Asc: sorts the results in chronological order.
        self.sort_by = sort_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The status of the online editing project. By default, online editing projects in all states are queried.
        self.status = status
        # The template type. This parameter is required if you create a template-based online editing project. Default value: Timeline.
        # 
        # *
        # *
        # 
        # Valid values:
        # 
        # *   Timeline: a regular template.
        # *   VETemplate: an advanced template.
        # *   None: general editing.
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

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

