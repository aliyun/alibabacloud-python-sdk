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
        # The configurations returned in the response body.
        self.configs = configs
        # The current page number, which is the same as the PageNumber request parameter.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count
        # The total number of pages.
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
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. You can use this parameter to query global or rule configurations. Valid values:
        # 
        # - global: global configuration.
        # - rule: rule configuration.
        self.config_type = config_type
        # Specifies whether to enable gRPC. This feature is disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.grpc = grpc
        # Specifies whether to enable HTTP/2 back-to-origin. This feature is disabled by default. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.http_2origin = http_2origin
        # The rule content, which uses conditional expressions to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: set the value to true.
        # - Match specified requests: set the value to a custom expression, such as (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. Default value: 0.
        self.site_version = site_version
        # Specifies whether to enable the smart routing service. This feature is disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.smart_routing = smart_routing
        # The maximum upload file size, in MB. Valid values: 100 to 500.
        self.upload_max_filesize = upload_max_filesize
        # Specifies whether to enable WebSocket. This feature is enabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
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

