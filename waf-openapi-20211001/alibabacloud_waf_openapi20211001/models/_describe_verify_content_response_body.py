# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyContentResponseBody(DaraModel):
    def __init__(
        self,
        dns_content: main_models.DescribeVerifyContentResponseBodyDnsContent = None,
        file_content: main_models.DescribeVerifyContentResponseBodyFileContent = None,
        request_id: str = None,
        verify_result: bool = None,
    ):
        # The DNS-based verification content, including the TXT record details.
        self.dns_content = dns_content
        # The file-based verification content, including the file name, path, and download URL.
        self.file_content = file_content
        # The request ID.
        self.request_id = request_id
        # Indicates whether the domain ownership verification is successful.
        self.verify_result = verify_result

    def validate(self):
        if self.dns_content:
            self.dns_content.validate()
        if self.file_content:
            self.file_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_content is not None:
            result['DnsContent'] = self.dns_content.to_map()

        if self.file_content is not None:
            result['FileContent'] = self.file_content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsContent') is not None:
            temp_model = main_models.DescribeVerifyContentResponseBodyDnsContent()
            self.dns_content = temp_model.from_map(m.get('DnsContent'))

        if m.get('FileContent') is not None:
            temp_model = main_models.DescribeVerifyContentResponseBodyFileContent()
            self.file_content = temp_model.from_map(m.get('FileContent'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')

        return self

class DescribeVerifyContentResponseBodyFileContent(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        file_name: str = None,
        top_domain: str = None,
        value: str = None,
        verify_path: str = None,
    ):
        # The download URL of the verification file.
        self.download_url = download_url
        # The name of the verification file.
        self.file_name = file_name
        # The root domain of the domain name to be verified.
        self.top_domain = top_domain
        # The content of the verification file.
        self.value = value
        # The URL that is used to access the verification file.
        self.verify_path = verify_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.top_domain is not None:
            result['TopDomain'] = self.top_domain

        if self.value is not None:
            result['Value'] = self.value

        if self.verify_path is not None:
            result['VerifyPath'] = self.verify_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('TopDomain') is not None:
            self.top_domain = m.get('TopDomain')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('VerifyPath') is not None:
            self.verify_path = m.get('VerifyPath')

        return self

class DescribeVerifyContentResponseBodyDnsContent(DaraModel):
    def __init__(
        self,
        rr: str = None,
        type: str = None,
        value: str = None,
    ):
        # The host record of the DNS TXT record used for domain ownership verification.
        self.rr = rr
        # The type of the DNS record used for verification.
        self.type = type
        # The value of the DNS TXT record used for verification.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rr is not None:
            result['RR'] = self.rr

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

