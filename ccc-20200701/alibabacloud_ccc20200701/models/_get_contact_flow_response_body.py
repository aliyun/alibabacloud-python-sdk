# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetContactFlowResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetContactFlowResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetContactFlowResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetContactFlowResponseBodyData(DaraModel):
    def __init__(
        self,
        contact_flow_id: str = None,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        draft_id: str = None,
        editor: str = None,
        instance_id: str = None,
        name: str = None,
        published: bool = None,
        type: str = None,
        updated_time: str = None,
    ):
        self.contact_flow_id = contact_flow_id
        self.created_time = created_time
        self.definition = definition
        self.description = description
        self.draft_id = draft_id
        self.editor = editor
        self.instance_id = instance_id
        self.name = name
        self.published = published
        self.type = type
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.description is not None:
            result['Description'] = self.description

        if self.draft_id is not None:
            result['DraftId'] = self.draft_id

        if self.editor is not None:
            result['Editor'] = self.editor

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.published is not None:
            result['Published'] = self.published

        if self.type is not None:
            result['Type'] = self.type

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DraftId') is not None:
            self.draft_id = m.get('DraftId')

        if m.get('Editor') is not None:
            self.editor = m.get('Editor')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Published') is not None:
            self.published = m.get('Published')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

