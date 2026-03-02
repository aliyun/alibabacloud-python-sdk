# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeploymentsByLabelRequest(DaraModel):
    def __init__(
        self,
        ignore_job_summary: bool = None,
        ignore_resource_setting: bool = None,
        label_key: str = None,
        label_value: str = None,
    ):
        self.ignore_job_summary = ignore_job_summary
        self.ignore_resource_setting = ignore_resource_setting
        # This parameter is required.
        self.label_key = label_key
        # This parameter is required.
        self.label_value = label_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_job_summary is not None:
            result['ignoreJobSummary'] = self.ignore_job_summary

        if self.ignore_resource_setting is not None:
            result['ignoreResourceSetting'] = self.ignore_resource_setting

        if self.label_key is not None:
            result['labelKey'] = self.label_key

        if self.label_value is not None:
            result['labelValue'] = self.label_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ignoreJobSummary') is not None:
            self.ignore_job_summary = m.get('ignoreJobSummary')

        if m.get('ignoreResourceSetting') is not None:
            self.ignore_resource_setting = m.get('ignoreResourceSetting')

        if m.get('labelKey') is not None:
            self.label_key = m.get('labelKey')

        if m.get('labelValue') is not None:
            self.label_value = m.get('labelValue')

        return self

