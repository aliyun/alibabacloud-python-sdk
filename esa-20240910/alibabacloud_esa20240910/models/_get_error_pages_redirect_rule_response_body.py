# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetErrorPagesRedirectRuleResponseBody(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        error_pages_redirect: List[main_models.GetErrorPagesRedirectRuleResponseBodyErrorPagesRedirect] = None,
        request_id: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
    ):
        # The ID of the configuration. You can call the [ListCompressionRules](https://help.aliyun.com/document_detail/2867498.html) operation to obtain the configuration ID.
        self.config_id = config_id
        # The configuration type. You can use this parameter to query global configurations or rule configurations. Valid values:
        # - global: queries global configurations
        # - rule: queries rule configurations
        # 
        # This parameter is optional. If you do not specify this parameter, global and rule configurations are not distinguished. This parameter takes effect only when the functionName parameter is specified.
        self.config_type = config_type
        # The error code redirect.
        self.error_pages_redirect = error_pages_redirect
        # The ID of the request.
        self.request_id = request_id
        # The rule content, which uses conditional expressions to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: Set the value to true.
        # - Match specific requests: Set the value to a custom expression, such as (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: enables the rule
        # - off: disables the rule
        self.rule_enable = rule_enable
        # The name of the rule. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The execution sequence of the rule. A smaller value indicates a higher priority.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.GetErrorPagesRedirectRuleResponseBodyErrorPagesRedirect()
                self.error_pages_redirect.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

class GetErrorPagesRedirectRuleResponseBodyErrorPagesRedirect(DaraModel):
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
        # The target URL after the redirect.
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

