# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class ConfirmTransferInEmailResponseBody(DaraModel):
    def __init__(
        self,
        fail_list: main_models.ConfirmTransferInEmailResponseBodyFailList = None,
        request_id: str = None,
        success_list: main_models.ConfirmTransferInEmailResponseBodySuccessList = None,
    ):
        self.fail_list = fail_list
        self.request_id = request_id
        self.success_list = success_list

    def validate(self):
        if self.fail_list:
            self.fail_list.validate()
        if self.success_list:
            self.success_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_list is not None:
            result['FailList'] = self.fail_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_list is not None:
            result['SuccessList'] = self.success_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailList') is not None:
            temp_model = main_models.ConfirmTransferInEmailResponseBodyFailList()
            self.fail_list = temp_model.from_map(m.get('FailList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessList') is not None:
            temp_model = main_models.ConfirmTransferInEmailResponseBodySuccessList()
            self.success_list = temp_model.from_map(m.get('SuccessList'))

        return self

class ConfirmTransferInEmailResponseBodySuccessList(DaraModel):
    def __init__(
        self,
        success_domain: List[str] = None,
    ):
        self.success_domain = success_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.success_domain is not None:
            result['SuccessDomain'] = self.success_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccessDomain') is not None:
            self.success_domain = m.get('SuccessDomain')

        return self

class ConfirmTransferInEmailResponseBodyFailList(DaraModel):
    def __init__(
        self,
        fail_domain: List[str] = None,
    ):
        self.fail_domain = fail_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_domain is not None:
            result['FailDomain'] = self.fail_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailDomain') is not None:
            self.fail_domain = m.get('FailDomain')

        return self

