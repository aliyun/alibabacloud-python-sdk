# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetMultipartFileUploadInfosResponseBody(DaraModel):
    def __init__(
        self,
        multipart_header_signature_infos: List[main_models.GetMultipartFileUploadInfosResponseBodyMultipartHeaderSignatureInfos] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.multipart_header_signature_infos = multipart_header_signature_infos
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.multipart_header_signature_infos:
            for v1 in self.multipart_header_signature_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['multipartHeaderSignatureInfos'] = []
        if self.multipart_header_signature_infos is not None:
            for k1 in self.multipart_header_signature_infos:
                result['multipartHeaderSignatureInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.multipart_header_signature_infos = []
        if m.get('multipartHeaderSignatureInfos') is not None:
            for k1 in m.get('multipartHeaderSignatureInfos'):
                temp_model = main_models.GetMultipartFileUploadInfosResponseBodyMultipartHeaderSignatureInfos()
                self.multipart_header_signature_infos.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetMultipartFileUploadInfosResponseBodyMultipartHeaderSignatureInfos(DaraModel):
    def __init__(
        self,
        header_signature_info: main_models.GetMultipartFileUploadInfosResponseBodyMultipartHeaderSignatureInfosHeaderSignatureInfo = None,
        part_number: int = None,
    ):
        self.header_signature_info = header_signature_info
        self.part_number = part_number

    def validate(self):
        if self.header_signature_info:
            self.header_signature_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header_signature_info is not None:
            result['HeaderSignatureInfo'] = self.header_signature_info.to_map()

        if self.part_number is not None:
            result['PartNumber'] = self.part_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderSignatureInfo') is not None:
            temp_model = main_models.GetMultipartFileUploadInfosResponseBodyMultipartHeaderSignatureInfosHeaderSignatureInfo()
            self.header_signature_info = temp_model.from_map(m.get('HeaderSignatureInfo'))

        if m.get('PartNumber') is not None:
            self.part_number = m.get('PartNumber')

        return self

class GetMultipartFileUploadInfosResponseBodyMultipartHeaderSignatureInfosHeaderSignatureInfo(DaraModel):
    def __init__(
        self,
        expiration_seconds: int = None,
        headers: Dict[str, str] = None,
        internal_resource_urls: List[str] = None,
        region: str = None,
        resource_urls: List[str] = None,
    ):
        self.expiration_seconds = expiration_seconds
        self.headers = headers
        self.internal_resource_urls = internal_resource_urls
        self.region = region
        self.resource_urls = resource_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_seconds is not None:
            result['ExpirationSeconds'] = self.expiration_seconds

        if self.headers is not None:
            result['Headers'] = self.headers

        if self.internal_resource_urls is not None:
            result['InternalResourceUrls'] = self.internal_resource_urls

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_urls is not None:
            result['ResourceUrls'] = self.resource_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirationSeconds') is not None:
            self.expiration_seconds = m.get('ExpirationSeconds')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('InternalResourceUrls') is not None:
            self.internal_resource_urls = m.get('InternalResourceUrls')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceUrls') is not None:
            self.resource_urls = m.get('ResourceUrls')

        return self

