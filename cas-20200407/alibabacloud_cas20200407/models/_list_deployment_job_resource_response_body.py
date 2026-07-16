# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListDeploymentJobResourceResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDeploymentJobResourceResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The unique ID of the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDeploymentJobResourceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeploymentJobResourceResponseBodyData(DaraModel):
    def __init__(
        self,
        cert_end_time: str = None,
        cert_id: int = None,
        cert_name: str = None,
        cert_start_time: str = None,
        cloud_access_id: str = None,
        cloud_name: str = None,
        cloud_product: str = None,
        cloud_region: str = None,
        default_resource: int = None,
        domain: str = None,
        enable_https: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        listener_id: str = None,
        listener_port: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        use_ssl: int = None,
        user_id: int = None,
    ):
        # The expiration date of the certificate that is attached to the cloud product resource. The value is a UNIX timestamp. Unit: milliseconds.
        self.cert_end_time = cert_end_time
        # The ID of the certificate that is attached to the cloud product resource.
        self.cert_id = cert_id
        # The name of the certificate that is attached to the cloud product resource.
        self.cert_name = cert_name
        # The start date of the certificate that is attached to the cloud product resource. The value is a UNIX timestamp. Unit: milliseconds.
        self.cert_start_time = cert_start_time
        # The key ID used to access the cloud resource set.
        # 
        # > This parameter is returned only for multicloud deployments.
        self.cloud_access_id = cloud_access_id
        # The provider of the cloud product resource.
        # 
        # - **aliyun**: Alibaba Cloud
        # 
        # - **Tencent**: Tencent Cloud
        self.cloud_name = cloud_name
        # The cloud service.
        # 
        # <props="china">
        # 
        # - **SLB**: Classic Load Balancer (CLB) (China site only)
        # 
        # - **LIVE**: ApsaraVideo Live (China site only)
        # 
        # - **webHosting**: Cloud Web Hosting (China site only)
        # 
        # - **VOD**: ApsaraVideo VOD (China site only)
        # 
        # - **CR**: Container Registry (China site only)
        # 
        # 
        # 
        # - **DCDN**: DCDN
        # 
        # - **DDOS**: Anti-DDoS
        # 
        # - **CDN**: Alibaba Cloud CDN
        # 
        # - **ALB**: Application Load Balancer
        # 
        # - **APIGateway**: API Gateway
        # 
        # - **FC**: Function Compute
        # 
        # - **GA**: Global Accelerator
        # 
        # - **MSE**: MSE
        # 
        # - **NLB**: Network Load Balancer
        # 
        # - **OSS**: OSS
        # 
        # - **SAE**: SAE
        # 
        # - **TencentCDN**: Tencent CDN
        # 
        # - **WAF**: WAF
        self.cloud_product = cloud_product
        # The region ID of the cloud product resource from the cloud provider.
        self.cloud_region = cloud_region
        # Indicates whether the cloud product resource is a default resource.
        # 
        # - **1**: Default resource
        # 
        # - **0**: Not a default resource
        # 
        # > This parameter is returned only for deployments of SLB, NLB, ALB, and GA.
        self.default_resource = default_resource
        # The domain name that is attached to the cloud product resource.
        self.domain = domain
        # Indicates whether HTTPS is enabled for the cloud product resource.
        # 
        # - **1**: Enabled
        # 
        # - **0**: Disabled
        self.enable_https = enable_https
        # The time when the synchronized resource was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The time when the synchronized resource was last modified. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The ID of the cloud product resource.
        self.id = id
        # The instance ID of the cloud product resource.
        # 
        # > This parameter is returned only for deployments of SLB, NLB, ALB, and GA.
        self.instance_id = instance_id
        # The listener ID of the cloud product resource.
        # 
        # > This parameter is returned only for deployments of SLB, NLB, ALB, and GA.
        self.listener_id = listener_id
        # The listener port of the cloud product resource.
        # 
        # > This parameter is returned only for deployments of SLB, NLB, ALB, and GA.
        self.listener_port = listener_port
        # The region ID of the synchronized cloud product resource.
        self.region_id = region_id
        # Other metadata about the cloud product resource.
        self.remark = remark
        # The status of the synchronized cloud product resource.
        self.status = status
        # Indicates whether an Alibaba Cloud SSL certificate is used.
        # 
        # - **1**: Yes
        # 
        # - **0**: No
        # 
        # > This parameter is returned only for multicloud deployments.
        self.use_ssl = use_ssl
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_end_time is not None:
            result['CertEndTime'] = self.cert_end_time

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time

        if self.cloud_access_id is not None:
            result['CloudAccessId'] = self.cloud_access_id

        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name

        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product

        if self.cloud_region is not None:
            result['CloudRegion'] = self.cloud_region

        if self.default_resource is not None:
            result['DefaultResource'] = self.default_resource

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable_https is not None:
            result['EnableHttps'] = self.enable_https

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertEndTime') is not None:
            self.cert_end_time = m.get('CertEndTime')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')

        if m.get('CloudAccessId') is not None:
            self.cloud_access_id = m.get('CloudAccessId')

        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')

        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')

        if m.get('CloudRegion') is not None:
            self.cloud_region = m.get('CloudRegion')

        if m.get('DefaultResource') is not None:
            self.default_resource = m.get('DefaultResource')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EnableHttps') is not None:
            self.enable_https = m.get('EnableHttps')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

