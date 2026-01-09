# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class LogtailConfig(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        create_time: int = None,
        input_detail: Dict[str, Any] = None,
        input_type: str = None,
        last_modify_time: int = None,
        log_sample: str = None,
        output_detail: main_models.LogtailConfigOutputDetail = None,
        output_type: str = None,
    ):
        # This parameter is required.
        self.config_name = config_name
        self.create_time = create_time
        # This parameter is required.
        self.input_detail = input_detail
        # This parameter is required.
        self.input_type = input_type
        self.last_modify_time = last_modify_time
        self.log_sample = log_sample
        # This parameter is required.
        self.output_detail = output_detail
        # This parameter is required.
        self.output_type = output_type

    def validate(self):
        if self.output_detail:
            self.output_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['configName'] = self.config_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.input_detail is not None:
            result['inputDetail'] = self.input_detail

        if self.input_type is not None:
            result['inputType'] = self.input_type

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.log_sample is not None:
            result['logSample'] = self.log_sample

        if self.output_detail is not None:
            result['outputDetail'] = self.output_detail.to_map()

        if self.output_type is not None:
            result['outputType'] = self.output_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('inputDetail') is not None:
            self.input_detail = m.get('inputDetail')

        if m.get('inputType') is not None:
            self.input_type = m.get('inputType')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')

        if m.get('outputDetail') is not None:
            temp_model = main_models.LogtailConfigOutputDetail()
            self.output_detail = temp_model.from_map(m.get('outputDetail'))

        if m.get('outputType') is not None:
            self.output_type = m.get('outputType')

        return self

class LogtailConfigOutputDetail(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        logstore_name: str = None,
        region: str = None,
        telemetry_type: str = None,
    ):
        # This parameter is required.
        self.endpoint = endpoint
        # This parameter is required.
        self.logstore_name = logstore_name
        self.region = region
        self.telemetry_type = telemetry_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name

        if self.region is not None:
            result['region'] = self.region

        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')

        return self

