# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListSaasInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSaasInfoResponseBodyData] = None,
        request_id: str = None,
        saas_token: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id
        self.saas_token = saas_token

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.saas_token is not None:
            result['SaasToken'] = self.saas_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSaasInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SaasToken') is not None:
            self.saas_token = m.get('SaasToken')

        return self

class ListSaasInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        en_name: str = None,
        name: str = None,
        service_url: str = None,
        url: str = None,
    ):
        self.code = code
        self.en_name = en_name
        self.name = name
        self.service_url = service_url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.name is not None:
            result['Name'] = self.name

        if self.service_url is not None:
            result['ServiceUrl'] = self.service_url

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServiceUrl') is not None:
            self.service_url = m.get('ServiceUrl')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

