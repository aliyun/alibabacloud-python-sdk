# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListErrorPagesRedirectRulesResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListErrorPagesRedirectRulesResponseBodyConfigs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The error code redirection configurations.
        self.configs = configs
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 500. Valid values: 1 to 500.
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
                temp_model = main_models.ListErrorPagesRedirectRulesResponseBodyConfigs()
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

class ListErrorPagesRedirectRulesResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        error_pages_redirect: List[main_models.ListErrorPagesRedirectRulesResponseBodyConfigsErrorPagesRedirect] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. Valid values:
        # - global: Global configuration.
        # - rule: Rule configuration.
        self.config_type = config_type
        # The error code redirection.
        self.error_pages_redirect = error_pages_redirect
        # The rule content. Uses a conditional expression to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: Set the value to true.
        # - Match specific requests: Set the value to a custom expression, such as (http.host eq "video.example.com").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The execution order of the rule. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. Default value: 0.
        self.site_version = site_version

    def validate(self):
        if self.error_pages_redirect:
            for v1 in self.error_pages_redirect:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        result['ErrorPagesRedirect'] = []
        if self.error_pages_redirect is not None:
            for k1 in self.error_pages_redirect:
                result['ErrorPagesRedirect'].append(k1.to_map() if k1 else None)

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        self.error_pages_redirect = []
        if m.get('ErrorPagesRedirect') is not None:
            for k1 in m.get('ErrorPagesRedirect'):
                temp_model = main_models.ListErrorPagesRedirectRulesResponseBodyConfigsErrorPagesRedirect()
                self.error_pages_redirect.append(temp_model.from_map(k1))

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

        return self

class ListErrorPagesRedirectRulesResponseBodyConfigsErrorPagesRedirect(DaraModel):
    def __init__(
        self,
        status_code: str = None,
        target_url: str = None,
    ):
        # The response status code used by the node when responding to the client with a redirect address. Valid values:
        # - 400
        # - 403
        # - 404
        # - 405
        # - 414
        # - 416
        # - 500
        # - 501
        # - 502
        # - 503
        # - 504
        self.status_code = status_code
        # The target URL after redirection.
        self.target_url = target_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.target_url is not None:
            result['TargetURL'] = self.target_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TargetURL') is not None:
            self.target_url = m.get('TargetURL')

        return self

