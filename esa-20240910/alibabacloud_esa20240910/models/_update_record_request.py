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
        http_ports: str = None,
        https_ports: str = None,
        proxied: bool = None,
        record_id: int = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The origin authentication settings for the CNAME record.
        self.auth_conf = auth_conf
        # The use case for proxy acceleration. Omit this parameter if proxy acceleration is disabled. Valid values:
        # 
        # - **video_image**: Video and images.
        # 
        # - **api**: APIs.
        # 
        # - **web**: Web pages.
        self.biz_name = biz_name
        # A comment for the record.
        self.comment = comment
        # The DNS data for the record. The required content varies based on the record type. For more information, see <props="china">[Documentation](https://help.aliyun.com/document_detail/2708761.html)<props="intl">[Documentation](https://www.alibabacloud.com/help/doc-detail/2708761.html).
        # 
        # This parameter is required.
        self.data = data
        # The origin HOST policy. This policy, which applies only to CNAME records, determines the value of the `HOST` header in requests sent to the origin. Valid values:
        # 
        # - **follow_hostname**: Follows the host record.
        # 
        # - **follow_origin_domain**: Follows the origin domain name.
        self.host_policy = host_policy
        self.http_ports = http_ports
        self.https_ports = https_ports
        # Indicates whether to enable proxy acceleration for the record. Only CNAME and A/AAAA records support proxy acceleration. Valid values:
        # 
        # - **true**: Enables proxy acceleration.
        # 
        # - **false**: Disables proxy acceleration.
        self.proxied = proxied
        # The record ID. Call the [ListRecords](https://help.aliyun.com/document_detail/2850265.html) operation to get this ID.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The origin type for the CNAME record. This parameter is required for CNAME records. Valid values:
        # 
        # - **OSS**: An OSS origin.
        # 
        # - **S3**: An S3 origin.
        # 
        # - **LB**: A load balancer origin.
        # 
        # - **OP**: An origin address pool origin.
        # 
        # - **Domain**: A standard domain name origin.
        # 
        # If this parameter is omitted or left empty, the default value is `Domain`.
        self.source_type = source_type
        # The record\\"s time to live (TTL) in seconds. The value must be an integer from **30 to 86400** or 1. A value of 1 sets the TTL to automatic.
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

        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

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

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

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
        # The encryption algorithm specified in the record. The value must be an integer from **0 to 255**. This parameter is required for CERT and SSHFP records.
        self.algorithm = algorithm
        # The public key certificate data for the record. This parameter is required for CERT, SMIMEA, and TLSA records.
        self.certificate = certificate
        # The public key fingerprint for the record. This parameter is required for SSHFP records.
        self.fingerprint = fingerprint
        # The flag for the record. For a CAA record, this flag indicates its priority and handling behavior. The value must be an integer from **0 to 255**. This parameter is required for CAA records.
        self.flag = flag
        # The public key identifier for the record. The value must be an integer from **0 to 65535**. This parameter is required for CERT records.
        self.key_tag = key_tag
        # The algorithm policy used to match or validate the certificate. The value must be an integer from **0 to 255**. This parameter is required for SMIMEA and TLSA records.
        self.matching_type = matching_type
        # The port number for the record. The value must be an integer from **0 to 65535**. This parameter is required for SRV records.
        self.port = port
        # The record\\"s priority. The value must be an integer from **0 to 65535**, where a lower value indicates higher priority. This parameter is required for MX, SRV, and URI records.
        self.priority = priority
        # The type of certificate or public key specified in the record. The value must be an integer from **0 to 255**. This parameter is required for SMIMEA and TLSA records.
        self.selector = selector
        # The tag for the record. For a CAA record, the tag specifies the record\\"s type and purpose. This parameter is required for CAA records.
        self.tag = tag
        # The certificate type for a CERT record, or the public key type for an SSHFP record. This parameter is required for CERT and SSHFP records.
        self.type = type
        # The usage identifier for the record. The value must be an integer from **0 to 255**. This parameter is required for SMIMEA and TLSA records.
        self.usage = usage
        # The value of the record or part of its content. This parameter is required for A/AAAA, CNAME, NS, MX, TXT, CAA, SRV, and URI records. The meaning of this parameter varies by record type:
        # 
        # - **A/AAAA**: The target IP address. To specify multiple IP addresses, separate them with a comma (,). At least one IPv4 address is required.
        # 
        # - **CNAME**: The target domain name.
        # 
        # - **NS**: The name server for the domain.
        # 
        # - **MX**: A valid domain name for the target mail server.
        # 
        # - **TXT**: A valid text string.
        # 
        # - **CAA**: A valid domain name for the certificate authority.
        # 
        # - **SRV**: A valid domain name for the target host.
        # 
        # - **URI**: A valid URI string.
        self.value = value
        # The weight of the record. The value must be an integer from **0 to 65535**. This parameter is required for SRV and URI records.
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
        # The access key for the account that owns the origin. This is required for private, cross-account access to OSS origins, and for S3 origins where the authentication type is **private**.
        self.access_key = access_key
        # The origin authentication type. This parameter is required when the **SourceType** is **OSS** or **S3**. Supported authentication types vary depending on the origin type. Valid values:
        # 
        # - **public**: Public read. Use for publicly readable OSS or S3 origins.
        # 
        # - **private**: Private read. Use for private S3 origins.
        # 
        # - **private_same_account**: Private read within the same account. Use for private OSS origins accessed from the same Alibaba Cloud account.
        self.auth_type = auth_type
        # The region where the origin is located. This parameter is required when the origin type is S3. You can find the region ID on the official S3 website.
        # 
        # - **v2**
        # 
        # - **v4**
        # 
        # If you do not specify a value, it defaults to v4.
        self.region = region
        # The secret key for the account that owns the origin. This is required for private, cross-account access to OSS origins, and for S3 origins where the authentication type is **private**.
        self.secret_key = secret_key
        # The signing algorithm version. This parameter is required when the origin type is S3 and the authentication type is **private**. Supported versions: v2 and v4. If this parameter is not specified, the default value is v4.
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

