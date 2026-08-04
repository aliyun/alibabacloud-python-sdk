# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class GetAgAccountAkResponseBody(DaraModel):
    def __init__(
        self,
        account_ak_dto: main_models.GetAgAccountAkResponseBodyAccountAkDto = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.account_ak_dto = account_ak_dto
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.account_ak_dto:
            self.account_ak_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ak_dto is not None:
            result['AccountAkDto'] = self.account_ak_dto.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAkDto') is not None:
            temp_model = main_models.GetAgAccountAkResponseBodyAccountAkDto()
            self.account_ak_dto = temp_model.from_map(m.get('AccountAkDto'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAgAccountAkResponseBodyAccountAkDto(DaraModel):
    def __init__(
        self,
        ak: str = None,
        secret: str = None,
    ):
        self.ak = ak
        self.secret = secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak is not None:
            result['Ak'] = self.ak

        if self.secret is not None:
            result['Secret'] = self.secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')

        if m.get('Secret') is not None:
            self.secret = m.get('Secret')

        return self

