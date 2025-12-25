# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetSmartAuditResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSmartAuditResultResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            temp_model = main_models.GetSmartAuditResultResponseBodyData()
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

class GetSmartAuditResultResponseBodyData(DaraModel):
    def __init__(
        self,
        error_item_details: List[main_models.GetSmartAuditResultResponseBodyDataErrorItemDetails] = None,
        error_message: str = None,
        status: str = None,
    ):
        self.error_item_details = error_item_details
        self.error_message = error_message
        self.status = status

    def validate(self):
        if self.error_item_details:
            for v1 in self.error_item_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorItemDetails'] = []
        if self.error_item_details is not None:
            for k1 in self.error_item_details:
                result['ErrorItemDetails'].append(k1.to_map() if k1 else None)

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_item_details = []
        if m.get('ErrorItemDetails') is not None:
            for k1 in m.get('ErrorItemDetails'):
                temp_model = main_models.GetSmartAuditResultResponseBodyDataErrorItemDetails()
                self.error_item_details.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetSmartAuditResultResponseBodyDataErrorItemDetails(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        context: str = None,
        context_offset: int = None,
        error_level: int = None,
        error_word: str = None,
        major_code: str = None,
        major_code_desc: str = None,
        offset: int = None,
        reason: str = None,
        right_word: str = None,
        sub_class_code: str = None,
        sub_class_desc: str = None,
        url: str = None,
    ):
        self.check_id = check_id
        self.context = context
        self.context_offset = context_offset
        self.error_level = error_level
        self.error_word = error_word
        self.major_code = major_code
        self.major_code_desc = major_code_desc
        self.offset = offset
        self.reason = reason
        self.right_word = right_word
        self.sub_class_code = sub_class_code
        self.sub_class_desc = sub_class_desc
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.context is not None:
            result['Context'] = self.context

        if self.context_offset is not None:
            result['ContextOffset'] = self.context_offset

        if self.error_level is not None:
            result['ErrorLevel'] = self.error_level

        if self.error_word is not None:
            result['ErrorWord'] = self.error_word

        if self.major_code is not None:
            result['MajorCode'] = self.major_code

        if self.major_code_desc is not None:
            result['MajorCodeDesc'] = self.major_code_desc

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.right_word is not None:
            result['RightWord'] = self.right_word

        if self.sub_class_code is not None:
            result['SubClassCode'] = self.sub_class_code

        if self.sub_class_desc is not None:
            result['SubClassDesc'] = self.sub_class_desc

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('ContextOffset') is not None:
            self.context_offset = m.get('ContextOffset')

        if m.get('ErrorLevel') is not None:
            self.error_level = m.get('ErrorLevel')

        if m.get('ErrorWord') is not None:
            self.error_word = m.get('ErrorWord')

        if m.get('MajorCode') is not None:
            self.major_code = m.get('MajorCode')

        if m.get('MajorCodeDesc') is not None:
            self.major_code_desc = m.get('MajorCodeDesc')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RightWord') is not None:
            self.right_word = m.get('RightWord')

        if m.get('SubClassCode') is not None:
            self.sub_class_code = m.get('SubClassCode')

        if m.get('SubClassDesc') is not None:
            self.sub_class_desc = m.get('SubClassDesc')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

