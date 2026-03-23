# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_workorder20200801 import models as main_models
from darabonba.model import DaraModel

class GetTicketResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        create_time: str = None,
        email: str = None,
        list: List[main_models.GetTicketResponseBodyList] = None,
        message: str = None,
        notify_time_range: str = None,
        phone: str = None,
        product_code: str = None,
        request_id: str = None,
        success: bool = None,
        ticket_id: str = None,
        ticket_status: str = None,
        title: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.create_time = create_time
        self.email = email
        self.list = list
        self.message = message
        self.notify_time_range = notify_time_range
        self.phone = phone
        self.product_code = product_code
        self.request_id = request_id
        self.success = success
        self.ticket_id = ticket_id
        self.ticket_status = ticket_status
        self.title = title

    def validate(self):
        if self.list:
            for v1 in self.list:
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.email is not None:
            result['Email'] = self.email

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.notify_time_range is not None:
            result['NotifyTimeRange'] = self.notify_time_range

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.ticket_status is not None:
            result['TicketStatus'] = self.ticket_status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetTicketResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NotifyTimeRange') is not None:
            self.notify_time_range = m.get('NotifyTimeRange')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('TicketStatus') is not None:
            self.ticket_status = m.get('TicketStatus')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self



class GetTicketResponseBodyList(DaraModel):
    def __init__(
        self,
        attach_list: List[str] = None,
        content: str = None,
        from_official: bool = None,
        gmt_created: str = None,
        note_id: str = None,
        special: bool = None,
    ):
        self.attach_list = attach_list
        self.content = content
        self.from_official = from_official
        self.gmt_created = gmt_created
        self.note_id = note_id
        self.special = special

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_list is not None:
            result['AttachList'] = self.attach_list

        if self.content is not None:
            result['Content'] = self.content

        if self.from_official is not None:
            result['FromOfficial'] = self.from_official

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.special is not None:
            result['Special'] = self.special

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachList') is not None:
            self.attach_list = m.get('AttachList')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FromOfficial') is not None:
            self.from_official = m.get('FromOfficial')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('Special') is not None:
            self.special = m.get('Special')

        return self

