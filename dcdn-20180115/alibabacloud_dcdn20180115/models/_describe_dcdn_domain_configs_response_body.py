# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainConfigsResponseBody(DaraModel):
    def __init__(
        self,
        domain_configs: main_models.DescribeDcdnDomainConfigsResponseBodyDomainConfigs = None,
        request_id: str = None,
    ):
        # The configurations of the domain name.
        self.domain_configs = domain_configs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainConfigs') is not None:
            temp_model = main_models.DescribeDcdnDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m.get('DomainConfigs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnDomainConfigsResponseBodyDomainConfigs(DaraModel):
    def __init__(
        self,
        domain_config: List[main_models.DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig] = None,
    ):
        self.domain_config = domain_config

    def validate(self):
        if self.domain_config:
            for v1 in self.domain_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainConfig'] = []
        if self.domain_config is not None:
            for k1 in self.domain_config:
                result['DomainConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_config = []
        if m.get('DomainConfig') is not None:
            for k1 in m.get('DomainConfig'):
                temp_model = main_models.DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        function_args: main_models.DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs = None,
        function_name: str = None,
        parent_id: str = None,
        status: str = None,
    ):
        # The ID of the configuration.
        self.config_id = config_id
        # The configurations of the features.
        self.function_args = function_args
        # The feature name.
        self.function_name = function_name
        # The ID of the advanced condition configuration.
        self.parent_id = parent_id
        # The status of the configuration. Valid values:
        # 
        # *   **success**: successful
        # *   **testing**: testing
        # *   **failed**: The configuration failed.
        # *   **configuring**: The configuration is in progress.
        self.status = status

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()

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

        if m.get('FunctionArgs') is not None:
            temp_model = main_models.DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m.get('FunctionArgs'))

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(DaraModel):
    def __init__(
        self,
        function_arg: List[main_models.DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg] = None,
    ):
        self.function_arg = function_arg

    def validate(self):
        if self.function_arg:
            for v1 in self.function_arg:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k1 in self.function_arg:
                result['FunctionArg'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k1 in m.get('FunctionArg'):
                temp_model = main_models.DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(DaraModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        # The name of the configuration.
        self.arg_name = arg_name
        # The value of the configuration.
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

