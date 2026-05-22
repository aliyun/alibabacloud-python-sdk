# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRecordShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_conf_shrink: str = None,
        biz_name: str = None,
        comment: str = None,
        data_shrink: str = None,
        host_policy: str = None,
        proxied: bool = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The origin authentication information of the CNAME record.
        self.auth_conf_shrink = auth_conf_shrink
        # The business scenario of the record for acceleration. Leave the parameter empty if your record is not proxied. Valid values:
        # 
        # *   **image_video**: video and image.
        # *   **api**: API.
        # *   **web**: web page.
        self.biz_name = biz_name
        # The comment of the record. The maximum length is 100 characters.
        self.comment = comment
        # The DNS record information. The format of this field varies based on the record type. For more information, see [References](https://www.alibabacloud.com/help/doc-detail/2708761.html) .
        # 
        # This parameter is required.
        self.data_shrink = data_shrink
        # The origin host policy. This policy takes effect when the record type is CNAME. You can set the policy in two modes:
        # 
        # *   follow_hostname: Follow the host record.
        # *   follow_origin_domain: match the origin\\"s domain name.
        self.host_policy = host_policy
        # Specifies whether to proxy the record. Only CNAME and A/AAAA records can be proxied. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.proxied = proxied
        # The record name.
        # 
        # This parameter is required.
        self.record_name = record_name
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
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
        # The type of the DNS record. For example, A/AAAA, TXT, MX, or CNAME.
        # 
        # This parameter is required.
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
            self.auth_conf_shrink = m.get('AuthConf')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Data') is not None:
            self.data_shrink = m.get('Data')

        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')

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

