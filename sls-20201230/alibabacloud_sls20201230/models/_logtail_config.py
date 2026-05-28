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
        # The name of the Logtail configuration. The name must be unique in the project to which the Logtail configuration belongs. After the Logtail configuration is created, you cannot change the name of the Logtail configuration. The name must meet the following requirements:
        # 
        # *   The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 2 to 128 characters in length.
        # 
        # This parameter is required.
        self.config_name = config_name
        # The time at which the Logtail configuration was created. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The detailed settings of the data source. For more information, see [inputDetail](https://help.aliyun.com/document_detail/29058.html).
        # 
        # This parameter is required.
        self.input_detail = input_detail
        # The type of the data source. Valid values:
        # 
        # *   **plugin**: Logs such as MySQL binary logs are collected by using Logtail plug-ins.
        # *   **file**: Logs from text files are collected by using existing modes, including the full regex mode and delimiter mode.
        # 
        # This parameter is required.
        self.input_type = input_type
        # The time at which the Logtail configuration was last modified. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # The sample log.
        self.log_sample = log_sample
        # The detailed settings of the data destination. For more information, see [outputDetail](https://help.aliyun.com/document_detail/29058.html).
        # 
        # This parameter is required.
        self.output_detail = output_detail
        # The type of the data destination. Set the value to LogService. Collected logs can be uploaded to only Simple Log Service.
        # 
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
        # The endpoint. For more information, see [Endpoints](https://help.aliyun.com/document_detail/29008.html).
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The ID of the region.
        self.region = region
        # The type of observable data in the Logstore.
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

