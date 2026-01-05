# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateRequest(DaraModel):
    def __init__(
        self,
        template_body: str = None,
        template_type: str = None,
        terraform_variables: List[main_models.CreateTemplateRequestTerraformVariables] = None,
    ):
        # The content of the template.
        # 
        # For more information about the template syntax, see [Structure of Terraform templates](https://help.aliyun.com/document_detail/184397.html).
        # 
        # This parameter is required.
        self.template_body = template_body
        # The type of the product template. Valid values:
        # 
        # *   RosTerraformTemplate: the Terraform template that is supported by Resource Orchestration Service (ROS).
        # *   RosStandardTemplate: the standard ROS template.
        # 
        # This parameter is required.
        self.template_type = template_type
        # The variable settings of the Terraform template. You can configure the variables in a structured manner. Service Catalog applies the variable settings to the template.
        # 
        # >  The variables must be defined in the Terraform template.
        self.terraform_variables = terraform_variables

    def validate(self):
        if self.terraform_variables:
            for v1 in self.terraform_variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        result['TerraformVariables'] = []
        if self.terraform_variables is not None:
            for k1 in self.terraform_variables:
                result['TerraformVariables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        self.terraform_variables = []
        if m.get('TerraformVariables') is not None:
            for k1 in m.get('TerraformVariables'):
                temp_model = main_models.CreateTemplateRequestTerraformVariables()
                self.terraform_variables.append(temp_model.from_map(k1))

        return self

class CreateTemplateRequestTerraformVariables(DaraModel):
    def __init__(
        self,
        description: str = None,
        variable_name: str = None,
    ):
        # The description of the variable.
        # 
        # For more information about the format of variable descriptions, see [Methods and suggestions for Terraform code development](https://help.aliyun.com/document_detail/322216.html).
        self.description = description
        # The name of the variable.
        self.variable_name = variable_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.variable_name is not None:
            result['VariableName'] = self.variable_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')

        return self

