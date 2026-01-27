# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUserResourcesRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        auto_refresh: bool = None,
        category_id: int = None,
        category_type: int = None,
        client_id: str = None,
        client_type: str = None,
        client_version: str = None,
        dual_center_forward: bool = None,
        language: str = None,
        login_region_id: str = None,
        login_token: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_ids: List[str] = None,
        order_by: str = None,
        product_types: List[str] = None,
        protocol_type: str = None,
        query_desktop_duration_list: bool = None,
        query_desktop_timers: bool = None,
        query_fota_update: bool = None,
        refresh_fota_update: bool = None,
        resource_ids: List[str] = None,
        resource_name: str = None,
        resource_types: List[str] = None,
        scene: str = None,
        search_region_id: str = None,
        session_id: str = None,
        sort_type: str = None,
    ):
        # The access type. If you leave this parameter empty, both types will be displayed.
        # 
        # Valid values:
        # 
        # *   INTERNET: access over the Internet.
        # *   VPC: access over an enterprise virtual private cloud (VPC).
        self.access_type = access_type
        # Specifies whether to enable the immediate refresh feature.
        # 
        # >  To ensure the operation response speed, we recommend that you set the value to `false`.
        # 
        # Valid values:
        # 
        # *   false
        # *   true
        self.auto_refresh = auto_refresh
        # The level-2 resource category.
        self.category_id = category_id
        # The level-1 resource category.
        self.category_type = category_type
        # The client ID. The system generates a unique ID for each client. This parameter is non-sensitive and does not need encryption.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client type.
        # 
        # Valid values:
        # 
        # *   html5: the web client.
        # *   android: the Android client.
        # *   windows: the Windows client.
        # *   ios: the iOS client.
        # *   macos: the macOS client.
        self.client_type = client_type
        # The client version.
        self.client_version = client_version
        # Specifies whether to enable geo-redundant forwarding. Set the value to `false`.
        # 
        # Valid value:
        # 
        # *   false: disables geo-redundant forwarding.
        self.dual_center_forward = dual_center_forward
        # The client language.
        # 
        # Valid values:
        # 
        # *   en_US: English.
        # *   zh_CN: Simplified Chinese.
        # *   ja_JP: Japanese.
        self.language = language
        # The ID of the region where end users log on to clients. This parameter applies to office network ID-based logons. For organization ID-based logons, you can leave this parameter empty.
        self.login_region_id = login_region_id
        # The logon token. You can call the `GetLoginToken` or `RefreshLoginToken` operation to retrieve the logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The number of entries per page. Default value: 500.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The office network IDs. This parameter is required for logons by using enterprise Active Directory (AD) accounts.
        self.office_site_ids = office_site_ids
        # The sorting field. If you do not specify this parameter, resources are sorted by creation time by default.
        # 
        # Valid values:
        # 
        # *   CreateTime: the time when resources are created.
        # *   AssignTime: the time when resources are assigned.
        self.order_by = order_by
        # The service types. If you leave this parameter empty, services of all supported types will be queried.
        self.product_types = product_types
        # The protocol type. You can specify this parameter to filter cloud computers.
        # 
        # Valid values:
        # 
        # *   HDX: High-definition Experience (HDX).
        # *   ASP: Adaptive Streaming Protocol (ASP).
        self.protocol_type = protocol_type
        # 是否查询云桌面套餐包信息，默认为true。
        self.query_desktop_duration_list = query_desktop_duration_list
        # 是否查询云电脑定时任务信息，默认为true。
        self.query_desktop_timers = query_desktop_timers
        # Specifies whether to return the image version information of cloud computers.
        self.query_fota_update = query_fota_update
        # Specifies whether to refresh over-the-air (OTA) information in real time.
        self.refresh_fota_update = refresh_fota_update
        # The resource IDs. You can specify up to 100 resource IDs.
        self.resource_ids = resource_ids
        # The resource name. Fuzzy search is supported.
        self.resource_name = resource_name
        # The resource types. If you leave this parameter empty, resources of all supported types will be queried.
        self.resource_types = resource_types
        # The client usage scenario. Set the value to `desktop`.
        # 
        # Valid value:
        # 
        # *   desktop: cloud computers.
        self.scene = scene
        # The ID of the searched region. You can specify this parameter to filter cloud resources in specific regions.
        self.search_region_id = search_region_id
        # The session ID. You can call the `GetLoginToken` operation to retrieve the session ID.
        self.session_id = session_id
        # The sorting method.
        # 
        # Valid values:
        # 
        # *   ASC (default): the ascending order.
        # *   DESC: the descending order.
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.auto_refresh is not None:
            result['AutoRefresh'] = self.auto_refresh

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.dual_center_forward is not None:
            result['DualCenterForward'] = self.dual_center_forward

        if self.language is not None:
            result['Language'] = self.language

        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_ids is not None:
            result['OfficeSiteIds'] = self.office_site_ids

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.product_types is not None:
            result['ProductTypes'] = self.product_types

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.query_desktop_duration_list is not None:
            result['QueryDesktopDurationList'] = self.query_desktop_duration_list

        if self.query_desktop_timers is not None:
            result['QueryDesktopTimers'] = self.query_desktop_timers

        if self.query_fota_update is not None:
            result['QueryFotaUpdate'] = self.query_fota_update

        if self.refresh_fota_update is not None:
            result['RefreshFotaUpdate'] = self.refresh_fota_update

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('AutoRefresh') is not None:
            self.auto_refresh = m.get('AutoRefresh')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('DualCenterForward') is not None:
            self.dual_center_forward = m.get('DualCenterForward')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteIds') is not None:
            self.office_site_ids = m.get('OfficeSiteIds')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('ProductTypes') is not None:
            self.product_types = m.get('ProductTypes')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('QueryDesktopDurationList') is not None:
            self.query_desktop_duration_list = m.get('QueryDesktopDurationList')

        if m.get('QueryDesktopTimers') is not None:
            self.query_desktop_timers = m.get('QueryDesktopTimers')

        if m.get('QueryFotaUpdate') is not None:
            self.query_fota_update = m.get('QueryFotaUpdate')

        if m.get('RefreshFotaUpdate') is not None:
            self.refresh_fota_update = m.get('RefreshFotaUpdate')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

