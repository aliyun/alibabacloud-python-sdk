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
        # Specifies whether to exclude job summary information, such as jobName and status, from the response. If set to true, the response includes only the JobId. This improves performance.
        self.ignore_job_summary = ignore_job_summary
        # Specifies whether to exclude resource configuration information, such as parallelism and the number of CUs, from the response. This reduces the size of the returned data.
        self.ignore_resource_setting = ignore_resource_setting
        # The label key used for filtering.
        # 
        # This parameter is required.
        self.label_key = label_key
        # The label value. You can specify multiple values separated by commas (,) to create an OR condition.
        # 
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

