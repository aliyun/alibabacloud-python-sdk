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
        # The list of DNS records to be created.
        # 
        # This parameter is required.
        self.record_list = record_list
        # The site ID. You can obtain the site ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
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
        # The origin server authentication information for the CNAME record.
        self.auth_conf = auth_conf
        # The business scenario for record acceleration. Valid values:
        # - **image_video**: images and videos.
        # - **api**: API operations.
        # - **web**: web pages.
        self.biz_name = biz_name
        # The DNS information of the record. Specify different fields based on the record type.
        # 
        # This parameter is required.
        self.data = data
        # The HTTP port. By default, port 80 is supported.
        self.http_ports = http_ports
        # The HTTPS port. By default, port 443 is supported.
        self.https_ports = https_ports
        # Specifies whether to enable proxy acceleration for the record. Only CNAME and A/AAAA records can enable proxy acceleration. Valid values:
        # - **true**: enables proxy acceleration.
        # - **false**: disables proxy acceleration.
        # 
        # This parameter is required.
        self.proxied = proxied
        # The record name.
        # 
        # This parameter is required.
        self.record_name = record_name
        # The origin server type for the CNAME record. This parameter is required when you add a CNAME record. Valid values:
        # 
        # - **OSS**: an OSS origin server.
        # - **S3**: an S3 origin server.
        # - **LB**: a load balancing origin server.
        # - **OP**: an IPAM pool origin server.
        # - **Domain**: a common domain name origin server.
        # 
        # If this parameter is not specified or is left empty, the default value is Domain, which indicates a common domain name origin server type.
        self.source_type = source_type
        # The time-to-live (TTL) of the record, in seconds. A value of 1 indicates that the TTL is automatic.
        # 
        # This parameter is required.
        self.ttl = ttl
        # The DNS record type.
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
        # The encryption algorithm used by the record. Valid values: **0** to **255**. This parameter applies to CERT and SSHFP records.
        self.algorithm = algorithm
        # The public key certificate information of the record. This parameter applies to CERT, SMIMEA, and TLSA records.
        self.certificate = certificate
        # The public key fingerprint of the record. This parameter applies to SSHFP records.
        self.fingerprint = fingerprint
        # The flag of the CAA record, which indicates its priority and processing method. Valid values: **0** to **255**.
        self.flag = flag
        # The public key identifier of the record. Valid values: **0** to **65535**. This parameter applies to CERT records.
        self.key_tag = key_tag
        # The algorithm policy used by the record to match or verify the certificate. Valid values: **0** to **255**. This parameter applies to SMIMEA and TLSA records.
        self.matching_type = matching_type
        # The port of the record. Valid values: **0** to **65535**. This parameter applies only to SRV records.
        self.port = port
        # The priority of the record. Valid values: **0** to **65535**. A smaller value indicates a higher priority. This parameter is required when you add MX, SRV, or URI records.
        self.priority = priority
        # The type of the certificate or public key used by the record. Valid values: **0** to **255**. This parameter applies to SMIMEA and TLSA records.
        self.selector = selector
        # The tag of the CAA record, which indicates its specific type and usage, such as issue, issuewild, and iodef.
        self.tag = tag
        # The certificate type for CERT records or the public key type for SSHFP records.
        self.type = type
        # The usage identifier of the record. Valid values: **0** to **255**. This parameter applies to SMIMEA and TLSA records.
        self.usage = usage
        # The record value or partial content.
        # - **A/AAAA**: the IP address.
        # - **CNAME**: the target domain name.
        # - **MX**: the valid target mail server domain name.
        # - **TXT**: the valid character string.
        # - **CAA**: the valid domain name of the certification authority to issue certificates.
        # - **SRV**: the valid target host domain name.
        # - **URI**: the valid URI string.
        self.value = value
        # The weight of the record. Valid values: **0** to **65535**. This parameter applies to SRV and URI records.
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
        # The AccessKey of the account to which the origin server belongs. This parameter is required when the origin server type is OSS and the origin server authentication type is private cross-account read, or when the origin server type is S3 and the origin server authentication type is private read.
        self.access_key = access_key
        # The origin server authentication type. Different origin server types support different authentication types. The origin server type refers to the SourceType parameter in this operation. When the origin server type is OSS or S3, this parameter is required. Valid values:
        # - **public**: public read. Select this value when the origin server type is OSS or S3 and the origin server is publicly readable.
        # - **private**: private read. Select this value when the origin server type is S3 and the origin server is privately readable.
        # - **private_same_account**: private same-account read. Select this value when the origin server type is OSS, the origin server is under the same Alibaba Cloud account, and the origin server is privately readable.
        # - **private_cross_account**: private cross-account read. Select this value when the origin server type is OSS, the origin server is under a different Alibaba Cloud account, and the origin server is privately readable.
        self.auth_type = auth_type
        # The region to which the origin server belongs. This parameter is required when the origin server type is S3. You can obtain the region of the origin server from the official website of S3.
        self.region = region
        # The SecretKey of the account to which the origin server belongs. This parameter is required when the origin server type is OSS and the origin server authentication type is private cross-account read, or when the origin server type is S3 and the origin server authentication type is private read.
        self.secret_key = secret_key
        # The signature algorithm version. This parameter is available when the origin server type is S3 and the origin server authentication type is private read. Valid values:
        # - **v2**
        # - **v4**
        # 
        # If this parameter is not specified, the default value is v4.
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

