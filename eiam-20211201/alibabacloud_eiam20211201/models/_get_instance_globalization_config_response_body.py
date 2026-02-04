# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceGlobalizationConfigResponseBody(DaraModel):
    def __init__(
        self,
        globalization_config: main_models.GetInstanceGlobalizationConfigResponseBodyGlobalizationConfig = None,
        request_id: str = None,
    ):
        self.globalization_config = globalization_config
        self.request_id = request_id

    def validate(self):
        if self.globalization_config:
            self.globalization_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.globalization_config is not None:
            result['GlobalizationConfig'] = self.globalization_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalizationConfig') is not None:
            temp_model = main_models.GetInstanceGlobalizationConfigResponseBodyGlobalizationConfig()
            self.globalization_config = temp_model.from_map(m.get('GlobalizationConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceGlobalizationConfigResponseBodyGlobalizationConfig(DaraModel):
    def __init__(
        self,
        language: str = None,
        time_zone: str = None,
    ):
        # 语言
        self.language = language
        # 时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

