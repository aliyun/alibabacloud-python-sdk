# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnDomainStagingConfigResponseBody(DaraModel):
    def __init__(
        self,
        domain_configs: List[main_models.DescribeCdnDomainStagingConfigResponseBodyDomainConfigs] = None,
        domain_name: str = None,
        request_id: str = None,
    ):
        # The domain name configurations.
        self.domain_configs = domain_configs
        # The accelerated domain name.
        self.domain_name = domain_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_configs:
            for v1 in self.domain_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k1 in self.domain_configs:
                result['DomainConfigs'].append(k1.to_map() if k1 else None)

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k1 in m.get('DomainConfigs'):
                temp_model = main_models.DescribeCdnDomainStagingConfigResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k1))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnDomainStagingConfigResponseBodyDomainConfigs(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        function_args: List[main_models.DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs] = None,
        function_name: str = None,
        parent_id: str = None,
        status: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The description of each feature.
        self.function_args = function_args
        # The feature name.
        self.function_name = function_name
        # The rule condition ID. This parameter is optional. To create a rule condition, you can configure the **condition** feature that is described in the [Parameters for configuring features for domain names](https://help.aliyun.com/document_detail/388460.html) topic. A rule condition can identify parameters that are included in requests and filter requests based on the identified parameters. Each rule condition has a [ConfigId](https://help.aliyun.com/document_detail/388994.html). You can reference ConfigId instead of ParentId in other features. This way, you can combine rule conditions and features for flexible configurations. For more information, see [BatchSetCdnDomainConfig](https://help.aliyun.com/document_detail/90915.html) or ParentId configuration example in this topic.
        self.parent_id = parent_id
        # The configuration status. Valid values:
        # 
        # *   **testing**
        # *   **configuring**
        # *   **success**
        # *   **failed**
        self.status = status

    def validate(self):
        if self.function_args:
            for v1 in self.function_args:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        result['FunctionArgs'] = []
        if self.function_args is not None:
            for k1 in self.function_args:
                result['FunctionArgs'].append(k1.to_map() if k1 else None)

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        self.function_args = []
        if m.get('FunctionArgs') is not None:
            for k1 in m.get('FunctionArgs'):
                temp_model = main_models.DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k1))

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs(DaraModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        # The configuration name.
        self.arg_name = arg_name
        # The configuration value.
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name

        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')

        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')

        return self

