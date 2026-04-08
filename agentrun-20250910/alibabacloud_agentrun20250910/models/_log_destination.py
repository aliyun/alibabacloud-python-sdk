# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class LogDestination(DaraModel):
    def __init__(
        self,
        sls_log_destination: main_models.SLSLogDestination = None,
    ):
        # 阿里云日志服务（SLS）的日志目标配置
        self.sls_log_destination = sls_log_destination

    def validate(self):
        if self.sls_log_destination:
            self.sls_log_destination.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sls_log_destination is not None:
            result['slsLogDestination'] = self.sls_log_destination.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('slsLogDestination') is not None:
            temp_model = main_models.SLSLogDestination()
            self.sls_log_destination = temp_model.from_map(m.get('slsLogDestination'))

        return self

