# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeClientConfSetupResponseBody(DaraModel):
    def __init__(
        self,
        client_conf: main_models.DescribeClientConfSetupResponseBodyClientConf = None,
        request_id: str = None,
    ):
        # The configurations of the Security Center agent.
        self.client_conf = client_conf
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.client_conf:
            self.client_conf.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_conf is not None:
            result['ClientConf'] = self.client_conf.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientConf') is not None:
            temp_model = main_models.DescribeClientConfSetupResponseBodyClientConf()
            self.client_conf = temp_model.from_map(m.get('ClientConf'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClientConfSetupResponseBodyClientConf(DaraModel):
    def __init__(
        self,
        config: str = None,
        strategy_tag: str = None,
        strategy_tag_value: str = None,
    ):
        # The configurations of the usage for the Security Center agent.
        self.config = config
        # The tag that is added to the configuration.
        self.strategy_tag = strategy_tag
        # The value of the tag. Valid values:
        # 
        # *   major
        # *   advanced
        # *   basic
        self.strategy_tag_value = strategy_tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.strategy_tag is not None:
            result['StrategyTag'] = self.strategy_tag

        if self.strategy_tag_value is not None:
            result['StrategyTagValue'] = self.strategy_tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('StrategyTag') is not None:
            self.strategy_tag = m.get('StrategyTag')

        if m.get('StrategyTagValue') is not None:
            self.strategy_tag_value = m.get('StrategyTagValue')

        return self

