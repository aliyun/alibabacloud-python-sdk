# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class BindAxnResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_bind_dto: main_models.BindAxnResponseBodySecretBindDTO = None,
    ):
        # The status code of the request.
        # * A value of OK indicates that the request is successful.
        # * For other error codes, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The struct returned after the number is successfully bound.
        self.secret_bind_dto = secret_bind_dto

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

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

        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecretBindDTO') is not None:
            temp_model = main_models.BindAxnResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m.get('SecretBindDTO'))

        return self

class BindAxnResponseBodySecretBindDTO(DaraModel):
    def __init__(
        self,
        extension: str = None,
        secret_no: str = None,
        subs_id: str = None,
    ):
        # The extension number.
        # 
        # > The BindAxn operation does not involve extension numbers. Ignore this parameter.
        self.extension = extension
        # The privacy number, which is Number X.
        self.secret_no = secret_no
        # The ID of the binding relationship.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension

        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no

        if self.subs_id is not None:
            result['SubsId'] = self.subs_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')

        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')

        return self

