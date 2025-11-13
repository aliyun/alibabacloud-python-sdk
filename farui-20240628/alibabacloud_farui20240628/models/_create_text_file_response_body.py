# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class CreateTextFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateTextFileResponseBodyData = None,
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
            temp_model = main_models.CreateTextFileResponseBodyData()
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



class CreateTextFileResponseBodyData(DaraModel):
    def __init__(
        self,
        contract_id: str = None,
        text_file_id: str = None,
        text_file_name: str = None,
        text_file_url: str = None,
    ):
        self.contract_id = contract_id
        self.text_file_id = text_file_id
        self.text_file_name = text_file_name
        self.text_file_url = text_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contract_id is not None:
            result['ContractId'] = self.contract_id

        if self.text_file_id is not None:
            result['TextFileId'] = self.text_file_id

        if self.text_file_name is not None:
            result['TextFileName'] = self.text_file_name

        if self.text_file_url is not None:
            result['TextFileUrl'] = self.text_file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContractId') is not None:
            self.contract_id = m.get('ContractId')

        if m.get('TextFileId') is not None:
            self.text_file_id = m.get('TextFileId')

        if m.get('TextFileName') is not None:
            self.text_file_name = m.get('TextFileName')

        if m.get('TextFileUrl') is not None:
            self.text_file_url = m.get('TextFileUrl')

        return self

