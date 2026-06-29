# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListCompressionRulesResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListCompressionRulesResponseBodyConfigs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The list of compression rule configurations.
        self.configs = configs
        # The current page number, which is the same as the PageNumber request parameter.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
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
                temp_model = main_models.ListCompressionRulesResponseBodyConfigs()
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

class ListCompressionRulesResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        brotli: str = None,
        config_id: int = None,
        config_type: str = None,
        gzip: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
        zstd: str = None,
    ):
        # Brotli compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.brotli = brotli
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. Valid values:
        # - global: global configuration.
        # - rule: rule configuration.
        self.config_type = config_type
        # Gzip compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.gzip = gzip
        # The rule content, which uses a conditional expression to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: Set the value to true.
        # - Match specified requests: Set the value to a custom expression, for example, (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The version number of the site configuration. For sites with version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. Default value: 0.
        self.site_version = site_version
        # Zstd compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.zstd = zstd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brotli is not None:
            result['Brotli'] = self.brotli

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.gzip is not None:
            result['Gzip'] = self.gzip

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

        if self.zstd is not None:
            result['Zstd'] = self.zstd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brotli') is not None:
            self.brotli = m.get('Brotli')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')

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

        if m.get('Zstd') is not None:
            self.zstd = m.get('Zstd')

        return self

