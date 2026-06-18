# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class BatchCreateRecordsRequest(DaraModel):
    def __init__(
        self,
        record_list: List[main_models.BatchCreateRecordsRequestRecordList] = None,
        site_id: int = None,
    ):
        # The list of DNS records to create.
        # 
        # This parameter is required.
        self.record_list = record_list
        # The ID of the site. You can get this ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        if self.record_list:
            for v1 in self.record_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordList'] = []
        if self.record_list is not None:
            for k1 in self.record_list:
                result['RecordList'].append(k1.to_map() if k1 else None)

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_list = []
        if m.get('RecordList') is not None:
            for k1 in m.get('RecordList'):
                temp_model = main_models.BatchCreateRecordsRequestRecordList()
                self.record_list.append(temp_model.from_map(k1))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class BatchCreateRecordsRequestRecordList(DaraModel):
    def __init__(
        self,
        auth_conf: main_models.BatchCreateRecordsRequestRecordListAuthConf = None,
        biz_name: str = None,
        data: main_models.BatchCreateRecordsRequestRecordListData = None,
        http_ports: str = None,
        https_ports: str = None,
        proxied: bool = None,
        record_name: str = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The origin authentication information for the CNAME record.
        self.auth_conf = auth_conf
        # The use case for proxy acceleration. Valid values:
        # 
        # - **image_video**: Images and videos.
        # 
        # - **api**: APIs.
        # 
        # - **web**: Web pages.
        self.biz_name = biz_name
        # The content of the DNS record. The required fields depend on the record type.
        # 
        # This parameter is required.
        self.data = data
        self.http_ports = http_ports
        self.https_ports = https_ports
        # Specifies whether to enable proxy acceleration for the record. Only CNAME and A/AAAA records support proxy acceleration. Valid values:
        # 
        # - **true**: Enables proxy acceleration.
        # 
        # - **false**: Disables proxy acceleration.
        # 
        # This parameter is required.
        self.proxied = proxied
        # The name of the record.
        # 
        # This parameter is required.
        self.record_name = record_name
        # The origin type for the CNAME record. This parameter is required when you add a CNAME record. Valid values:
        # 
        # - **OSS**: An OSS origin.
        # 
        # - **S3**: An S3 origin.
        # 
        # - **LB**: A load balancer origin.
        # 
        # - **OP**: An origin pool origin.
        # 
        # - **Domain**: A domain name origin.
        # 
        # If omitted or left empty, this parameter defaults to `Domain`.
        self.source_type = source_type
        # The Time to Live (TTL) for the record, in seconds. A value of `1` indicates an automatic TTL.
        # 
        # This parameter is required.
        self.ttl = ttl
        # The type of the DNS record.
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

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_name is not None:
            result['RecordName'] = self.record_name

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
            temp_model = main_models.BatchCreateRecordsRequestRecordListAuthConf()
            self.auth_conf = temp_model.from_map(m.get('AuthConf'))

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Data') is not None:
            temp_model = main_models.BatchCreateRecordsRequestRecordListData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class BatchCreateRecordsRequestRecordListData(DaraModel):
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
        # The algorithm identifier for the record. Valid values range from **0-255**. This parameter applies to CERT and SSHFP records.
        self.algorithm = algorithm
        # The certificate or public key data for the record. This parameter applies to CERT, SMIMEA, and TLSA records.
        self.certificate = certificate
        # The public key fingerprint for the record. This parameter applies to SSHFP records.
        self.fingerprint = fingerprint
        # The flag for the CAA record, which specifies how a Certificate Authority must handle the record. Valid values range from **0-255**.
        self.flag = flag
        # The public key identifier for the record. Valid values range from **0-65535**. This parameter applies to CERT records.
        self.key_tag = key_tag
        # The algorithm policy used to match or validate a certificate. Valid values range from **0-255**. This parameter applies to SMIMEA and TLSA records.
        self.matching_type = matching_type
        # The port number for the record. Valid values range from **0-65535**. This parameter applies only to SRV records.
        self.port = port
        # The priority of the record. Valid values range from **0-65535**. A lower value indicates a higher priority. This parameter is required for MX, SRV, or URI records.
        self.priority = priority
        # The type of certificate or public key used by the record. Valid values range from **0-255**. This parameter applies to SMIMEA and TLSA records.
        self.selector = selector
        # The tag for the CAA record, which specifies its type and purpose, such as `issue`, `issuewild`, or `iodef`.
        self.tag = tag
        # The certificate type for a CERT record or the public key type for an SSHFP record.
        self.type = type
        # The usage identifier for the record. Valid values range from **0-255**. This parameter applies to SMIMEA and TLSA records.
        self.usage = usage
        # The record value. The format depends on the record type.
        # 
        # - **A/AAAA**: An IP address.
        # 
        # - **CNAME**: The target domain name.
        # 
        # - **MX**: The domain name of the target mail server.
        # 
        # - **TXT**: A text string.
        # 
        # - **CAA**: The domain name of a Certificate Authority.
        # 
        # - **SRV**: The domain name of the target host.
        # 
        # - **URI**: A URI string.
        self.value = value
        # The weight of the record. Valid values range from **0-65535**. This parameter applies to SRV and URI records.
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

class BatchCreateRecordsRequestRecordListAuthConf(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        # The access key ID of the account that owns the origin. This parameter is required when the origin type is `OSS` and the authentication type is `private_cross_account`, or when the origin type is `S3` and the authentication type is `private`.
        self.access_key = access_key
        # The type of origin authentication. Supported authentication types depend on the origin type, which is specified by the `SourceType` parameter. This parameter is required when the origin type is `OSS` or `S3`. Valid values:
        # 
        # - **public**: For OSS or S3 origins with public read access.
        # 
        # - **private**: For S3 origins with private read access.
        # 
        # - **private_same_account**: For OSS origins with private read access within the same Alibaba Cloud account.
        # 
        # - **private_cross_account**: For OSS origins with private read access from a different Alibaba Cloud account.
        self.auth_type = auth_type
        # The region where the S3 origin is located. This parameter is required when the origin type is `S3`. For a list of valid region IDs, refer to the official S3 documentation.
        self.region = region
        # The secret key associated with the specified AccessKey. This parameter is required when the origin type is `OSS` and the authentication type is `private_cross_account`, or when the origin type is `S3` and the authentication type is `private`.
        self.secret_key = secret_key
        # The signature algorithm version. This parameter is applicable when the origin type is `S3` and the authentication type is `private`. Supported versions:
        # 
        # - **v2**
        # 
        # - **v4**
        # 
        # If omitted, the default version is `v4`.
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

