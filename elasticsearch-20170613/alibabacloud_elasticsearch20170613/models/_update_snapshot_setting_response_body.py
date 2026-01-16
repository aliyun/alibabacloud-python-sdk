# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdateSnapshotSettingResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.UpdateSnapshotSettingResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return results.
        self.result = result

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.UpdateSnapshotSettingResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class UpdateSnapshotSettingResponseBodyResult(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        quartz_regex: str = None,
    ):
        # Specifies whether to enable automatic backup.
        self.enable = enable
        # The start time of automatic backup.
        self.quartz_regex = quartz_regex

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.quartz_regex is not None:
            result['quartzRegex'] = self.quartz_regex

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('quartzRegex') is not None:
            self.quartz_regex = m.get('quartzRegex')

        return self

