# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class CreateCloudResourceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        listen: main_models.CreateCloudResourceRequestListen = None,
        owner_user_id: str = None,
        redirect: main_models.CreateCloudResourceRequestRedirect = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        tag: List[main_models.CreateCloudResourceRequestTag] = None,
    ):
        # The ID of the WAF instance.
        # 
        # > Call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The listener configuration.
        # 
        # This parameter is required.
        self.listen = listen
        # The Alibaba Cloud account ID of the resource owner.
        self.owner_user_id = owner_user_id
        # The forwarding configuration.
        self.redirect = redirect
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The list of tags. You can add up to 20 tags.
        self.tag = tag

    def validate(self):
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.listen is not None:
            result['Listen'] = self.listen.to_map()

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Listen') is not None:
            temp_model = main_models.CreateCloudResourceRequestListen()
            self.listen = temp_model.from_map(m.get('Listen'))

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Redirect') is not None:
            temp_model = main_models.CreateCloudResourceRequestRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateCloudResourceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateCloudResourceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class CreateCloudResourceRequestRedirect(DaraModel):
    def __init__(
        self,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        max_body_size: int = None,
        read_timeout: int = None,
        request_headers: List[main_models.CreateCloudResourceRequestRedirectRequestHeaders] = None,
        write_timeout: int = None,
        xff_header_mode: int = None,
        xff_headers: List[str] = None,
        xff_proto: bool = None,
    ):
        # Specifies whether to enable persistent connections. Valid values:
        # 
        # - **true** (default): enables persistent connections.
        # 
        # - **false**: disables persistent connections.
        self.keepalive = keepalive
        # The number of requests that can be reused in a persistent connection. Valid values: 60 to 1000.
        # 
        # > The number of requests that are reused over a persistent connection.
        self.keepalive_requests = keepalive_requests
        # The timeout period for an idle persistent connection. Valid values: 10 to 3600. Default value: 3600. Unit: seconds.
        # 
        # > The period of time after which an idle persistent connection is released.
        self.keepalive_timeout = keepalive_timeout
        # The maximum size of a request body. Valid values: 2 to 10. Default value: 2. Unit: GB.
        # 
        # > This feature is available only for the WAF Ultimate edition.
        self.max_body_size = max_body_size
        # The read timeout period. Unit: seconds. Valid values: 1 to 3600.
        self.read_timeout = read_timeout
        # The value of this parameter is in the \\`[**{"k":"*****key*****","v":"*****value*****"}**]\\` format. ***key*** indicates the custom request header field. ***value*** indicates the value of the field.
        # 
        # > If the custom header field already exists in the request, the system overwrites the value of the custom header field with the specified value.
        self.request_headers = request_headers
        # The write timeout period. Unit: seconds. Valid values: 1 to 3600.
        self.write_timeout = write_timeout
        # The method that WAF uses to obtain the real IP address of a client. Valid values:
        # 
        # - **0**: No Layer 7 proxy is deployed before WAF.
        # 
        # - **1**: WAF reads the first value of the XFF header field to obtain the client IP address.
        # 
        # - **2**: WAF reads the value of a custom header field to obtain the client IP address.
        self.xff_header_mode = xff_header_mode
        # The list of custom header fields that are used to obtain the client IP address. The value is in the \\`[**"header1","header2",...**]\\` format.
        # 
        # > This parameter is required only when **XffHeaderMode** is set to 2, which indicates that WAF reads the value of a custom header field to obtain the client IP address.
        self.xff_headers = xff_headers
        # Specifies whether to use the X-Forwarded-Proto header to pass the WAF protocol. Valid values:
        # 
        # - **true** (default): passes the WAF protocol.
        # 
        # - **false**: does not pass the WAF protocol.
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
                temp_model = main_models.CreateCloudResourceRequestRedirectRequestHeaders()
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

class CreateCloudResourceRequestRedirectRequestHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom request header field.
        self.key = key
        # The value of the custom request header field.
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

class CreateCloudResourceRequestListen(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.CreateCloudResourceRequestListenCertificates] = None,
        cipher_suite: int = None,
        custom_ciphers: List[str] = None,
        enable_tlsv_3: bool = None,
        http_2enabled: bool = None,
        port: int = None,
        protocol: str = None,
        resource_instance_id: str = None,
        resource_product: str = None,
        resource_region_id: str = None,
        tlsversion: str = None,
    ):
        # The list of certificate IDs.
        self.certificates = certificates
        # The type of cipher suite to add. This parameter is used only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        # 
        # - **1**: Adds all cipher suites.
        # 
        # - **2**: Adds strong cipher suites. You can select this value only when **TLSVersion** is set to **tlsv1.2**.
        # 
        # - **99**: Adds custom cipher suites.
        self.cipher_suite = cipher_suite
        # The custom cipher suites to add. This parameter is used only when **CipherSuite** is set to **99**.
        self.custom_ciphers = custom_ciphers
        # Specifies whether to support TLS 1.3. This parameter is used only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        # 
        # - **true**: TLS 1.3 is supported.
        # 
        # - **false**: TLS 1.3 is not supported.
        self.enable_tlsv_3 = enable_tlsv_3
        # Specifies whether to enable HTTP/2. This parameter is used only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        # 
        # - **true**: enables HTTP/2.
        # 
        # - **false** (default): disables HTTP/2.
        self.http_2enabled = http_2enabled
        # The port of the cloud product that is added to WAF.
        # 
        # This parameter is required.
        self.port = port
        # The protocol type. Valid values:
        # 
        # - **http**: HTTP.
        # 
        # - **https**: HTTPS.
        # 
        # This parameter is required.
        self.protocol = protocol
        # The ID of the cloud product instance.
        # 
        # This parameter is required.
        self.resource_instance_id = resource_instance_id
        # The type of the cloud product. Valid values:
        # 
        # - **clb4**: Layer 4 CLB instance.
        # 
        # - **clb7**: Layer 7 CLB instance.
        # 
        # - **ecs**: ECS instance.
        # 
        # - **nlb**: Network Load Balancer (NLB) instance.
        # 
        # This parameter is required.
        self.resource_product = resource_product
        # The region ID of the cloud product.
        # 
        # > This parameter is required if the ID of the instance that you want to add has not been synchronized to WAF.
        self.resource_region_id = resource_region_id
        # The TLS version to add. This parameter is used only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        # 
        # - **tlsv1**
        # 
        # - **tlsv1.1**
        # 
        # - **tlsv1.2**
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

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.CreateCloudResourceRequestListenCertificates()
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

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')

        return self



class CreateCloudResourceRequestListenCertificates(DaraModel):
    def __init__(
        self,
        applied_type: str = None,
        certificate_id: str = None,
    ):
        # The type of the certificate for the HTTPS protocol. Valid values:
        # 
        # - **default**: the default certificate.
        # 
        # - **extension**: the additional certificate.
        self.applied_type = applied_type
        # The ID of the certificate to add.
        # 
        # > Call [DescribeResourceInstanceCerts](https://help.aliyun.com/document_detail/2718120.html) to query the IDs of all SSL certificates that are associated with the cloud product instance.
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

