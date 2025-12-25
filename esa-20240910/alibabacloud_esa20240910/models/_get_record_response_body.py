# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetRecordResponseBody(DaraModel):
    def __init__(
        self,
        record_model: main_models.GetRecordResponseBodyRecordModel = None,
        request_id: str = None,
    ):
        # The information about the queried record.
        self.record_model = record_model
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.record_model:
            self.record_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_model is not None:
            result['RecordModel'] = self.record_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordModel') is not None:
            temp_model = main_models.GetRecordResponseBodyRecordModel()
            self.record_model = temp_model.from_map(m.get('RecordModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRecordResponseBodyRecordModel(DaraModel):
    def __init__(
        self,
        auth_conf: main_models.GetRecordResponseBodyRecordModelAuthConf = None,
        biz_name: str = None,
        comment: str = None,
        create_time: str = None,
        data: main_models.GetRecordResponseBodyRecordModelData = None,
        host_policy: str = None,
        proxied: bool = None,
        record_cname: str = None,
        record_id: int = None,
        record_name: str = None,
        record_source_type: str = None,
        record_type: str = None,
        site_id: int = None,
        site_name: str = None,
        ttl: int = None,
        update_time: str = None,
    ):
        # The origin authentication information of the CNAME record.
        self.auth_conf = auth_conf
        # The business scenario of the record for acceleration. Leave this parameter empty if your record is not proxied. Valid values:
        # 
        # *   **image_video**
        # *   **api**
        # *   **web**
        self.biz_name = biz_name
        # The comments of the record.
        self.comment = comment
        # The time when the record was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The DNS record information. The content returned by this parameter varies based on the record type.
        self.data = data
        # The origin host policy. This policy takes effect when the record type is CNAME. Valid values:
        # 
        # *   follow_hostname: matches the requested domain name.
        # *   follow_origin_domain: matches the origin\\"s domain name.
        self.host_policy = host_policy
        # Indicates whether the record is proxied. Only CNAME and A/AAAA records can be proxied. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.proxied = proxied
        # The CNAME. If you use CNAME setup when you add your website to ESA, the value is the CNAME that you configured then.
        self.record_cname = record_cname
        # The record ID.
        self.record_id = record_id
        # The record name.
        self.record_name = record_name
        # The origin type for the CNAME record. This parameter is required when you add a CNAME record. Valid values:
        # 
        # *   **OSS**: OSS bucket.
        # *   **S3**: S3 bucket.
        # *   **LB**: load balancer.
        # *   **OP**: origin pool.
        # *   **Domain**: domain name.
        # 
        # If you do not pass this parameter or if you leave its value empty, Domain is returned by default.
        self.record_source_type = record_source_type
        # The type of the DNS record, such as **A/AAAA, CNAME, and TXT**.
        self.record_type = record_type
        # The website ID.
        self.site_id = site_id
        # The website name.
        self.site_name = site_name
        # The TTL of the record. Unit: seconds. If the value is 1, the TTL of the record is determined by the system.
        self.ttl = ttl
        # The time when the record was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_cname is not None:
            result['RecordCname'] = self.record_cname

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.record_source_type is not None:
            result['RecordSourceType'] = self.record_source_type

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            temp_model = main_models.GetRecordResponseBodyRecordModelAuthConf()
            self.auth_conf = temp_model.from_map(m.get('AuthConf'))

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Data') is not None:
            temp_model = main_models.GetRecordResponseBodyRecordModelData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordCname') is not None:
            self.record_cname = m.get('RecordCname')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('RecordSourceType') is not None:
            self.record_source_type = m.get('RecordSourceType')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetRecordResponseBodyRecordModelData(DaraModel):
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
        tags: Dict[str, Any] = None,
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
        # The public key identification for the record. Valid values: 0 to 65535. This parameter is required when you add a CAA record.
        self.key_tag = key_tag
        # The algorithm policy used to match or validate the certificate, specified within the range 0 to 255. This parameter is required when you add SMIMEA or TLSA records.
        self.matching_type = matching_type
        # The port of the record. Valid values: 0 to 65535. This parameter is required when you add an SRV record.
        self.port = port
        # The priority of the record. Valid values: 0 to 65535. A smaller value indicates a higher priority. This parameter is required when you add MX, SRV, and URI records.
        self.priority = priority
        # The type of the certificate or public key, specified within the range of 0 to 255. This parameter is required when you add SMIMEA or TLSA records.
        self.selector = selector
        # The tag of the record. The Tag of a CAA record indicate its specific type and usage.
        self.tag = tag
        self.tags = tags
        # The certificate type of the record (in CERT records), or the public key type (in SSHFP records). This parameter is required when you add CERT or SSHFP records.
        self.type = type
        # The usage identifier of the record, specified within the range of 0 to 255. This parameter is required when you add SMIMEA or TLSA records.
        self.usage = usage
        # The record value or part of the record content. This parameter is returned when you add A/AAAA, CNAME, NS, MX, TXT, CAA, SRV, and URI records. It has different meanings based on types of records.
        # 
        # *   **A/AAAA**: the IP address. Multiple IP addresses are separated with commas (,). There is at least one IPv4 address.
        # *   **CNAME**: the target domain name.
        # *   **NS**: the nameserver for the domain name.
        # *   **MX**: a valid domain name of the target mail server.
        # *   **TXT**: a valid text string.
        # *   **CAA**: a valid domain name of the certificate authority.
        # *   **SRV**: a valid domain name of the target host.
        # *   **URI**: a valid URI string.
        self.value = value
        # The weight of the record, specified within the range of 0 to 65535. This parameter is required when you add SRV or URI records.
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

        if self.tags is not None:
            result['Tags'] = self.tags

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

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class GetRecordResponseBodyRecordModelAuthConf(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        # The access key ID of the account to which the origin server belongs. This parameter is returned if the origin type is OSS and AuthType is set to private_cross_account, or the origin type is S3 and AuthType is set to private.
        self.access_key = access_key
        # The authentication type of the origin server. Different origins support different authentication types. The origin type refers to the SourceType parameter in this operation. This parameter is returned if the origin type is OSS or S3Valid values:
        # 
        # *   **public**: public read. This value is returned when the origin is a public OSS or S3 bucket.
        # *   **private**: private read. This value is returned when the origin is a private S3 bucket.
        # *   **private_same_account**: private read in the same account. This value is returned when the origin is a private OSS bucket in your account.
        # *   **private_cross_account**: private read across accounts. This value is returned when the origin is a private OSS bucket in a different Alibaba Cloud account.
        self.auth_type = auth_type
        # The region of the origin. If the origin type is S3, you must specify this value. You can obtain the region information from the official website of S3.
        self.region = region
        # The secret access key of the account to which the origin server belongs. This parameter is returned if the origin type is OSS and AuthType is set to private_cross_account, or the origin type is S3 and AuthType is set to private.SecretKey
        self.secret_key = secret_key
        # The version of the signature algorithm. This parameter is returned when the origin type is S3 and AuthType is private. The following two types are supported:
        # 
        # *   **v2**
        # *   **v4**
        # 
        # If this parameter is left empty, the default value v4 is used.
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

