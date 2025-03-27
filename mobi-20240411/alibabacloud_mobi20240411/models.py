# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CreateAppFromTemplateRequest(TeaModel):
    def __init__(
        self,
        actual_parameters: str = None,
        connections_content: str = None,
        databases_content: str = None,
        description: str = None,
        from_: str = None,
        icon: str = None,
        name: str = None,
        template_id: str = None,
        type: str = None,
        variables_content: str = None,
        workspace_id: str = None,
    ):
        self.actual_parameters = actual_parameters
        self.connections_content = connections_content
        self.databases_content = databases_content
        self.description = description
        self.from_ = from_
        # This parameter is required.
        self.icon = icon
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.template_id = template_id
        self.type = type
        self.variables_content = variables_content
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_parameters is not None:
            result['ActualParameters'] = self.actual_parameters
        if self.connections_content is not None:
            result['ConnectionsContent'] = self.connections_content
        if self.databases_content is not None:
            result['DatabasesContent'] = self.databases_content
        if self.description is not None:
            result['Description'] = self.description
        if self.from_ is not None:
            result['From'] = self.from_
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.type is not None:
            result['Type'] = self.type
        if self.variables_content is not None:
            result['VariablesContent'] = self.variables_content
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualParameters') is not None:
            self.actual_parameters = m.get('ActualParameters')
        if m.get('ConnectionsContent') is not None:
            self.connections_content = m.get('ConnectionsContent')
        if m.get('DatabasesContent') is not None:
            self.databases_content = m.get('DatabasesContent')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VariablesContent') is not None:
            self.variables_content = m.get('VariablesContent')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateAppFromTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon: str = None,
        name: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icon = icon
        self.name = name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateAppFromTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateAppFromTemplateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateAppFromTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppFromTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppFromTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppFromTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


