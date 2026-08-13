# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        current_page: str = None,
        description: str = None,
        destination: str = None,
        direction: str = None,
        ip_version: str = None,
        lang: str = None,
        page_size: str = None,
        proto: str = None,
        release: str = None,
        repeat_type: str = None,
        source: str = None,
    ):
        # The action that Cloud Firewall performs on the traffic in the access control policy. Valid values:
        self.acl_action = acl_action
        # The unique ID of the access control policy. You must specify at least one of AclUuid and Direction. If AclUuid is specified, you can query the policy by its ID.
        self.acl_uuid = acl_uuid
        # The page number of the current page displayed in a paging query.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The description of the access control policy. Fuzzy queries are supported.
        self.description = description
        # The destination address in the access control policy. Fuzzy queries are supported. The value varies depending on the DestinationType (destination type).
        self.destination = destination
        # The traffic direction controlled by the access control policy. Valid values: in (inbound) or out (outbound). You must specify at least one of Direction and AclUuid. If AclUuid is not specified, you must specify a non-empty Direction. Otherwise, the ErrorParametersDirection error is returned.
        self.direction = direction
        # The supported IP address version. Valid values:
        self.ip_version = ip_version
        # The language type for receiving messages. Valid values:
        self.lang = lang
        # The maximum number of entries per page displayed in a paging query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The protocol type of the traffic in the access control policy. Valid values:
        self.proto = proto
        # The enabled status of the access control policy. Valid values:
        self.release = release
        # The recurrence type of the policy validity period for the access control policy. Valid values:
        self.repeat_type = repeat_type
        # The source address in the access control policy. Fuzzy queries are supported. The value varies depending on the SourceType (source type).
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action

        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.description is not None:
            result['Description'] = self.description

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.release is not None:
            result['Release'] = self.release

        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('Release') is not None:
            self.release = m.get('Release')

        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

