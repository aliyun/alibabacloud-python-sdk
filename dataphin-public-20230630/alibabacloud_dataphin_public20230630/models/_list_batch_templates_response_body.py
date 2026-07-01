# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListBatchTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListBatchTemplatesResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The paged query result.
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListBatchTemplatesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListBatchTemplatesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        template_list: List[main_models.ListBatchTemplatesResponseBodyPageResultTemplateList] = None,
        total_count: int = None,
    ):
        # The list of template records.
        self.template_list = template_list
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.template_list:
            for v1 in self.template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TemplateList'] = []
        if self.template_list is not None:
            for k1 in self.template_list:
                result['TemplateList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template_list = []
        if m.get('TemplateList') is not None:
            for k1 in m.get('TemplateList'):
                temp_model = main_models.ListBatchTemplatesResponseBodyPageResultTemplateList()
                self.template_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBatchTemplatesResponseBodyPageResultTemplateList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content: str = None,
        current_version: int = None,
        description: str = None,
        engine: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        modifier: str = None,
        modifier_id: str = None,
        name: str = None,
        operator_type: int = None,
        owner: str = None,
        owner_id: str = None,
        project_id: int = None,
        status: str = None,
    ):
        # The template submission comment.
        self.comment = comment
        # The template content.
        self.content = content
        # The current latest version.
        self.current_version = current_version
        # The template description.
        self.description = description
        # The compute engine version. Currently supported Python versions: Python 2.7 and Python 3.7.
        self.engine = engine
        # The template creation time. Format: yyyy-MM-dd HH:mm:ss.
        self.gmt_create = gmt_create
        # The template update time. Format: yyyy-MM-dd HH:mm:ss.
        self.gmt_modified = gmt_modified
        # The template ID, which is the same as the menu tree node ID.
        self.id = id
        # The last modifier of the template.
        self.modifier = modifier
        # The ID of the last modifier of the template.
        self.modifier_id = modifier_id
        # The template name.
        self.name = name
        # The node type. Valid values: 10 (Shell) and 21 (Python).
        self.operator_type = operator_type
        # The template owner.
        self.owner = owner
        # The template owner ID.
        self.owner_id = owner_id
        # The project ID.
        self.project_id = project_id
        # The template status. Valid values: 0 (draft), 2 (submitted), and 100 (in development).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.content is not None:
            result['Content'] = self.content

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.description is not None:
            result['Description'] = self.description

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

