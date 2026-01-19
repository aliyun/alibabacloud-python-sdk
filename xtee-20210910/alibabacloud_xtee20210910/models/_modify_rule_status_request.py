# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRuleStatusRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        apply_user_id: str = None,
        apply_user_name: str = None,
        audit_remark: str = None,
        audit_user_id: str = None,
        audit_user_name: str = None,
        console_rule_id: int = None,
        event_type: str = None,
        reg_id: str = None,
        rule_audit_type: str = None,
        rule_id: str = None,
        rule_version_id: int = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # UID of the applicant.
        self.apply_user_id = apply_user_id
        # Name of the applicant.
        self.apply_user_name = apply_user_name
        # Approval remarks.
        self.audit_remark = audit_remark
        # UID of the auditor.
        self.audit_user_id = audit_user_id
        # Name of the auditor.
        self.audit_user_name = audit_user_name
        # Primary key ID of the policy.
        self.console_rule_id = console_rule_id
        # Event type.
        self.event_type = event_type
        # Region code.
        self.reg_id = reg_id
        # Audit status.
        self.rule_audit_type = rule_audit_type
        # Policy ID.
        self.rule_id = rule_id
        # Primary key ID of the policy version.
        self.rule_version_id = rule_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.apply_user_id is not None:
            result['applyUserId'] = self.apply_user_id

        if self.apply_user_name is not None:
            result['applyUserName'] = self.apply_user_name

        if self.audit_remark is not None:
            result['auditRemark'] = self.audit_remark

        if self.audit_user_id is not None:
            result['auditUserId'] = self.audit_user_id

        if self.audit_user_name is not None:
            result['auditUserName'] = self.audit_user_name

        if self.console_rule_id is not None:
            result['consoleRuleId'] = self.console_rule_id

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_audit_type is not None:
            result['ruleAuditType'] = self.rule_audit_type

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_version_id is not None:
            result['ruleVersionId'] = self.rule_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('applyUserId') is not None:
            self.apply_user_id = m.get('applyUserId')

        if m.get('applyUserName') is not None:
            self.apply_user_name = m.get('applyUserName')

        if m.get('auditRemark') is not None:
            self.audit_remark = m.get('auditRemark')

        if m.get('auditUserId') is not None:
            self.audit_user_id = m.get('auditUserId')

        if m.get('auditUserName') is not None:
            self.audit_user_name = m.get('auditUserName')

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleAuditType') is not None:
            self.rule_audit_type = m.get('ruleAuditType')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleVersionId') is not None:
            self.rule_version_id = m.get('ruleVersionId')

        return self

