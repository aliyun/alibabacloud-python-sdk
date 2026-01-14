# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListAppBySwimmingLaneGroupTagsResponseBody(DaraModel):
    def __init__(
        self,
        data: Dict[str, List[main_models.DataValue]] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The additional request information.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = {}
        if self.data is not None:
            for k1, v1 in self.data.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['Data'][k1] = l1

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = {}
        if m.get('Data') is not None:
            for k1, v1 in m.get('Data').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DataValue()
                    l1.append(temp_model.from_map(k2))
                self.data[k1] = l1

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

