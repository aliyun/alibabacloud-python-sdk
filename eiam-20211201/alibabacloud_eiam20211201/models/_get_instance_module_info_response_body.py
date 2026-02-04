# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceModuleInfoResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.GetInstanceModuleInfoResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = main_models.GetInstanceModuleInfoResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceModuleInfoResponseBodyModule(DaraModel):
    def __init__(
        self,
        features: List[main_models.GetInstanceModuleInfoResponseBodyModuleFeatures] = None,
        module_key: str = None,
        module_status: str = None,
    ):
        # 二级模块信息
        self.features = features
        # 模块状态
        self.module_key = module_key
        # 一级模块状态
        self.module_status = module_status

    def validate(self):
        if self.features:
            for v1 in self.features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Features'] = []
        if self.features is not None:
            for k1 in self.features:
                result['Features'].append(k1.to_map() if k1 else None)

        if self.module_key is not None:
            result['ModuleKey'] = self.module_key

        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.GetInstanceModuleInfoResponseBodyModuleFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('ModuleKey') is not None:
            self.module_key = m.get('ModuleKey')

        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')

        return self

class GetInstanceModuleInfoResponseBodyModuleFeatures(DaraModel):
    def __init__(
        self,
        feature_key: str = None,
        feature_status: str = None,
    ):
        # 二级模块标识
        self.feature_key = feature_key
        # 二级模块状态
        self.feature_status = feature_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_key is not None:
            result['FeatureKey'] = self.feature_key

        if self.feature_status is not None:
            result['FeatureStatus'] = self.feature_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureKey') is not None:
            self.feature_key = m.get('FeatureKey')

        if m.get('FeatureStatus') is not None:
            self.feature_status = m.get('FeatureStatus')

        return self

