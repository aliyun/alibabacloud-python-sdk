# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule: main_models.DescribeDefenseRuleResponseBodyRule = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the protection rule.
        self.rule = rule

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rule') is not None:
            temp_model = main_models.DescribeDefenseRuleResponseBodyRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        return self

class DescribeDefenseRuleResponseBodyRule(DaraModel):
    def __init__(
        self,
        config: str = None,
        defense_origin: str = None,
        defense_scene: str = None,
        defense_type: str = None,
        gmt_modified: int = None,
        resource: str = None,
        rule_id: int = None,
        rule_name: str = None,
        status: int = None,
        template_id: int = None,
    ):
        # The configuration of the protection rule, returned as a JSON string. For more information, see the **Protection rule parameters** section in [CreateDefenseRule](https://help.aliyun.com/document_detail/461421.html).
        self.config = config
        # The origin of the protection rule. This parameter indicates whether the rule was created by the user or by the system. Valid values:
        # 
        # - **custom**: a custom rule.
        # 
        # - **system**: a system-generated rule.
        self.defense_origin = defense_origin
        # The scenario to which the protection rule applies.
        # 
        # If the **DefenseType** parameter is set to **template**, the valid values are:
        # 
        # - **waf_group**: basic protection with regular expression rules.
        # 
        # - **waf_base**: web core protection.
        # 
        # - **waf_base_compliance**: basic protection with protocol compliance rules.
        # 
        # - **waf_base_sema**: basic protection with semantic analysis rules.
        # 
        # - **cc**: HTTP flood protection.
        # 
        # - **antiscan_dirscan**: directory traversal blocking in scan protection.
        # 
        # - **antiscan_highfreq**: high-frequency scan blocking in scan protection.
        # 
        # - **antiscan_scantools**: scanning tool blocking in scan protection.
        # 
        # - **ip_blacklist**: an IP address blacklist.
        # 
        # - **custom_acl**: a custom rule.
        # 
        # - **region_block**: a location blacklist.
        # 
        # - **tamperproof**: webpage tamper protection.
        # 
        # - **dlp**: data leakage prevention.
        # 
        # - **custom_response_block**: a custom response.
        # 
        # - **spike_throttle**: peak traffic throttling.
        # 
        # If the **DefenseType** parameter is set to **resource**, the valid values are:
        # 
        # - **account_identifier**: account identification.
        # 
        # - **custom_response**: a custom response.
        # 
        # - **waf_codec**: data decoding settings.
        # 
        # If the **DefenseType** parameter is set to **global**, the valid values are:
        # 
        # - **regular_custom**: a custom regular expression.
        # 
        # - **address_book**: an IP address book.
        # 
        # - **custom_response**: a custom response.
        self.defense_scene = defense_scene
        # The type of the protection rule. Valid values:
        # 
        # - **template** (default): a protection rule template.
        # 
        # - **resource**: a rule for a protected object.
        # 
        # - **global**: a global rule.
        self.defense_type = defense_type
        # The time when the protection rule was modified. This value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The protected object to which the protection rule applies.
        # 
        # > This parameter is returned only if the **DefenseType** parameter is set to **resource**.
        self.resource = resource
        # The ID of the protection rule.
        self.rule_id = rule_id
        # The name of the protection rule.
        self.rule_name = rule_name
        # The status of the protection rule. Valid values:
        # 
        # - **0**: disabled.
        # 
        # - **1**: enabled.
        self.status = status
        # The ID of the protection rule template.
        # 
        # > This parameter is returned only if the **DefenseType** parameter is set to **template**.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.defense_origin is not None:
            result['DefenseOrigin'] = self.defense_origin

        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DefenseOrigin') is not None:
            self.defense_origin = m.get('DefenseOrigin')

        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

