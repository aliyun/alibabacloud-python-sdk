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
        # The current page number.
        self.page_number = page_number
        # The number of records returned per page.
        self.page_size = page_size
        # A list of DNS records. For details, see the <props="china">[documentation](https://help.aliyun.com/document_detail/2708761.html)<props="intl">[documentation](https://www.alibabacloud.com/help/doc-detail/2708761.html).
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
        # The origin authentication settings for the CNAME record.
        self.auth_conf = auth_conf
        # The business scenario for record acceleration. Valid values:
        # 
        # - **image_video**: Images and videos.
        # 
        # - **api**: API.
        # 
        # - **web**: Web page.
        self.biz_name = biz_name
        # The record\\"s comment.
        self.comment = comment
        # The UTC time when the record was created, in ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`.
        self.create_time = create_time
        self.custom_port = custom_port
        # The DNS details of the record. The fields in this object vary based on the record type.
        self.data = data
        # The policy for the `HOST` header in back-to-origin requests. This parameter applies only to CNAME records. Valid values:
        # 
        # - **follow_hostname**: Uses the `HOST` header of the incoming request.
        # 
        # - **follow_origin_domain**: Uses the domain name of the origin server.
        self.host_policy = host_policy
        self.http_ports = http_ports
        self.https_ports = https_ports
        # Indicates whether proxy acceleration is enabled for the record. Valid values:
        # 
        # - **true**: Proxy acceleration is enabled.
        # 
        # - **false**: Proxy acceleration is disabled.
        self.proxied = proxied
        # The CNAME value assigned to this record. To enable the service, create a CNAME record in your DNS provider\\"s settings that points to this value.
        self.record_cname = record_cname
        # The record ID.
        self.record_id = record_id
        # The record name.
        self.record_name = record_name
        # The type of origin for the CNAME record. This parameter is required when you add a CNAME record. Valid values:
        # 
        # - **OSS**: OSS origin.
        # 
        # - **S3**: S3 origin.
        # 
        # - **LB**: Load balancer origin.
        # 
        # - **OP**: Origin pool.
        # 
        # - **Domain**: Domain origin.
        # 
        # If this parameter is not specified, the default value is `Domain`.
        self.record_source_type = record_source_type
        # The DNS record type, such as **A/AAAA, CNAME, and TXT**.
        self.record_type = record_type
        # The ID of the site to which the record belongs.
        self.site_id = site_id
        # The name of the site to which the record belongs.
        self.site_name = site_name
        # The Time to Live (TTL) for the record, in seconds. A value of 1 indicates that the TTL is automatic.
        self.ttl = ttl
        # The UTC time when the record was last updated, in ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`.
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
        # The encryption algorithm for the record. The value ranges from **0 to 255**. This parameter is valid only for CERT and SSHFP records.
        self.algorithm = algorithm
        # The public key certificate. This parameter is valid only for CERT, SMIMEA, and TLSA records.
        self.certificate = certificate
        # The public key fingerprint. This parameter is valid only for SSHFP records.
        self.fingerprint = fingerprint
        # The record\\"s flag. For a CAA record, the flag determines how a certificate authority (CA) processes the record. The value ranges from **0 to 255**. This parameter applies only to CAA records.
        self.flag = flag
        # The public key identifier. The value ranges from **0 to 65535**. This parameter is valid only for CERT records.
        self.key_tag = key_tag
        # The algorithm policy for matching or validating certificates. The value ranges from **0 to 255**. This parameter is valid only for SMIMEA and TLSA records.
        self.matching_type = matching_type
        # The port number, which must be an integer from **0 to 65535**. This parameter applies only to SRV records.
        self.port = port
        # The priority of the record, which must be an integer from **0 to 65535**. A lower value indicates a higher priority. This parameter applies only to MX, SRV, and URI records.
        self.priority = priority
        # The type of certificate or public key for the record. The value ranges from **0 to 255**. This parameter is valid only for SMIMEA and TLSA records.
        self.selector = selector
        # The record\\"s tag. For a CAA record, the tag indicates its specific type and purpose. This parameter is valid only for CAA records.
        self.tag = tag
        self.tags = tags
        # The certificate type for a CERT record, or the public key type for an SSHFP record.
        self.type = type
        # The usage identifier. The value ranges from **0 to 255**. This parameter is valid only for SMIMEA and TLSA records.
        self.usage = usage
        # The value of the record. This parameter applies to A/AAAA, CNAME, NS, MX, TXT, CAA, SRV, and URI records. The meaning of this parameter varies based on the record type:
        # 
        # - **A/AAAA**: The target IP address. Use an IPv4 address for an A record and an IPv6 address for an AAAA record.
        # 
        # - **CNAME**: The target domain name.
        # 
        # - **NS**: The name server for the specified domain.
        # 
        # - **MX**: The domain name of the target mail server.
        # 
        # - **TXT**: A text string.
        # 
        # - **CAA**: The domain name of the certificate authority.
        # 
        # - **SRV**: The domain name of the target host.
        # 
        # - **URI**: A URI string.
        self.value = value
        # The weight of the record, which must be an integer from **0 to 65535**. This parameter applies only to SRV and URI records.
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
        # The AccessKey for the account that owns the origin server. This parameter is required if the origin type is OSS and the authentication type is `private_cross_account`, or if the origin type is S3 and the authentication type is `private`.
        self.access_key = access_key
        # The origin authentication type. The available authentication types depend on the origin type, which is specified by the `RecordSourceType` parameter. This parameter is required if the origin type is OSS or S3. Valid values:
        # 
        # - **public**: Public read. Use this value if the origin type is OSS or S3 and the origin server allows public read access.
        # 
        # - **private**: Private read. Use this value if the origin type is S3 and the origin server requires private read access.
        # 
        # - **private_same_account**: Private read within the same account. Use this value if the origin type is OSS, the origin server is in the same Alibaba Cloud account, and requires private read access.
        # 
        # - **private_cross_account**: Private read across different accounts. Use this value if the origin type is OSS, the origin server is in a different Alibaba Cloud account, and requires private read access.
        self.auth_type = auth_type
        # The region where the origin server is located. This parameter is required if the origin type is S3. For valid region names, refer to the official S3 documentation.
        self.region = region
        # The SecretKey for the account that owns the origin server. This parameter is required if the origin type is OSS and the authentication type is `private_cross_account`, or if the origin type is S3 and the authentication type is `private`.
        self.secret_key = secret_key
        # The signature algorithm version. This parameter is required if the origin type is S3 and the authentication type is `private`. Valid values:
        # 
        # - **v2**
        # 
        # - **v4**
        # 
        # The default is `v4`.
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

