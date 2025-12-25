# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_workorder20210610 import models as main_models
from darabonba.model import DaraModel

class GetAttachmentUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAttachmentUploadUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned after the call succeeds.
        self.data = data
        # The error message. If success is set to false, the message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates that the call is normal.
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
            temp_model = main_models.GetAttachmentUploadUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAttachmentUploadUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        get_signed_url: str = None,
        object_key: str = None,
        put_signed_url: str = None,
    ):
        # Query the signed URL of an OSS object
        self.get_signed_url = get_signed_url
        # Uploaded file identifier
        self.object_key = object_key
        # The signed URL used to upload the object to OSS.
        self.put_signed_url = put_signed_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_signed_url is not None:
            result['GetSignedUrl'] = self.get_signed_url

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.put_signed_url is not None:
            result['PutSignedUrl'] = self.put_signed_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetSignedUrl') is not None:
            self.get_signed_url = m.get('GetSignedUrl')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('PutSignedUrl') is not None:
            self.put_signed_url = m.get('PutSignedUrl')

        return self

