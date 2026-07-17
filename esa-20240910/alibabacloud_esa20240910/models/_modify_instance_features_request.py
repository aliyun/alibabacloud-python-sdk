# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceFeaturesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        site_features: List[main_models.ModifyInstanceFeaturesRequestSiteFeatures] = None,
    ):
        # The plan instance ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of site feature configurations.
        # 
        # This parameter is required.
        self.site_features = site_features

    def validate(self):
        if self.site_features:
            for v1 in self.site_features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['SiteFeatures'] = []
        if self.site_features is not None:
            for k1 in self.site_features:
                result['SiteFeatures'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.site_features = []
        if m.get('SiteFeatures') is not None:
            for k1 in m.get('SiteFeatures'):
                temp_model = main_models.ModifyInstanceFeaturesRequestSiteFeatures()
                self.site_features.append(temp_model.from_map(k1))

        return self

class ModifyInstanceFeaturesRequestSiteFeatures(DaraModel):
    def __init__(
        self,
        features: str = None,
        site_id: int = None,
    ):
        # The site feature configurations to modify.
        self.features = features
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.features is not None:
            result['Features'] = self.features

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

