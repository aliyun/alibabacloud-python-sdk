# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlertRuleTemplate(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        apply_count: int = None,
        biz_type: str = None,
        datasource: str = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        is_system: int = None,
        labels: str = None,
        namespace: str = None,
        product_category: str = None,
        rule_configs: str = None,
        scenes: str = None,
        schema_version: str = None,
        source_type: str = None,
        status: int = None,
        sub_type: str = None,
        template_name: str = None,
        user_id: str = None,
        uuid: str = None,
    ):
        # The alert type.
        self.alert_type = alert_type
        # The number of rules that have been applied from this template.
        self.apply_count = apply_count
        # The business type.
        self.biz_type = biz_type
        # The data source, in JSON string format.
        self.datasource = datasource
        # The template description.
        self.description = description
        # The creation time, in UNIX millisecond timestamp format.
        self.gmt_create = gmt_create
        # The last modified time, in UNIX millisecond timestamp format.
        self.gmt_modified = gmt_modified
        # The template ID.
        self.id = id
        # Indicates whether the template is a system template. Valid values: 1: yes. 0: no.
        self.is_system = is_system
        # The labels, in JSON string format.
        self.labels = labels
        # The namespace.
        self.namespace = namespace
        # The cloud service category.
        self.product_category = product_category
        # The rule configurations, in JSON string format.
        self.rule_configs = rule_configs
        # The applicable scenarios.
        self.scenes = scenes
        # The schema version.
        self.schema_version = schema_version
        # The source type.
        self.source_type = source_type
        # The template status. Valid values: 1: enabled. 0: disabled.
        self.status = status
        # The subtype.
        self.sub_type = sub_type
        # The template name.
        self.template_name = template_name
        # The ID of the user to whom the template belongs.
        self.user_id = user_id
        # The template UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_type is not None:
            result['alertType'] = self.alert_type

        if self.apply_count is not None:
            result['applyCount'] = self.apply_count

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.datasource is not None:
            result['datasource'] = self.datasource

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.is_system is not None:
            result['isSystem'] = self.is_system

        if self.labels is not None:
            result['labels'] = self.labels

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.product_category is not None:
            result['productCategory'] = self.product_category

        if self.rule_configs is not None:
            result['ruleConfigs'] = self.rule_configs

        if self.scenes is not None:
            result['scenes'] = self.scenes

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        if self.sub_type is not None:
            result['subType'] = self.sub_type

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertType') is not None:
            self.alert_type = m.get('alertType')

        if m.get('applyCount') is not None:
            self.apply_count = m.get('applyCount')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('datasource') is not None:
            self.datasource = m.get('datasource')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isSystem') is not None:
            self.is_system = m.get('isSystem')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')

        if m.get('ruleConfigs') is not None:
            self.rule_configs = m.get('ruleConfigs')

        if m.get('scenes') is not None:
            self.scenes = m.get('scenes')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subType') is not None:
            self.sub_type = m.get('subType')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

