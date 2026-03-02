# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SessionCluster(DaraModel):
    def __init__(
        self,
        basic_resource_setting: main_models.BasicResourceSetting = None,
        created_at: int = None,
        creator: str = None,
        creator_name: str = None,
        deployment_target_name: str = None,
        engine_version: str = None,
        flink_conf: Dict[str, Any] = None,
        labels: Dict[str, Any] = None,
        logging: main_models.Logging = None,
        modified_at: int = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        session_cluster_id: str = None,
        status: main_models.SessionClusterStatus = None,
        workspace: str = None,
    ):
        self.basic_resource_setting = basic_resource_setting
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_target_name = deployment_target_name
        self.engine_version = engine_version
        self.flink_conf = flink_conf
        self.labels = labels
        self.logging = logging
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
        self.session_cluster_id = session_cluster_id
        self.status = status
        self.workspace = workspace

    def validate(self):
        if self.basic_resource_setting:
            self.basic_resource_setting.validate()
        if self.logging:
            self.logging.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_resource_setting is not None:
            result['basicResourceSetting'] = self.basic_resource_setting.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.deployment_target_name is not None:
            result['deploymentTargetName'] = self.deployment_target_name

        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version

        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf

        if self.labels is not None:
            result['labels'] = self.labels

        if self.logging is not None:
            result['logging'] = self.logging.to_map()

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basicResourceSetting') is not None:
            temp_model = main_models.BasicResourceSetting()
            self.basic_resource_setting = temp_model.from_map(m.get('basicResourceSetting'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('deploymentTargetName') is not None:
            self.deployment_target_name = m.get('deploymentTargetName')

        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')

        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('logging') is not None:
            temp_model = main_models.Logging()
            self.logging = temp_model.from_map(m.get('logging'))

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')

        if m.get('status') is not None:
            temp_model = main_models.SessionClusterStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

