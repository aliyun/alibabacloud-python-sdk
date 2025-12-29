# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListTicketsResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        page: main_models.ListTicketsResponseBodyPage = None,
        request_id: str = None,
        result: List[main_models.ListTicketsResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Page') is not None:
            temp_model = main_models.ListTicketsResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListTicketsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class ListTicketsResponseBodyResult(DaraModel):
    def __init__(
        self,
        action: bool = None,
        assigned_handler: str = None,
        charges_remark: str = None,
        complete_remark: str = None,
        dialogs: List[main_models.ListTicketsResponseBodyResultDialogs] = None,
        gmt_called: str = None,
        gmt_create: str = None,
        gmt_delayed: str = None,
        gmt_modified: str = None,
        group_key: str = None,
        id: int = None,
        is_accepted_charges: bool = None,
        is_delayed: bool = None,
        is_need_callback: bool = None,
        is_need_charges: bool = None,
        operations: List[Dict[str, Any]] = None,
        remark: str = None,
        room_no: str = None,
        status: str = None,
        type: str = None,
    ):
        self.action = action
        self.assigned_handler = assigned_handler
        self.charges_remark = charges_remark
        self.complete_remark = complete_remark
        self.dialogs = dialogs
        self.gmt_called = gmt_called
        self.gmt_create = gmt_create
        self.gmt_delayed = gmt_delayed
        self.gmt_modified = gmt_modified
        self.group_key = group_key
        self.id = id
        self.is_accepted_charges = is_accepted_charges
        self.is_delayed = is_delayed
        self.is_need_callback = is_need_callback
        self.is_need_charges = is_need_charges
        self.operations = operations
        self.remark = remark
        self.room_no = room_no
        self.status = status
        self.type = type

    def validate(self):
        if self.dialogs:
            for v1 in self.dialogs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.assigned_handler is not None:
            result['AssignedHandler'] = self.assigned_handler

        if self.charges_remark is not None:
            result['ChargesRemark'] = self.charges_remark

        if self.complete_remark is not None:
            result['CompleteRemark'] = self.complete_remark

        result['Dialogs'] = []
        if self.dialogs is not None:
            for k1 in self.dialogs:
                result['Dialogs'].append(k1.to_map() if k1 else None)

        if self.gmt_called is not None:
            result['GmtCalled'] = self.gmt_called

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_delayed is not None:
            result['GmtDelayed'] = self.gmt_delayed

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_key is not None:
            result['GroupKey'] = self.group_key

        if self.id is not None:
            result['Id'] = self.id

        if self.is_accepted_charges is not None:
            result['IsAcceptedCharges'] = self.is_accepted_charges

        if self.is_delayed is not None:
            result['IsDelayed'] = self.is_delayed

        if self.is_need_callback is not None:
            result['IsNeedCallback'] = self.is_need_callback

        if self.is_need_charges is not None:
            result['IsNeedCharges'] = self.is_need_charges

        if self.operations is not None:
            result['Operations'] = self.operations

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('AssignedHandler') is not None:
            self.assigned_handler = m.get('AssignedHandler')

        if m.get('ChargesRemark') is not None:
            self.charges_remark = m.get('ChargesRemark')

        if m.get('CompleteRemark') is not None:
            self.complete_remark = m.get('CompleteRemark')

        self.dialogs = []
        if m.get('Dialogs') is not None:
            for k1 in m.get('Dialogs'):
                temp_model = main_models.ListTicketsResponseBodyResultDialogs()
                self.dialogs.append(temp_model.from_map(k1))

        if m.get('GmtCalled') is not None:
            self.gmt_called = m.get('GmtCalled')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtDelayed') is not None:
            self.gmt_delayed = m.get('GmtDelayed')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsAcceptedCharges') is not None:
            self.is_accepted_charges = m.get('IsAcceptedCharges')

        if m.get('IsDelayed') is not None:
            self.is_delayed = m.get('IsDelayed')

        if m.get('IsNeedCallback') is not None:
            self.is_need_callback = m.get('IsNeedCallback')

        if m.get('IsNeedCharges') is not None:
            self.is_need_charges = m.get('IsNeedCharges')

        if m.get('Operations') is not None:
            self.operations = m.get('Operations')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListTicketsResponseBodyResultDialogs(DaraModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
    ):
        self.answer = answer
        self.question = question

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.question is not None:
            result['Question'] = self.question

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        return self

class ListTicketsResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

