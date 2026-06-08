# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetServiceProvisionsRequest(DaraModel):
    def __init__(
        self,
        parameters: List[main_models.GetServiceProvisionsRequestParameters] = None,
        region_id: str = None,
        services: List[main_models.GetServiceProvisionsRequestServices] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The parameters.
        self.parameters = parameters
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The services.
        self.services = services
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs. You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_body = template_body
        # The template ID. This parameter applies to shared and private templates.
        # 
        # You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and Services.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body must be 1 to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and Services.
        self.template_url = template_url
        # The version of the template. If you do not specify this parameter, the latest version is used.
        # 
        # This parameter takes effect only when TemplateId is specified.
        self.template_version = template_version

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetServiceProvisionsRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.GetServiceProvisionsRequestServices()
                self.services.append(temp_model.from_map(k1))

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

class GetServiceProvisionsRequestServices(DaraModel):
    def __init__(
        self,
        service_name: str = None,
    ):
        # The name of the service or feature. Valid values:
        # 
        # *   AHAS: Application High Availability Service
        # *   ARMS: Application Real-Time Monitoring Service (ARMS)
        # *   ApiGateway: API Gateway
        # *   BatchCompute: Batch Compute
        # *   BrainIndustrial: Industrial Brain
        # *   CloudStorageGateway: Cloud Storage Gateway (CSG)
        # *   CMS: CloudMonitor
        # *   CR: Container Registry
        # *   CS: Container Service for Kubernetes (ACK)
        # *   DCDN: Dynamic Content Delivery Network (DCDN)
        # *   DataHub: DataHub
        # *   DataWorks: DataWorks
        # *   EDAS: Enterprise Distributed Application Service (EDAS)
        # *   EHPC: E-HPC
        # *   EMAS: Enterprise Mobile Application Studio (EMAS)
        # *   FC: Function Compute
        # *   FNF: CloudFlow (SWF)
        # *   MaxCompute: MaxCompute
        # *   MNS: Message Service (MNS)
        # *   HBR: Cloud Backup
        # *   IMM: Intelligent Media Management (IMM)
        # *   IOT: IoT Platform
        # *   KMS: Key Management Service (KMS)
        # *   NAS: File Storage NAS (NAS)
        # *   NLP: Natural Language Processing (NLP)
        # *   OSS: Object Storage Service (OSS)
        # *   OTS: Tablestore
        # *   PrivateLink: PrivateLink
        # *   PrivateZone: Alibaba Cloud DNS PrivateZone
        # *   RocketMQ: ApsaraMQ for RocketMQ
        # *   SAE: Serverless App Engine (SAE)
        # *   SLS: Simple Log Service (SLS)
        # *   TrafficMirror: traffic mirroring
        # *   VS: Video Surveillance System
        # *   Xtrace: Managed Service for OpenTelemetry
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class GetServiceProvisionsRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter. If you do not specify the name and value of a parameter, Resource Orchestration Service (ROS) uses the default name and value that are specified in the template.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify ParameterKey.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of the parameter.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify ParameterValue.
        # 
        # This parameter is required.
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

