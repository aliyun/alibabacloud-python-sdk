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
        self.dim = dim
        self.dim_disabled = dim_disabled
        self.display_name_cn = display_name_cn
        self.display_name_en = display_name_en
        self.hidden = hidden
        self.label_disabled = label_disabled
        self.opt = opt
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
        self.display_name_cn = display_name_cn
        self.display_name_en = display_name_en
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

