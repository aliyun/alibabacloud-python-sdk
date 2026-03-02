# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class BriefResourceSetting(DaraModel):
    def __init__(
        self,
        batch_resource_setting: main_models.BatchResourceSetting = None,
        flink_conf: Dict[str, Any] = None,
        streaming_resource_setting: main_models.StreamingResourceSetting = None,
    ):
        # The resource configuration for the deployment in batch mode. This parameter is required for a deployment in batch mode.
        self.batch_resource_setting = batch_resource_setting
        # The Realtime Compute for Apache Flink configuration.
        self.flink_conf = flink_conf
        # The resource configuration for the deployment in streaming mode. This parameter is required for a deployment in streaming mode.
        self.streaming_resource_setting = streaming_resource_setting

    def validate(self):
        if self.batch_resource_setting:
            self.batch_resource_setting.validate()
        if self.streaming_resource_setting:
            self.streaming_resource_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_resource_setting is not None:
            result['batchResourceSetting'] = self.batch_resource_setting.to_map()

        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf

        if self.streaming_resource_setting is not None:
            result['streamingResourceSetting'] = self.streaming_resource_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchResourceSetting') is not None:
            temp_model = main_models.BatchResourceSetting()
            self.batch_resource_setting = temp_model.from_map(m.get('batchResourceSetting'))

        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')

        if m.get('streamingResourceSetting') is not None:
            temp_model = main_models.StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m.get('streamingResourceSetting'))

        return self

