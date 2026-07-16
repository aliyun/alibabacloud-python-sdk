# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetSiteTrafficSequenceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_sequences: List[main_models.GetSiteTrafficSequenceResponseBodyTrafficSequences] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The traffic sequences of the site.
        self.traffic_sequences = traffic_sequences

    def validate(self):
        if self.traffic_sequences:
            for v1 in self.traffic_sequences:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TrafficSequences'] = []
        if self.traffic_sequences is not None:
            for k1 in self.traffic_sequences:
                result['TrafficSequences'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.traffic_sequences = []
        if m.get('TrafficSequences') is not None:
            for k1 in m.get('TrafficSequences'):
                temp_model = main_models.GetSiteTrafficSequenceResponseBodyTrafficSequences()
                self.traffic_sequences.append(temp_model.from_map(k1))

        return self

class GetSiteTrafficSequenceResponseBodyTrafficSequences(DaraModel):
    def __init__(
        self,
        function_list: List[main_models.GetSiteTrafficSequenceResponseBodyTrafficSequencesFunctionList] = None,
        order: str = None,
        router: str = None,
        sequence_code: str = None,
        sequence_name: str = None,
    ):
        # The list of site features associated with the traffic sequence.
        self.function_list = function_list
        # The order of the current sequence in the entire traffic sequence.
        self.order = order
        # The traffic sequence routing.
        self.router = router
        # The sequence code.
        self.sequence_code = sequence_code
        # The sequence name.
        self.sequence_name = sequence_name

    def validate(self):
        if self.function_list:
            for v1 in self.function_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FunctionList'] = []
        if self.function_list is not None:
            for k1 in self.function_list:
                result['FunctionList'].append(k1.to_map() if k1 else None)

        if self.order is not None:
            result['Order'] = self.order

        if self.router is not None:
            result['Router'] = self.router

        if self.sequence_code is not None:
            result['SequenceCode'] = self.sequence_code

        if self.sequence_name is not None:
            result['SequenceName'] = self.sequence_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function_list = []
        if m.get('FunctionList') is not None:
            for k1 in m.get('FunctionList'):
                temp_model = main_models.GetSiteTrafficSequenceResponseBodyTrafficSequencesFunctionList()
                self.function_list.append(temp_model.from_map(k1))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Router') is not None:
            self.router = m.get('Router')

        if m.get('SequenceCode') is not None:
            self.sequence_code = m.get('SequenceCode')

        if m.get('SequenceName') is not None:
            self.sequence_name = m.get('SequenceName')

        return self

class GetSiteTrafficSequenceResponseBodyTrafficSequencesFunctionList(DaraModel):
    def __init__(
        self,
        configs: List[main_models.GetSiteTrafficSequenceResponseBodyTrafficSequencesFunctionListConfigs] = None,
        function_name: str = None,
        has_config: bool = None,
    ):
        # The list of configurations for the site feature associated with the traffic sequence.
        # 
        # This parameter is required.
        self.configs = configs
        # The feature name.
        self.function_name = function_name
        # Indicates whether the site has a corresponding configuration. Valid values:
        # - true: The site has a corresponding configuration.
        # - false: The site does not have a corresponding configuration.
        self.has_config = has_config

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.has_config is not None:
            result['HasConfig'] = self.has_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.GetSiteTrafficSequenceResponseBodyTrafficSequencesFunctionListConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('HasConfig') is not None:
            self.has_config = m.get('HasConfig')

        return self

class GetSiteTrafficSequenceResponseBodyTrafficSequencesFunctionListConfigs(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. Valid values:
        # - global: global configuration.
        # - rule: rule configuration.
        self.config_type = config_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        return self

