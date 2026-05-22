# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class UpdateRecordRequest(DaraModel):
    def __init__(
        self,
        auth_conf: main_models.UpdateRecordRequestAuthConf = None,
        biz_name: str = None,
        comment: str = None,
        data: main_models.UpdateRecordRequestData = None,
        host_policy: str = None,
        proxied: bool = None,
        record_id: int = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The origin authentication information of the CNAME record.
        self.auth_conf = auth_conf
        # The business scenario of the record for acceleration. Leave the parameter empty if your record is not proxied. Valid values:
        # 
        # *   **video_image**: video and image.
        # *   **api**: API.
        # *   **web**: web page.
        self.biz_name = biz_name
        # The comments of the record.
        self.comment = comment
        # The DNS record information. The format of this field varies based on the record type. For more information, see [Add DNS records](https://www.alibabacloud.com/help/doc-detail/2708761.html).
        # 
        # This parameter is required.
        self.data = data
        # The origin host policy. This policy takes effect when the record type is CNAME. You can set the policy in two modes:
        # 
        # *   **follow_hostname**: match the requested domain name.
        # *   **follow_origin_domain**: match the origin\\"s domain name.
        self.host_policy = host_policy
        # Specifies whether to proxy the record. Only CNAME and A/AAAA records can be proxied. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.proxied = proxied
        # The record ID, which can be obtained by calling [ListRecords](https://help.aliyun.com/document_detail/2850265.html).
        # 
        # This parameter is required.
        self.record_id = record_id
        # The type of the origin for the CNAME record. This parameter is required when you add a CNAME record. Valid values:
        # 
        # *   **OSS** : OSS origin.
        # *   **S3** : S3 origin.
        # *   **LB**: Load Balancer origin.
        # *   **OP**: origin in an origin pool.
        # *   **Domain**: common domain name.
        # 
        # If you leave the parameter empty or set its value as null, the default is Domain, which is common domain name.
        self.source_type = source_type
        # The TTL of the record. Unit: seconds. The range is 30 to 86,400, or 1. If the value is 1, the TTL of the record is determined by the system.
        self.ttl = ttl
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

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_id is not None:
            result['RecordId'] = self.record_id

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
            temp_model = main_models.UpdateRecordRequestAuthConf()
            self.auth_conf = temp_model.from_map(m.get('AuthConf'))

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateRecordRequestData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateRecordRequestData(DaraModel):
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
        # The encryption algorithm used for the record, specified within the range from 0 to 255. This parameter is required when you add CERT or SSHFP records.
        self.algorithm = algorithm
        # The public key of the certificate. This parameter is required when you add CERT, SMIMEA, or TLSA records.
        self.certificate = certificate
        # The public key fingerprint of the record. This parameter is required when you add a SSHFP record.
        self.fingerprint = fingerprint
        # The flag bit of the record. The Flag for a CAA record indicates its priority and how it is processed, specified within the range of 0 to 255. This parameter is required when you add a CAA record.
        self.flag = flag
        # The public key identification for the record, specified within the range of 0 to 65,535. This parameter is required when you add a CAA record.
        self.key_tag = key_tag
        # The algorithm policy used to match or validate the certificate, specified within the range 0 to 255. This parameter is required when you add SMIMEA or TLSA records.
        self.matching_type = matching_type
        # The port of the record, specified within the range of 0 to 65,535. This parameter is required when you add an SRV record.
        self.port = port
        # The priority of the record, specified within the range of 0 to 65,535. A smaller value indicates a higher priority. This parameter is required when you add MX, SRV, and URI records.
        self.priority = priority
        # The type of certificate or public key, specified within the range of 0 to 255. This parameter is required when you add SMIMEA or TLSA records.
        self.selector = selector
        # The label of the record. The Tag of a CAA record indicate its specific type and usage. This parameter is required when you add a CAA record.
        self.tag = tag
        # The certificate type of the record (in CERT records), or the public key type (in SSHFP records). This parameter is required when you add CERT or SSHFP records.
        self.type = type
        # The usage identifier of the record, specified within the range of 0 to 255. This parameter is required when you add SMIMEA or TLSA records.
        self.usage = usage
        # The record value or part of the record content. This parameter is required when you add A/AAAA, CNAME, NS, MX, TXT, CAA, SRV, and URI records. It has different meanings based on different types of records:
        # 
        # *   **A/AAAA**: the IP address(es). Separate multiple IPs with commas (,). You must have at least one IPv4 address.
        # *   **CNAME**: the target domain name.
        # *   **NS**: the name servers for the domain name.
        # *   **MX**: a valid domain name of the target mail server.
        # *   **TXT**: a valid text string.
        # *   **CAA**: a valid domain name of the certificate authority.
        # *   **SRV**: a valid domain name of the target host.
        # *   **URI**: a valid URI string.
        self.value = value
        # The weight of the record, specified within the range of 0 to 65,535. This parameter is required when you add SRV or URI records.
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

class UpdateRecordRequestAuthConf(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        # The access key of the account to which the origin server belongs. This parameter is required when the SourceType is OSS, and AuthType is private_same_account, or when the SourceType is S3 and AuthType is private.
        self.access_key = access_key
        # The authentication type of the origin server. Different origins support different authentication types. The type of origin refers to the SourceType parameter in this operation. If the type of origin is OSS or S3, you must specify the authentication type of the origin. Valid values:
        # 
        # *   **public**: public read. Select this value when the origin type is OSS or S3 and the origin access is public read.
        # *   **private**: private read. Select this value when the origin type is S3 and the origin access is private read.
        # *   **private_same_account**: private read under the same account. Select this value when the origin type is OSS, the origins belong to the same Alibaba Cloud account, and the origins have private read access.
        self.auth_type = auth_type
        # The version of the signature algorithm. This parameter is required when the origin type is S3 and AuthType is private. The following two types are supported:
        # 
        # *   **v2**
        # *   **v4**
        # 
        # If you leave this parameter empty, the default value v4 is used.
        self.region = region
        # The secret access key of the account to which the origin server belongs. This parameter is required when the SourceType is OSS, and AuthType is private_same_account, or when the SourceType is S3 and AuthType is private.
        self.secret_key = secret_key
        # The region of the origin. If the origin type is S3, you must specify this value. You can get the region information from the official website of S3.
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

