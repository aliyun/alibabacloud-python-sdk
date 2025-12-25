# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAbnormalCloudResourcesResponseBody(DaraModel):
    def __init__(
        self,
        abnormal_cloud_resources: List[main_models.DescribeAbnormalCloudResourcesResponseBodyAbnormalCloudResources] = None,
        request_id: str = None,
    ):
        self.abnormal_cloud_resources = abnormal_cloud_resources
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.abnormal_cloud_resources:
            for v1 in self.abnormal_cloud_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AbnormalCloudResources'] = []
        if self.abnormal_cloud_resources is not None:
            for k1 in self.abnormal_cloud_resources:
                result['AbnormalCloudResources'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abnormal_cloud_resources = []
        if m.get('AbnormalCloudResources') is not None:
            for k1 in m.get('AbnormalCloudResources'):
                temp_model = main_models.DescribeAbnormalCloudResourcesResponseBodyAbnormalCloudResources()
                self.abnormal_cloud_resources.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAbnormalCloudResourcesResponseBodyAbnormalCloudResources(DaraModel):
    def __init__(
        self,
        cloud_resource_id: str = None,
        details: List[main_models.DescribeAbnormalCloudResourcesResponseBodyAbnormalCloudResourcesDetails] = None,
        reason: str = None,
        resource_instance_id: str = None,
        resource_instance_name: str = None,
        resource_instance_port: int = None,
        resource_product: str = None,
    ):
        self.cloud_resource_id = cloud_resource_id
        self.details = details
        self.reason = reason
        self.resource_instance_id = resource_instance_id
        self.resource_instance_name = resource_instance_name
        self.resource_instance_port = resource_instance_port
        self.resource_product = resource_product

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_resource_id is not None:
            result['CloudResourceId'] = self.cloud_resource_id

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_instance_port is not None:
            result['ResourceInstancePort'] = self.resource_instance_port

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudResourceId') is not None:
            self.cloud_resource_id = m.get('CloudResourceId')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DescribeAbnormalCloudResourcesResponseBodyAbnormalCloudResourcesDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourceInstancePort') is not None:
            self.resource_instance_port = m.get('ResourceInstancePort')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        return self

class DescribeAbnormalCloudResourcesResponseBodyAbnormalCloudResourcesDetails(DaraModel):
    def __init__(
        self,
        applied_type: str = None,
        cert_name: str = None,
        code: str = None,
        common_name: str = None,
        expire_time: int = None,
        product_cert_id: str = None,
        product_cert_name: str = None,
        product_domain_extension: str = None,
    ):
        self.applied_type = applied_type
        self.cert_name = cert_name
        self.code = code
        self.common_name = common_name
        self.expire_time = expire_time
        self.product_cert_id = product_cert_id
        self.product_cert_name = product_cert_name
        self.product_domain_extension = product_domain_extension

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_type is not None:
            result['AppliedType'] = self.applied_type

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.code is not None:
            result['Code'] = self.code

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.product_cert_id is not None:
            result['ProductCertId'] = self.product_cert_id

        if self.product_cert_name is not None:
            result['ProductCertName'] = self.product_cert_name

        if self.product_domain_extension is not None:
            result['ProductDomainExtension'] = self.product_domain_extension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedType') is not None:
            self.applied_type = m.get('AppliedType')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ProductCertId') is not None:
            self.product_cert_id = m.get('ProductCertId')

        if m.get('ProductCertName') is not None:
            self.product_cert_name = m.get('ProductCertName')

        if m.get('ProductDomainExtension') is not None:
            self.product_domain_extension = m.get('ProductDomainExtension')

        return self

