# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListNetworkOptimizationsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListNetworkOptimizationsResponseBodyConfigs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # Response body configurations.
        self.configs = configs
        # The current page number.
        self.page_number = page_number
        # The size of the page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Total number of records.
        self.total_count = total_count
        # Total number of pages.
        self.total_page = total_page

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListNetworkOptimizationsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListNetworkOptimizationsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        grpc: str = None,
        http_2origin: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
        smart_routing: str = None,
        upload_max_filesize: str = None,
        websocket: str = None,
    ):
        # Configuration ID.
        self.config_id = config_id
        # Configuration type, which can be used to query global or rule-based configurations. The value range is as follows:
        # 
        # - global: Query global configuration.
        # - rule: Query rule-based configuration.
        self.config_type = config_type
        # Whether to enable GRPC, default is off. The value range is:
        # - on: enabled.
        # - off: disabled.
        self.grpc = grpc
        # Whether to enable HTTP2 origin, defaulting to off. The value range is as follows:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.http_2origin = http_2origin
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, e.g., (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. The value range is as follows:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        # Rule execution order. The smaller the value, the higher the priority.
        self.sequence = sequence
        # Site configuration version number. For sites with version management enabled, this parameter can specify the site version for which the configuration takes effect, defaulting to version 0.
        self.site_version = site_version
        # Whether to enable smart routing service, defaulting to off. The value range is as follows:
        # - on: Enabled.
        # - off: Disabled.
        self.smart_routing = smart_routing
        # Maximum file size for upload, in MB. The value range is 100 to 500.
        self.upload_max_filesize = upload_max_filesize
        # Whether to enable Websocket, enabled by default. Value range: 
        # - on: Enabled. 
        # - off: Disabled.
        self.websocket = websocket

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

        if self.grpc is not None:
            result['Grpc'] = self.grpc

        if self.http_2origin is not None:
            result['Http2Origin'] = self.http_2origin

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.smart_routing is not None:
            result['SmartRouting'] = self.smart_routing

        if self.upload_max_filesize is not None:
            result['UploadMaxFilesize'] = self.upload_max_filesize

        if self.websocket is not None:
            result['Websocket'] = self.websocket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Grpc') is not None:
            self.grpc = m.get('Grpc')

        if m.get('Http2Origin') is not None:
            self.http_2origin = m.get('Http2Origin')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('SmartRouting') is not None:
            self.smart_routing = m.get('SmartRouting')

        if m.get('UploadMaxFilesize') is not None:
            self.upload_max_filesize = m.get('UploadMaxFilesize')

        if m.get('Websocket') is not None:
            self.websocket = m.get('Websocket')

        return self

