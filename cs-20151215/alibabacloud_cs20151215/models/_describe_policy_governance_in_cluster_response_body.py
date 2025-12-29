# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribePolicyGovernanceInClusterResponseBody(DaraModel):
    def __init__(
        self,
        violation: main_models.DescribePolicyGovernanceInClusterResponseBodyViolation = None,
        admit_log: main_models.DescribePolicyGovernanceInClusterResponseBodyAdmitLog = None,
        on_state: List[main_models.DescribePolicyGovernanceInClusterResponseBodyOnState] = None,
    ):
        self.violation = violation
        # The audit logs of the policies in the cluster.
        self.admit_log = admit_log
        # Details about the policies of different severity levels that are enabled for the cluster.
        self.on_state = on_state

    def validate(self):
        if self.violation:
            self.violation.validate()
        if self.admit_log:
            self.admit_log.validate()
        if self.on_state:
            for v1 in self.on_state:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.violation is not None:
            result['Violation'] = self.violation.to_map()

        if self.admit_log is not None:
            result['admit_log'] = self.admit_log.to_map()

        result['on_state'] = []
        if self.on_state is not None:
            for k1 in self.on_state:
                result['on_state'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Violation') is not None:
            temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyViolation()
            self.violation = temp_model.from_map(m.get('Violation'))

        if m.get('admit_log') is not None:
            temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyAdmitLog()
            self.admit_log = temp_model.from_map(m.get('admit_log'))

        self.on_state = []
        if m.get('on_state') is not None:
            for k1 in m.get('on_state'):
                temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyOnState()
                self.on_state.append(temp_model.from_map(k1))

        return self

class DescribePolicyGovernanceInClusterResponseBodyOnState(DaraModel):
    def __init__(
        self,
        enabled_count: int = None,
        severity: str = None,
        total: int = None,
    ):
        # The number of policies that are enabled.
        self.enabled_count = enabled_count
        # The severity level of the policy.
        self.severity = severity
        # The total number of policies of the severity level.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled_count is not None:
            result['enabled_count'] = self.enabled_count

        if self.severity is not None:
            result['severity'] = self.severity

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled_count') is not None:
            self.enabled_count = m.get('enabled_count')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class DescribePolicyGovernanceInClusterResponseBodyAdmitLog(DaraModel):
    def __init__(
        self,
        count: int = None,
        log_project: str = None,
        log_store: str = None,
        logs: List[main_models.DescribePolicyGovernanceInClusterResponseBodyAdmitLogLogs] = None,
        progress: str = None,
    ):
        # The number of audit log entries.
        self.count = count
        self.log_project = log_project
        self.log_store = log_store
        self.logs = logs
        # The status of the query. Valid values:
        # 
        # *   `Complete`: The query succeeded and the complete query result is returned.
        # *   `Incomplete`: The query succeeded but the query result is incomplete. To obtain the complete query result, you must repeat the request.
        self.progress = progress

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.log_project is not None:
            result['log_project'] = self.log_project

        if self.log_store is not None:
            result['log_store'] = self.log_store

        result['logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['logs'].append(k1.to_map() if k1 else None)

        if self.progress is not None:
            result['progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('log_project') is not None:
            self.log_project = m.get('log_project')

        if m.get('log_store') is not None:
            self.log_store = m.get('log_store')

        self.logs = []
        if m.get('logs') is not None:
            for k1 in m.get('logs'):
                temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyAdmitLogLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        return self

class DescribePolicyGovernanceInClusterResponseBodyAdmitLogLogs(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        constraint_action: str = None,
        constraint_api_version: str = None,
        constraint_category: str = None,
        constraint_group: str = None,
        constraint_kind: str = None,
        constraint_name: str = None,
        event_msg: str = None,
        event_type: str = None,
        request_uid: str = None,
        request_userinfo: str = None,
        request_username: str = None,
        resource_kind: str = None,
        resource_name: str = None,
        time: str = None,
    ):
        self.cluster_id = cluster_id
        self.constraint_action = constraint_action
        self.constraint_api_version = constraint_api_version
        self.constraint_category = constraint_category
        self.constraint_group = constraint_group
        self.constraint_kind = constraint_kind
        self.constraint_name = constraint_name
        self.event_msg = event_msg
        self.event_type = event_type
        self.request_uid = request_uid
        self.request_userinfo = request_userinfo
        self.request_username = request_username
        self.resource_kind = resource_kind
        self.resource_name = resource_name
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.constraint_action is not None:
            result['constraint_action'] = self.constraint_action

        if self.constraint_api_version is not None:
            result['constraint_api_version'] = self.constraint_api_version

        if self.constraint_category is not None:
            result['constraint_category'] = self.constraint_category

        if self.constraint_group is not None:
            result['constraint_group'] = self.constraint_group

        if self.constraint_kind is not None:
            result['constraint_kind'] = self.constraint_kind

        if self.constraint_name is not None:
            result['constraint_name'] = self.constraint_name

        if self.event_msg is not None:
            result['event_msg'] = self.event_msg

        if self.event_type is not None:
            result['event_type'] = self.event_type

        if self.request_uid is not None:
            result['request_uid'] = self.request_uid

        if self.request_userinfo is not None:
            result['request_userinfo'] = self.request_userinfo

        if self.request_username is not None:
            result['request_username'] = self.request_username

        if self.resource_kind is not None:
            result['resource_kind'] = self.resource_kind

        if self.resource_name is not None:
            result['resource_name'] = self.resource_name

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('constraint_action') is not None:
            self.constraint_action = m.get('constraint_action')

        if m.get('constraint_api_version') is not None:
            self.constraint_api_version = m.get('constraint_api_version')

        if m.get('constraint_category') is not None:
            self.constraint_category = m.get('constraint_category')

        if m.get('constraint_group') is not None:
            self.constraint_group = m.get('constraint_group')

        if m.get('constraint_kind') is not None:
            self.constraint_kind = m.get('constraint_kind')

        if m.get('constraint_name') is not None:
            self.constraint_name = m.get('constraint_name')

        if m.get('event_msg') is not None:
            self.event_msg = m.get('event_msg')

        if m.get('event_type') is not None:
            self.event_type = m.get('event_type')

        if m.get('request_uid') is not None:
            self.request_uid = m.get('request_uid')

        if m.get('request_userinfo') is not None:
            self.request_userinfo = m.get('request_userinfo')

        if m.get('request_username') is not None:
            self.request_username = m.get('request_username')

        if m.get('resource_kind') is not None:
            self.resource_kind = m.get('resource_kind')

        if m.get('resource_name') is not None:
            self.resource_name = m.get('resource_name')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class DescribePolicyGovernanceInClusterResponseBodyViolation(DaraModel):
    def __init__(
        self,
        total_violations: main_models.DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolations = None,
        violations: main_models.DescribePolicyGovernanceInClusterResponseBodyViolationViolations = None,
    ):
        self.total_violations = total_violations
        self.violations = violations

    def validate(self):
        if self.total_violations:
            self.total_violations.validate()
        if self.violations:
            self.violations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_violations is not None:
            result['totalViolations'] = self.total_violations.to_map()

        if self.violations is not None:
            result['violations'] = self.violations.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalViolations') is not None:
            temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolations()
            self.total_violations = temp_model.from_map(m.get('totalViolations'))

        if m.get('violations') is not None:
            temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyViolationViolations()
            self.violations = temp_model.from_map(m.get('violations'))

        return self

class DescribePolicyGovernanceInClusterResponseBodyViolationViolations(DaraModel):
    def __init__(
        self,
        deny: List[main_models.DescribePolicyGovernanceInClusterResponseBodyViolationViolationsDeny] = None,
        warn: List[main_models.DescribePolicyGovernanceInClusterResponseBodyViolationViolationsWarn] = None,
    ):
        self.deny = deny
        self.warn = warn

    def validate(self):
        if self.deny:
            for v1 in self.deny:
                 if v1:
                    v1.validate()
        if self.warn:
            for v1 in self.warn:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['deny'] = []
        if self.deny is not None:
            for k1 in self.deny:
                result['deny'].append(k1.to_map() if k1 else None)

        result['warn'] = []
        if self.warn is not None:
            for k1 in self.warn:
                result['warn'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deny = []
        if m.get('deny') is not None:
            for k1 in m.get('deny'):
                temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyViolationViolationsDeny()
                self.deny.append(temp_model.from_map(k1))

        self.warn = []
        if m.get('warn') is not None:
            for k1 in m.get('warn'):
                temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyViolationViolationsWarn()
                self.warn.append(temp_model.from_map(k1))

        return self

class DescribePolicyGovernanceInClusterResponseBodyViolationViolationsWarn(DaraModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_name: str = None,
        severity: str = None,
        violations: int = None,
    ):
        self.policy_description = policy_description
        self.policy_name = policy_name
        self.severity = severity
        self.violations = violations

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_description is not None:
            result['policyDescription'] = self.policy_description

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.severity is not None:
            result['severity'] = self.severity

        if self.violations is not None:
            result['violations'] = self.violations

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyDescription') is not None:
            self.policy_description = m.get('policyDescription')

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('violations') is not None:
            self.violations = m.get('violations')

        return self

class DescribePolicyGovernanceInClusterResponseBodyViolationViolationsDeny(DaraModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_name: str = None,
        severity: str = None,
        violations: int = None,
    ):
        self.policy_description = policy_description
        self.policy_name = policy_name
        self.severity = severity
        self.violations = violations

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_description is not None:
            result['policyDescription'] = self.policy_description

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.severity is not None:
            result['severity'] = self.severity

        if self.violations is not None:
            result['violations'] = self.violations

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyDescription') is not None:
            self.policy_description = m.get('policyDescription')

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('violations') is not None:
            self.violations = m.get('violations')

        return self

class DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolations(DaraModel):
    def __init__(
        self,
        deny: List[main_models.DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolationsDeny] = None,
        warn: List[main_models.DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolationsWarn] = None,
    ):
        self.deny = deny
        self.warn = warn

    def validate(self):
        if self.deny:
            for v1 in self.deny:
                 if v1:
                    v1.validate()
        if self.warn:
            for v1 in self.warn:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['deny'] = []
        if self.deny is not None:
            for k1 in self.deny:
                result['deny'].append(k1.to_map() if k1 else None)

        result['warn'] = []
        if self.warn is not None:
            for k1 in self.warn:
                result['warn'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deny = []
        if m.get('deny') is not None:
            for k1 in m.get('deny'):
                temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolationsDeny()
                self.deny.append(temp_model.from_map(k1))

        self.warn = []
        if m.get('warn') is not None:
            for k1 in m.get('warn'):
                temp_model = main_models.DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolationsWarn()
                self.warn.append(temp_model.from_map(k1))

        return self

class DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolationsWarn(DaraModel):
    def __init__(
        self,
        severity: str = None,
        violations: int = None,
    ):
        self.severity = severity
        self.violations = violations

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.severity is not None:
            result['severity'] = self.severity

        if self.violations is not None:
            result['violations'] = self.violations

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('violations') is not None:
            self.violations = m.get('violations')

        return self

class DescribePolicyGovernanceInClusterResponseBodyViolationTotalViolationsDeny(DaraModel):
    def __init__(
        self,
        severity: str = None,
        violations: str = None,
    ):
        self.severity = severity
        self.violations = violations

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.severity is not None:
            result['severity'] = self.severity

        if self.violations is not None:
            result['violations'] = self.violations

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('violations') is not None:
            self.violations = m.get('violations')

        return self

