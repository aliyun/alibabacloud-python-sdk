# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class SetCdnDomainStagingConfigResponseBody(DaraModel):
    def __init__(
        self,
        domain_config_list: List[main_models.SetCdnDomainStagingConfigResponseBodyDomainConfigList] = None,
        request_id: str = None,
    ):
        # The list of domain configurations.
        self.domain_config_list = domain_config_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_config_list:
            for v1 in self.domain_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainConfigList'] = []
        if self.domain_config_list is not None:
            for k1 in self.domain_config_list:
                result['DomainConfigList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_config_list = []
        if m.get('DomainConfigList') is not None:
            for k1 in m.get('DomainConfigList'):
                temp_model = main_models.SetCdnDomainStagingConfigResponseBodyDomainConfigList()
                self.domain_config_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SetCdnDomainStagingConfigResponseBodyDomainConfigList(DaraModel):
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

