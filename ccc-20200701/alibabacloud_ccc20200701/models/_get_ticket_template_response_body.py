# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetTicketTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTicketTemplateResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
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

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTicketTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTicketTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        editor: str = None,
        instance_id: str = None,
        name: str = None,
        process_definition: str = None,
        state: str = None,
        template_id: str = None,
        ticket_fields: List[main_models.GetTicketTemplateResponseBodyDataTicketFields] = None,
        updated_time: int = None,
    ):
        self.category_id = category_id
        self.editor = editor
        self.instance_id = instance_id
        self.name = name
        self.process_definition = process_definition
        self.state = state
        self.template_id = template_id
        self.ticket_fields = ticket_fields
        self.updated_time = updated_time

    def validate(self):
        if self.ticket_fields:
            for v1 in self.ticket_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.editor is not None:
            result['Editor'] = self.editor

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.process_definition is not None:
            result['ProcessDefinition'] = self.process_definition

        if self.state is not None:
            result['State'] = self.state

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        result['TicketFields'] = []
        if self.ticket_fields is not None:
            for k1 in self.ticket_fields:
                result['TicketFields'].append(k1.to_map() if k1 else None)

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Editor') is not None:
            self.editor = m.get('Editor')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProcessDefinition') is not None:
            self.process_definition = m.get('ProcessDefinition')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.ticket_fields = []
        if m.get('TicketFields') is not None:
            for k1 in m.get('TicketFields'):
                temp_model = main_models.GetTicketTemplateResponseBodyDataTicketFields()
                self.ticket_fields.append(temp_model.from_map(k1))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class GetTicketTemplateResponseBodyDataTicketFields(DaraModel):
    def __init__(
        self,
        array: bool = None,
        attributes: str = None,
        created_time: int = None,
        creator: str = None,
        data_type: str = None,
        description: str = None,
        disabled: bool = None,
        display_name: str = None,
        display_order: int = None,
        editor_type: str = None,
        max_length: int = None,
        maximum: float = None,
        min_length: int = None,
        minimum: float = None,
        name: str = None,
        pattern: str = None,
        pattern_error_message: str = None,
        read_only: bool = None,
        required: bool = None,
        system: bool = None,
        updated_time: int = None,
    ):
        self.array = array
        self.attributes = attributes
        self.created_time = created_time
        self.creator = creator
        self.data_type = data_type
        self.description = description
        self.disabled = disabled
        self.display_name = display_name
        self.display_order = display_order
        self.editor_type = editor_type
        self.max_length = max_length
        self.maximum = maximum
        self.min_length = min_length
        self.minimum = minimum
        self.name = name
        self.pattern = pattern
        self.pattern_error_message = pattern_error_message
        self.read_only = read_only
        self.required = required
        self.system = system
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array is not None:
            result['Array'] = self.array

        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_order is not None:
            result['DisplayOrder'] = self.display_order

        if self.editor_type is not None:
            result['EditorType'] = self.editor_type

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.maximum is not None:
            result['Maximum'] = self.maximum

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        if self.minimum is not None:
            result['Minimum'] = self.minimum

        if self.name is not None:
            result['Name'] = self.name

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.pattern_error_message is not None:
            result['PatternErrorMessage'] = self.pattern_error_message

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.required is not None:
            result['Required'] = self.required

        if self.system is not None:
            result['System'] = self.system

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')

        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayOrder') is not None:
            self.display_order = m.get('DisplayOrder')

        if m.get('EditorType') is not None:
            self.editor_type = m.get('EditorType')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('PatternErrorMessage') is not None:
            self.pattern_error_message = m.get('PatternErrorMessage')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('System') is not None:
            self.system = m.get('System')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

