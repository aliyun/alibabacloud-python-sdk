# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyScaDetailRequest(DaraModel):
    def __init__(
        self,
        biz: str = None,
        biz_type: str = None,
        current_page: int = None,
        lang: str = None,
        name: int = None,
        next_token: str = None,
        page_size: int = None,
        pid: str = None,
        port: str = None,
        process_started_end: int = None,
        process_started_start: int = None,
        remark: str = None,
        sca_name: str = None,
        sca_name_pattern: str = None,
        sca_version: str = None,
        search_info: str = None,
        search_info_sub: str = None,
        search_item: str = None,
        search_item_sub: str = None,
        use_next_token: bool = None,
        user: str = None,
        uuid: str = None,
    ):
        # The type of the asset fingerprint that you want to query. Default value: **sca**. Valid values:
        # 
        # *   **sca**: middleware
        # *   **sca_database**: database
        # *   **sca_web**: web service
        # 
        # >  If you do not specify this parameter, the default value **sca** is used, which indicates that middleware fingerprints are queried.
        self.biz = biz
        # The type of the middleware, database, or web service that you want to query. Valid values:
        # 
        # *   **system_service**: system service
        # *   **software_library**: software library
        # *   **docker_component**: container component
        # *   **database**: database
        # *   **web_container**: web container
        # *   **jar**: JAR package
        # *   **web_framework**: web framework
        self.biz_type = biz_type
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the middleware, database, or web service.
        # 
        # >  This parameter is deprecated. You can ignore it.
        self.name = name
        # The value of NextToken that is returned when the NextToken method is used. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The number of entries to return on each page. Default value: **10**.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The PID.
        self.pid = pid
        # The port that the process monitors.
        self.port = port
        # The timestamp when the process ends. Unit: milliseconds.
        self.process_started_end = process_started_end
        # The timestamp when the process starts. Unit: milliseconds.
        self.process_started_start = process_started_start
        # The search condition, such as a server name or a server IP address.
        # 
        # >  Fuzzy match is supported.
        self.remark = remark
        # The name of the asset fingerprint that you want to query.
        self.sca_name = sca_name
        # The name of the process.
        self.sca_name_pattern = sca_name_pattern
        # The version of the middleware, database, or web service.
        self.sca_version = sca_version
        # The search keyword. You must specify this parameter based on the value of the **SearchItem** parameter.
        # 
        # *   If the **SearchItem** parameter is set to **name**, you must enter the name of an asset fingerprint.
        # 
        # *   If the **SearchItem** parameter is set to **type**, you must enter the type of an asset fingerprint. Valid values:
        # 
        #     *   **system_service**: system service
        #     *   **software_library**: software library
        #     *   **docker_component**: container component
        #     *   **database**: database
        #     *   **web_container**: web container
        #     *   **jar**: JAR package
        #     *   **web_framework**: web framework
        # 
        # >  You must specify both the **SearchItem** and **SearchInfo** parameters before you can query the asset fingerprints based on the specified name or type.
        self.search_info = search_info
        # The keyword of the subquery. You must specify this parameter based on the value of the **SearchItemSub** parameter.
        # 
        # *   If the **SearchItemSub** parameter is set to **port**, you must enter a port number.
        # *   If the **SearchItemSub** parameter is set to **pid**, you must enter a process ID (PID).
        # *   If the **SearchItemSub** parameter is set to **version**, you must enter the version of a database, middleware, or web service.
        # *   If the **SearchItemSub** parameter is set to **user**, you must enter a username.
        # 
        # >  The subquery is used to search for data of a specified database, middleware, or web service.
        self.search_info_sub = search_info_sub
        # The type of the search condition. Valid values:
        # 
        # *   **name**: the name of a database, middleware, or web service
        # *   **type**: the type of a database, middleware, or web service
        # 
        # >  You must specify both the **SearchItem** and **SearchInfo** parameters before you can query the asset fingerprints based on the specified name or type.
        self.search_item = search_item
        # The type of the subquery. Valid values:
        # 
        # *   **port**
        # *   **pid**
        # *   **version**
        # *   **user**
        self.search_item_sub = search_item_sub
        # Specifies whether to use the NextToken method to retrieve a new page of results. If you set UseNextToken to true, the value of TotalCount is not returned. Valid values:
        # 
        # - **true**: The NextToken method is used.
        # - **false**: The NextToken method is not used.
        self.use_next_token = use_next_token
        # The user who runs the process.
        self.user = user
        # The UUID of the server on which the middleware, database, or web service is run.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.port is not None:
            result['Port'] = self.port

        if self.process_started_end is not None:
            result['ProcessStartedEnd'] = self.process_started_end

        if self.process_started_start is not None:
            result['ProcessStartedStart'] = self.process_started_start

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sca_name is not None:
            result['ScaName'] = self.sca_name

        if self.sca_name_pattern is not None:
            result['ScaNamePattern'] = self.sca_name_pattern

        if self.sca_version is not None:
            result['ScaVersion'] = self.sca_version

        if self.search_info is not None:
            result['SearchInfo'] = self.search_info

        if self.search_info_sub is not None:
            result['SearchInfoSub'] = self.search_info_sub

        if self.search_item is not None:
            result['SearchItem'] = self.search_item

        if self.search_item_sub is not None:
            result['SearchItemSub'] = self.search_item_sub

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        if self.user is not None:
            result['User'] = self.user

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProcessStartedEnd') is not None:
            self.process_started_end = m.get('ProcessStartedEnd')

        if m.get('ProcessStartedStart') is not None:
            self.process_started_start = m.get('ProcessStartedStart')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ScaName') is not None:
            self.sca_name = m.get('ScaName')

        if m.get('ScaNamePattern') is not None:
            self.sca_name_pattern = m.get('ScaNamePattern')

        if m.get('ScaVersion') is not None:
            self.sca_version = m.get('ScaVersion')

        if m.get('SearchInfo') is not None:
            self.search_info = m.get('SearchInfo')

        if m.get('SearchInfoSub') is not None:
            self.search_info_sub = m.get('SearchInfoSub')

        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')

        if m.get('SearchItemSub') is not None:
            self.search_item_sub = m.get('SearchItemSub')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

