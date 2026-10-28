# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openagent20260801 import models as main_models
from darabonba.model import DaraModel

class GetReadonlyModeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetReadonlyModeResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetReadonlyModeResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetReadonlyModeResponseBodyData(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        exists: bool = None,
        gmt_update: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # The configuration name. The value is fixed to readonly.
        self.config_name = config_name
        # Indicates whether a configuration record exists.
        self.exists = exists
        # The last update time in ISO 8601 format. The value is null if no configuration record exists.
        self.gmt_update = gmt_update
        # The current effective read-only mode, returned as a string. A value of true indicates that the mode is enabled, and a value of false indicates that the mode is disabled. The value is true if not configured.
        self.value = value
        # The configuration value type. The value is fixed to BOOL.
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['configName'] = self.config_name

        if self.exists is not None:
            result['exists'] = self.exists

        if self.gmt_update is not None:
            result['gmtUpdate'] = self.gmt_update

        if self.value is not None:
            result['value'] = self.value

        if self.value_type is not None:
            result['valueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')

        if m.get('exists') is not None:
            self.exists = m.get('exists')

        if m.get('gmtUpdate') is not None:
            self.gmt_update = m.get('gmtUpdate')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')

        return self

