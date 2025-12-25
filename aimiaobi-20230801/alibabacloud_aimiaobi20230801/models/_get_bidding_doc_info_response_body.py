# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetBiddingDocInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBiddingDocInfoResponseBodyData = None,
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
            temp_model = main_models.GetBiddingDocInfoResponseBodyData()
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

class GetBiddingDocInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_format: str = None,
        content_type: str = None,
        status: int = None,
        step: str = None,
        task_id: str = None,
        tender_doc_url: str = None,
        tender_file_type: str = None,
    ):
        self.content = content
        self.content_format = content_format
        self.content_type = content_type
        self.status = status
        self.step = step
        self.task_id = task_id
        self.tender_doc_url = tender_doc_url
        self.tender_file_type = tender_file_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_format is not None:
            result['ContentFormat'] = self.content_format

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.status is not None:
            result['Status'] = self.status

        if self.step is not None:
            result['Step'] = self.step

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tender_doc_url is not None:
            result['TenderDocUrl'] = self.tender_doc_url

        if self.tender_file_type is not None:
            result['TenderFileType'] = self.tender_file_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentFormat') is not None:
            self.content_format = m.get('ContentFormat')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TenderDocUrl') is not None:
            self.tender_doc_url = m.get('TenderDocUrl')

        if m.get('TenderFileType') is not None:
            self.tender_file_type = m.get('TenderFileType')

        return self

