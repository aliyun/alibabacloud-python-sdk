# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class PushApplicationDataResponseBody(DaraModel):
    def __init__(
        self,
        push_results: main_models.PushApplicationDataResponseBodyPushResults = None,
        request_id: str = None,
    ):
        # The push results of data files.
        self.push_results = push_results
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.push_results:
            self.push_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_results is not None:
            result['PushResults'] = self.push_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResults') is not None:
            temp_model = main_models.PushApplicationDataResponseBodyPushResults()
            self.push_results = temp_model.from_map(m.get('PushResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PushApplicationDataResponseBodyPushResults(DaraModel):
    def __init__(
        self,
        push_result: List[main_models.PushApplicationDataResponseBodyPushResultsPushResult] = None,
    ):
        self.push_result = push_result

    def validate(self):
        if self.push_result:
            for v1 in self.push_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PushResult'] = []
        if self.push_result is not None:
            for k1 in self.push_result:
                result['PushResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_result = []
        if m.get('PushResult') is not None:
            for k1 in m.get('PushResult'):
                temp_model = main_models.PushApplicationDataResponseBodyPushResultsPushResult()
                self.push_result.append(temp_model.from_map(k1))

        return self

class PushApplicationDataResponseBodyPushResultsPushResult(DaraModel):
    def __init__(
        self,
        name: str = None,
        result_code: int = None,
        result_descrip: str = None,
        version: str = None,
    ):
        # The name of the data file.
        self.name = name
        # The push result. The value is of the enumeration type. Valid values:
        # 
        # *   0: The push operation is successful.
        # *   100: The push operation has been performed and the file is pushed.
        # *   200: The push operation has been performed and the file is being pushed to specific file servers.
        # *   300: The push operation failed. You must trigger the push operation again. The ResultDescrip parameter indicates the error description.
        self.result_code = result_code
        # The description of the push status.
        self.result_descrip = result_descrip
        # The version number of the data file.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_descrip is not None:
            result['ResultDescrip'] = self.result_descrip

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultDescrip') is not None:
            self.result_descrip = m.get('ResultDescrip')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

