# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCloudResourcesRequest(DaraModel):
    def __init__(
        self,
        cert_ids: List[int] = None,
        cloud_name: str = None,
        cloud_product: str = None,
        current_page: int = None,
        keyword: str = None,
        secret_id: str = None,
        show_size: int = None,
    ):
        # The certificate IDs.
        self.cert_ids = cert_ids
        # The cloud service provider.
        # 
        # Valid values:
        # 
        # *   Tencent
        # *   Huawei
        # *   Aws
        # *   aliyun
        self.cloud_name = cloud_name
        # The cloud service.
        # 
        # Valid values when CloudName is set to aliyun:
        # 
        # *   SLB: Classic Load Balancer (CLB). This value is available only on the China site (aliyun.com).
        # *   LIVE: ApsaraVideo Live. This value is available only on the China site (aliyun.com).
        # *   webHosting: Cloud Web Hosting. This value is available only on the China site (aliyun.com).
        # *   VOD: ApsaraVideo VOD. This value is available only on the China site (aliyun.com).
        # *   CR: Container Registry. This value is available only on the China site (aliyun.com).
        # *   DCDN: Dynamic Content Delivery Network (DCDN).
        # *   DDOS: Anti-DDoS.
        # *   CDN: Alibaba Cloud CDN (CDN).
        # *   ALB: Application Load Balancer (ALB).
        # *   APIGateway: API Gateway.
        # *   FC: Function Compute.
        # *   GA: Global Accelerator (GA).
        # *   MSE: Microservices Engine (MSE).
        # *   NLB: Network Load Balancer (NLB).
        # *   OSS: Object Storage Service (OSS).
        # *   SAE: Serverless App Engine (SAE).
        # *   WAF: Web Application Firewall (WAF).
        # 
        # Valid values when CloudName is set to Tencent:
        # 
        # *   TencentCDN: Content Delivery Network (CDN).
        # *   TencentCLB: CLB.
        # *   TencentWAF: WAF.
        # 
        # Valid value when CloudName is set to Huawei:
        # 
        # *   HuaweiCDN: CDN.
        # 
        # Valid values when CloudName is set to Aws:
        # 
        # *   AwsCloudFront: Amazon CloudFront.
        # *   AwsCLB: CLB.
        # *   AwsALB: ALB.
        # *   AwsNLB: NLB.
        self.cloud_product = cloud_product
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The keyword of the domain name or instance ID bound to the cloud resource.
        self.keyword = keyword
        # The AccessKey ID that is used to access cloud resources.
        self.secret_id = secret_id
        # The number of entries per page. Default value: **20**.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids

        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name

        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')

        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')

        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self

