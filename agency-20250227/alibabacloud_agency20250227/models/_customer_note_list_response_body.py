# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20250227 import models as main_models
from darabonba.model import DaraModel

class CustomerNoteListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CustomerNoteListResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.msg = msg
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
            temp_model = main_models.CustomerNoteListResponseBodyData()
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

class CustomerNoteListResponseBodyData(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.CustomerNoteListResponseBodyDataData] = None,
        http_status_code: int = None,
        message: str = None,
        msg: str = None,
        page_info: main_models.CustomerNoteListResponseBodyDataPageInfo = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.msg = msg
        self.page_info = page_info
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

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
                temp_model = main_models.CustomerNoteListResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PageInfo') is not None:
            temp_model = main_models.CustomerNoteListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class CustomerNoteListResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self



class CustomerNoteListResponseBodyDataData(DaraModel):
    def __init__(
        self,
        contact_name: str = None,
        creator: int = None,
        creator_name: str = None,
        gmt_create: str = None,
        note_content: str = None,
        note_id: int = None,
        note_type: str = None,
        note_type_label: str = None,
        touch_date: str = None,
    ):
        self.contact_name = contact_name
        self.creator = creator
        self.creator_name = creator_name
        self.gmt_create = gmt_create
        self.note_content = note_content
        self.note_id = note_id
        self.note_type = note_type
        self.note_type_label = note_type_label
        self.touch_date = touch_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

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
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

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

