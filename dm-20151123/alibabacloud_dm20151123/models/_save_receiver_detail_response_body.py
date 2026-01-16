# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class SaveReceiverDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SaveReceiverDetailResponseBodyData = None,
        error_count: int = None,
        request_id: str = None,
        success_count: int = None,
    ):
        # List of recipient addresses that failed to upload.
        self.data = data
        # Number of errors.
        self.error_count = error_count
        # Request ID
        self.request_id = request_id
        # Number of successes.
        self.success_count = success_count

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

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SaveReceiverDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

class SaveReceiverDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        detail: List[main_models.SaveReceiverDetailResponseBodyDataDetail] = None,
    ):
        self.detail = detail

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.SaveReceiverDetailResponseBodyDataDetail()
                self.detail.append(temp_model.from_map(k1))

        return self

class SaveReceiverDetailResponseBodyDataDetail(DaraModel):
    def __init__(
        self,
        email: str = None,
        err_message: str = None,
    ):
        # Recipient address.
        self.email = email
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        return self

