# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ModifyHostsProjectResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.ModifyHostsProjectResponseBodyResults] = None,
        success_count: int = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The call results of the operation.
        self.results = results
        # The number of hosts that were successfully moved.
        self.success_count = success_count
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.ModifyHostsProjectResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ModifyHostsProjectResponseBodyResults(DaraModel):
    def __init__(
        self,
        asset_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # The host ID.
        self.asset_id = asset_id
        # The error code. A value of **200** indicates that the operation was successful. Other values indicate that the operation failed.
        self.code = code
        # The result message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

