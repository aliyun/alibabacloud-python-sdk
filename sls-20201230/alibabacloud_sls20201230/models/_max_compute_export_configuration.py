# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class MaxComputeExportConfiguration(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        logstore: str = None,
        role_arn: str = None,
        sink: main_models.MaxComputeExportConfigurationSink = None,
        to_time: int = None,
    ):
        # This parameter is required.
        self.from_time = from_time
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.role_arn = role_arn
        # This parameter is required.
        self.sink = sink
        # This parameter is required.
        self.to_time = to_time

    def validate(self):
        if self.sink:
            self.sink.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.sink is not None:
            result['sink'] = self.sink.to_map()

        if self.to_time is not None:
            result['toTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('sink') is not None:
            temp_model = main_models.MaxComputeExportConfigurationSink()
            self.sink = temp_model.from_map(m.get('sink'))

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

