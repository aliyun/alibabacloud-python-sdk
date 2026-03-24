# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeUserConfigsResponseBody(DaraModel):
    def __init__(
        self,
        configs: main_models.DescribeUserConfigsResponseBodyConfigs = None,
        request_id: str = None,
    ):
        # The configurations of the specified feature.
        self.configs = configs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            temp_model = main_models.DescribeUserConfigsResponseBodyConfigs()
            self.configs = temp_model.from_map(m.get('Configs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserConfigsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        oss_log_config: main_models.DescribeUserConfigsResponseBodyConfigsOssLogConfig = None,
        waf_config: main_models.DescribeUserConfigsResponseBodyConfigsWafConfig = None,
    ):
        # The configurations of Object Storage Service (OSS).
        self.oss_log_config = oss_log_config
        # The configurations of Web Application Firewall (WAF).
        self.waf_config = waf_config

    def validate(self):
        if self.oss_log_config:
            self.oss_log_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_log_config is not None:
            result['OssLogConfig'] = self.oss_log_config.to_map()

        if self.waf_config is not None:
            result['WafConfig'] = self.waf_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssLogConfig') is not None:
            temp_model = main_models.DescribeUserConfigsResponseBodyConfigsOssLogConfig()
            self.oss_log_config = temp_model.from_map(m.get('OssLogConfig'))

        if m.get('WafConfig') is not None:
            temp_model = main_models.DescribeUserConfigsResponseBodyConfigsWafConfig()
            self.waf_config = temp_model.from_map(m.get('WafConfig'))

        return self

class DescribeUserConfigsResponseBodyConfigsWafConfig(DaraModel):
    def __init__(
        self,
        enable: str = None,
    ):
        # Indicates whether WAF is enabled.
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

class DescribeUserConfigsResponseBodyConfigsOssLogConfig(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        enable: str = None,
        prefix: str = None,
    ):
        # The name of the bucket.
        self.bucket = bucket
        # Indicates whether the OSS bucket is enabled.
        self.enable = enable
        # The prefix.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        return self

