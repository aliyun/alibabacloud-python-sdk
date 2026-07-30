# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeOfficeSiteBridgeInfoResponseBody(DaraModel):
    def __init__(
        self,
        bridge: main_models.DescribeOfficeSiteBridgeInfoResponseBodyBridge = None,
        request_id: str = None,
    ):
        # The virtual bridge information.
        self.bridge = bridge
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.bridge:
            self.bridge.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bridge is not None:
            result['Bridge'] = self.bridge.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bridge') is not None:
            temp_model = main_models.DescribeOfficeSiteBridgeInfoResponseBodyBridge()
            self.bridge = temp_model.from_map(m.get('Bridge'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOfficeSiteBridgeInfoResponseBodyBridge(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        bridge_id: str = None,
        bridge_level: str = None,
        bridge_status: str = None,
        bridge_type: str = None,
        default_password: str = None,
        default_user: str = None,
        deploy_time: str = None,
        expire_time: str = None,
        internet_url: str = None,
        intranet_url: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        start_time: str = None,
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
        # The default password for the administrator page.
        self.default_password = default_password
        # The default account for the administrator page.
        self.default_user = default_user
        # The deployment time of the virtual bridge.
        self.deploy_time = deploy_time
        # The expiration time of the virtual bridge.
        self.expire_time = expire_time
        # The public network address.
        self.internet_url = internet_url
        # The internal network address.
        self.intranet_url = intranet_url
        # The ID of the locked convenience office network.
        self.office_site_id = office_site_id
        # The office network name. The name must be 2 to 255 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter or Chinese character and cannot start with `http://` or `https://`.
        self.office_site_name = office_site_name
        # The start time of the virtual bridge.
        self.start_time = start_time

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

        if self.default_password is not None:
            result['DefaultPassword'] = self.default_password

        if self.default_user is not None:
            result['DefaultUser'] = self.default_user

        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.internet_url is not None:
            result['InternetUrl'] = self.internet_url

        if self.intranet_url is not None:
            result['IntranetUrl'] = self.intranet_url

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

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

        if m.get('DefaultPassword') is not None:
            self.default_password = m.get('DefaultPassword')

        if m.get('DefaultUser') is not None:
            self.default_user = m.get('DefaultUser')

        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InternetUrl') is not None:
            self.internet_url = m.get('InternetUrl')

        if m.get('IntranetUrl') is not None:
            self.intranet_url = m.get('IntranetUrl')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

