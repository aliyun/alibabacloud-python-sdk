# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListWorkerResourceResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.ListWorkerResourceResponseBodyData] = None,
        request_id: str = None,
        show_size: int = None,
        total: int = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The number of entries per page. Default value: **50**.
        self.show_size = show_size
        # The total number of entries returned.
        self.total = total

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListWorkerResourceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListWorkerResourceResponseBodyData(DaraModel):
    def __init__(
        self,
        cert_domain: str = None,
        cert_id: int = None,
        cert_instance_id: str = None,
        cert_name: str = None,
        cloud_name: str = None,
        cloud_product: str = None,
        cloud_region: str = None,
        default_resource: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        job_id: int = None,
        listener_id: str = None,
        namespace_id: str = None,
        order_id: int = None,
        port: int = None,
        region_id: str = None,
        resource_cert_id: int = None,
        resource_domain: str = None,
        resource_id: int = None,
        status: str = None,
        user_id: int = None,
    ):
        # The domain name bound to the certificate in the worker task.
        self.cert_domain = cert_domain
        # The ID of the certificate in the worker task.
        self.cert_id = cert_id
        # The instance ID of the certificate in the worker task.
        self.cert_instance_id = cert_instance_id
        # The name of the certificate in the worker task.
        self.cert_name = cert_name
        # The cloud service provider to which the cloud resource in the worker task belongs.
        # 
        # >  This parameter is not returned if you deploy certificates to Alibaba Cloud services.
        self.cloud_name = cloud_name
        # The cloud service to which the cloud resource in the worker task belongs. Valid values:
        # 
        # *   **CDN**: Alibaba Cloud CDN (CDN). This value is supported only at the China site (aliyun.com).
        # *   **SLB**: Classic Load Balancer (CLB). This value is supported only at the China site (aliyun.com).
        # *   **DCDN**: Dynamic Content Delivery Network (DCDN). This value is supported only at the China site (aliyun.com).
        # *   **DDOS**: Anti-DDoS. This value is supported only at the China site (aliyun.com).
        # *   **LIVE**: ApsaraVideo Live. This value is supported only at the China site (aliyun.com).
        # *   **webHosting**: Cloud Web Hosting. This value is supported only at the China site (aliyun.com).
        # *   **VOD**: ApsaraVideo VOD. This value is supported only at the China site (aliyun.com).
        # *   **CR**: Container Registry. This value is supported only at the China site (aliyun.com).
        # *   **ALB**: Application Load Balancer (ALB).
        # *   **APIGateway**: API Gateway.
        # *   **FC**: Function Compute.
        # *   **GA**: Global Accelerator (GA).
        # *   **MSE**: Microservices Engine (MSE).
        # *   **NLB**: Network Load Balancer (NLB).
        # *   **OSS**: Object Storage Service (OSS).
        # *   **SAE**: Serverless App Engine (SAE).
        # *   **TencentCDN**: Tencent Cloud Content Delivery Network (CDN).
        # *   **WAF**: Web Application Firewall (WAF).
        self.cloud_product = cloud_product
        # The original region ID of the cloud resource in the worker task. The value is the region ID defined by the cloud service provider. This parameter is required only when you deploy certificates to services of multiple clouds.
        self.cloud_region = cloud_region
        # Indicates whether the cloud resource in the worker task is the default resource. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.default_resource = default_resource
        # The time when the worker task was created. The time is a timestamp in seconds.
        self.gmt_create = gmt_create
        # The time when the worker task was last modified. The time is a timestamp in seconds.
        self.gmt_modified = gmt_modified
        # The ID of the worker task.
        self.id = id
        # The ID of the cloud resource in the worker task.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.instance_id = instance_id
        # The ID of the deployment task to which the worker task belongs.
        self.job_id = job_id
        # The listener ID of the cloud resource in the worker task.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.listener_id = listener_id
        # The ID of the namespace in SAE. This parameter is returned only if you deploy certificates to SAE.
        self.namespace_id = namespace_id
        # The order ID of the worker task, which is the same as the order ID of the certificate.
        # 
        # >  If the CertId parameter is returned, this parameter is not returned.
        self.order_id = order_id
        # The listening port of the cloud resource in the worker task.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.port = port
        # The region ID of the cloud resource in the worker task.
        self.region_id = region_id
        # The ID of the certificate that was originally bound to the cloud resource in the worker task.
        self.resource_cert_id = resource_cert_id
        # The domain name that was originally bound to the cloud resource in the worker task.
        self.resource_domain = resource_domain
        # The ID of the cloud resource in the worker task.
        self.resource_id = resource_id
        # The status of the worker task. Valid values:
        # 
        # *   **editing**
        # *   **pending**
        # *   **scheduling**
        # *   **processing**
        # *   **error**
        # *   **success**
        # *   **rollback**
        # *   **rollback_success**
        # *   **rollback_error**
        self.status = status
        # The ID of the Alibaba Cloud account to which the worker task belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_domain is not None:
            result['CertDomain'] = self.cert_domain

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_instance_id is not None:
            result['CertInstanceId'] = self.cert_instance_id

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name

        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product

        if self.cloud_region is not None:
            result['CloudRegion'] = self.cloud_region

        if self.default_resource is not None:
            result['DefaultResource'] = self.default_resource

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_cert_id is not None:
            result['ResourceCertId'] = self.resource_cert_id

        if self.resource_domain is not None:
            result['ResourceDomain'] = self.resource_domain

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDomain') is not None:
            self.cert_domain = m.get('CertDomain')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertInstanceId') is not None:
            self.cert_instance_id = m.get('CertInstanceId')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')

        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')

        if m.get('CloudRegion') is not None:
            self.cloud_region = m.get('CloudRegion')

        if m.get('DefaultResource') is not None:
            self.default_resource = m.get('DefaultResource')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceCertId') is not None:
            self.resource_cert_id = m.get('ResourceCertId')

        if m.get('ResourceDomain') is not None:
            self.resource_domain = m.get('ResourceDomain')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

