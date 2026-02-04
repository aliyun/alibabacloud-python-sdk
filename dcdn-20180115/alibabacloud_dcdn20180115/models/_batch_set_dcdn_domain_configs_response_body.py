# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class BatchSetDcdnDomainConfigsResponseBody(DaraModel):
    def __init__(
        self,
        domain_config_list: main_models.BatchSetDcdnDomainConfigsResponseBodyDomainConfigList = None,
        request_id: str = None,
    ):
        # The list of domain configurations.
        self.domain_config_list = domain_config_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_config_list:
            self.domain_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_config_list is not None:
            result['DomainConfigList'] = self.domain_config_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainConfigList') is not None:
            temp_model = main_models.BatchSetDcdnDomainConfigsResponseBodyDomainConfigList()
            self.domain_config_list = temp_model.from_map(m.get('DomainConfigList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchSetDcdnDomainConfigsResponseBodyDomainConfigList(DaraModel):
    def __init__(
        self,
        domain_config_model: List[main_models.BatchSetDcdnDomainConfigsResponseBodyDomainConfigListDomainConfigModel] = None,
    ):
        self.domain_config_model = domain_config_model

    def validate(self):
        if self.domain_config_model:
            for v1 in self.domain_config_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainConfigModel'] = []
        if self.domain_config_model is not None:
            for k1 in self.domain_config_model:
                result['DomainConfigModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_config_model = []
        if m.get('DomainConfigModel') is not None:
            for k1 in m.get('DomainConfigModel'):
                temp_model = main_models.BatchSetDcdnDomainConfigsResponseBodyDomainConfigListDomainConfigModel()
                self.domain_config_model.append(temp_model.from_map(k1))

        return self

class BatchSetDcdnDomainConfigsResponseBodyDomainConfigListDomainConfigModel(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        domain_name: str = None,
        function_name: str = None,
    ):
        # The ID of the configuration.
        self.config_id = config_id
        # The domain name.
        self.domain_name = domain_name
        # The name of the feature.
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        return self

