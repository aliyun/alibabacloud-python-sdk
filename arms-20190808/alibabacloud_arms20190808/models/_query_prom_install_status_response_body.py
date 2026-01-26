# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class QueryPromInstallStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryPromInstallStatusResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned struct.
        self.data = data
        # The request ID.
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
            temp_model = main_models.QueryPromInstallStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryPromInstallStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        is_controller_installed: bool = None,
    ):
        # Indicates whether the call was successful. Valid values:
        # 
        # true: The call was successful. false: The call fails.
        self.is_controller_installed = is_controller_installed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_controller_installed is not None:
            result['isControllerInstalled'] = self.is_controller_installed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isControllerInstalled') is not None:
            self.is_controller_installed = m.get('isControllerInstalled')

        return self

