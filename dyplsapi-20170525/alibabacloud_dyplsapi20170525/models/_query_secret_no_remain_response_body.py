# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySecretNoRemainResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_remain_dto: main_models.QuerySecretNoRemainResponseBodySecretRemainDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information returned after the operation was called.
        self.secret_remain_dto = secret_remain_dto

    def validate(self):
        if self.secret_remain_dto:
            self.secret_remain_dto.validate()

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

        if self.secret_remain_dto is not None:
            result['SecretRemainDTO'] = self.secret_remain_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecretRemainDTO') is not None:
            temp_model = main_models.QuerySecretNoRemainResponseBodySecretRemainDTO()
            self.secret_remain_dto = temp_model.from_map(m.get('SecretRemainDTO'))

        return self

class QuerySecretNoRemainResponseBodySecretRemainDTO(DaraModel):
    def __init__(
        self,
        amount: int = None,
        city: str = None,
        remain_dtolist: main_models.QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList = None,
    ):
        # The quantity of remaining phone numbers available for online purchase.
        self.amount = amount
        # The home location of the phone numbers.
        self.city = city
        self.remain_dtolist = remain_dtolist

    def validate(self):
        if self.remain_dtolist:
            self.remain_dtolist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.city is not None:
            result['City'] = self.city

        if self.remain_dtolist is not None:
            result['RemainDTOList'] = self.remain_dtolist.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('RemainDTOList') is not None:
            temp_model = main_models.QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList()
            self.remain_dtolist = temp_model.from_map(m.get('RemainDTOList'))

        return self

class QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList(DaraModel):
    def __init__(
        self,
        remain_dto: List[main_models.QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO] = None,
    ):
        self.remain_dto = remain_dto

    def validate(self):
        if self.remain_dto:
            for v1 in self.remain_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['remainDTO'] = []
        if self.remain_dto is not None:
            for k1 in self.remain_dto:
                result['remainDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remain_dto = []
        if m.get('remainDTO') is not None:
            for k1 in m.get('remainDTO'):
                temp_model = main_models.QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO()
                self.remain_dto.append(temp_model.from_map(k1))

        return self

class QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO(DaraModel):
    def __init__(
        self,
        amount: int = None,
        city: str = None,
    ):
        self.amount = amount
        self.city = city

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.city is not None:
            result['City'] = self.city

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('City') is not None:
            self.city = m.get('City')

        return self

