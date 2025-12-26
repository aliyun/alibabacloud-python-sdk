# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class CredentialGetResultIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CredentialGetResultIntlResponseBodyResult = None,
    ):
        # Return code.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Return result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CredentialGetResultIntlResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CredentialGetResultIntlResponseBodyResult(DaraModel):
    def __init__(
        self,
        ext_id_info: str = None,
        status: str = None,
        sub_code: str = None,
    ):
        # Identified key information, in JSON format.
        self.ext_id_info = ext_id_info
        # Task status:
        # - PROCESSING: In progress (please continue polling)
        # - SUCCESS: Execution succeeded
        # - FAILED: Execution failed
        self.status = status
        # Authentication result description. For more information, see ResultObject.SubCode error codes.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        return self

