# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class UpdatePersonalICodeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.UpdatePersonalICodeResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The AK model.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.UpdatePersonalICodeResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdatePersonalICodeResponseBodyResult(DaraModel):
    def __init__(
        self,
        icode: str = None,
        icode_key: str = None,
        type: int = None,
    ):
        # SK
        self.icode = icode
        # AK
        self.icode_key = icode_key
        # The AK type. Currently, only the value 1 is supported, which indicates a personal AK.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icode is not None:
            result['Icode'] = self.icode

        if self.icode_key is not None:
            result['IcodeKey'] = self.icode_key

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icode') is not None:
            self.icode = m.get('Icode')

        if m.get('IcodeKey') is not None:
            self.icode_key = m.get('IcodeKey')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

