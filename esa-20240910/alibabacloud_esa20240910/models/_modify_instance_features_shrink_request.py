# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceFeaturesShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        site_features_shrink: str = None,
    ):
        # The plan instance ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of site feature configurations.
        # 
        # This parameter is required.
        self.site_features_shrink = site_features_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.site_features_shrink is not None:
            result['SiteFeatures'] = self.site_features_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SiteFeatures') is not None:
            self.site_features_shrink = m.get('SiteFeatures')

        return self

