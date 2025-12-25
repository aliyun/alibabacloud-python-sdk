# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class ModifyCloudResourceRequest(DaraModel):
    def __init__(
        self,
        cloud_resource_id: str = None,
        instance_id: str = None,
        listen: main_models.ModifyCloudResourceRequestListen = None,
        redirect: main_models.ModifyCloudResourceRequestRedirect = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        self.cloud_resource_id = cloud_resource_id
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The listener configurations.
        # 
        # This parameter is required.
        self.listen = listen
        # The forwarding configurations.
        self.redirect = redirect
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_resource_id is not None:
            result['CloudResourceId'] = self.cloud_resource_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.listen is not None:
            result['Listen'] = self.listen.to_map()

        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudResourceId') is not None:
            self.cloud_resource_id = m.get('CloudResourceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Listen') is not None:
            temp_model = main_models.ModifyCloudResourceRequestListen()
            self.listen = temp_model.from_map(m.get('Listen'))

        if m.get('Redirect') is not None:
            temp_model = main_models.ModifyCloudResourceRequestRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

class ModifyCloudResourceRequestRedirect(DaraModel):
    def __init__(
        self,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        max_body_size: int = None,
        read_timeout: int = None,
        request_headers: List[main_models.ModifyCloudResourceRequestRedirectRequestHeaders] = None,
        write_timeout: int = None,
        xff_header_mode: int = None,
        xff_headers: List[str] = None,
        xff_proto: bool = None,
    ):
        # Specifies whether to enable the persistent connection feature. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.keepalive = keepalive
        # The number of reused persistent connections. Valid values: 60 to 1000.
        # 
        # >  This parameter specifies the number of persistent connections that can be reused after you enable the persistent connection feature.
        self.keepalive_requests = keepalive_requests
        # The timeout period of idle persistent connections. Valid values: 10 to 3600. Default value: 3600. Unit: seconds.
        # 
        # >  This parameter specifies the period of time after which an idle persistent connection is closed.
        self.keepalive_timeout = keepalive_timeout
        self.max_body_size = max_body_size
        # The timeout period of read connections. Unit: seconds. Valid values: 1 to 3600.
        self.read_timeout = read_timeout
        # The custom header fields, which are key-value pairs. The fields are used to mark requests that pass through WAF.
        self.request_headers = request_headers
        # The timeout period of write connections. Unit: seconds. Valid values: 1 to 3600.
        self.write_timeout = write_timeout
        # The method that is used to obtain the originating IP address of a client. Valid values:
        # 
        # *   **0**: No Layer 7 proxies are deployed in front of WAF.
        # *   **1**: WAF reads the first value of the X-Forwarded-For (XFF) header field as the originating IP address of the client.
        # *   **2**: WAF reads the value of a custom header field as the originating IP address of the client.
        self.xff_header_mode = xff_header_mode
        # The custom header fields that are used to obtain the originating IP address of a client. Specify the value in the ["header1","header2",...] format.
        # 
        # >  This parameter is required only if you set **XffHeaderMode** to 2.
        self.xff_headers = xff_headers
        # Specifies whether to use the X-Forward-For-Proto header field to pass the protocol used by WAF to forward requests to the origin server. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.xff_proto = xff_proto

    def validate(self):
        if self.request_headers:
            for v1 in self.request_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive

        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests

        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout

        if self.max_body_size is not None:
            result['MaxBodySize'] = self.max_body_size

        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout

        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k1 in self.request_headers:
                result['RequestHeaders'].append(k1.to_map() if k1 else None)

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
        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')

        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')

        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')

        if m.get('MaxBodySize') is not None:
            self.max_body_size = m.get('MaxBodySize')

        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')

        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k1 in m.get('RequestHeaders'):
                temp_model = main_models.ModifyCloudResourceRequestRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k1))

        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')

        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')

        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')

        if m.get('XffProto') is not None:
            self.xff_proto = m.get('XffProto')

        return self

class ModifyCloudResourceRequestRedirectRequestHeaders(DaraModel):
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

class ModifyCloudResourceRequestListen(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.ModifyCloudResourceRequestListenCertificates] = None,
        cipher_suite: int = None,
        custom_ciphers: List[str] = None,
        enable_tlsv_3: bool = None,
        http_2enabled: bool = None,
        port: int = None,
        protocol: str = None,
        resource_instance_id: str = None,
        resource_product: str = None,
        tlsversion: str = None,
    ):
        # The certificates.
        self.certificates = certificates
        # The type of the cipher suites that you want to add. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **1**: all cipher suites.
        # *   **2**: strong cipher suites. This value is available only if you set **TLSVersion** to **tlsv1.2**.
        # *   **99**: custom cipher suites.
        self.cipher_suite = cipher_suite
        # The custom cipher suites that you want to add.
        self.custom_ciphers = custom_ciphers
        # Specifies whether to support TLS 1.3. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_tlsv_3 = enable_tlsv_3
        # Specifies whether to enable HTTP/2. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.http_2enabled = http_2enabled
        # The port of the cloud service instance that is added to WAF.
        self.port = port
        # The protocol type. Valid values:
        # 
        # *   **http**
        # *   **https**
        # 
        # This parameter is required.
        self.protocol = protocol
        # The ID of the cloud service instance that is added to WAF.
        self.resource_instance_id = resource_instance_id
        # The type of the cloud service. Valid values:
        # 
        # *   **clb4**: Layer 4 Classic Load Balancer (CLB).
        # *   **clb7**: Layer 7 CLB.
        # *   **ecs**: Elastic Compute Service (ECS).
        # *   **nlb**: Network Load Balancer (NLB).
        self.resource_product = resource_product
        # The Transport Layer Security (TLS) version that you want to add. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **tlsv1**
        # *   **tlsv1.1**
        # *   **tlsv1.2**
        self.tlsversion = tlsversion

    def validate(self):
        if self.certificates:
            for v1 in self.certificates:
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

        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers

        if self.enable_tlsv_3 is not None:
            result['EnableTLSv3'] = self.enable_tlsv_3

        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.ModifyCloudResourceRequestListenCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')

        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')

        if m.get('EnableTLSv3') is not None:
            self.enable_tlsv_3 = m.get('EnableTLSv3')

        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')

        return self

class ModifyCloudResourceRequestListenCertificates(DaraModel):
    def __init__(
        self,
        applied_type: str = None,
        certificate_id: str = None,
    ):
        # The type of the certificate. Valid values:
        # 
        # *   **default**: default certificate.
        # *   **extension**: additional certificate.
        self.applied_type = applied_type
        # The ID of the certificate.
        self.certificate_id = certificate_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedType') is not None:
            self.applied_type = m.get('AppliedType')

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        return self

