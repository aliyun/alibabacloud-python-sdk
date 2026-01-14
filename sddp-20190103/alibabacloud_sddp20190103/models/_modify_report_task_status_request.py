# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyReportTaskStatusRequest(DaraModel):
    def __init__(
        self,
        feature_type: int = None,
        lang: str = None,
        report_task_status: int = None,
    ):
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang
        # Specifies the status of the report task. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # 
        # > This parameter is required.
        self.report_task_status = report_task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.report_task_status is not None:
            result['ReportTaskStatus'] = self.report_task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ReportTaskStatus') is not None:
            self.report_task_status = m.get('ReportTaskStatus')

        return self

