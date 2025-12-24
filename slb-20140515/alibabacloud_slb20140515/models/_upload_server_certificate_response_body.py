# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class UploadServerCertificateResponseBody(DaraModel):
    def __init__(
        self,
        ali_cloud_certificate_id: str = None,
        ali_cloud_certificate_name: str = None,
        common_name: str = None,
        create_time: str = None,
        create_time_stamp: int = None,
        expire_time: str = None,
        expire_time_stamp: int = None,
        fingerprint: str = None,
        is_ali_cloud_certificate: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        server_certificate_id: str = None,
        server_certificate_name: str = None,
        subject_alternative_names: main_models.UploadServerCertificateResponseBodySubjectAlternativeNames = None,
    ):
        # The AliCloud certificate ID.
        self.ali_cloud_certificate_id = ali_cloud_certificate_id
        # The AliCloud certificate name.
        self.ali_cloud_certificate_name = ali_cloud_certificate_name
        # The domain name of the CA certificate.
        self.common_name = common_name
        # The time when the CA certificate is uploaded.
        self.create_time = create_time
        # The timestamp generated when the CA certificate is uploaded.
        self.create_time_stamp = create_time_stamp
        # The time when the CA certificate expires.
        self.expire_time = expire_time
        # The timestamp generated when the CA certificate expires.
        self.expire_time_stamp = expire_time_stamp
        # The fingerprint of the CA certificate.
        self.fingerprint = fingerprint
        # Indicates whether the certificate is provided by Alibaba Cloud Certificate Management Service. Valid values:
        # - **0**: The certificate is not provided by Alibaba Cloud Certificate Management Service.
        # - **1**: The certificate is provided by Alibaba Cloud Certificate Management Service.
        self.is_ali_cloud_certificate = is_ali_cloud_certificate
        # The ID of the region where the Classic Load Balancer (CLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the server certificate.
        self.server_certificate_id = server_certificate_id
        # The name of the server certificate.
        # 
        # The name must be 1 to 80 characters in length. It must start with an English letter. It can contain letters, numbers, periods (.), underscores (_), and hyphens (-).
        self.server_certificate_name = server_certificate_name
        # The subject alternative names.
        # 
        # A domain name list is supported. A maximum of 10 domain names are supported.
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        if self.subject_alternative_names:
            self.subject_alternative_names.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_cloud_certificate_id is not None:
            result['AliCloudCertificateId'] = self.ali_cloud_certificate_id

        if self.ali_cloud_certificate_name is not None:
            result['AliCloudCertificateName'] = self.ali_cloud_certificate_name

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_time_stamp is not None:
            result['ExpireTimeStamp'] = self.expire_time_stamp

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.is_ali_cloud_certificate is not None:
            result['IsAliCloudCertificate'] = self.is_ali_cloud_certificate

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        if self.server_certificate_name is not None:
            result['ServerCertificateName'] = self.server_certificate_name

        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliCloudCertificateId') is not None:
            self.ali_cloud_certificate_id = m.get('AliCloudCertificateId')

        if m.get('AliCloudCertificateName') is not None:
            self.ali_cloud_certificate_name = m.get('AliCloudCertificateName')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimeStamp') is not None:
            self.expire_time_stamp = m.get('ExpireTimeStamp')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('IsAliCloudCertificate') is not None:
            self.is_ali_cloud_certificate = m.get('IsAliCloudCertificate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        if m.get('ServerCertificateName') is not None:
            self.server_certificate_name = m.get('ServerCertificateName')

        if m.get('SubjectAlternativeNames') is not None:
            temp_model = main_models.UploadServerCertificateResponseBodySubjectAlternativeNames()
            self.subject_alternative_names = temp_model.from_map(m.get('SubjectAlternativeNames'))

        return self

class UploadServerCertificateResponseBodySubjectAlternativeNames(DaraModel):
    def __init__(
        self,
        subject_alternative_name: List[str] = None,
    ):
        self.subject_alternative_name = subject_alternative_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.subject_alternative_name is not None:
            result['SubjectAlternativeName'] = self.subject_alternative_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubjectAlternativeName') is not None:
            self.subject_alternative_name = m.get('SubjectAlternativeName')

        return self

