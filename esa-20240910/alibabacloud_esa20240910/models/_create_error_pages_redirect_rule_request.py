# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateErrorPagesRedirectRuleRequest(DaraModel):
    def __init__(
        self,
        error_pages_redirect: List[main_models.CreateErrorPagesRedirectRuleRequestErrorPagesRedirect] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The error code redirect configuration.
        # 
        # This parameter is required.
        self.error_pages_redirect = error_pages_redirect
        # The rule content, which uses conditional expressions to match user requests. You do not need to specify this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: Set the value to true.
        # - Match specific requests: Set the value to a custom expression, such as (http.host eq "video.example.com").
        self.rule = rule
        # Specifies whether to enable the rule. You do not need to specify this parameter when adding a global configuration. Valid values:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # The name of the rule. You do not need to specify this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The execution sequence of the rule. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The ID of the site. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version to which the configuration applies. Default value: 0.
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

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_pages_redirect = []
        if m.get('ErrorPagesRedirect') is not None:
            for k1 in m.get('ErrorPagesRedirect'):
                temp_model = main_models.CreateErrorPagesRedirectRuleRequestErrorPagesRedirect()
                self.error_pages_redirect.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

class CreateErrorPagesRedirectRuleRequestErrorPagesRedirect(DaraModel):
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
        # 
        # This parameter is required.
        self.status_code = status_code
        # The target URL after redirection.
        # 
        # This parameter is required.
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

