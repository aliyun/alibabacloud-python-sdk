# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListIntegrationPolicyStorageRequirementsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        storage_requirements: List[main_models.ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirements] = None,
    ):
        # ID of the request
        self.request_id = request_id
        # List of storage requirements
        self.storage_requirements = storage_requirements

    def validate(self):
        if self.storage_requirements:
            for v1 in self.storage_requirements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['storageRequirements'] = []
        if self.storage_requirements is not None:
            for k1 in self.storage_requirements:
                result['storageRequirements'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.storage_requirements = []
        if m.get('storageRequirements') is not None:
            for k1 in m.get('storageRequirements'):
                temp_model = main_models.ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirements()
                self.storage_requirements.append(temp_model.from_map(k1))

        return self

class ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirements(DaraModel):
    def __init__(
        self,
        addon_release_names: List[str] = None,
        api_version: str = None,
        kind: str = None,
        metadata: main_models.ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsMetadata = None,
        spec: main_models.ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsSpec = None,
        status: main_models.ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsStatus = None,
    ):
        # Collection of AddonReleases.
        self.addon_release_names = addon_release_names
        # API Version
        self.api_version = api_version
        # Resource kind
        self.kind = kind
        # Metadata
        self.metadata = metadata
        # Resource spec
        self.spec = spec
        # Storage requirement status
        self.status = status

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_release_names is not None:
            result['addonReleaseNames'] = self.addon_release_names

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.kind is not None:
            result['kind'] = self.kind

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.spec is not None:
            result['spec'] = self.spec.to_map()

        if self.status is not None:
            result['status'] = self.status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonReleaseNames') is not None:
            self.addon_release_names = m.get('addonReleaseNames')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('metadata') is not None:
            temp_model = main_models.ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('spec') is not None:
            temp_model = main_models.ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsSpec()
            self.spec = temp_model.from_map(m.get('spec'))

        if m.get('status') is not None:
            temp_model = main_models.ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsStatus()
            self.status = temp_model.from_map(m.get('status'))

        return self

class ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsStatus(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        inter_url: str = None,
        intra_url: str = None,
        name: str = None,
        project: str = None,
        prom_metric_store: str = None,
        region: str = None,
        storage_type: str = None,
        workspace: str = None,
    ):
        # Instance ID
        self.instance_id = instance_id
        # Internal URL
        self.inter_url = inter_url
        # External URL
        self.intra_url = intra_url
        # 存储需求名称
        self.name = name
        # 存储需求项目
        self.project = project
        # Prom\\"s metric center
        self.prom_metric_store = prom_metric_store
        # Region
        self.region = region
        # Instance storage type
        self.storage_type = storage_type
        # Workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.inter_url is not None:
            result['interUrl'] = self.inter_url

        if self.intra_url is not None:
            result['intraUrl'] = self.intra_url

        if self.name is not None:
            result['name'] = self.name

        if self.project is not None:
            result['project'] = self.project

        if self.prom_metric_store is not None:
            result['promMetricStore'] = self.prom_metric_store

        if self.region is not None:
            result['region'] = self.region

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('interUrl') is not None:
            self.inter_url = m.get('interUrl')

        if m.get('intraUrl') is not None:
            self.intra_url = m.get('intraUrl')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('promMetricStore') is not None:
            self.prom_metric_store = m.get('promMetricStore')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsSpec(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        instance: str = None,
        instance_name: str = None,
        project: str = None,
        region: str = None,
        share_scope: str = None,
        storage_type: str = None,
        system_tags: Dict[str, str] = None,
        tags: Dict[str, str] = None,
        user_id: str = None,
        workspace: str = None,
    ):
        # Instance ID, which can be specified if you need to pinpoint to the instance level. It depends on the data in EntityStore.
        self.entity_id = entity_id
        # Prom Instance ID.
        self.instance = instance
        # Prom instance name
        self.instance_name = instance_name
        # Optional parameter, determined based on the current environment type
        self.project = project
        # Region
        self.region = region
        # Storage sharing scope: Environment | Region | Workspace | Custom
        self.share_scope = share_scope
        # Instance storage type
        self.storage_type = storage_type
        # Tags to be applied to the target storage (injected as system tags)
        self.system_tags = system_tags
        # Tags to be applied to the target storage (injected as regular tags)
        self.tags = tags
        # User ID
        self.user_id = user_id
        # Workspace
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.instance is not None:
            result['instance'] = self.instance

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.project is not None:
            result['project'] = self.project

        if self.region is not None:
            result['region'] = self.region

        if self.share_scope is not None:
            result['shareScope'] = self.share_scope

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        if self.system_tags is not None:
            result['systemTags'] = self.system_tags

        if self.tags is not None:
            result['tags'] = self.tags

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('shareScope') is not None:
            self.share_scope = m.get('shareScope')

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        if m.get('systemTags') is not None:
            self.system_tags = m.get('systemTags')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListIntegrationPolicyStorageRequirementsResponseBodyStorageRequirementsMetadata(DaraModel):
    def __init__(
        self,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
        name: str = None,
        namespace: str = None,
    ):
        # Annotations
        self.annotations = annotations
        # Resource labels
        self.labels = labels
        # Resource name
        self.name = name
        # Namespace
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.labels is not None:
            result['labels'] = self.labels

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        return self

