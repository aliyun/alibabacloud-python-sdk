# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateRecordRequest(DaraModel):
    def __init__(
        self,
        auth_conf: main_models.CreateRecordRequestAuthConf = None,
        biz_name: str = None,
        comment: str = None,
        data: main_models.CreateRecordRequestData = None,
        host_policy: str = None,
        http_ports: str = None,
        https_ports: str = None,
        proxied: bool = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The origin authentication information for the CNAME record.
        self.auth_conf = auth_conf
        # Used to tag the business scenario of the DNS record. This parameter is required when proxy acceleration is enabled for the DNS record (i.e., when the proxied parameter is set to true), and is not required when proxy acceleration is disabled (i.e., when the proxied parameter is set to false). Valid values:
        # - **image_video**: Image and video.
        # - **api**: API.
        # - **web**: Web page.
        self.biz_name = biz_name
        # The comment for the record, with a maximum length of 100 characters.
        self.comment = comment
        # The DNS information of the record. Different types of records require different content for this field. For more information, see
        # <props="china">[Documentation](https://help.aliyun.com/document_detail/2708761.html)<props="intl">[Documentation](https://www.alibabacloud.com/help/doc-detail/2708761.html)
        # .
        # 
        # This parameter is required.
        self.data = data
        # The origin host policy. This takes effect when the record type is CNAME. It specifies the host policy for back-to-origin requests. Two modes are available:
        # 
        # - **follow_hostname**: Follow the request host.
        # - **follow_origin_domain**: Follow the origin domain.
        self.host_policy = host_policy
        self.http_ports = http_ports
        self.https_ports = https_ports
        # Specifies whether to enable proxy acceleration for the record. Only CNAME records or A/AAAA records (i.e., when the type parameter is set to A/AAAA or CNAME) can enable proxy acceleration. Valid values:
        # - **true**: Enable proxy acceleration.
        # - **false**: Disable proxy acceleration.
        self.proxied = proxied
        # The record name.
        # 
        # This parameter is required.
        self.record_name = record_name
        # The site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) API.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The origin type of the CNAME record. This parameter is required when adding a CNAME record (i.e., when the type parameter is set to CNAME). Valid values:
        # 
        # - **OSS**: OSS origin.
        # - **S3**: S3 origin.
        # - **LB**: Load balancer origin.
        # - **OP**: Origin pool origin.
        # - **Domain**: Standard domain origin.
        # 
        # If this parameter is not specified or is left empty, it defaults to Domain, which is the standard domain origin type.
        self.source_type = source_type
        # The time-to-live (TTL) of the record, in seconds. When set to 1, the TTL is automatic.
        # 
        # This parameter is required.
        self.ttl = ttl
        # The DNS type of the record, such as **A/AAAA**, **CNAME**, **TXT**, etc.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.auth_conf:
            self.auth_conf.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_conf is not None:
            result['AuthConf'] = self.auth_conf.to_map()

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy

        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            temp_model = main_models.CreateRecordRequestAuthConf()
            self.auth_conf = temp_model.from_map(m.get('AuthConf'))

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Data') is not None:
            temp_model = main_models.CreateRecordRequestData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateRecordRequestData(DaraModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        # The encryption algorithm used by the record, ranging from **0 to 255**. This field is required when adding CERT or SSHFP records.
        self.algorithm = algorithm
        # The public key certificate information of the record. This parameter is required when adding CERT, SMIMEA, or TLSA records.
        self.certificate = certificate
        # The public key fingerprint value of the record. This parameter is required when adding an SSHFP record.
        self.fingerprint = fingerprint
        # The flag of the record. The Flag of a CAA record indicates its priority and processing method, with a value range of **0 to 255**. This parameter is required when adding a CAA record.
        self.flag = flag
        # The public key identifier of the record, ranging from **0 to 65535**. This parameter is required when adding a CERT record.
        self.key_tag = key_tag
        # The algorithm policy used by the record to match or verify certificates, ranging from **0 to 255**. This parameter is required when adding SMIMEA or TLSA records.
        self.matching_type = matching_type
        # The port of the record, ranging from **0 to 65535**. This parameter is required when adding an SRV record.
        self.port = port
        # The priority of the record, ranging from **0 to 65535**. A smaller value indicates a higher priority. This parameter is required when adding MX, SRV, or URI records.
        self.priority = priority
        # The type of certificate or public key used by the record, ranging from **0 to 255**. This parameter is required when adding SMIMEA or TLSA records.
        self.selector = selector
        # The tag of the record. The Tag of a CAA record indicates its specific type and purpose. This parameter is required when adding a CAA record. Valid values for Tag:
        # - **issue**: Authorizes a specific CA to issue certificates for the domain. It is usually followed by the CA\\"s domain name.
        # - **issuewild**: Authorizes a specific CA to issue wildcard certificates for the domain (e.g., *.example.com).
        # - **iodef**: Specifies a URI for receiving reports about violations of CAA records.
        self.tag = tag
        # The certificate type of the record (for CERT records) or the public key type (for SSHFP records). This parameter is required when adding CERT or SSHFP records.
        self.type = type
        # The usage identifier of the record, ranging from **0 to 255**. This parameter is required when adding SMIMEA or TLSA records.
        self.usage = usage
        # The record value or partial content. This parameter is required when the record type is A/AAAA, CNAME, NS, MX, TXT, CAA, SRV, or URI. It represents different meanings for different record types:
        # 
        # - **A/AAAA**: The IP address to point to. Multiple IPs are separated by commas (,). At least one IPv4 address is required.
        # - **CNAME**: The target domain name to point to.
        # - **NS**: The name server for the specified domain.
        # - **MX**: A valid target mail server domain name.
        # - **TXT**: A valid text string.
        # - **CAA**: A valid certificate authority domain name.
        # - **SRV**: A valid target host domain name.
        # - **URI**: A valid URI string.
        self.value = value
        # The weight of the record, ranging from **0 to 65535**. This parameter is required when adding SRV or URI records.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag

        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type

        if self.port is not None:
            result['Port'] = self.port

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.selector is not None:
            result['Selector'] = self.selector

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.type is not None:
            result['Type'] = self.type

        if self.usage is not None:
            result['Usage'] = self.usage

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')

        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Selector') is not None:
            self.selector = m.get('Selector')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreateRecordRequestAuthConf(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        # The AccessKey of the account that owns the origin. This value is required when the origin type is OSS and the authentication type is private cross-account read, or when the origin type is S3 and the authentication type is private read.
        self.access_key = access_key
        # The origin authentication type. Different origin types support different authentication types. The origin type refers to the SourceType parameter in this API. When the origin type is OSS or S3, you need to specify the origin authentication type. Valid values:
        # - **public**: Public read. Select this value when the origin type is OSS or S3 and the origin has public read access.
        # - **private**: Private read. Select this value when the origin type is S3 and the origin has private read access.
        # - **private_same_account**: Private same-account read. Select this value when the origin type is OSS, the origin is under the same Alibaba Cloud account, and the origin has private read access.
        # - **private_cross_account**: Private cross-account read. Select this value when the origin type is OSS, the origin is not under the same Alibaba Cloud account, and the origin has private read access.
        self.auth_type = auth_type
        # The region where the origin is located. This value is required when the origin type is S3. The region information can be obtained from the official S3 website.
        self.region = region
        # The SecretKey of the account that owns the origin. This value is required when the origin type is OSS and the authentication type is private cross-account read, or when the origin type is S3 and the authentication type is private read.
        self.secret_key = secret_key
        # The signature algorithm version. This is required when the origin type is S3 and the authentication type is private read. The following two versions are supported:
        # - **v2**
        # - **v4**
        # 
        # If not specified, the default value is v4.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.region is not None:
            result['Region'] = self.region

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

