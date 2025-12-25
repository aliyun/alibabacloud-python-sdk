# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_workorder20210610 import models as main_models
from darabonba.model import DaraModel

class ListTicketNotesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        data: List[main_models.ListTicketNotesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The return code of the request result.
        self.code = code
        # Return value, that is, the dialog record list data of the specified ticket
        self.data = data
        # The error message. If success is set to false, the message is returned.
        self.message = message
        # The unique ID of the API request. The requestID is unique for each call.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates that the call is normal.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListTicketNotesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTicketNotesResponseBodyData(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.ListTicketNotesResponseBodyDataAttachments] = None,
        create_time: int = None,
        dialog: main_models.ListTicketNotesResponseBodyDataDialog = None,
        dialog_id: int = None,
        status: int = None,
        tip: str = None,
        type: int = None,
        user: main_models.ListTicketNotesResponseBodyDataUser = None,
    ):
        # Attachment List
        self.attachments = attachments
        # The timestamp when the communication message was created.
        self.create_time = create_time
        # Work order communication record object
        self.dialog = dialog
        # The unique ID of the conversation record.
        self.dialog_id = dialog_id
        # Communication message status field, reference value Unread=1, Read=2
        self.status = status
        # Fields Not Used
        self.tip = tip
        # Conversation Type 1 card, that is, schema 2 Text, that is, content
        self.type = type
        # Conversation of users
        self.user = user

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()
        if self.dialog:
            self.dialog.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['Attachments'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dialog is not None:
            result['Dialog'] = self.dialog.to_map()

        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tip is not None:
            result['Tip'] = self.tip

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('Attachments') is not None:
            for k1 in m.get('Attachments'):
                temp_model = main_models.ListTicketNotesResponseBodyDataAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Dialog') is not None:
            temp_model = main_models.ListTicketNotesResponseBodyDataDialog()
            self.dialog = temp_model.from_map(m.get('Dialog'))

        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tip') is not None:
            self.tip = m.get('Tip')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            temp_model = main_models.ListTicketNotesResponseBodyDataUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class ListTicketNotesResponseBodyDataUser(DaraModel):
    def __init__(
        self,
        name: str = None,
        role: int = None,
    ):
        # Dialog User Name
        self.name = name
        # Dialogue user role, distinguish between agent and user.
        # 2 represents agent, 3 represents user.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

class ListTicketNotesResponseBodyDataDialog(DaraModel):
    def __init__(
        self,
        content: str = None,
        schema: str = None,
    ):
        # Work order communication content
        self.content = content
        # The ticket communication record system card will be used when the system card docking capability is opened in the future. At present, the content can be used to obtain plain text content.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

class ListTicketNotesResponseBodyDataAttachments(DaraModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        # Attachment Name
        self.name = name
        # Temporary Accessible Attachment Address
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

