# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ListVirtualBridgesResponseBody(DaraModel):
    def __init__(
        self,
        bridges: List[main_models.ListVirtualBridgesResponseBodyBridges] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The virtual bridge information.
        self.bridges = bridges
        # The maximum number of entries returned. Valid values: 1 to 100. If this parameter is not specified, the default value 100 is used.
        # The number of returned entries can be less than the specified value but cannot exceed it.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.bridges:
            for v1 in self.bridges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bridges'] = []
        if self.bridges is not None:
            for k1 in self.bridges:
                result['Bridges'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bridges = []
        if m.get('Bridges') is not None:
            for k1 in m.get('Bridges'):
                temp_model = main_models.ListVirtualBridgesResponseBodyBridges()
                self.bridges.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVirtualBridgesResponseBodyBridges(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        bridge_id: str = None,
        bridge_level: str = None,
        bridge_status: str = None,
        bridge_type: str = None,
        expire_time: str = None,
        intranet_url: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
    ):
        # The access type of the management page.
        self.access_type = access_type
        # The virtual bridge ID.
        self.bridge_id = bridge_id
        # The virtual bridge specifications.
        self.bridge_level = bridge_level
        # The virtual bridge status.
        self.bridge_status = bridge_status
        # The third-party plugin type of the virtual bridge.
        self.bridge_type = bridge_type
        # The expiration time.
        self.expire_time = expire_time
        # The internal network address.
        self.intranet_url = intranet_url
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.bridge_id is not None:
            result['BridgeId'] = self.bridge_id

        if self.bridge_level is not None:
            result['BridgeLevel'] = self.bridge_level

        if self.bridge_status is not None:
            result['BridgeStatus'] = self.bridge_status

        if self.bridge_type is not None:
            result['BridgeType'] = self.bridge_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.intranet_url is not None:
            result['IntranetUrl'] = self.intranet_url

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('BridgeId') is not None:
            self.bridge_id = m.get('BridgeId')

        if m.get('BridgeLevel') is not None:
            self.bridge_level = m.get('BridgeLevel')

        if m.get('BridgeStatus') is not None:
            self.bridge_status = m.get('BridgeStatus')

        if m.get('BridgeType') is not None:
            self.bridge_type = m.get('BridgeType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('IntranetUrl') is not None:
            self.intranet_url = m.get('IntranetUrl')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        return self

