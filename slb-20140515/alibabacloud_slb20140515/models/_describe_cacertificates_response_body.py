# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeCACertificatesResponseBody(DaraModel):
    def __init__(
        self,
        cacertificates: main_models.DescribeCACertificatesResponseBodyCACertificates = None,
        request_id: str = None,
    ):
        # The information about the CA certificate.
        self.cacertificates = cacertificates
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cacertificates:
            self.cacertificates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cacertificates is not None:
            result['CACertificates'] = self.cacertificates.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CACertificates') is not None:
            temp_model = main_models.DescribeCACertificatesResponseBodyCACertificates()
            self.cacertificates = temp_model.from_map(m.get('CACertificates'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCACertificatesResponseBodyCACertificates(DaraModel):
    def __init__(
        self,
        cacertificate: List[main_models.DescribeCACertificatesResponseBodyCACertificatesCACertificate] = None,
    ):
        self.cacertificate = cacertificate

    def validate(self):
        if self.cacertificate:
            for v1 in self.cacertificate:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CACertificate'] = []
        if self.cacertificate is not None:
            for k1 in self.cacertificate:
                result['CACertificate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cacertificate = []
        if m.get('CACertificate') is not None:
            for k1 in m.get('CACertificate'):
                temp_model = main_models.DescribeCACertificatesResponseBodyCACertificatesCACertificate()
                self.cacertificate.append(temp_model.from_map(k1))

        return self

class DescribeCACertificatesResponseBodyCACertificatesCACertificate(DaraModel):
    def __init__(
        self,
        cacertificate_id: str = None,
        cacertificate_name: str = None,
        common_name: str = None,
        create_time: str = None,
        create_time_stamp: int = None,
        expire_time: str = None,
        expire_time_stamp: int = None,
        fingerprint: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribeCACertificatesResponseBodyCACertificatesCACertificateTags = None,
    ):
        # The CA certificate ID.
        self.cacertificate_id = cacertificate_id
        # The CA certificate name.
        self.cacertificate_name = cacertificate_name
        # The domain name of the CA certificate.
        self.common_name = common_name
        # The time when the CA certificate was created. The time is in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The timestamp when the CA certificate was created. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_time_stamp = create_time_stamp
        # The time when the CA certificate expires. The time is in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.expire_time = expire_time
        # The timestamp that indicates when the CA certificate expires. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.expire_time_stamp = expire_time_stamp
        # The fingerprint of the CA certificate.
        self.fingerprint = fingerprint
        # The region of the CA certificate.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tag.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id

        if self.cacertificate_name is not None:
            result['CACertificateName'] = self.cacertificate_name

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')

        if m.get('CACertificateName') is not None:
            self.cacertificate_name = m.get('CACertificateName')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCACertificatesResponseBodyCACertificatesCACertificateTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeCACertificatesResponseBodyCACertificatesCACertificateTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCACertificatesResponseBodyCACertificatesCACertificateTagsTag] = None,
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
                temp_model = main_models.DescribeCACertificatesResponseBodyCACertificatesCACertificateTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCACertificatesResponseBodyCACertificatesCACertificateTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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

