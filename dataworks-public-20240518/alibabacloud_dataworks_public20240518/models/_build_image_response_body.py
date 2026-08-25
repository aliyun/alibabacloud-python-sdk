# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class BuildImageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.BuildImageResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result of the API request.
        self.data = data
        # The request ID, which is used for locating logs and troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.BuildImageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BuildImageResponseBodyData(DaraModel):
    def __init__(
        self,
        process_id: str = None,
        success: bool = None,
    ):
        # The image build execution ID.
        self.process_id = process_id
        # Indicates whether the build was triggered successfully.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

