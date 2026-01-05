# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CheckMobilesCardSupportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CheckMobilesCardSupportResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.CheckMobilesCardSupportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CheckMobilesCardSupportResponseBodyData(DaraModel):
    def __init__(
        self,
        query_result: List[main_models.CheckMobilesCardSupportResponseBodyDataQueryResult] = None,
    ):
        # The list of returned results.
        self.query_result = query_result

    def validate(self):
        if self.query_result:
            for v1 in self.query_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['queryResult'] = []
        if self.query_result is not None:
            for k1 in self.query_result:
                result['queryResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_result = []
        if m.get('queryResult') is not None:
            for k1 in m.get('queryResult'):
                temp_model = main_models.CheckMobilesCardSupportResponseBodyDataQueryResult()
                self.query_result.append(temp_model.from_map(k1))

        return self

class CheckMobilesCardSupportResponseBodyDataQueryResult(DaraModel):
    def __init__(
        self,
        mobile: str = None,
        support: bool = None,
    ):
        # The mobile phone number.
        self.mobile = mobile
        # Indicates whether the mobile phone number supports card messages.
        # 
        # *   **true**
        # *   **false**
        self.support = support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile is not None:
            result['mobile'] = self.mobile

        if self.support is not None:
            result['support'] = self.support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')

        if m.get('support') is not None:
            self.support = m.get('support')

        return self

