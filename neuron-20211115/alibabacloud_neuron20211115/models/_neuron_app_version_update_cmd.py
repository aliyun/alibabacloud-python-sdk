# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class NeuronAppVersionUpdateCmd(DaraModel):
    def __init__(
        self,
        app_entry: str = None,
        desc: str = None,
        envs: List[str] = None,
        feature_desc: List[main_models.NeuronAppInfoContent] = None,
        id: int = None,
        image_urls: List[str] = None,
        instruction_url: str = None,
        manage_type: str = None,
        mobi_id: int = None,
        pbcs: List[int] = None,
        private_info: List[str] = None,
        scopes: List[str] = None,
        sidebar: str = None,
        status: str = None,
        unbind_effect: str = None,
        unbind_reasons: List[str] = None,
        updated_feature: List[main_models.NeuronAppInfoContent] = None,
    ):
        self.app_entry = app_entry
        self.desc = desc
        self.envs = envs
        self.feature_desc = feature_desc
        # This parameter is required.
        self.id = id
        self.image_urls = image_urls
        self.instruction_url = instruction_url
        self.manage_type = manage_type
        self.mobi_id = mobi_id
        self.pbcs = pbcs
        self.private_info = private_info
        self.scopes = scopes
        self.sidebar = sidebar
        self.status = status
        self.unbind_effect = unbind_effect
        self.unbind_reasons = unbind_reasons
        self.updated_feature = updated_feature

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
        if self.app_entry is not None:
            result['appEntry'] = self.app_entry

        if self.desc is not None:
            result['desc'] = self.desc

        if self.envs is not None:
            result['envs'] = self.envs

        result['featureDesc'] = []
        if self.feature_desc is not None:
            for k1 in self.feature_desc:
                result['featureDesc'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['id'] = self.id

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

        if self.private_info is not None:
            result['privateInfo'] = self.private_info

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appEntry') is not None:
            self.app_entry = m.get('appEntry')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('envs') is not None:
            self.envs = m.get('envs')

        self.feature_desc = []
        if m.get('featureDesc') is not None:
            for k1 in m.get('featureDesc'):
                temp_model = main_models.NeuronAppInfoContent()
                self.feature_desc.append(temp_model.from_map(k1))

        if m.get('id') is not None:
            self.id = m.get('id')

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

        if m.get('privateInfo') is not None:
            self.private_info = m.get('privateInfo')

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

        return self

