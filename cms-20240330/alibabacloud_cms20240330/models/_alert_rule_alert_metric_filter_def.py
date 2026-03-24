# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleAlertMetricFilterDef(DaraModel):
    def __init__(
        self,
        dim: str = None,
        dim_disabled: bool = None,
        display_name_cn: str = None,
        display_name_en: str = None,
        hidden: bool = None,
        label_disabled: bool = None,
        opt: str = None,
        supported_opts: List[main_models.AlertRuleAlertMetricFilterDefSupportedOpts] = None,
    ):
        # APM指标中为维度
        self.dim = dim
        # 为true是，过滤项不出现在promQL的group by中
        self.dim_disabled = dim_disabled
        # 显示名称中文
        self.display_name_cn = display_name_cn
        # 显示名称英文
        self.display_name_en = display_name_en
        # 是否隐藏。 如果隐藏则在前端交互中不显示，但在渲染promQL时可将该过滤条件的值上传上来。  典型的例子是APM场景中的pid这个过滤条件，一般不会通过配置化的方式进行显示，而是前端显为独立的应用搜索列表。
        self.hidden = hidden
        # 为true时，过滤项不出现在promQL的label filter中
        self.label_disabled = label_disabled
        # 过滤条件操作符
        self.opt = opt
        # 支持的选项的列表
        self.supported_opts = supported_opts

    def validate(self):
        if self.supported_opts:
            for v1 in self.supported_opts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dim is not None:
            result['dim'] = self.dim

        if self.dim_disabled is not None:
            result['dimDisabled'] = self.dim_disabled

        if self.display_name_cn is not None:
            result['displayNameCn'] = self.display_name_cn

        if self.display_name_en is not None:
            result['displayNameEn'] = self.display_name_en

        if self.hidden is not None:
            result['hidden'] = self.hidden

        if self.label_disabled is not None:
            result['labelDisabled'] = self.label_disabled

        if self.opt is not None:
            result['opt'] = self.opt

        result['supportedOpts'] = []
        if self.supported_opts is not None:
            for k1 in self.supported_opts:
                result['supportedOpts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dim') is not None:
            self.dim = m.get('dim')

        if m.get('dimDisabled') is not None:
            self.dim_disabled = m.get('dimDisabled')

        if m.get('displayNameCn') is not None:
            self.display_name_cn = m.get('displayNameCn')

        if m.get('displayNameEn') is not None:
            self.display_name_en = m.get('displayNameEn')

        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')

        if m.get('labelDisabled') is not None:
            self.label_disabled = m.get('labelDisabled')

        if m.get('opt') is not None:
            self.opt = m.get('opt')

        self.supported_opts = []
        if m.get('supportedOpts') is not None:
            for k1 in m.get('supportedOpts'):
                temp_model = main_models.AlertRuleAlertMetricFilterDefSupportedOpts()
                self.supported_opts.append(temp_model.from_map(k1))

        return self

class AlertRuleAlertMetricFilterDefSupportedOpts(DaraModel):
    def __init__(
        self,
        display_name_cn: str = None,
        display_name_en: str = None,
        value: str = None,
    ):
        # 显示名称中文
        self.display_name_cn = display_name_cn
        # 显示名称英文
        self.display_name_en = display_name_en
        # 匹配值。
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name_cn is not None:
            result['displayNameCn'] = self.display_name_cn

        if self.display_name_en is not None:
            result['displayNameEn'] = self.display_name_en

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayNameCn') is not None:
            self.display_name_cn = m.get('displayNameCn')

        if m.get('displayNameEn') is not None:
            self.display_name_en = m.get('displayNameEn')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

