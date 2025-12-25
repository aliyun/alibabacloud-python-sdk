# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudResourceAccessPortDetailsResponseBody(DaraModel):
    def __init__(
        self,
        access_port_details: List[main_models.DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the ports of cloud services that are added to WAF.
        self.access_port_details = access_port_details
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.access_port_details:
            for v1 in self.access_port_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessPortDetails'] = []
        if self.access_port_details is not None:
            for k1 in self.access_port_details:
                result['AccessPortDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_port_details = []
        if m.get('AccessPortDetails') is not None:
            for k1 in m.get('AccessPortDetails'):
                temp_model = main_models.DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetails()
                self.access_port_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetails(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsCertificates] = None,
        cipher_suite: int = None,
        cloud_resource_id: str = None,
        custom_ciphers: List[str] = None,
        enable_tlsv_3: bool = None,
        http_2enabled: bool = None,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        log_headers: List[main_models.DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsLogHeaders] = None,
        max_body_size: int = None,
        owner_user_id: str = None,
        port: int = None,
        protocol: str = None,
        read_timeout: int = None,
        status: int = None,
        sub_status: str = None,
        sub_status_details: List[main_models.DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsSubStatusDetails] = None,
        tlsversion: str = None,
        write_timeout: int = None,
        xff_header_mode: int = None,
        xff_headers: List[str] = None,
        xff_proto: bool = None,
    ):
        # The certificates that are associated with the ports of cloud services.
        self.certificates = certificates
        # The type of the cipher suites. Valid values:
        # 
        # *   **1**: all cipher suites.
        # *   **2**: strong cipher suites.
        # *   **99**: custom cipher suites.
        self.cipher_suite = cipher_suite
        self.cloud_resource_id = cloud_resource_id
        # The custom cipher suites that you want to add. This parameter is available only if you set **CipherSuite** to **99**.
        self.custom_ciphers = custom_ciphers
        # Indicates whether to support TLS 1.3. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_tlsv_3 = enable_tlsv_3
        # Indicates whether to enable HTTP/2. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.http_2enabled = http_2enabled
        # Indicates whether to enable the persistent connection feature. Valid values:
        # 
        # *   **true** (default)
        # *   **false:**
        self.keepalive = keepalive
        # The number of reused persistent connections. Valid values: 60 to 1000.
        # 
        # >  This parameter specifies the number of requests that reuse persistent connections after you enable the persistent connection feature.
        self.keepalive_requests = keepalive_requests
        # The timeout period for idle persistent connections. Valid values: 10 to 3600. Default value: 15. Unit: seconds.
        # 
        # >  If no new requests are initiated over the idle persistent connection within the specified timeout period, the connection is closed.
        self.keepalive_timeout = keepalive_timeout
        # The custom header field that you want to use to label requests that are processed by WAF.
        # 
        # >  This parameter is returned only when the traffic marking feature is enabled for the domain name.
        self.log_headers = log_headers
        self.max_body_size = max_body_size
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.owner_user_id = owner_user_id
        # The port of the cloud service that is added to WAF.
        self.port = port
        # The type of the protocol. Valid values:
        # 
        # *   **http**
        # *   **https**
        self.protocol = protocol
        # The timeout period for read connections. Unit: seconds. Valid values: 1 to 3600.
        self.read_timeout = read_timeout
        # The status of the domain name. Valid values:
        # 
        # *   **1**: indicates that the port is available.
        # *   **2**: indicates that the port is being created.
        # *   **3**: indicates that the port is being modified.
        # *   **4**: indicates that the port is being released.
        self.status = status
        self.sub_status = sub_status
        self.sub_status_details = sub_status_details
        # The version of the Transport Layer Security (TLS) protocol. Valid values:
        # 
        # *   **tlsv1**
        # *   **tlsv1.1**
        # *   **tlsv1.2**
        self.tlsversion = tlsversion
        # The timeout period for write connections. Unit: seconds. Valid values: 1 to 3600.
        self.write_timeout = write_timeout
        # The method that WAF uses to obtain the originating IP address of a client. Valid values:
        # 
        # *   **0**: No Layer 7 proxies are deployed in front of WAF.
        # *   **1**: WAF reads the first value of the X-Forwarded-For (XFF) header field as the originating IP address of the client.
        # *   **2**: WAF reads the value of a custom header field as the originating IP address of the client.
        self.xff_header_mode = xff_header_mode
        # The custom header field that is used to obtain the originating IP address of a client. Specify the value in the ["header1","header2",...] format.
        # 
        # >  This parameter is required only if you set **XffHeaderMode** to 2.
        self.xff_headers = xff_headers
        # Indicates whether to use the X-Forward-For-Proto header to identify the protocol used by WAF to forward requests to the origin server. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.xff_proto = xff_proto

    def validate(self):
        if self.certificates:
            for v1 in self.certificates:
                 if v1:
                    v1.validate()
        if self.log_headers:
            for v1 in self.log_headers:
                 if v1:
                    v1.validate()
        if self.sub_status_details:
            for v1 in self.sub_status_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.cipher_suite is not None:
            result['CipherSuite'] = self.cipher_suite

        if self.cloud_resource_id is not None:
            result['CloudResourceId'] = self.cloud_resource_id

        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers

        if self.enable_tlsv_3 is not None:
            result['EnableTLSv3'] = self.enable_tlsv_3

        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled

        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive

        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests

        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout

        result['LogHeaders'] = []
        if self.log_headers is not None:
            for k1 in self.log_headers:
                result['LogHeaders'].append(k1.to_map() if k1 else None)

        if self.max_body_size is not None:
            result['MaxBodySize'] = self.max_body_size

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        result['SubStatusDetails'] = []
        if self.sub_status_details is not None:
            for k1 in self.sub_status_details:
                result['SubStatusDetails'].append(k1.to_map() if k1 else None)

        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion

        if self.write_timeout is not None:
            result['WriteTimeout'] = self.write_timeout

        if self.xff_header_mode is not None:
            result['XffHeaderMode'] = self.xff_header_mode

        if self.xff_headers is not None:
            result['XffHeaders'] = self.xff_headers

        if self.xff_proto is not None:
            result['XffProto'] = self.xff_proto

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')

        if m.get('CloudResourceId') is not None:
            self.cloud_resource_id = m.get('CloudResourceId')

        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')

        if m.get('EnableTLSv3') is not None:
            self.enable_tlsv_3 = m.get('EnableTLSv3')

        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')

        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')

        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')

        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')

        self.log_headers = []
        if m.get('LogHeaders') is not None:
            for k1 in m.get('LogHeaders'):
                temp_model = main_models.DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsLogHeaders()
                self.log_headers.append(temp_model.from_map(k1))

        if m.get('MaxBodySize') is not None:
            self.max_body_size = m.get('MaxBodySize')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        self.sub_status_details = []
        if m.get('SubStatusDetails') is not None:
            for k1 in m.get('SubStatusDetails'):
                temp_model = main_models.DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsSubStatusDetails()
                self.sub_status_details.append(temp_model.from_map(k1))

        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')

        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')

        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')

        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')

        if m.get('XffProto') is not None:
            self.xff_proto = m.get('XffProto')

        return self

class DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsSubStatusDetails(DaraModel):
    def __init__(
        self,
        applied_type: str = None,
        cert_id: str = None,
        cert_name: str = None,
        common_name: str = None,
        domain: str = None,
        expire_time: int = None,
        product_cert_id: str = None,
        product_cert_name: str = None,
        reason_code: str = None,
    ):
        self.applied_type = applied_type
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.common_name = common_name
        self.domain = domain
        self.expire_time = expire_time
        self.product_cert_id = product_cert_id
        self.product_cert_name = product_cert_name
        self.reason_code = reason_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_type is not None:
            result['AppliedType'] = self.applied_type

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.product_cert_id is not None:
            result['ProductCertId'] = self.product_cert_id

        if self.product_cert_name is not None:
            result['ProductCertName'] = self.product_cert_name

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedType') is not None:
            self.applied_type = m.get('AppliedType')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ProductCertId') is not None:
            self.product_cert_id = m.get('ProductCertId')

        if m.get('ProductCertName') is not None:
            self.product_cert_name = m.get('ProductCertName')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        return self

class DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsLogHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the custom header field.
        self.key = key
        # The value of the custom header field.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeCloudResourceAccessPortDetailsResponseBodyAccessPortDetailsCertificates(DaraModel):
    def __init__(
        self,
        applied_type: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
    ):
        # The type of the HTTPS certificate. Valid values:
        # 
        # *   **default**: default certificate.
        # *   **extension**: additional certificate.
        self.applied_type = applied_type
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The name of the certificate.
        self.certificate_name = certificate_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_type is not None:
            result['AppliedType'] = self.applied_type

        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedType') is not None:
            self.applied_type = m.get('AppliedType')

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        return self

