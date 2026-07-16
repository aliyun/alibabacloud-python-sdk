# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class DeleteFaceRecordV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.DeleteFaceRecordV2ResponseBodyResult = None,
    ):
        # The return code.
        self.code = code
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The response result.
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
            temp_model = main_models.DeleteFaceRecordV2ResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DeleteFaceRecordV2ResponseBodyResult(DaraModel):
    def __init__(
        self,
        deleted: str = None,
        deleted_group_codes: str = None,
    ):
        # The deletion result. Valid values:
        # - Y: Succeeded.
        # - N: Failed.
        self.deleted = deleted
        # The list of face group codes from which the face data was actually deleted (comma-separated). This parameter is returned with all deleted group codes when FaceGroupCode is not specified.
        self.deleted_group_codes = deleted_group_codes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.deleted_group_codes is not None:
            result['DeletedGroupCodes'] = self.deleted_group_codes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('DeletedGroupCodes') is not None:
            self.deleted_group_codes = m.get('DeletedGroupCodes')

        return self

