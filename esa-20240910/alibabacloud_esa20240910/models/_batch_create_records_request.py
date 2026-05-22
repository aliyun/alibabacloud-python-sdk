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
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
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
        proxied: bool = None,
        record_name: str = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        self.auth_conf = auth_conf
        # The business scenario of the record for acceleration. Valid values:
        # 
        # *   **image_video**
        # *   **api**
        # *   **web**
        self.biz_name = biz_name
        # The DNS information of the record. Enter fields based on the record type.
        # 
        # This parameter is required.
        self.data = data
        # Specifies whether to proxy the record. Only CNAME and A/AAAA records can be proxied. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # This parameter is required.
        self.proxied = proxied
        # The record name.
        # 
        # This parameter is required.
        self.record_name = record_name
        # The origin type for the CNAME record. This parameter is required when you add a CNAME record. Valid values:
        # 
        # *   **OSS**: OSS bucket.
        # *   **S3**: S3 bucket.
        # *   **LB**: load balancer.
        # *   **OP**: origin pool.
        # *   **Domain**: domain name.
        # 
        # If you do not pass this parameter or if you leave its value empty, Domain is used by default.
        self.source_type = source_type
        # The TTL of the record. Unit: seconds. If the value is 1, the TTL of the record is determined by the system.
        # 
        # This parameter is required.
        self.ttl = ttl
        # The DNS type of the record.
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
        # The encryption algorithm used for the record. Valid values: 0 to 255. Applicable to CERT and SSHFP records.
        self.algorithm = algorithm
        # The public key of the certificate. Applicable to CERT, SMIMEA, and TLSA records.
        self.certificate = certificate
        # The public key fingerprint of the record. Applicable to SSHFP records.
        self.fingerprint = fingerprint
        # The Flag for a CAA record indicates its priority and how it is processed. Valid values: 0 to 255.
        self.flag = flag
        # The public key identification for the record. Valid values: 0 to 65535. Applicable to CERT records.
        self.key_tag = key_tag
        # The algorithm policy used to match or validate the certificate. Valid values: 0 to 255. Applicable to SMIMEA, and TLSA records.
        self.matching_type = matching_type
        # The port of the record. Valid values: 0 to 65535. Exclusive to SRV records.
        self.port = port
        # The priority of the record. Valid values: 0 to 65535. A smaller value indicates a higher priority. This parameter is required when you add MX, SRV, and URI records.
        self.priority = priority
        # The type of certificate or public key. Valid values: 0 to 255. Applicable to SMIMEA and TLSA records.
        self.selector = selector
        # The tag of a CAA record, which indicates its specific type and purpose, such as issue, issuewild, and iodef.
        self.tag = tag
        # The certificate type of the record (in CERT records), or the public key type (in SSHFP records).
        self.type = type
        # The usage identifier of the record. Valid values: 0 to 255. Applicable to SMIMEA and TLSA records.
        self.usage = usage
        # The record value or part of the record content. A/AAAA: the IP address being pointed to. CNAME: the target domain name being pointed to. MX: valid target mail server domain name. TXT: valid text string. CAA: valid certificate authority domain name. SRV: valid target host domain name. URI: valid URI string.
        self.value = value
        # The weight of the record. Valid values: 0 to 65,535. Applicable to SRV and URI records.
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
        self.access_key = access_key
        self.auth_type = auth_type
        self.region = region
        self.secret_key = secret_key
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

