# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class CheckAccountExistResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CheckAccountExistResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CheckAccountExistResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckAccountExistResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        nick_name: str = None,
        pk: str = None,
        result: bool = None,
    ):
        self.account_id = account_id
        self.nick_name = nick_name
        self.pk = pk
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

