# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecordShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_conf_shrink: str = None,
        biz_name: str = None,
        comment: str = None,
        data_shrink: str = None,
        host_policy: str = None,
        http_ports: str = None,
        https_ports: str = None,
        proxied: bool = None,
        record_id: int = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The origin authentication information of the CNAME record.
        self.auth_conf_shrink = auth_conf_shrink
        # The business scenario for record acceleration. This parameter is not required for records without acceleration enabled. Valid values:
        # - **video_image**: video and image.
        # - **api**: API.
        # - **web**: web page.
        self.biz_name = biz_name
        # The comment for the record.
        self.comment = comment
        # The DNS information of the record. The content varies depending on the record type. For more information, see <props="china">[documentation](https://help.aliyun.com/document_detail/2708761.html)<props="intl">[documentation](https://www.alibabacloud.com/help/doc-detail/2708761.html).
        # 
        # This parameter is required.
        self.data_shrink = data_shrink
        # The back-to-origin HOST policy. This parameter takes effect when the record type is CNAME. Settings the HOST policy for back-to-origin requests. Valid values:
        # 
        # - **follow_hostname**: follows the host record.
        # - **follow_origin_domain**: follows the Origin Domain Name.
        self.host_policy = host_policy
        self.http_ports = http_ports
        self.https_ports = https_ports
        # Specifies whether to enable proxy acceleration for the record. Only CNAME records and A/AAAA records support proxy acceleration. Valid values:
        # - **true**: Enable proxy acceleration.
        # - **false**: Disable proxy acceleration.
        self.proxied = proxied
        # The ID of the record. You can call [ListRecords](https://help.aliyun.com/document_detail/2850265.html) to obtain the record ID.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The origin server type of the CNAME record. This parameter is required when you add a CNAME record. Valid values:
        # 
        # - **OSS**: OSS origin server.
        # - **S3**: S3 origin server.
        # - **LB**: load balancing origin server.
        # - **OP**: IPAM pool origin server.
        # - **Domain**: standard domain name origin server.
        # 
        # If this parameter is not specified or is left empty, the default value is Domain, which indicates a standard domain name origin server type.
        self.source_type = source_type
        # The time-to-live (TTL) of the record, in seconds. Valid values: **30 to 86400**, or 1. A value of 1 indicates that the TTL of the record is automatically determined.
        self.ttl = ttl
        # The DNS type of the record, such as A/AAAA, CNAME, or TXT.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_conf_shrink is not None:
            result['AuthConf'] = self.auth_conf_shrink

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data_shrink is not None:
            result['Data'] = self.data_shrink

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
            self.auth_conf_shrink = m.get('AuthConf')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Data') is not None:
            self.data_shrink = m.get('Data')

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

