# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class MigrationJob(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        detail: str = None,
        job_status: str = None,
        plan: main_models.MigrationJobPlan = None,
        rule_names: List[str] = None,
        source: List[main_models.MigrationJobSource] = None,
        update_time: str = None,
        uuid: str = None,
    ):
        self.create_time = create_time
        self.detail = detail
        self.job_status = job_status
        self.plan = plan
        self.rule_names = rule_names
        self.source = source
        self.update_time = update_time
        self.uuid = uuid

    def validate(self):
        if self.plan:
            self.plan.validate()
        if self.source:
            for v1 in self.source:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.plan is not None:
            result['Plan'] = self.plan.to_map()

        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names

        result['Source'] = []
        if self.source is not None:
            for k1 in self.source:
                result['Source'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('Plan') is not None:
            temp_model = main_models.MigrationJobPlan()
            self.plan = temp_model.from_map(m.get('Plan'))

        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')

        self.source = []
        if m.get('Source') is not None:
            for k1 in m.get('Source'):
                temp_model = main_models.MigrationJobSource()
                self.source.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class MigrationJobSource(DaraModel):
    def __init__(
        self,
        rule: main_models.MigrationJobSourceRule = None,
        targets: List[main_models.MigrationJobSourceTargets] = None,
    ):
        self.rule = rule
        self.targets = targets

    def validate(self):
        if self.rule:
            self.rule.validate()
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            temp_model = main_models.MigrationJobSourceRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.MigrationJobSourceTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class MigrationJobSourceTargets(DaraModel):
    def __init__(
        self,
        content: main_models.MigrationJobSourceTargetsContent = None,
        type: str = None,
    ):
        self.content = content
        self.type = type

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.MigrationJobSourceTargetsContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MigrationJobSourceTargetsContent(DaraModel):
    def __init__(
        self,
        group: str = None,
        level: str = None,
        method: str = None,
        region: str = None,
        resource_path: str = None,
        url: str = None,
    ):
        self.group = group
        self.level = level
        self.method = method
        self.region = region
        self.resource_path = resource_path
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group

        if self.level is not None:
            result['Level'] = self.level

        if self.method is not None:
            result['Method'] = self.method

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_path is not None:
            result['ResourcePath'] = self.resource_path

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourcePath') is not None:
            self.resource_path = m.get('ResourcePath')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class MigrationJobSourceRule(DaraModel):
    def __init__(
        self,
        keyword_filter: main_models.MigrationJobSourceRuleKeywordFilter = None,
        name: str = None,
        primary_filters: List[main_models.MigrationJobSourceRulePrimaryFilters] = None,
    ):
        self.keyword_filter = keyword_filter
        self.name = name
        self.primary_filters = primary_filters

    def validate(self):
        if self.keyword_filter:
            self.keyword_filter.validate()
        if self.primary_filters:
            for v1 in self.primary_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword_filter is not None:
            result['KeywordFilter'] = self.keyword_filter.to_map()

        if self.name is not None:
            result['Name'] = self.name

        result['PrimaryFilters'] = []
        if self.primary_filters is not None:
            for k1 in self.primary_filters:
                result['PrimaryFilters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordFilter') is not None:
            temp_model = main_models.MigrationJobSourceRuleKeywordFilter()
            self.keyword_filter = temp_model.from_map(m.get('KeywordFilter'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.primary_filters = []
        if m.get('PrimaryFilters') is not None:
            for k1 in m.get('PrimaryFilters'):
                temp_model = main_models.MigrationJobSourceRulePrimaryFilters()
                self.primary_filters.append(temp_model.from_map(k1))

        return self

class MigrationJobSourceRulePrimaryFilters(DaraModel):
    def __init__(
        self,
        field: str = None,
        op_type: str = None,
        value: str = None,
    ):
        self.field = field
        self.op_type = op_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class MigrationJobSourceRuleKeywordFilter(DaraModel):
    def __init__(
        self,
        keywords: List[str] = None,
        relation: str = None,
    ):
        self.keywords = keywords
        self.relation = relation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.relation is not None:
            result['Relation'] = self.relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        return self

class MigrationJobPlan(DaraModel):
    def __init__(
        self,
        contacts: List[main_models.MigrationJobPlanContacts] = None,
        escalations: List[main_models.MigrationJobPlanEscalations] = None,
        groups: List[main_models.MigrationJobPlanGroups] = None,
        rule_names: List[str] = None,
        strategies: List[main_models.MigrationJobPlanStrategies] = None,
        subscriptions: List[main_models.MigrationJobPlanSubscriptions] = None,
        targets: List[main_models.MigrationJobPlanTargets] = None,
    ):
        self.contacts = contacts
        self.escalations = escalations
        self.groups = groups
        self.rule_names = rule_names
        self.strategies = strategies
        self.subscriptions = subscriptions
        self.targets = targets

    def validate(self):
        if self.contacts:
            for v1 in self.contacts:
                 if v1:
                    v1.validate()
        if self.escalations:
            for v1 in self.escalations:
                 if v1:
                    v1.validate()
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.strategies:
            for v1 in self.strategies:
                 if v1:
                    v1.validate()
        if self.subscriptions:
            for v1 in self.subscriptions:
                 if v1:
                    v1.validate()
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['Contacts'].append(k1.to_map() if k1 else None)

        result['Escalations'] = []
        if self.escalations is not None:
            for k1 in self.escalations:
                result['Escalations'].append(k1.to_map() if k1 else None)

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names

        result['Strategies'] = []
        if self.strategies is not None:
            for k1 in self.strategies:
                result['Strategies'].append(k1.to_map() if k1 else None)

        result['Subscriptions'] = []
        if self.subscriptions is not None:
            for k1 in self.subscriptions:
                result['Subscriptions'].append(k1.to_map() if k1 else None)

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('Contacts') is not None:
            for k1 in m.get('Contacts'):
                temp_model = main_models.MigrationJobPlanContacts()
                self.contacts.append(temp_model.from_map(k1))

        self.escalations = []
        if m.get('Escalations') is not None:
            for k1 in m.get('Escalations'):
                temp_model = main_models.MigrationJobPlanEscalations()
                self.escalations.append(temp_model.from_map(k1))

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.MigrationJobPlanGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')

        self.strategies = []
        if m.get('Strategies') is not None:
            for k1 in m.get('Strategies'):
                temp_model = main_models.MigrationJobPlanStrategies()
                self.strategies.append(temp_model.from_map(k1))

        self.subscriptions = []
        if m.get('Subscriptions') is not None:
            for k1 in m.get('Subscriptions'):
                temp_model = main_models.MigrationJobPlanSubscriptions()
                self.subscriptions.append(temp_model.from_map(k1))

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.MigrationJobPlanTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class MigrationJobPlanTargets(DaraModel):
    def __init__(
        self,
        arn: str = None,
        http_request_target: main_models.MigrationJobPlanTargetsHttpRequestTarget = None,
        name: str = None,
        type: str = None,
        uuid: str = None,
    ):
        self.arn = arn
        self.http_request_target = http_request_target
        self.name = name
        self.type = type
        self.uuid = uuid

    def validate(self):
        if self.http_request_target:
            self.http_request_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.http_request_target is not None:
            result['HttpRequestTarget'] = self.http_request_target.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('HttpRequestTarget') is not None:
            temp_model = main_models.MigrationJobPlanTargetsHttpRequestTarget()
            self.http_request_target = temp_model.from_map(m.get('HttpRequestTarget'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class MigrationJobPlanTargetsHttpRequestTarget(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        method: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.method = method
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.method is not None:
            result['Method'] = self.method

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class MigrationJobPlanSubscriptions(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.MigrationJobPlanSubscriptionsConditions] = None,
        name: str = None,
        strategy_uuid: str = None,
    ):
        self.conditions = conditions
        self.name = name
        self.strategy_uuid = strategy_uuid

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.strategy_uuid is not None:
            result['StrategyUuid'] = self.strategy_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.MigrationJobPlanSubscriptionsConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StrategyUuid') is not None:
            self.strategy_uuid = m.get('StrategyUuid')

        return self

class MigrationJobPlanSubscriptionsConditions(DaraModel):
    def __init__(
        self,
        field: str = None,
        op: str = None,
        value: str = None,
    ):
        self.field = field
        self.op = op
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.op is not None:
            result['Op'] = self.op

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class MigrationJobPlanStrategies(DaraModel):
    def __init__(
        self,
        escalation_setting: main_models.MigrationJobPlanStrategiesEscalationSetting = None,
        name: str = None,
        pushing_setting: main_models.MigrationJobPlanStrategiesPushingSetting = None,
    ):
        self.escalation_setting = escalation_setting
        self.name = name
        self.pushing_setting = pushing_setting

    def validate(self):
        if self.escalation_setting:
            self.escalation_setting.validate()
        if self.pushing_setting:
            self.pushing_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.escalation_setting is not None:
            result['EscalationSetting'] = self.escalation_setting.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.pushing_setting is not None:
            result['PushingSetting'] = self.pushing_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EscalationSetting') is not None:
            temp_model = main_models.MigrationJobPlanStrategiesEscalationSetting()
            self.escalation_setting = temp_model.from_map(m.get('EscalationSetting'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PushingSetting') is not None:
            temp_model = main_models.MigrationJobPlanStrategiesPushingSetting()
            self.pushing_setting = temp_model.from_map(m.get('PushingSetting'))

        return self

class MigrationJobPlanStrategiesPushingSetting(DaraModel):
    def __init__(
        self,
        target_uuids: List[str] = None,
    ):
        self.target_uuids = target_uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_uuids is not None:
            result['TargetUuids'] = self.target_uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetUuids') is not None:
            self.target_uuids = m.get('TargetUuids')

        return self

class MigrationJobPlanStrategiesEscalationSetting(DaraModel):
    def __init__(
        self,
        escalation_uuid: str = None,
    ):
        self.escalation_uuid = escalation_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.escalation_uuid is not None:
            result['escalationUuid'] = self.escalation_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('escalationUuid') is not None:
            self.escalation_uuid = m.get('escalationUuid')

        return self

class MigrationJobPlanGroups(DaraModel):
    def __init__(
        self,
        contacts: List[str] = None,
        name: str = None,
    ):
        self.contacts = contacts
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacts is not None:
            result['Contacts'] = self.contacts

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class MigrationJobPlanEscalations(DaraModel):
    def __init__(
        self,
        escalations: List[main_models.MigrationJobPlanEscalationsEscalations] = None,
        name: str = None,
        uuid: str = None,
    ):
        self.escalations = escalations
        self.name = name
        self.uuid = uuid

    def validate(self):
        if self.escalations:
            for v1 in self.escalations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Escalations'] = []
        if self.escalations is not None:
            for k1 in self.escalations:
                result['Escalations'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalations = []
        if m.get('Escalations') is not None:
            for k1 in m.get('Escalations'):
                temp_model = main_models.MigrationJobPlanEscalationsEscalations()
                self.escalations.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class MigrationJobPlanEscalationsEscalations(DaraModel):
    def __init__(
        self,
        groups: List[str] = None,
        level_groups: main_models.MigrationJobPlanEscalationsEscalationsLevelGroups = None,
    ):
        self.groups = groups
        self.level_groups = level_groups

    def validate(self):
        if self.level_groups:
            self.level_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.groups is not None:
            result['Groups'] = self.groups

        if self.level_groups is not None:
            result['LevelGroups'] = self.level_groups.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')

        if m.get('LevelGroups') is not None:
            temp_model = main_models.MigrationJobPlanEscalationsEscalationsLevelGroups()
            self.level_groups = temp_model.from_map(m.get('LevelGroups'))

        return self

class MigrationJobPlanEscalationsEscalationsLevelGroups(DaraModel):
    def __init__(
        self,
        critical: List[str] = None,
        info: List[str] = None,
        resolved: List[str] = None,
        warning: List[str] = None,
    ):
        self.critical = critical
        self.info = info
        self.resolved = resolved
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical

        if self.info is not None:
            result['Info'] = self.info

        if self.resolved is not None:
            result['Resolved'] = self.resolved

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            self.critical = m.get('Critical')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Resolved') is not None:
            self.resolved = m.get('Resolved')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

class MigrationJobPlanContacts(DaraModel):
    def __init__(
        self,
        channels: List[main_models.MigrationJobPlanContactsChannels] = None,
        name: str = None,
    ):
        self.channels = channels
        self.name = name

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['Channels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('Channels') is not None:
            for k1 in m.get('Channels'):
                temp_model = main_models.MigrationJobPlanContactsChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class MigrationJobPlanContactsChannels(DaraModel):
    def __init__(
        self,
        level: int = None,
        type: str = None,
        value: str = None,
    ):
        self.level = level
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

