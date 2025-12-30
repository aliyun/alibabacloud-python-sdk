# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListEditingProjectsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        project_list: List[main_models.ListEditingProjectsResponseBodyProjectList] = None,
        request_id: str = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The queried online editing projects.
        self.project_list = project_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.project_list:
            for v1 in self.project_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ProjectList'] = []
        if self.project_list is not None:
            for k1 in self.project_list:
                result['ProjectList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.project_list = []
        if m.get('ProjectList') is not None:
            for k1 in m.get('ProjectList'):
                temp_model = main_models.ListEditingProjectsResponseBodyProjectList()
                self.project_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEditingProjectsResponseBodyProjectList(DaraModel):
    def __init__(
        self,
        business_config: str = None,
        business_status: str = None,
        cover_url: str = None,
        create_source: str = None,
        create_time: str = None,
        description: str = None,
        error_code: str = None,
        error_message: str = None,
        modified_source: str = None,
        modified_time: str = None,
        project_id: str = None,
        project_type: str = None,
        status: str = None,
        template_type: str = None,
        title: str = None,
    ):
        # The business configuration of the project. This parameter can be ignored for general editing projects.
        self.business_config = business_config
        # The business status of the project. This parameter can be ignored for general editing projects.
        self.business_status = business_status
        # The thumbnail URL of the online editing project.
        self.cover_url = cover_url
        # The method for editing the online editing project. Valid values:
        # 
        # \\- OpenAPI
        # 
        # \\- AliyunConsole
        # 
        # \\- WebSDK
        self.create_source = create_source
        # The time when the online editing project was created.
        self.create_time = create_time
        # The description of the online editing project.
        self.description = description
        # The error code returned if the production of the online editing project failed.
        self.error_code = error_code
        # The error message returned if the production of the online editing project failed.
        self.error_message = error_message
        # The method for modifying the online editing project last time.
        self.modified_source = modified_source
        # The time when the online editing project was last modified.
        self.modified_time = modified_time
        # The ID of the online editing project.
        self.project_id = project_id
        # The type of the editing project. Valid values:
        # 
        # *   EditingProject: a regular editing project.
        # *   LiveEditingProject: a live stream editing project.
        self.project_type = project_type
        # The status of the online editing project. Valid values:
        # 
        # \\- Draft
        # 
        # \\- Editing
        # 
        # \\- Producing
        # 
        # \\- Produced
        # 
        # \\- ProduceFailed
        self.status = status
        # The template type. Valid values:
        # 
        # *   Timeline: a regular template.
        # *   VETemplate: an advanced template.
        self.template_type = template_type
        # The title of the online editing project.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_config is not None:
            result['BusinessConfig'] = self.business_config

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.create_source is not None:
            result['CreateSource'] = self.create_source

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_type is not None:
            result['ProjectType'] = self.project_type

        if self.status is not None:
            result['Status'] = self.status

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessConfig') is not None:
            self.business_config = m.get('BusinessConfig')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

