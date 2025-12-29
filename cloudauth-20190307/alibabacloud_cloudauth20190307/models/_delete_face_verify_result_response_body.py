# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DeleteFaceVerifyResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DeleteFaceVerifyResultResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DeleteFaceVerifyResultResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DeleteFaceVerifyResultResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        delete_result: str = None,
        fail_reason: str = None,
    ):
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Deletion result. Possible values are as follows:
        # 
        # - Y: Deletion successful.
        # - N: Deletion failed.
        self.delete_result = delete_result
        # Reason for deletion failure
        # 
        # - NOT_DELETE_REPEATEDLY: Cannot be deleted repeatedly
        # - NEED_QUERY_VERIFY_RESULT: Need to query the verification result first, then delete
        self.fail_reason = fail_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        return self

