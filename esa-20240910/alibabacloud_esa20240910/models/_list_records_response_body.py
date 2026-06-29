# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListRecordsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number, same as the PageNumber request parameter.
        self.page_number = page_number
        # The number of records displayed per page.
        self.page_size = page_size
        # DNS information of the records. For details, refer to <props="china">[Documentation](https://help.aliyun.com/document_detail/2708761.html)<props="intl">[Documentation](https://www.alibabacloud.com/help/doc-detail/2708761.html).
        self.records = records
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        auth_conf: main_models.ListRecordsResponseBodyRecordsAuthConf = None,
        biz_name: str = None,
        comment: str = None,
        create_time: str = None,
        custom_port: str = None,
        data: main_models.ListRecordsResponseBodyRecordsData = None,
        host_policy: str = None,
        http_ports: str = None,
        https_ports: str = None,
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
        # The business scenario for record acceleration. Valid values:
        # - **image_video**: Image and video.
        # - **api**: API.
        # - **web**: Web page.
        self.biz_name = biz_name
        # The comment of the record.
        self.comment = comment
        # The creation time of the record. The date format follows the ISO 8601 standard and uses UTC time in the format of yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        self.custom_port = custom_port
        # The specific DNS information of the record. Different record types contain different information.
        self.data = data
        # The origin host policy. This takes effect when the record type is CNAME. It sets the policy for the host header used during origin requests. Two modes are available:
        # 
        # - **follow_hostname**: Follow the request host.
        # - **follow_origin_domain**: Follow the origin domain.
        self.host_policy = host_policy
        self.http_ports = http_ports
        self.https_ports = https_ports
        # Indicates whether proxy acceleration is enabled for the record. Valid values:
        # 
        # - **true**: Proxy enabled.
        # - **false**: Proxy acceleration disabled.
        self.proxied = proxied
        # The CNAME of the record. This is the CNAME value that needs to be configured for the record when the site access method is CNAME access.
        self.record_cname = record_cname
        # The record ID.
        self.record_id = record_id
        # The record name.
        self.record_name = record_name
        # The origin type of the CNAME record. This parameter is required when adding a CNAME record. Valid values:
        # 
        # - **OSS**: OSS origin.
        # - **S3**: S3 origin.
        # - **LB**: Load balancer origin.
        # - **OP**: Origin pool.
        # - **Domain**: Standard domain origin.
        # 
        # If this parameter is not specified or left empty, the default value is Domain, which indicates a standard domain origin type.
        self.record_source_type = record_source_type
        # The DNS type of the record, such as **A/AAAA, CNAME, TXT**, etc.
        self.record_type = record_type
        # The ID of the site to which the record belongs.
        self.site_id = site_id
        # The name of the site to which the record belongs.
        self.site_name = site_name
        # The TTL (Time to Live) of the record, in seconds. When the value is 1, it indicates that the TTL is set to automatic.
        self.ttl = ttl
        # The update time of the record. The date format follows the ISO 8601 standard and uses UTC time in the format of yyyy-MM-ddTHH:mm:ssZ.
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

        if self.custom_port is not None:
            result['CustomPort'] = self.custom_port

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
            temp_model = main_models.ListRecordsResponseBodyRecordsAuthConf()
            self.auth_conf = temp_model.from_map(m.get('AuthConf'))

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomPort') is not None:
            self.custom_port = m.get('CustomPort')

        if m.get('Data') is not None:
            temp_model = main_models.ListRecordsResponseBodyRecordsData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

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

class ListRecordsResponseBodyRecordsData(DaraModel):
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
        # The encryption algorithm used by the record. Valid values: **0 to 255**. Exclusive to CERT and SSHFP records.
        self.algorithm = algorithm
        # The public key certificate information of the record. Exclusive to CERT, SMIMEA, and TLSA records.
        self.certificate = certificate
        # The public key fingerprint value of the record. Exclusive to SSHFP records.
        self.fingerprint = fingerprint
        # The flag of the record. The Flag of a CAA record indicates its priority and processing method. Valid values: **0 to 255**. Exclusive to CAA records.
        self.flag = flag
        # The public key identifier of the record. Valid values: **0 to 65535**. Exclusive to CERT records.
        self.key_tag = key_tag
        # The algorithm strategy used by the record for matching or verifying certificates. Valid values: **0 to 255**. Exclusive to SMIMEA and TLSA records.
        self.matching_type = matching_type
        # The port of the record. Valid values: **0 to 65535**. Exclusive to SRV records.
        self.port = port
        # The priority of the record. Valid values: **0 to 65535**. A smaller value indicates a higher priority. Exclusive to MX, SRV, and URI records.
        self.priority = priority
        # The type of certificate or public key used by the record. Valid values: **0 to 255**. Exclusive to SMIMEA and TLSA records.
        self.selector = selector
        # The tag of the record. The Tag of a CAA record indicates its specific type and purpose. Exclusive to CAA records.
        self.tag = tag
        # The tags of the record.
        self.tags = tags
        # The certificate type of the record (in CERT records), or the public key type (in SSHFP records).
        self.type = type
        # The usage identifier of the record. Valid values: **0 to 255**. Exclusive to SMIMEA and TLSA records.
        self.usage = usage
        # The record value or partial content. This parameter is included in A/AAAA, CNAME, NS, MX, TXT, CAA, SRV, and URI records. It has different meanings for different record types:
        # 
        # - **A/AAAA**: The IP address pointed to. When there are multiple IPs, they are separated by commas (,). At least one IPv4 address is required.
        # - **CNAME**: The target domain name pointed to.
        # - **NS**: The name server for the specified domain.
        # - **MX**: A valid target mail server domain name.
        # - **TXT**: A valid text string.
        # - **CAA**: A valid certificate authority domain name.
        # - **SRV**: A valid target host domain name.
        # - **URI**: A valid URI string.
        self.value = value
        # The weight of the record. Valid values: **0 to 65535**. Exclusive to SRV and URI records.
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

class ListRecordsResponseBodyRecordsAuthConf(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        # The AccessKey of the account to which the origin belongs. This parameter is available when the origin type is OSS with private cross-account read authentication, or when the origin type is S3 with private read authentication.
        self.access_key = access_key
        # The origin authentication type. Different origin types support different authentication types. The origin type refers to the SourceType parameter in this API. When the origin type is OSS or S3, the origin authentication type must be specified. Valid values:
        # - **public**: Public read. Use this value when the origin type is OSS or S3 and the origin has public read access.
        # - **private**: Private read. Use this value when the origin type is S3 and the origin has private read access.
        # - **private_same_account**: Private same-account read. Use this value when the origin type is OSS, the origin is under the same Alibaba Cloud account, and the origin has private read access.
        # - **private_cross_account**: Private cross-account read. Use this value when the origin type is OSS, the origin is not under the same Alibaba Cloud account, and the origin has private read access.
        self.auth_type = auth_type
        # The region where the origin is located. This parameter is available when the origin type is S3. The region of the origin can be obtained from the official S3 website.
        self.region = region
        # The SecretKey of the account to which the origin belongs. This parameter is available when the origin type is OSS with private cross-account read authentication, or when the origin type is S3 with private read authentication.
        self.secret_key = secret_key
        # The signature algorithm version. This parameter is available when the origin type is S3 and the origin authentication type is private read. Valid values:
        # - **v2**
        # - **v4**
        # 
        # Default value: v4.
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

