# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainConfigsResponseBody(DaraModel):
    def __init__(
        self,
        domain_configs: List[main_models.DescribeVsDomainConfigsResponseBodyDomainConfigs] = None,
        request_id: str = None,
    ):
        self.domain_configs = domain_configs
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k1 in m.get('DomainConfigs'):
                temp_model = main_models.DescribeVsDomainConfigsResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVsDomainConfigsResponseBodyDomainConfigs(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        function_args: List[main_models.DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs] = None,
        function_name: str = None,
        status: str = None,
    ):
        self.config_id = config_id
        self.function_args = function_args
        self.function_name = function_name
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
                temp_model = main_models.DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k1))

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs(DaraModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        self.arg_name = arg_name
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

