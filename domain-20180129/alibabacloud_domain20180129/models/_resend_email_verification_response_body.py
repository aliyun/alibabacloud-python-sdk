# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class ResendEmailVerificationResponseBody(DaraModel):
    def __init__(
        self,
        fail_list: List[main_models.ResendEmailVerificationResponseBodyFailList] = None,
        request_id: str = None,
        success_list: List[main_models.ResendEmailVerificationResponseBodySuccessList] = None,
    ):
        self.fail_list = fail_list
        self.request_id = request_id
        self.success_list = success_list

    def validate(self):
        if self.fail_list:
            for v1 in self.fail_list:
                 if v1:
                    v1.validate()
        if self.success_list:
            for v1 in self.success_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailList'] = []
        if self.fail_list is not None:
            for k1 in self.fail_list:
                result['FailList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SuccessList'] = []
        if self.success_list is not None:
            for k1 in self.success_list:
                result['SuccessList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_list = []
        if m.get('FailList') is not None:
            for k1 in m.get('FailList'):
                temp_model = main_models.ResendEmailVerificationResponseBodyFailList()
                self.fail_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.success_list = []
        if m.get('SuccessList') is not None:
            for k1 in m.get('SuccessList'):
                temp_model = main_models.ResendEmailVerificationResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k1))

        return self

class ResendEmailVerificationResponseBodySuccessList(DaraModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.email is not None:
            result['Email'] = self.email

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class ResendEmailVerificationResponseBodyFailList(DaraModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.email is not None:
            result['Email'] = self.email

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

