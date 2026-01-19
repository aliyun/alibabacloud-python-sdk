# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleVersionListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[main_models.DescribeRuleVersionListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Returned object
        self.result_object = result_object
        # Total number of items
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeRuleVersionListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeRuleVersionListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        console_audit: main_models.DescribeRuleVersionListResponseBodyResultObjectConsoleAudit = None,
        console_rule_id: int = None,
        console_rule_memo: str = None,
        console_rule_name: str = None,
        event_code: str = None,
        event_type: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        last_operator: str = None,
        priority: int = None,
        rule_id: str = None,
        rule_status: str = None,
        rule_type: str = None,
        version: int = None,
    ):
        # Audit object
        self.console_audit = console_audit
        # Console rule ID.
        self.console_rule_id = console_rule_id
        # Associated policy remarks
        self.console_rule_memo = console_rule_memo
        # Associated policy name
        self.console_rule_name = console_rule_name
        # Event code
        self.event_code = event_code
        # Event type
        self.event_type = event_type
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Primary key ID of the policy
        self.id = id
        # The user who last operated.
        self.last_operator = last_operator
        # Policy priority, the higher the number, the higher the priority.
        self.priority = priority
        # Policy ID
        self.rule_id = rule_id
        # Policy status
        self.rule_status = rule_status
        # Rule Type
        self.rule_type = rule_type
        # Version number
        self.version = version

    def validate(self):
        if self.console_audit:
            self.console_audit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_audit is not None:
            result['consoleAudit'] = self.console_audit.to_map()

        if self.console_rule_id is not None:
            result['consoleRuleId'] = self.console_rule_id

        if self.console_rule_memo is not None:
            result['consoleRuleMemo'] = self.console_rule_memo

        if self.console_rule_name is not None:
            result['consoleRuleName'] = self.console_rule_name

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.last_operator is not None:
            result['lastOperator'] = self.last_operator

        if self.priority is not None:
            result['priority'] = self.priority

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        if self.rule_type is not None:
            result['ruleType'] = self.rule_type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consoleAudit') is not None:
            temp_model = main_models.DescribeRuleVersionListResponseBodyResultObjectConsoleAudit()
            self.console_audit = temp_model.from_map(m.get('consoleAudit'))

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('consoleRuleMemo') is not None:
            self.console_rule_memo = m.get('consoleRuleMemo')

        if m.get('consoleRuleName') is not None:
            self.console_rule_name = m.get('consoleRuleName')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastOperator') is not None:
            self.last_operator = m.get('lastOperator')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class DescribeRuleVersionListResponseBodyResultObjectConsoleAudit(DaraModel):
    def __init__(
        self,
        apply_user_id: str = None,
        apply_user_name: str = None,
        audit_msg: str = None,
        audit_real_user_id: str = None,
        audit_real_user_name: str = None,
        audit_remark: str = None,
        audit_status: str = None,
        audit_time: int = None,
        audit_user_id: str = None,
        audit_user_name: str = None,
        gmt_create: int = None,
        id: int = None,
        relation_ext: str = None,
        relation_id: int = None,
        relation_name: str = None,
        relation_type: str = None,
    ):
        # Initiator UID
        self.apply_user_id = apply_user_id
        # Initiator name
        self.apply_user_name = apply_user_name
        # Approval comment
        self.audit_msg = audit_msg
        # Final approver UID
        self.audit_real_user_id = audit_real_user_id
        # Final approver name
        self.audit_real_user_name = audit_real_user_name
        # Approver\\"s remarks.
        self.audit_remark = audit_remark
        # Approval status
        self.audit_status = audit_status
        # Approval time.
        self.audit_time = audit_time
        # Designated approver UID
        self.audit_user_id = audit_user_id
        # Designated auditor\\"s name
        self.audit_user_name = audit_user_name
        # Creation time.
        self.gmt_create = gmt_create
        # Primary key ID
        self.id = id
        # Information of related others (in JSON format)
        self.relation_ext = relation_ext
        # ID of the associated transaction
        self.relation_id = relation_id
        # Name of the associated item
        self.relation_name = relation_name
        # Type of approval (e.g., `rule` for policy approval)
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_user_id is not None:
            result['applyUserId'] = self.apply_user_id

        if self.apply_user_name is not None:
            result['applyUserName'] = self.apply_user_name

        if self.audit_msg is not None:
            result['auditMsg'] = self.audit_msg

        if self.audit_real_user_id is not None:
            result['auditRealUserId'] = self.audit_real_user_id

        if self.audit_real_user_name is not None:
            result['auditRealUserName'] = self.audit_real_user_name

        if self.audit_remark is not None:
            result['auditRemark'] = self.audit_remark

        if self.audit_status is not None:
            result['auditStatus'] = self.audit_status

        if self.audit_time is not None:
            result['auditTime'] = self.audit_time

        if self.audit_user_id is not None:
            result['auditUserId'] = self.audit_user_id

        if self.audit_user_name is not None:
            result['auditUserName'] = self.audit_user_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.relation_ext is not None:
            result['relationExt'] = self.relation_ext

        if self.relation_id is not None:
            result['relationId'] = self.relation_id

        if self.relation_name is not None:
            result['relationName'] = self.relation_name

        if self.relation_type is not None:
            result['relationType'] = self.relation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyUserId') is not None:
            self.apply_user_id = m.get('applyUserId')

        if m.get('applyUserName') is not None:
            self.apply_user_name = m.get('applyUserName')

        if m.get('auditMsg') is not None:
            self.audit_msg = m.get('auditMsg')

        if m.get('auditRealUserId') is not None:
            self.audit_real_user_id = m.get('auditRealUserId')

        if m.get('auditRealUserName') is not None:
            self.audit_real_user_name = m.get('auditRealUserName')

        if m.get('auditRemark') is not None:
            self.audit_remark = m.get('auditRemark')

        if m.get('auditStatus') is not None:
            self.audit_status = m.get('auditStatus')

        if m.get('auditTime') is not None:
            self.audit_time = m.get('auditTime')

        if m.get('auditUserId') is not None:
            self.audit_user_id = m.get('auditUserId')

        if m.get('auditUserName') is not None:
            self.audit_user_name = m.get('auditUserName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('relationExt') is not None:
            self.relation_ext = m.get('relationExt')

        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')

        if m.get('relationName') is not None:
            self.relation_name = m.get('relationName')

        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')

        return self

