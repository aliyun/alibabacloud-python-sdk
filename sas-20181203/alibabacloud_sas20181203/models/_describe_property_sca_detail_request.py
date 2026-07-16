# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
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
        search_criteria_list: List[main_models.DescribePropertyScaDetailRequestSearchCriteriaList] = None,
        search_info: str = None,
        search_info_sub: str = None,
        search_item: str = None,
        search_item_sub: str = None,
        use_next_token: bool = None,
        user: str = None,
        uuid: str = None,
    ):
        # The type of Asset Fingerprints to query. Default value: **sca**. Valid values:
        # 
        # - **sca**: middleware
        # - **sca_database**: database
        # - **sca_web**: web service
        # 
        # > If this parameter is not set, the default value **sca** is used, which queries Asset Fingerprints information of the middleware type.
        self.biz = biz
        # The type of middleware, database, or web service to query. Valid values:  
        # - **system_service**: system service
        # - **software_library**: software library
        # - **docker_component**: container component
        # - **database**: database
        # - **web_container**: web container
        # - **jar**: JAR package
        # - **web_framework**: web framework.
        self.biz_type = biz_type
        # The page number of the page to return in the query results. Default value: **1**, which indicates that the results are displayed starting from page 1.
        self.current_page = current_page
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The name of the middleware, database, or web service.
        # > This parameter is deprecated. You do not need to specify this parameter.
        self.name = name
        # The token that marks the current position from which to start reading. Leave this parameter empty to start reading from the beginning.
        # 
        # > Do not specify this parameter for the first call. The response includes the NextToken value for the second call. Each subsequent response contains the NextToken value for the next call.
        self.next_token = next_token
        # Sets the number of Asset Fingerprints entries per page in a paged query. Default value: **10**, which indicates that 10 Asset Fingerprints entries are displayed per page.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The process ID.
        self.pid = pid
        # The port on which the process listens.
        self.port = port
        # The end of the time range for querying the process start timestamp. Unit: seconds.
        self.process_started_end = process_started_end
        # The start of the time range for querying the process start timestamp. Unit: seconds.
        self.process_started_start = process_started_start
        # The search condition (server name or IP address).
        # > Fuzzy match is supported.
        self.remark = remark
        # The name of the Asset Fingerprints entry to query.
        self.sca_name = sca_name
        # The process name.
        self.sca_name_pattern = sca_name_pattern
        # The version of the middleware, database, or web service.
        self.sca_version = sca_version
        # The list of search criteria.
        self.search_criteria_list = search_criteria_list
        # The content to query. Depending on the value of **SearchItem**, you need to enter different query content:
        # - If **SearchItem** is set to **name**, enter the name of the asset fingerprint as the query condition.
        # - If **SearchItem** is set to **type**, select the type of asset fingerprint to query. Valid values:   
        #     - **system_service**: system service
        #     - **software_library**: software library
        #     - **docker_component**: container component
        #     - **database**: database
        #     - **web_container**: web container
        #     - **jar**: JAR package
        #     - **web_framework**: web framework  
        # 
        # > The **SearchItem** and **SearchInfo** parameters must be used together. Setting only one of them has no effect. By setting both parameters, you can view all data for asset fingerprints of a specified name or type.
        self.search_info = search_info
        # The content of the sub-query condition. Depending on the value of **SearchItemSub**, you need to enter different query content:
        # - If **SearchItemSub** is set to **port**, enter the port as the sub-query condition.
        # - If **SearchItemSub** is set to **pid**, enter the process ID as the sub-query condition.
        # - If **SearchItemSub** is set to **version**, enter the middleware, database, or web service version as the sub-query condition.
        # - If **SearchItemSub** is set to **user**, enter the username as the sub-query condition.
        # 
        # > Sub-query conditions help you search for the data list of a specific middleware, database, or web service.
        self.search_info_sub = search_info_sub
        # The type of query condition. Valid values:
        # - **name**: the name of the middleware, database, or web service.
        # - **type**: the type of the middleware, database, or web service.
        # 
        # > The **SearchItem** and **SearchInfo** parameters must be used together. Setting only one of them has no effect. By setting both parameters, you can view all data for asset fingerprints of a specified name or type.
        self.search_item = search_item
        # The type of sub-query condition. Valid values:
        # - **port**: port
        # - **pid**: process ID
        # - **version**: version
        # - **user**: user.
        self.search_item_sub = search_item_sub
        # Specifies whether to use the NextToken method to retrieve asset list data. If this parameter is used, TotalCount is no longer returned. Valid values:
        # 
        # - **true**: Use the NextToken method.
        # - **false**: Do not use the NextToken method.
        self.use_next_token = use_next_token
        # The user that runs the process.
        self.user = user
        # The UUID of the server on which the middleware, database, or web service is deployed.
        self.uuid = uuid

    def validate(self):
        if self.search_criteria_list:
            for v1 in self.search_criteria_list:
                 if v1:
                    v1.validate()

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

        result['SearchCriteriaList'] = []
        if self.search_criteria_list is not None:
            for k1 in self.search_criteria_list:
                result['SearchCriteriaList'].append(k1.to_map() if k1 else None)

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

        self.search_criteria_list = []
        if m.get('SearchCriteriaList') is not None:
            for k1 in m.get('SearchCriteriaList'):
                temp_model = main_models.DescribePropertyScaDetailRequestSearchCriteriaList()
                self.search_criteria_list.append(temp_model.from_map(k1))

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

class DescribePropertyScaDetailRequestSearchCriteriaList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the search criterion.
        self.name = name
        # The filter value of the search criterion.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

