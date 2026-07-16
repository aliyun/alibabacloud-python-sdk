# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBatchTemplateVersionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBatchTemplateVersionsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetBatchTemplateVersionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBatchTemplateVersionsResponseBodyData(DaraModel):
    def __init__(
        self,
        template_version_list: List[main_models.GetBatchTemplateVersionsResponseBodyDataTemplateVersionList] = None,
    ):
        self.template_version_list = template_version_list

    def validate(self):
        if self.template_version_list:
            for v1 in self.template_version_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TemplateVersionList'] = []
        if self.template_version_list is not None:
            for k1 in self.template_version_list:
                result['TemplateVersionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template_version_list = []
        if m.get('TemplateVersionList') is not None:
            for k1 in m.get('TemplateVersionList'):
                temp_model = main_models.GetBatchTemplateVersionsResponseBodyDataTemplateVersionList()
                self.template_version_list.append(temp_model.from_map(k1))

        return self

class GetBatchTemplateVersionsResponseBodyDataTemplateVersionList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content: str = None,
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
        version: int = None,
    ):
        self.comment = comment
        self.content = content
        self.description = description
        self.engine = engine
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.modifier = modifier
        self.modifier_id = modifier_id
        self.name = name
        self.operator_type = operator_type
        self.owner = owner
        self.owner_id = owner_id
        self.project_id = project_id
        self.status = status
        self.version = version

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

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Content') is not None:
            self.content = m.get('Content')

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

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

