# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeServerCertificatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        server_certificates: main_models.DescribeServerCertificatesResponseBodyServerCertificates = None,
    ):
        # The request ID.
        self.request_id = request_id
        self.server_certificates = server_certificates

    def validate(self):
        if self.server_certificates:
            self.server_certificates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.server_certificates is not None:
            result['ServerCertificates'] = self.server_certificates.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServerCertificates') is not None:
            temp_model = main_models.DescribeServerCertificatesResponseBodyServerCertificates()
            self.server_certificates = temp_model.from_map(m.get('ServerCertificates'))

        return self

class DescribeServerCertificatesResponseBodyServerCertificates(DaraModel):
    def __init__(
        self,
        server_certificate: List[main_models.DescribeServerCertificatesResponseBodyServerCertificatesServerCertificate] = None,
    ):
        self.server_certificate = server_certificate

    def validate(self):
        if self.server_certificate:
            for v1 in self.server_certificate:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServerCertificate'] = []
        if self.server_certificate is not None:
            for k1 in self.server_certificate:
                result['ServerCertificate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_certificate = []
        if m.get('ServerCertificate') is not None:
            for k1 in m.get('ServerCertificate'):
                temp_model = main_models.DescribeServerCertificatesResponseBodyServerCertificatesServerCertificate()
                self.server_certificate.append(temp_model.from_map(k1))

        return self

class DescribeServerCertificatesResponseBodyServerCertificatesServerCertificate(DaraModel):
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
        resource_group_id: str = None,
        server_certificate_id: str = None,
        server_certificate_name: str = None,
        subject_alternative_names: main_models.DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateSubjectAlternativeNames = None,
        tags: main_models.DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateTags = None,
    ):
        self.ali_cloud_certificate_id = ali_cloud_certificate_id
        self.ali_cloud_certificate_name = ali_cloud_certificate_name
        self.common_name = common_name
        self.create_time = create_time
        self.create_time_stamp = create_time_stamp
        self.expire_time = expire_time
        self.expire_time_stamp = expire_time_stamp
        self.fingerprint = fingerprint
        self.is_ali_cloud_certificate = is_ali_cloud_certificate
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.server_certificate_id = server_certificate_id
        self.server_certificate_name = server_certificate_name
        self.subject_alternative_names = subject_alternative_names
        self.tags = tags

    def validate(self):
        if self.subject_alternative_names:
            self.subject_alternative_names.validate()
        if self.tags:
            self.tags.validate()

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        if self.server_certificate_name is not None:
            result['ServerCertificateName'] = self.server_certificate_name

        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        if m.get('ServerCertificateName') is not None:
            self.server_certificate_name = m.get('ServerCertificateName')

        if m.get('SubjectAlternativeNames') is not None:
            temp_model = main_models.DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateSubjectAlternativeNames()
            self.subject_alternative_names = temp_model.from_map(m.get('SubjectAlternativeNames'))

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateSubjectAlternativeNames(DaraModel):
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

