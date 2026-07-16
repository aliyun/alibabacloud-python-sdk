# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetServiceTemplateParameterConstraintsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deploy_region_id: str = None,
        enable_private_vpc_connection: bool = None,
        parameters: List[main_models.GetServiceTemplateParameterConstraintsRequestParameters] = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Generate a unique value from your client for each request. The token can contain only ASCII characters and cannot be more than 64 characters long.
        self.client_token = client_token
        # The deployment region ID.
        # 
        # This parameter is required.
        self.deploy_region_id = deploy_region_id
        # Indicates whether PrivateLink is enabled. Valid values:
        # 
        # - true: enabled
        # 
        # - false: disabled
        self.enable_private_vpc_connection = enable_private_vpc_connection
        # The configuration parameters of the service instance.
        self.parameters = parameters
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # The specification name.
        self.specification_name = specification_name
        # The template name.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The usage type. Valid values:
        # 
        # - Trial: The service supports a trial.
        # 
        # - NotTrial: The service does not support a trial.
        self.trial_type = trial_type

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id

        if self.enable_private_vpc_connection is not None:
            result['EnablePrivateVpcConnection'] = self.enable_private_vpc_connection

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')

        if m.get('EnablePrivateVpcConnection') is not None:
            self.enable_private_vpc_connection = m.get('EnablePrivateVpcConnection')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetServiceTemplateParameterConstraintsRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        return self

class GetServiceTemplateParameterConstraintsRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter. If you do not specify the name and value of the parameter, Resource Orchestration Service (ROS) uses the default value that is specified in the template.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, ParameterKey is required.
        self.parameter_key = parameter_key
        # The value of the parameter that is defined in the template.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, ParameterValue is required.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

