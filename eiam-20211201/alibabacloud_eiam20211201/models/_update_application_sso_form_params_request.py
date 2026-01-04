# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationSsoFormParamsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_template_params: List[main_models.UpdateApplicationSsoFormParamsRequestApplicationTemplateParams] = None,
        instance_id: str = None,
    ):
        # IDaaS的应用主键id
        # 
        # This parameter is required.
        self.application_id = application_id
        # 应用模板创建参数，应用创建来源为模板时才可以指定
        # 
        # This parameter is required.
        self.application_template_params = application_template_params
        # IDaaS EIAM的实例id
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.application_template_params:
            for v1 in self.application_template_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['ApplicationTemplateParams'] = []
        if self.application_template_params is not None:
            for k1 in self.application_template_params:
                result['ApplicationTemplateParams'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.application_template_params = []
        if m.get('ApplicationTemplateParams') is not None:
            for k1 in m.get('ApplicationTemplateParams'):
                temp_model = main_models.UpdateApplicationSsoFormParamsRequestApplicationTemplateParams()
                self.application_template_params.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class UpdateApplicationSsoFormParamsRequestApplicationTemplateParams(DaraModel):
    def __init__(
        self,
        template_param_name: str = None,
        template_param_value: str = None,
    ):
        # 应用模板创建参数具体名称
        self.template_param_name = template_param_name
        # 应用模板创建参数真实的取值
        self.template_param_value = template_param_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_param_name is not None:
            result['TemplateParamName'] = self.template_param_name

        if self.template_param_value is not None:
            result['TemplateParamValue'] = self.template_param_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateParamName') is not None:
            self.template_param_name = m.get('TemplateParamName')

        if m.get('TemplateParamValue') is not None:
            self.template_param_value = m.get('TemplateParamValue')

        return self

