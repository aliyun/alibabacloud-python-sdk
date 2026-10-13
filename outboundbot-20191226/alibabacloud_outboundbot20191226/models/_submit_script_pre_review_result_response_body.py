# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class SubmitScriptPreReviewResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        script: main_models.SubmitScriptPreReviewResultResponseBodyScript = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message returned by the API operation.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The script information for which the pre-review result is submitted.
        self.script = script
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.script:
            self.script.validate()

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

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.success is not None:
            result['Success'] = self.success

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

        if m.get('Script') is not None:
            temp_model = main_models.SubmitScriptPreReviewResultResponseBodyScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SubmitScriptPreReviewResultResponseBodyScript(DaraModel):
    def __init__(
        self,
        script_description: str = None,
        script_id: str = None,
        script_name: str = None,
    ):
        # The script description.
        self.script_description = script_description
        # The script ID.
        self.script_id = script_id
        # The script name.
        self.script_name = script_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        return self

