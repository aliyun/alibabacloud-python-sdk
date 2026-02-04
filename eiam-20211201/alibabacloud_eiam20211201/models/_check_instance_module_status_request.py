# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckInstanceModuleStatusRequest(DaraModel):
    def __init__(
        self,
        feature_key: str = None,
        instance_id: str = None,
        module_key: str = None,
        sub_feature_key: str = None,
    ):
        # 二级模块标识
        self.feature_key = feature_key
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 一级模块标识，必填
        # 
        # This parameter is required.
        self.module_key = module_key
        self.sub_feature_key = sub_feature_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_key is not None:
            result['FeatureKey'] = self.feature_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_key is not None:
            result['ModuleKey'] = self.module_key

        if self.sub_feature_key is not None:
            result['SubFeatureKey'] = self.sub_feature_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureKey') is not None:
            self.feature_key = m.get('FeatureKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleKey') is not None:
            self.module_key = m.get('ModuleKey')

        if m.get('SubFeatureKey') is not None:
            self.sub_feature_key = m.get('SubFeatureKey')

        return self

