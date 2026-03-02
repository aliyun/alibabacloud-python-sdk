# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class NeuronAppVersion(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        app_entry: str = None,
        app_id: int = None,
        description: str = None,
        enterprise_id: int = None,
        envs: List[str] = None,
        feature_desc: List[main_models.NeuronAppInfoContent] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        image_urls: List[str] = None,
        instruction_url: str = None,
        is_latest: int = None,
        manage_type: str = None,
        mobi_commit_id: str = None,
        mobi_id: int = None,
        mobi_module_id: str = None,
        mobi_url: str = None,
        pbcs: List[int] = None,
        private_info: List[str] = None,
        product_id: int = None,
        scopes: List[str] = None,
        sidebar: str = None,
        status: str = None,
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
        self.enterprise_id = enterprise_id
        self.envs = envs
        self.feature_desc = feature_desc
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.id = id
        self.image_urls = image_urls
        self.instruction_url = instruction_url
        self.is_latest = is_latest
        self.manage_type = manage_type
        self.mobi_commit_id = mobi_commit_id
        self.mobi_id = mobi_id
        self.mobi_module_id = mobi_module_id
        self.mobi_url = mobi_url
        self.pbcs = pbcs
        self.private_info = private_info
        self.product_id = product_id
        self.scopes = scopes
        self.sidebar = sidebar
        self.status = status
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

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.envs is not None:
            result['envs'] = self.envs

        result['featureDesc'] = []
        if self.feature_desc is not None:
            for k1 in self.feature_desc:
                result['featureDesc'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls

        if self.instruction_url is not None:
            result['instructionUrl'] = self.instruction_url

        if self.is_latest is not None:
            result['isLatest'] = self.is_latest

        if self.manage_type is not None:
            result['manageType'] = self.manage_type

        if self.mobi_commit_id is not None:
            result['mobiCommitId'] = self.mobi_commit_id

        if self.mobi_id is not None:
            result['mobiId'] = self.mobi_id

        if self.mobi_module_id is not None:
            result['mobiModuleId'] = self.mobi_module_id

        if self.mobi_url is not None:
            result['mobiUrl'] = self.mobi_url

        if self.pbcs is not None:
            result['pbcs'] = self.pbcs

        if self.private_info is not None:
            result['privateInfo'] = self.private_info

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.scopes is not None:
            result['scopes'] = self.scopes

        if self.sidebar is not None:
            result['sidebar'] = self.sidebar

        if self.status is not None:
            result['status'] = self.status

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

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('envs') is not None:
            self.envs = m.get('envs')

        self.feature_desc = []
        if m.get('featureDesc') is not None:
            for k1 in m.get('featureDesc'):
                temp_model = main_models.NeuronAppInfoContent()
                self.feature_desc.append(temp_model.from_map(k1))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')

        if m.get('instructionUrl') is not None:
            self.instruction_url = m.get('instructionUrl')

        if m.get('isLatest') is not None:
            self.is_latest = m.get('isLatest')

        if m.get('manageType') is not None:
            self.manage_type = m.get('manageType')

        if m.get('mobiCommitId') is not None:
            self.mobi_commit_id = m.get('mobiCommitId')

        if m.get('mobiId') is not None:
            self.mobi_id = m.get('mobiId')

        if m.get('mobiModuleId') is not None:
            self.mobi_module_id = m.get('mobiModuleId')

        if m.get('mobiUrl') is not None:
            self.mobi_url = m.get('mobiUrl')

        if m.get('pbcs') is not None:
            self.pbcs = m.get('pbcs')

        if m.get('privateInfo') is not None:
            self.private_info = m.get('privateInfo')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')

        if m.get('sidebar') is not None:
            self.sidebar = m.get('sidebar')

        if m.get('status') is not None:
            self.status = m.get('status')

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

