# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotSettingResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeSnapshotSettingResponseBodyResult = None,
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
            temp_model = main_models.DescribeSnapshotSettingResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeSnapshotSettingResponseBodyResult(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        quartz_regex: str = None,
    ):
        # Whether to enable automatic backup.
        self.enable = enable
        # Automatic backup time configuration, using Quartz Cron expression.
        self.quartz_regex = quartz_regex

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.quartz_regex is not None:
            result['QuartzRegex'] = self.quartz_regex

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('QuartzRegex') is not None:
            self.quartz_regex = m.get('QuartzRegex')

        return self

