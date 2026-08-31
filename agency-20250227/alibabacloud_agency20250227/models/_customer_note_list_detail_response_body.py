# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20250227 import models as main_models
from darabonba.model import DaraModel

class CustomerNoteListDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CustomerNoteListDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        # The access denied details returned by the POP API when RAM permissions are missing.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code returned by the POP API.
        self.http_status_code = http_status_code
        # The prompt message.
        self.message = message
        # The prompt message. This is the same as Message.
        self.msg = msg
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CustomerNoteListDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CustomerNoteListDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        ai_result: str = None,
        attachment: List[main_models.CustomerNoteListDetailResponseBodyDataAttachment] = None,
        contact_information: str = None,
        contact_name: str = None,
        creator: int = None,
        creator_name: str = None,
        customer_name: str = None,
        customer_uid: int = None,
        gmt_create: str = None,
        note_content: str = None,
        note_id: int = None,
        note_type: str = None,
        note_type_label: str = None,
        touch_date: str = None,
    ):
        # The AI parsing result (JSON string).
        self.ai_result = ai_result
        # The attachment list.
        self.attachment = attachment
        # The contact information.
        self.contact_information = contact_information
        # The contact name.
        self.contact_name = contact_name
        # The UID of the creator.
        self.creator = creator
        # The logon name of the creator.
        self.creator_name = creator_name
        # The customer name.
        self.customer_name = customer_name
        # The customer UID.
        self.customer_uid = customer_uid
        # The creation time in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_create = gmt_create
        # The note content.
        self.note_content = note_content
        # The note ID.
        self.note_id = note_id
        # The note type (CUSTOMER).
        self.note_type = note_type
        # The note type label.
        self.note_type_label = note_type_label
        # The touch date (timestamp).
        self.touch_date = touch_date

    def validate(self):
        if self.attachment:
            for v1 in self.attachment:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_result is not None:
            result['AiResult'] = self.ai_result

        result['Attachment'] = []
        if self.attachment is not None:
            for k1 in self.attachment:
                result['Attachment'].append(k1.to_map() if k1 else None)

        if self.contact_information is not None:
            result['ContactInformation'] = self.contact_information

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.note_content is not None:
            result['NoteContent'] = self.note_content

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.note_type is not None:
            result['NoteType'] = self.note_type

        if self.note_type_label is not None:
            result['NoteTypeLabel'] = self.note_type_label

        if self.touch_date is not None:
            result['TouchDate'] = self.touch_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiResult') is not None:
            self.ai_result = m.get('AiResult')

        self.attachment = []
        if m.get('Attachment') is not None:
            for k1 in m.get('Attachment'):
                temp_model = main_models.CustomerNoteListDetailResponseBodyDataAttachment()
                self.attachment.append(temp_model.from_map(k1))

        if m.get('ContactInformation') is not None:
            self.contact_information = m.get('ContactInformation')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('NoteContent') is not None:
            self.note_content = m.get('NoteContent')

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('NoteType') is not None:
            self.note_type = m.get('NoteType')

        if m.get('NoteTypeLabel') is not None:
            self.note_type_label = m.get('NoteTypeLabel')

        if m.get('TouchDate') is not None:
            self.touch_date = m.get('TouchDate')

        return self

class CustomerNoteListDetailResponseBodyDataAttachment(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        id: int = None,
        name: str = None,
        signature: str = None,
        size: int = None,
        type: str = None,
    ):
        # The attachment signature.
        self.download_url = download_url
        # The attachment ID.
        self.id = id
        # The attachment name.
        self.name = name
        # The attachment signature.
        self.signature = signature
        # The attachment size in bytes.
        self.size = size
        # The attachment type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

