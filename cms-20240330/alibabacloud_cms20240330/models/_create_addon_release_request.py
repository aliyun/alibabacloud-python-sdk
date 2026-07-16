# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateAddonReleaseRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        aliyun_lang: str = None,
        dry_run: bool = None,
        entity_rules: main_models.EntityDiscoverRule = None,
        env_type: str = None,
        parent_addon_release_id: str = None,
        release_name: str = None,
        values: str = None,
        version: str = None,
        workspace: str = None,
    ):
        # The name of the add-on to integrate.
        # 
        # This parameter is required.
        self.addon_name = addon_name
        # The language of the add-on.
        self.aliyun_lang = aliyun_lang
        # Specifies whether to perform a dry run. The default value is false.
        self.dry_run = dry_run
        # The entity discovery rules.
        self.entity_rules = entity_rules
        # The environment type. Set this parameter to CS for container environments or ECS for ECS environments. For all other environment types, set this parameter to Cloud.
        self.env_type = env_type
        # The ID of the parent AddonRelease.
        self.parent_addon_release_id = parent_addon_release_id
        # The name of the release after the integration. If you do not specify this parameter, a default name is generated.
        self.release_name = release_name
        # The metadata.
        self.values = values
        # The version of the add-on to integrate.
        # 
        # This parameter is required.
        self.version = version
        # The name of the workspace where the add-on is installed.
        self.workspace = workspace

    def validate(self):
        if self.entity_rules:
            self.entity_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['addonName'] = self.addon_name

        if self.aliyun_lang is not None:
            result['aliyunLang'] = self.aliyun_lang

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.entity_rules is not None:
            result['entityRules'] = self.entity_rules.to_map()

        if self.env_type is not None:
            result['envType'] = self.env_type

        if self.parent_addon_release_id is not None:
            result['parentAddonReleaseId'] = self.parent_addon_release_id

        if self.release_name is not None:
            result['releaseName'] = self.release_name

        if self.values is not None:
            result['values'] = self.values

        if self.version is not None:
            result['version'] = self.version

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('aliyunLang') is not None:
            self.aliyun_lang = m.get('aliyunLang')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('entityRules') is not None:
            temp_model = main_models.EntityDiscoverRule()
            self.entity_rules = temp_model.from_map(m.get('entityRules'))

        if m.get('envType') is not None:
            self.env_type = m.get('envType')

        if m.get('parentAddonReleaseId') is not None:
            self.parent_addon_release_id = m.get('parentAddonReleaseId')

        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')

        if m.get('values') is not None:
            self.values = m.get('values')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

