# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetCanTrySasResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCanTrySasResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The detailed information.
        self.data = data
        # The message. The value is the same as the Code parameter value.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the current API call is successful. This does not indicate whether subsequent business operations are successful.
        # 
        # - **true**: Successful.
        # - **false**: Failed.
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

        if m.get('Data') is not None:
            temp_model = main_models.GetCanTrySasResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCanTrySasResponseBodyData(DaraModel):
    def __init__(
        self,
        body: main_models.GetCanTrySasResponseBodyDataBody = None,
    ):
        # The message body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.GetCanTrySasResponseBodyDataBody()
            self.body = temp_model.from_map(m.get('Body'))

        return self

class GetCanTrySasResponseBodyDataBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCanTrySasResponseBodyDataBodyData = None,
        request_id: str = None,
    ):
        # The data.
        self.data = data
        # Id of the request
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
            temp_model = main_models.GetCanTrySasResponseBodyDataBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCanTrySasResponseBodyDataBodyData(DaraModel):
    def __init__(
        self,
        can_try: int = None,
        can_try_versions: List[int] = None,
        try_type: int = None,
    ):
        # Indicates whether the user is eligible for a free trial. Valid values:
        # - **1**: Eligible.
        # - **0**: Not eligible.
        self.can_try = can_try
        # The list of editions available for trial.
        self.can_try_versions = can_try_versions
        # The trial type. Valid values:
        # - **0**: Trial is not allowed.
        # - **1**: First trial.
        # - **2**: Second trial.
        self.try_type = try_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_try is not None:
            result['CanTry'] = self.can_try

        if self.can_try_versions is not None:
            result['CanTryVersions'] = self.can_try_versions

        if self.try_type is not None:
            result['TryType'] = self.try_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanTry') is not None:
            self.can_try = m.get('CanTry')

        if m.get('CanTryVersions') is not None:
            self.can_try_versions = m.get('CanTryVersions')

        if m.get('TryType') is not None:
            self.try_type = m.get('TryType')

        return self

