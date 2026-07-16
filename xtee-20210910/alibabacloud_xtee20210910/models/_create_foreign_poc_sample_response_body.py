# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class CreateForeignPocSampleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.CreateForeignPocSampleResponseBodyResultObject = None,
    ):
        # Status code.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Return Result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.CreateForeignPocSampleResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class CreateForeignPocSampleResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        has_warnings: bool = None,
        sample_id: int = None,
        sample_name: str = None,
        tab: str = None,
        warning_message: str = None,
    ):
        # Indicates whether validation warnings exist.
        self.has_warnings = has_warnings
        # Sample ID.
        self.sample_id = sample_id
        # Sample Name.
        self.sample_name = sample_name
        # Scenario.
        self.tab = tab
        # Warning summary.
        self.warning_message = warning_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_warnings is not None:
            result['HasWarnings'] = self.has_warnings

        if self.sample_id is not None:
            result['SampleId'] = self.sample_id

        if self.sample_name is not None:
            result['SampleName'] = self.sample_name

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.warning_message is not None:
            result['WarningMessage'] = self.warning_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasWarnings') is not None:
            self.has_warnings = m.get('HasWarnings')

        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')

        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('WarningMessage') is not None:
            self.warning_message = m.get('WarningMessage')

        return self

