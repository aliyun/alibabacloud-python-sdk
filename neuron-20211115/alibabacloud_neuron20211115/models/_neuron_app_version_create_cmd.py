# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class NeuronAppVersionCreateCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        app_entry: str = None,
        app_id: int = None,
        description: str = None,
        envs: List[str] = None,
        feature_desc: List[main_models.NeuronAppInfoContent] = None,
        image_urls: List[str] = None,
        instruction_url: str = None,
        manage_type: str = None,
        mobi_id: int = None,
        pbcs: List[int] = None,
        plugin_list: List[main_models.AppPluginInfo] = None,
        private_info: List[str] = None,
        scopes: List[str] = None,
        sidebar: str = None,
        unbind_effect: str = None,
        unbind_reasons: List[str] = None,
        updated_feature: List[main_models.NeuronAppInfoContent] = None,
        version: str = None,
    ):
        self.account_id = account_id
        self.app_entry = app_entry
        # This parameter is required.
        self.app_id = app_id
        self.description = description
        self.envs = envs
        self.feature_desc = feature_desc
        self.image_urls = image_urls
        self.instruction_url = instruction_url
        self.manage_type = manage_type
        self.mobi_id = mobi_id
        self.pbcs = pbcs
        self.plugin_list = plugin_list
        self.private_info = private_info
        self.scopes = scopes
        self.sidebar = sidebar
        self.unbind_effect = unbind_effect
        self.unbind_reasons = unbind_reasons
        self.updated_feature = updated_feature
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.feature_desc:
            for v1 in self.feature_desc:
                 if v1:
                    v1.validate()
        if self.plugin_list:
            for v1 in self.plugin_list:
                 if v1:
                    v1.validate()
        if self.updated_feature:
            for v1 in self.updated_feature:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.app_entry is not None:
            result['appEntry'] = self.app_entry

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.description is not None:
            result['description'] = self.description

        if self.envs is not None:
            result['envs'] = self.envs

        result['featureDesc'] = []
        if self.feature_desc is not None:
            for k1 in self.feature_desc:
                result['featureDesc'].append(k1.to_map() if k1 else None)

        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls

        if self.instruction_url is not None:
            result['instructionUrl'] = self.instruction_url

        if self.manage_type is not None:
            result['manageType'] = self.manage_type

        if self.mobi_id is not None:
            result['mobiId'] = self.mobi_id

        if self.pbcs is not None:
            result['pbcs'] = self.pbcs

        result['pluginList'] = []
        if self.plugin_list is not None:
            for k1 in self.plugin_list:
                result['pluginList'].append(k1.to_map() if k1 else None)

        if self.private_info is not None:
            result['privateInfo'] = self.private_info

        if self.scopes is not None:
            result['scopes'] = self.scopes

        if self.sidebar is not None:
            result['sidebar'] = self.sidebar

        if self.unbind_effect is not None:
            result['unbindEffect'] = self.unbind_effect

        if self.unbind_reasons is not None:
            result['unbindReasons'] = self.unbind_reasons

        result['updatedFeature'] = []
        if self.updated_feature is not None:
            for k1 in self.updated_feature:
                result['updatedFeature'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('appEntry') is not None:
            self.app_entry = m.get('appEntry')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('envs') is not None:
            self.envs = m.get('envs')

        self.feature_desc = []
        if m.get('featureDesc') is not None:
            for k1 in m.get('featureDesc'):
                temp_model = main_models.NeuronAppInfoContent()
                self.feature_desc.append(temp_model.from_map(k1))

        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')

        if m.get('instructionUrl') is not None:
            self.instruction_url = m.get('instructionUrl')

        if m.get('manageType') is not None:
            self.manage_type = m.get('manageType')

        if m.get('mobiId') is not None:
            self.mobi_id = m.get('mobiId')

        if m.get('pbcs') is not None:
            self.pbcs = m.get('pbcs')

        self.plugin_list = []
        if m.get('pluginList') is not None:
            for k1 in m.get('pluginList'):
                temp_model = main_models.AppPluginInfo()
                self.plugin_list.append(temp_model.from_map(k1))

        if m.get('privateInfo') is not None:
            self.private_info = m.get('privateInfo')

        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')

        if m.get('sidebar') is not None:
            self.sidebar = m.get('sidebar')

        if m.get('unbindEffect') is not None:
            self.unbind_effect = m.get('unbindEffect')

        if m.get('unbindReasons') is not None:
            self.unbind_reasons = m.get('unbindReasons')

        self.updated_feature = []
        if m.get('updatedFeature') is not None:
            for k1 in m.get('updatedFeature'):
                temp_model = main_models.NeuronAppInfoContent()
                self.updated_feature.append(temp_model.from_map(k1))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

