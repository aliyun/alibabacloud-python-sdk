# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetOpaClusterBaseLineListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetOpaClusterBaseLineListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The information about baselines.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetOpaClusterBaseLineListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOpaClusterBaseLineListResponseBodyData(DaraModel):
    def __init__(
        self,
        alias: str = None,
        class_key: str = None,
        item_key: str = None,
        name_key: str = None,
    ):
        # The alias of the baseline.
        self.alias = alias
        # The key of the baseline type.
        self.class_key = class_key
        # The key of the name for the baseline check item.
        self.item_key = item_key
        # The key of the name for the baseline.
        self.name_key = name_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.class_key is not None:
            result['ClassKey'] = self.class_key

        if self.item_key is not None:
            result['ItemKey'] = self.item_key

        if self.name_key is not None:
            result['NameKey'] = self.name_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('ClassKey') is not None:
            self.class_key = m.get('ClassKey')

        if m.get('ItemKey') is not None:
            self.item_key = m.get('ItemKey')

        if m.get('NameKey') is not None:
            self.name_key = m.get('NameKey')

        return self

